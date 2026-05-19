from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple


SCRIPT_NAME = "validate_ww_role_contracts.py"
REPO_ROOT = Path(__file__).resolve().parent.parent


TARGETS = {
    "skill": REPO_ROOT / "plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md",
    "packet_contract": REPO_ROOT
    / "plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md",
    "reviewer_prompt": REPO_ROOT
    / "plugins/workwork/skills/ww-subagent-orchestrator/agents/reviewer-prompt.md",
    "explorer_prompt": REPO_ROOT
    / "plugins/workwork/skills/ww-subagent-orchestrator/agents/explorer-prompt.md",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate the WorkWork reviewer and explorer Markdown contracts."
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
    packet = documents["packet_contract"]
    reviewer_prompt = documents["reviewer_prompt"]
    explorer_prompt = documents["explorer_prompt"]

    skill_core = section_items(skill, "Core Rules")
    skill_persona = paragraph_items(skill, "Persona Planning")
    skill_persona_items = section_items(skill, "Persona Planning")
    skill_role_prompt_assets = label_items(
        skill,
        "Persona Planning",
        "For every chosen persona, write",
    )

    packet_required_fields = section_items(packet, "Required Fields")
    packet_execution_defaults = label_items(packet, "Execution Binding", "Defaults")
    packet_rules = section_items(packet, "Packet Rules")
    reviewer_defaults = section_items(packet, "Reviewer Packet Defaults")
    explorer_defaults = section_items(packet, "Explorer Packet Defaults")

    reviewer_responsibilities = label_items(reviewer_prompt, "Reviewer Prompt", "Responsibilities")
    reviewer_rules = label_items(reviewer_prompt, "Reviewer Prompt", "Operating rules")
    reviewer_outputs = label_items(reviewer_prompt, "Reviewer Prompt", "Required outputs")

    explorer_responsibilities = label_items(explorer_prompt, "Explorer Prompt", "Responsibilities")
    explorer_rules = label_items(explorer_prompt, "Explorer Prompt", "Operating rules")
    explorer_outputs = label_items(explorer_prompt, "Explorer Prompt", "Required outputs")

    checks = [
        (
            "WWRV001",
            skill.path,
            "Core Rules",
            has_fragment(skill_core, "Reviewer subagents point out problems only."),
            "Missing findings-only reviewer rule in `SKILL.md`.",
        ),
        (
            "WWRV002",
            skill.path,
            "Core Rules",
            has_fragment(skill_core, "Reviewer subagents must stay narrow and convergent"),
            "Missing narrow-reviewer rule in `SKILL.md`.",
        ),
        (
            "WWRV003",
            skill.path,
            "Core Rules",
            has_fragment(skill_core, "Every section must have reviewer coverage, orchestrator synthesis, and human judgment."),
            "Missing reviewer-coverage and human-judgment rule in `SKILL.md`.",
        ),
        (
            "WWRV004",
            skill.path,
            "Persona Planning",
            has_fragment(skill_persona, "Keep reviewers and implementers separate."),
            "Missing reviewer-versus-implementer separation rule in `SKILL.md`.",
        ),
        (
            "WWRV005",
            packet.path,
            "Required Fields / Reviewer packets additionally require",
            all(
                has_fragment(
                    label_items(packet, "Required Fields", "Reviewer packets additionally require"),
                    field,
                )
                for field in [
                    "`review_target_ref`",
                    "`review_type`",
                    "`pass_condition`",
                    "`reject_condition`",
                ]
            ),
            "Missing one or more reviewer packet required fields in the packet contract.",
        ),
        (
            "WWRV006",
            packet.path,
            "Reviewer Packet Defaults",
            all(
                has_fragment(reviewer_defaults, fragment)
                for fragment in [
                    "`task_mode: review`",
                    "`agent_type: default`",
                    "`output_contract: findings only`",
                    "`handoff_rule: return to orchestrator, then human judgment required`",
                    "`requires_human_judgment: true`",
                    "`write_scope: []`",
                ]
            ),
            "Missing one or more reviewer packet defaults in the packet contract.",
        ),
        (
            "WWRV007",
            packet.path,
            "Packet Rules",
            all(
                has_fragment(packet_rules, fragment)
                for fragment in [
                    "`handoff_rule` must route reviewer results back to the orchestrator before human judgment.",
                    "`requires_human_judgment` must be `true` for reviewer packets.",
                    "`write_scope` must be empty for reviewer packets unless the dispatch plan explicitly allows a rewrite stage.",
                ]
            ),
            "Missing one or more reviewer packet rules in the packet contract.",
        ),
        (
            "WWRV008",
            packet.path,
            "Execution Binding",
            has_fragment(packet_execution_defaults, "reviewer")
            and has_fragment(packet_execution_defaults, "`agent_type`: `default`"),
            "Missing reviewer execution-binding default in the packet contract.",
        ),
        (
            "WWRV009",
            packet.path,
            "Reviewer Packet Example",
            all(
                code_block_contains(packet, "Reviewer Packet Example", fragment)
                for fragment in [
                    "subagent_persona: secure-software-engineer",
                    "runtime_role: reviewer",
                    "template_path: agents/reviewer-prompt.md",
                    "non_goals: do not rewrite files, do not approve release, do not change scope",
                ]
            ),
            "Missing reviewer packet example role binding or non-goal protections.",
        ),
        (
            "WWRV010",
            reviewer_prompt.path,
            "Responsibilities",
            all(
                has_fragment(reviewer_responsibilities, fragment)
                for fragment in [
                    "inspect only the assigned target",
                    "return findings only, ordered by severity",
                    "keep the review narrow and actionable",
                ]
            ),
            "Missing one or more reviewer responsibilities in the reviewer prompt.",
        ),
        (
            "WWRV011",
            reviewer_prompt.path,
            "Operating rules",
            all(
                has_fragment(reviewer_rules, fragment)
                for fragment in [
                    "do not rewrite the artifact",
                    "do not propose new scope",
                    "do not approve the section",
                    "do not widen the review surface beyond the packet target",
                ]
            ),
            "Missing one or more reviewer operating rules in the reviewer prompt.",
        ),
        (
            "WWRV012",
            reviewer_prompt.path,
            "Required outputs",
            all(
                has_fragment(reviewer_outputs, fragment)
                for fragment in [
                    "at most five findings",
                    "explicit `no material findings` when the target is clean",
                ]
            ),
            "Missing one or more reviewer required outputs in the reviewer prompt.",
        ),
        (
            "WWEX001",
            skill.path,
            "Persona Planning",
            has_fragment(skill_role_prompt_assets, "`agents/explorer-prompt.md`"),
            "Missing explorer prompt asset binding in `SKILL.md`.",
        ),
        (
            "WWEX002",
            skill.path,
            "Persona Planning",
            has_fragment(skill_role_prompt_assets, "`agents/reviewer-prompt.md`")
            and has_fragment(skill_role_prompt_assets, "`agents/explorer-prompt.md`"),
            "Missing reviewer/explorer role prompt assets in `SKILL.md`.",
        ),
        (
            "WWEX003",
            packet.path,
            "Execution Binding",
            has_fragment(packet_execution_defaults, "read-only investigators")
            and has_fragment(packet_execution_defaults, "`agent_type`: `explorer`"),
            "Missing explorer execution-binding default in the packet contract.",
        ),
        (
            "WWEX004",
            packet.path,
            "Explorer Packet Defaults",
            all(
                has_fragment(explorer_defaults, fragment)
                for fragment in [
                    "`task_mode: investigate`",
                    "`agent_type: explorer`",
                    "`write_scope: []`",
                    "`retry_policy: relaunch only through orchestrator decision`",
                    "`close_policy: close after findings are handed back`",
                    "`requires_human_judgment: false`",
                ]
            ),
            "Missing one or more explorer packet defaults in the packet contract.",
        ),
        (
            "WWEX005",
            explorer_prompt.path,
            "Responsibilities",
            all(
                has_fragment(explorer_responsibilities, fragment)
                for fragment in [
                    "gather evidence for a narrow question",
                    "summarize concrete observations only",
                    "preserve scope boundaries and read-only behavior",
                ]
            ),
            "Missing one or more explorer responsibilities in the explorer prompt.",
        ),
        (
            "WWEX006",
            explorer_prompt.path,
            "Operating rules",
            all(
                has_fragment(explorer_rules, fragment)
                for fragment in [
                    "do not write files",
                    "do not rewrite deliverables",
                    "do not decide on behalf of the orchestrator",
                    "keep findings scoped to the requested investigation",
                ]
            ),
            "Missing one or more explorer operating rules in the explorer prompt.",
        ),
        (
            "WWEX007",
            explorer_prompt.path,
            "Required outputs",
            all(
                has_fragment(explorer_outputs, fragment)
                for fragment in [
                    "concise evidence notes",
                    "direct answer to the assigned question",
                ]
            ),
            "Missing one or more explorer required outputs in the explorer prompt.",
        ),
        (
            "WWRL001",
            packet.path,
            "Packet Rules",
            has_fragment(packet_rules, "`subagent_persona` must use the canonical persona `id`, not a free-text display label"),
            "Missing canonical persona-id rule in the packet contract.",
        ),
        (
            "WWRL002",
            packet.path,
            "Reviewer Packet Defaults",
            not any(
                has_fragment(reviewer_defaults, fragment)
                for fragment in ["`work_mode:`", "`implementation_principles`"]
            ),
            "Reviewer packet defaults drifted into worker-only fields.",
        ),
        (
            "WWRL003",
            packet.path,
            "Explorer Packet Defaults",
            not any(
                has_fragment(explorer_defaults, fragment)
                for fragment in ["`work_mode:`", "`implementation_principles`"]
            ),
            "Explorer packet defaults drifted into worker-only fields.",
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
            print(
                json.dumps(
                    {"ok": False, "rule_failures": 0, "results": [], "error": str(exc)},
                    indent=2,
                )
            )
        else:
            print(f"ERROR: {exc}")
        return 2
    except Exception as exc:  # pragma: no cover - operational safeguard
        if args.as_json:
            print(
                json.dumps(
                    {"ok": False, "rule_failures": 0, "results": [], "error": str(exc)},
                    indent=2,
                )
            )
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
