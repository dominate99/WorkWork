from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple


SCRIPT_NAME = "validate_ww_persona_selection_contracts.py"
REPO_ROOT = Path(__file__).resolve().parent.parent


TARGETS = {
    "skill": REPO_ROOT / "plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md",
    "registry": REPO_ROOT
    / "plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate the WorkWork persona runtime-selection Markdown contract."
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


def build_results(documents: Dict[str, Document]) -> List[Result]:
    results: List[Result] = []

    skill = documents["skill"]
    registry = documents["registry"]

    registry_selection = section_items(registry, "Selection Rules")
    registry_guidance_order = label_items(
        registry,
        "Runtime Selection Guidance",
        "Use this order when choosing between eligible personas",
    )
    registry_guidance_fields = label_items(
        registry,
        "Runtime Selection Guidance",
        "Use optional enrichment fields in these ways",
    )
    registry_guardrails = label_items(
        registry,
        "Runtime Selection Guidance",
        "Runtime-selection guardrails",
    )

    skill_persona = paragraph_items(skill, "Persona Planning")
    skill_runtime_guidance = label_items(
        skill,
        "Persona Planning",
        "Runtime selection guidance",
    )

    checks = [
        (
            "WWPS001",
            registry.path,
            "Selection Rules",
            has_fragment(
                registry_selection,
                "Runtime persona selection must always establish baseline eligibility from required fields first.",
            ),
            "Missing required-fields-first baseline eligibility rule in persona selection.",
        ),
        (
            "WWPS002",
            registry.path,
            "Selection Rules",
            has_fragment(
                registry_selection,
                "After required-field eligibility is satisfied, optional enrichment fields may influence ranking, tie-breaks, and rationale quality.",
            ),
            "Missing ranking and tie-break rule for optional enrichment fields.",
        ),
        (
            "WWPS003",
            registry.path,
            "Selection Rules",
            has_fragment(
                registry_selection,
                "Optional enrichment fields must never override runtime-role boundaries, worker-capability gates, or project-registry preference rules.",
            ),
            "Missing guardrail preventing enrichment from overriding role boundaries, worker gates, or project preference.",
        ),
        (
            "WWPS004",
            registry.path,
            "Selection Rules",
            has_fragment(
                registry_selection,
                "During partial enrichment rollout, a persona must not be rejected solely because it lacks optional enrichment fields if it still satisfies the required-field baseline.",
            ),
            "Missing rollout safeguard for personas that still satisfy the required baseline without enrichment fields.",
        ),
        (
            "WWPS005",
            registry.path,
            "Selection Rules",
            has_fragment(
                registry_selection,
                "If optional enrichment fields are used in rationale, they must sharpen why a persona was chosen, not replace the required-field justification.",
            ),
            "Missing rationale rule that keeps enrichment subordinate to required-field justification.",
        ),
        (
            "WWPS006",
            registry.path,
            "Runtime Selection Guidance",
            all(
                has_fragment(registry_guidance_order, fragment)
                for fragment in [
                    "confirm required-field eligibility and role compatibility",
                    "prefer the strongest project-registry match over a generic built-in fallback",
                    "use `strengths`, `use_when`, `domains`, and language fit to narrow the viable set",
                    "use optional enrichment fields to rank viable candidates by decision posture, quality bar, tradeoff bias, and escalation fit",
                    "write rationale that names both the baseline fit and the enrichment-level fit when enrichment affected the choice",
                ]
            ),
            "Missing one or more ordered runtime-selection steps in persona registry guidance.",
        ),
        (
            "WWPS007",
            registry.path,
            "Runtime Selection Guidance",
            all(
                has_fragment(registry_guidance_fields, fragment)
                for fragment in [
                    "use to decide which persona should lead when the task's main ambiguity is about how to frame or resolve the work",
                    "use to decide which persona best matches the level of rigor the round actually needs",
                    "use to break ties when two personas are both capable but protect different outcomes",
                    "use to prefer the persona most likely to notice the dominant risk early",
                    "use to prefer the persona whose stopping conditions match the round's real irreversible risks",
                    "use to shape which specialist should synthesize, gate, or support when more than one persona is involved",
                    "use when coherence, clarity, or felt quality materially changes whether the result is good enough",
                ]
            ),
            "Missing one or more enrichment-field usage rules in persona registry guidance.",
        ),
        (
            "WWPS008",
            registry.path,
            "Runtime Selection Guidance",
            all(
                has_fragment(registry_guardrails, fragment)
                for fragment in [
                    "do not use optional enrichment fields to invent capability the persona does not already have in required fields",
                    "do not use optional enrichment fields to force a reviewer or orchestrator into the worker selection set",
                    "do not treat the presence of enrichment text as stronger than better required-field fit",
                    "if two candidates are still effectively tied after enrichment review, prefer the simpler selection and record the unresolved tie in rationale instead of overfitting",
                ]
            ),
            "Missing one or more runtime-selection guardrails in persona registry guidance.",
        ),
        (
            "WWPS009",
            skill.path,
            "Persona Planning",
            has_fragment(
                skill_persona,
                "Check for project personas first at `docs/superpowers/personas/registry.yaml`.",
            ),
            "Missing project-registry-first persona planning rule in SKILL.md.",
        ),
        (
            "WWPS010",
            skill.path,
            "Persona Planning",
            all(
                has_fragment(skill_runtime_guidance, fragment)
                for fragment in [
                    "derive the initial candidate set from required fields first",
                    "prefer the strongest project persona match before falling back to built-in personas",
                    "use `strengths`, `use_when`, `domains`, and language fit to narrow the viable set",
                    "once multiple candidates are still viable, use optional enrichment fields from `references/persona-registry.md` to rank and break ties",
                ]
            ),
            "Missing one or more candidate-selection narrowing steps in SKILL persona planning guidance.",
        ),
        (
            "WWPS011",
            skill.path,
            "Persona Planning",
            all(
                has_fragment(skill_runtime_guidance, fragment)
                for fragment in [
                    "use `decision_style` when the round's main ambiguity is how to frame or resolve the work",
                    "use `quality_bar` when the main differentiator is the rigor level the round requires",
                    "use `tradeoff_bias` and `failure_modes_to_watch` when two candidates are capable but protect different risks",
                    "use `escalation_triggers` when the choice depends on who should stop and escalate under irreversible or high-blast-radius conditions",
                    "use `collaboration_posture` and `taste_criteria` only when they materially improve specialist composition or quality judgment",
                ]
            ),
            "Missing one or more enrichment-driven tie-break rules in SKILL persona planning guidance.",
        ),
        (
            "WWPS012",
            skill.path,
            "Persona Planning",
            has_fragment(
                skill_runtime_guidance,
                "do not use optional enrichment fields to bypass role compatibility, worker-capability gates, or stronger required-field fit",
            ),
            "Missing SKILL guardrail preventing enrichment from bypassing compatibility or worker gates.",
        ),
        (
            "WWPS013",
            skill.path,
            "Persona Planning",
            has_fragment(
                skill_runtime_guidance,
                "if enrichment meaningfully affected the choice, say so in the persona rationale after the required-field justification",
            ),
            "Missing SKILL rationale requirement for enrichment-influenced persona selection.",
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
