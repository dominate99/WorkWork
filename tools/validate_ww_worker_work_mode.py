from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple


SCRIPT_NAME = "validate_ww_worker_work_mode.py"
REPO_ROOT = Path(__file__).resolve().parent.parent


TARGETS = {
    "skill": REPO_ROOT / "plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md",
    "brief_template": REPO_ROOT
    / "plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md",
    "dispatch_template": REPO_ROOT
    / "plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md",
    "packet_contract": REPO_ROOT
    / "plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md",
    "worker_prompt": REPO_ROOT
    / "plugins/workwork/skills/ww-subagent-orchestrator/agents/worker-prompt.md",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate the WorkWork worker work-mode Markdown contract."
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="as_json",
        help="Emit machine-readable JSON output.",
    )
    return parser.parse_args()


@dataclass
class Result:
    rule_id: str
    passed: bool
    file: str
    section: str
    message: str

    def to_dict(self) -> dict:
        return {
            "rule_id": self.rule_id,
            "passed": self.passed,
            "file": self.file,
            "section": self.section,
            "message": self.message,
        }


class DependencyError(RuntimeError):
    pass


def load_markdown_parser():
    try:
        from markdown_it import MarkdownIt  # type: ignore
    except ImportError as exc:
        raise DependencyError(
            "Missing dependency: markdown-it-py. Install it with "
            "`python -m pip install markdown-it-py` before running "
            f"`python tools/{SCRIPT_NAME}`."
        ) from exc
    return MarkdownIt


@dataclass
class Document:
    path: Path
    headings: Dict[str, List[str]]
    labels: Dict[Tuple[str, str], List[str]]
    paragraphs: Dict[str, List[str]]
    code_blocks: Dict[str, List[str]]


def normalize(text: str) -> str:
    return " ".join(text.strip().split())


def is_list_open(token_type: str) -> bool:
    return token_type in {"bullet_list_open", "ordered_list_open"}


def is_list_close(token_type: str) -> bool:
    return token_type in {"bullet_list_close", "ordered_list_close"}


def collect_list_items(tokens: List, start: int) -> Tuple[List[str], int]:
    items: List[str] = []
    depth = 0
    current: List[str] = []
    i = start
    while i < len(tokens):
        token = tokens[i]
        if is_list_open(token.type):
            depth += 1
            i += 1
            continue
        if is_list_close(token.type):
            depth -= 1
            if depth == 0:
                if current:
                    items.append(normalize(" ".join(current)))
                    current = []
                return items, i + 1
            i += 1
            continue
        if token.type == "list_item_open":
            current = []
            i += 1
            continue
        if token.type == "list_item_close":
            if current:
                items.append(normalize(" ".join(current)))
            current = []
            i += 1
            continue
        if token.type == "inline" and depth >= 1:
            current.append(token.content)
        i += 1
    return items, i


def parse_document(path: Path, md_cls) -> Document:
    text = path.read_text(encoding="utf-8")
    tokens = md_cls().parse(text)

    headings: Dict[str, List[str]] = {}
    labels: Dict[Tuple[str, str], List[str]] = {}
    paragraphs: Dict[str, List[str]] = {}
    code_blocks: Dict[str, List[str]] = {}

    heading_stack: List[str] = []
    current_heading = "__root__"
    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token.type == "heading_open":
            if i + 1 < len(tokens) and tokens[i + 1].type == "inline":
                level = int(token.tag[1])
                heading_text = normalize(tokens[i + 1].content)
                heading_stack = heading_stack[: level - 1]
                heading_stack.append(heading_text)
                current_heading = " / ".join(heading_stack)
                headings.setdefault(current_heading, [])
                paragraphs.setdefault(current_heading, [])
                code_blocks.setdefault(current_heading, [])
            i += 3
            continue

        if token.type == "paragraph_open":
            inline_idx = i + 1
            if inline_idx < len(tokens) and tokens[inline_idx].type == "inline":
                label_text = normalize(tokens[inline_idx].content)
                next_idx = i + 3
                if label_text.endswith(":") and next_idx < len(tokens) and is_list_open(
                    tokens[next_idx].type
                ):
                    items, new_idx = collect_list_items(tokens, next_idx)
                    labels[(current_heading, label_text.rstrip(":"))] = items
                    i = new_idx
                    continue
                paragraphs.setdefault(current_heading, []).append(label_text)
            i += 3
            continue

        if is_list_open(token.type):
            items, new_idx = collect_list_items(tokens, i)
            headings.setdefault(current_heading, []).extend(items)
            i = new_idx
            continue

        if token.type == "fence":
            code_blocks.setdefault(current_heading, []).append(token.content)
            i += 1
            continue

        i += 1

    return Document(
        path=path,
        headings=headings,
        labels=labels,
        paragraphs=paragraphs,
        code_blocks=code_blocks,
    )


def has_fragment(items: List[str], fragment: str) -> bool:
    fragment_norm = normalize(fragment)
    return any(fragment_norm in normalize(item) for item in items)


def section_items(doc: Document, heading: str) -> List[str]:
    for key, items in doc.headings.items():
        if key == heading or key.endswith(f" / {heading}"):
            return items
    return []


def label_items(doc: Document, heading: str, label: str) -> List[str]:
    for (key_heading, key_label), items in doc.labels.items():
        if key_label != label:
            continue
        if key_heading == heading or key_heading.endswith(f" / {heading}"):
            return items
    return []


def paragraph_items(doc: Document, heading: str) -> List[str]:
    for key, items in doc.paragraphs.items():
        if key == heading or key.endswith(f" / {heading}"):
            return items
    return []


def code_block_contains(doc: Document, heading: str, fragment: str) -> bool:
    fragment_norm = normalize(fragment)
    for key, blocks in doc.code_blocks.items():
        if key == heading or key.endswith(f" / {heading}"):
            for block in blocks:
                if fragment_norm in normalize(block):
                    return True
    return False


def build_results(documents: Dict[str, Document]) -> List[Result]:
    results: List[Result] = []

    skill = documents["skill"]
    brief = documents["brief_template"]
    dispatch = documents["dispatch_template"]
    packet = documents["packet_contract"]
    prompt = documents["worker_prompt"]

    skill_core = section_items(skill, "Core Rules")
    skill_working_brief = label_items(
        skill,
        "Working Brief",
        "The working brief is the analysis snapshot for one dispatch round. It is the only valid basis for",
    )
    skill_working_brief_rules = label_items(skill, "Working Brief", "Working brief persistence rules")
    skill_packet = label_items(skill, "Subagent Packet Contract", "Every packet must encode")
    skill_packet_paragraphs = paragraph_items(skill, "Subagent Packet Contract")
    skill_dispatch = label_items(
        skill,
        "Dispatch Plan File",
        "The dispatch plan is the canonical runtime state for the dispatch round. The dispatch plan must",
    )
    skill_dispatch_rules = label_items(
        skill,
        "Dispatch Plan File",
        "Dispatch-plan validation rules are mandatory before the approval block is rendered",
    )
    skill_dispatch_paragraphs = paragraph_items(skill, "Dispatch Plan File")

    checks = [
        (
            "WWWM001",
            skill.path,
            "Core Rules",
            has_fragment(
                skill_core,
                "Worker execution order is `user constraints -> work_mode -> persona -> goal_tuning`.",
            ),
            "Missing worker execution order contract.",
        ),
        (
            "WWWM002",
            skill.path,
            "Core Rules",
            has_fragment(skill_core, "Keep `task_mode` separate from `work_mode`."),
            "Missing `task_mode` versus `work_mode` separation rule.",
        ),
        (
            "WWWM003",
            skill.path,
            "Working Brief",
            has_fragment(skill_working_brief, "section-level worker-mode recommendations"),
            "Missing working-brief worker-mode recommendation surface.",
        ),
        (
            "WWWM004",
            skill.path,
            "Working Brief / Working brief persistence rules",
            has_fragment(skill_working_brief_rules, "the working brief may recommend `worker mode`"),
            "Missing working-brief recommendation-only rule.",
        ),
        (
            "WWWM005",
            skill.path,
            "Subagent Packet Contract",
            has_fragment(skill_packet, "worker `work_mode`, `work_mode_rationale`, `goal_tuning`, and `constraint_precedence_note`"),
            "Missing worker packet field contract in `SKILL.md`.",
        ),
        (
            "WWWM006",
            skill.path,
            "Subagent Packet Contract",
            has_fragment(
                skill_packet_paragraphs,
                "Worker prompts consume packet state; they must not re-derive `work_mode` from the working brief.",
            ),
            "Missing packet-to-prompt authority rule in `SKILL.md`.",
        ),
        (
            "WWWM007",
            skill.path,
            "Dispatch Plan File",
            has_fragment(skill_dispatch, "record the section-level effective `worker mode` and its rationale"),
            "Missing dispatch-plan worker-mode recording rule in `SKILL.md`.",
        ),
        (
            "WWWM008",
            skill.path,
            "Dispatch Plan File",
            has_fragment(skill_dispatch, "track `Active Worker Mode` plus `Mode Change History`"),
            "Missing dispatch-plan mode-history rule in `SKILL.md`.",
        ),
        (
            "WWWM009",
            skill.path,
            "Dispatch Plan File / Dispatch-plan validation rules are mandatory before the approval block is rendered",
            has_fragment(skill_dispatch_rules, "`task_mode` must not be reused as `worker mode`"),
            "Missing dispatch-plan validation rule for `task_mode` separation in `SKILL.md`.",
        ),
        (
            "WWWM010",
            skill.path,
            "Dispatch Plan File",
            has_fragment(
                skill_dispatch_paragraphs,
                "the authority chain is fixed: the working brief recommends, the dispatch plan decides and records, the packet freezes one execution snapshot, and the worker prompt consumes packet state only",
            ),
            "Missing worker-mode authority chain in `SKILL.md`.",
        ),
        (
            "WWWM011",
            brief.path,
            "Persona And Workflow Guidance",
            all(
                has_fragment(section_items(brief, "Persona And Workflow Guidance"), field)
                for field in [
                    "`recommended_worker_mode_by_section`",
                    "`worker_mode_reasoning_by_section`",
                    "`goal_tuning_by_section`",
                    "`constraint_override_notes_by_section`",
                ]
            ),
            "Missing one or more worker-mode recommendation fields in the working-brief template.",
        ),
        (
            "WWWM012",
            brief.path,
            "Rules",
            has_fragment(section_items(brief, "Rules"), "The working brief recommends `worker mode` by section"),
            "Missing recommendation-only rule in the working-brief template.",
        ),
        (
            "WWWM013",
            brief.path,
            "Rules",
            has_fragment(section_items(brief, "Rules"), "`recommended_worker_mode_by_section` must be derived from task structure, scope shape, and risk"),
            "Missing structure/scope/risk recommendation rule in the working-brief template.",
        ),
        (
            "WWWM014",
            brief.path,
            "Rules",
            has_fragment(section_items(brief, "Rules"), "must be captured in `constraints` before any worker-mode recommendation is made"),
            "Missing constraint precedence rule in the working-brief template.",
        ),
        (
            "WWWM015",
            dispatch.path,
            "Planned Sections / Section: {{section_name}}",
            all(
                has_fragment(section_items(dispatch, "Planned Sections / Section: {{section_name}}"), field)
                for field in [
                    "Planned Worker Mode",
                    "Worker Mode Rationale",
                    "Goal Tuning",
                    "Constraint Interaction Rule",
                ]
            ),
            "Missing one or more planned worker-mode fields in the dispatch-plan template.",
        ),
        (
            "WWWM016",
            dispatch.path,
            "Section Runtime Ledger / Section: {{section_name}}",
            all(
                has_fragment(section_items(dispatch, "Section Runtime Ledger / Section: {{section_name}}"), field)
                for field in ["Active Worker Mode", "Mode Change History"]
            ),
            "Missing runtime worker-mode tracking fields in the dispatch-plan template.",
        ),
        (
            "WWWM017",
            dispatch.path,
            "Planned Sections / Section: {{section_name}}",
            has_fragment(
                section_items(dispatch, "Planned Sections / Section: {{section_name}}"),
                "`task_mode` remains the role-task field",
            ),
            "Missing dispatch-plan rule separating `task_mode` from `worker mode`.",
        ),
        (
            "WWWM018",
            packet.path,
            "Worker packets additionally require",
            all(
                has_fragment(
                    label_items(packet, "Required Fields", "Worker packets additionally require"),
                    field,
                )
                for field in [
                    "`work_mode`",
                    "`work_mode_rationale`",
                    "`goal_tuning`",
                    "`constraint_precedence_note`",
                ]
            ),
            "Missing one or more worker packet required fields in the packet contract.",
        ),
        (
            "WWWM019",
            packet.path,
            "Packet Rules",
            has_fragment(section_items(packet, "Packet Rules"), "worker packets must inherit exactly one effective `work_mode`"),
            "Missing worker packet inheritance rule in the packet contract.",
        ),
        (
            "WWWM020",
            packet.path,
            "Packet Rules",
            has_fragment(section_items(packet, "Packet Rules"), "`task_mode` remains separate from `work_mode`"),
            "Missing `task_mode` separation rule in the packet contract.",
        ),
        (
            "WWWM021",
            packet.path,
            "Worker Packet Example",
            all(
                code_block_contains(packet, "Worker Packet Example", fragment)
                for fragment in [
                    "work_mode: validate-first",
                    "work_mode_rationale:",
                    "goal_tuning: validation-biased",
                    "constraint_precedence_note:",
                ]
            ),
            "Missing one or more worker-mode example fields in the worker packet example.",
        ),
        (
            "WWWM022",
            prompt.path,
            "Responsibilities",
            has_fragment(label_items(prompt, "Worker Prompt", "Responsibilities"), "obey packet constraints, non-goals"),
            "Missing constraint-first responsibility in the worker prompt.",
        ),
        (
            "WWWM023",
            prompt.path,
            "Responsibilities",
            has_fragment(label_items(prompt, "Worker Prompt", "Responsibilities"), "apply the packet's `work_mode` before choosing the first execution step"),
            "Missing `work_mode` responsibility in the worker prompt.",
        ),
        (
            "WWWM024",
            prompt.path,
            "Operating rules",
            has_fragment(label_items(prompt, "Worker Prompt", "Operating rules"), "first obey `owned_scope`, `write_scope`, `non_goals`, and explicit packet-carried user constraints"),
            "Missing constraint-first operating rule in the worker prompt.",
        ),
        (
            "WWWM025",
            prompt.path,
            "Operating rules",
            has_fragment(label_items(prompt, "Worker Prompt", "Operating rules"), "then apply `work_mode` to determine the default execution sequence"),
            "Missing `work_mode` ordering rule in the worker prompt.",
        ),
        (
            "WWWM026",
            prompt.path,
            "Operating rules",
            has_fragment(label_items(prompt, "Worker Prompt", "Operating rules"), "use `goal_tuning` only to slightly adjust pace or emphasis; it must not override `work_mode`"),
            "Missing `goal_tuning` light-modifier rule in the worker prompt.",
        ),
        (
            "WWWM027",
            prompt.path,
            "Operating rules",
            all(
                has_fragment(label_items(prompt, "Worker Prompt", "Operating rules"), fragment)
                for fragment in [
                    "`plan-first` means",
                    "`validate-first` means",
                    "`iterate-first` means",
                    "`conservative-first` means",
                ]
            ),
            "Missing one or more work-mode definitions in the worker prompt.",
        ),
    ]

    for rule_id, file_path, section, passed, message in checks:
        results.append(
            Result(
                rule_id=rule_id,
                passed=passed,
                file=str(file_path.relative_to(REPO_ROOT)).replace("\\", "/"),
                section=section,
                message=message if not passed else "ok",
            )
        )

    return results


def emit_human(results: List[Result]) -> None:
    failures = [result for result in results if not result.passed]
    if not failures:
        print(f"PASS: {len(results)} rules checked")
        return

    print(f"FAIL: {len(failures)} rule violations")
    print()
    for failure in failures:
        print(f"[{failure.rule_id}] {failure.file}")
        print(f"Section: {failure.section}")
        print(failure.message)
        print()


def emit_json(results: List[Result]) -> None:
    failures = sum(1 for result in results if not result.passed)
    payload = {
        "ok": failures == 0,
        "rule_failures": failures,
        "results": [result.to_dict() for result in results],
    }
    print(json.dumps(payload, indent=2))


def main() -> int:
    args = parse_args()

    try:
        md_cls = load_markdown_parser()
        documents = {name: parse_document(path, md_cls) for name, path in TARGETS.items()}
        results = build_results(documents)
    except DependencyError as exc:
        if args.as_json:
            print(json.dumps({"ok": False, "rule_failures": 0, "results": [], "error": str(exc)}, indent=2))
        else:
            print(f"ERROR: {exc}")
        return 2
    except Exception as exc:  # pragma: no cover - operational safeguard
        if args.as_json:
            print(json.dumps({"ok": False, "rule_failures": 0, "results": [], "error": str(exc)}, indent=2))
        else:
            print(f"ERROR: {exc}")
        return 2

    if args.as_json:
        emit_json(results)
    else:
        emit_human(results)

    return 0 if all(result.passed for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
