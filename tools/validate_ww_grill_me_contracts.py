from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_ROOT = Path("plugins/workwork/skills/ww-subagent-orchestrator")
TARGETS = {
    "personas": SKILL_ROOT / "references/built-in-personas.yaml",
    "prompt": SKILL_ROOT / "agents/explorer-prompt.md",
    "registry": SKILL_ROOT / "references/persona-registry.md",
    "brief": SKILL_ROOT / "references/working-brief-template.md",
    "skill": SKILL_ROOT / "SKILL.md",
    "openai": SKILL_ROOT / "agents/openai.yaml",
    "readme": Path("README.md"),
}


@dataclass
class RuleResult:
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


@dataclass
class MarkdownSection:
    text: str
    list_items: list[str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate the WorkWork grill-me explorer contracts."
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="as_json",
        help="Emit machine-readable JSON output.",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=REPO_ROOT,
        help="Repository root to validate. Defaults to the current WorkWork checkout.",
    )
    return parser.parse_args()


def normalized(text: str) -> str:
    return " ".join(text.split()).casefold()


def contains_all(text: str, fragments: list[str]) -> bool:
    value = normalized(text)
    return all(normalized(fragment) in value for fragment in fragments)


def load_markdown_parser():
    try:
        from markdown_it import MarkdownIt  # type: ignore
    except ImportError as exc:
        raise DependencyError(
            "Missing dependency: markdown-it-py. Install it with "
            "`python -m pip install markdown-it-py` before running this validator."
        ) from exc
    return MarkdownIt


def inline_text(token: Any) -> str:
    if not token.children:
        return token.content
    parts: list[str] = []
    for child in token.children:
        if child.type in {"softbreak", "hardbreak"}:
            parts.append(" ")
        elif child.content:
            parts.append(child.content)
    return "".join(parts)


def visible_markdown_text(tokens: list[Any]) -> str:
    return "\n".join(
        inline_text(token) for token in tokens if token.type == "inline"
    )


def collect_list_items(tokens: list[Any]) -> list[str]:
    items: list[str] = []
    i = 0
    while i < len(tokens):
        if tokens[i].type != "list_item_open":
            i += 1
            continue
        depth = 1
        parts: list[str] = []
        i += 1
        while i < len(tokens) and depth:
            token = tokens[i]
            if token.type == "list_item_open":
                depth += 1
            elif token.type == "list_item_close":
                depth -= 1
            elif token.type == "inline" and depth == 1:
                parts.append(inline_text(token))
            i += 1
        items.append(" ".join(parts))
    return items


def extract_section(
    tokens: list[Any],
    heading: str,
    level: int,
) -> MarkdownSection | None:
    start = None
    end = len(tokens)
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.type != "heading_open":
            i += 1
            continue
        current_level = int(token.tag[1])
        current_heading = (
            inline_text(tokens[i + 1])
            if i + 1 < len(tokens) and tokens[i + 1].type == "inline"
            else ""
        )
        if start is None:
            if current_level == level and current_heading == heading:
                start = i + 3
        elif current_level <= level:
            end = i
            break
        i += 3
    if start is None:
        return None
    section_tokens = tokens[start:end]
    return MarkdownSection(
        text=visible_markdown_text(section_tokens),
        list_items=collect_list_items(section_tokens),
    )


def has_required_list_labels(
    items: list[str],
    labels: list[str],
) -> bool:
    normalized_items = [normalized(item) for item in items]
    return all(
        any(item.startswith(normalized(label)) for item in normalized_items)
        for label in labels
    )


def has_forbidden_instruction(
    list_items: list[str],
    forbidden_phrases: list[str],
) -> bool:
    protective_negations = [
        "do not",
        "must not",
        "never",
        "does not",
        "should not",
        "cannot",
        "can't",
    ]
    for item in list_items:
        normalized_item = normalized(item)
        for phrase in forbidden_phrases:
            phrase_index = normalized_item.find(normalized(phrase))
            if phrase_index < 0:
                continue
            prefix = normalized_item[:phrase_index].rstrip()
            if not any(
                prefix.endswith(negation)
                for negation in protective_negations
            ):
                return True
    return False


def result(
    rule_id: str,
    passed: bool,
    path: Path,
    section: str,
    message: str,
) -> RuleResult:
    return RuleResult(
        rule_id=rule_id,
        passed=passed,
        file=path.as_posix(),
        section=section,
        message="ok" if passed else message,
    )


def validate_repository(repo_root: Path = REPO_ROOT) -> list[RuleResult]:
    paths = {name: repo_root / relative for name, relative in TARGETS.items()}
    texts = {
        name: path.read_text(encoding="utf-8")
        for name, path in paths.items()
        if name != "personas"
    }
    payload = yaml.safe_load(paths["personas"].read_text(encoding="utf-8"))
    persona_shape_error = ""
    personas: list[dict] = []
    if not isinstance(payload, dict):
        persona_shape_error = "Persona YAML root must be a mapping."
    elif not isinstance(payload.get("personas"), list):
        persona_shape_error = "`personas` must be a list."
    elif not all(isinstance(persona, dict) for persona in payload["personas"]):
        persona_shape_error = "All `personas` entries must be mappings."
    else:
        personas = payload["personas"]
    grill = next(
        (persona for persona in personas if persona.get("id") == "grill-me"),
        {},
    )

    role_binding = yaml.safe_load(texts["openai"])
    role_binding_shape_error = ""
    explorer_binding: dict = {}
    if not isinstance(role_binding, dict):
        role_binding_shape_error = "OpenAI role binding YAML root must be a mapping."
    else:
        role_bindings = role_binding.get("role_bindings")
        if not isinstance(role_bindings, dict):
            role_binding_shape_error = "`role_bindings` must be a mapping."
        elif not isinstance(role_bindings.get("explorer"), dict):
            role_binding_shape_error = (
                "`role_bindings.explorer` must be a mapping."
            )
        else:
            explorer_binding = role_bindings["explorer"]

    md_cls = load_markdown_parser()
    markdown_tokens = {
        name: md_cls().parse(texts[name])
        for name in ["prompt", "skill", "registry", "brief", "readme"]
    }
    registry_plain = visible_markdown_text(markdown_tokens["registry"])
    readme_plain = visible_markdown_text(markdown_tokens["readme"])
    protocol_section = extract_section(
        markdown_tokens["prompt"],
        "Grill-Me Conditional Protocol",
        2,
    )
    skill_section = extract_section(
        markdown_tokens["skill"],
        "Grill-Me Explorer",
        3,
    )
    decision_log_section = extract_section(
        markdown_tokens["brief"],
        "Grill-Me Decision Log",
        2,
    )

    checks = [
        result(
            "WWGM001",
            not persona_shape_error and bool(grill),
            TARGETS["personas"],
            "Built-In Persona",
            persona_shape_error or "Missing built-in persona `grill-me`.",
        ),
        result(
            "WWGM002",
            not grill
            or (
                grill.get("role_type") == "specialist"
                and grill.get("review_only") is False
                and "implementation_principles" not in grill
            ),
            TARGETS["personas"],
            "Worker Capability Boundary",
            (
                "`grill-me` must be a non-reviewer specialist without "
                "implementation principles."
            ),
        ),
        result(
            "WWGM003",
            protocol_section is not None
            and contains_all(
                protocol_section.text,
                [
                    "only when subagent_persona is grill-me",
                    "ordinary explorer behavior remains unchanged",
                ],
            ),
            TARGETS["prompt"],
            "Conditional Protocol",
            (
                "Missing persona-conditional activation or ordinary-explorer "
                "preservation."
            ),
        ),
        result(
            "WWGM004",
            protocol_section is not None
            and contains_all(
                protocol_section.text,
                [
                    "investigate the codebase and current artifacts before asking",
                    "return exactly one unresolved question",
                    "include one recommended answer and a concise reason",
                    "keep the branch open until the user explicitly confirms",
                    "resolve prerequisite decisions before dependent decisions",
                    "allow the user to stop",
                    "shared-understanding summary",
                ],
            )
            and not has_forbidden_instruction(
                protocol_section.list_items,
                [
                    "return multiple unresolved questions at once",
                    "the recommended answer counts as user approval",
                ],
            ),
            TARGETS["prompt"],
            "Interview Protocol",
            "The grill-me interview protocol is incomplete.",
        ),
        result(
            "WWGM005",
            not role_binding_shape_error
            and explorer_binding.get("runtime_role") == "explorer"
            and explorer_binding.get("template_path")
            == "agents/explorer-prompt.md"
            and protocol_section is not None
            and contains_all(protocol_section.text, ["do not write files"]),
            TARGETS["openai"],
            "Read-Only Explorer Binding",
            role_binding_shape_error
            or "`grill-me` must use the existing read-only explorer role binding.",
        ),
        result(
            "WWGM006",
            skill_section is not None
            and contains_all(
                skill_section.text,
                [
                    "only when the user explicitly requests",
                    "the orchestrator asks the user",
                    "exactly one unresolved question",
                    (
                        "must not select grill-me merely because a plan "
                        "appears incomplete"
                    ),
                ],
            )
            and not has_forbidden_instruction(
                skill_section.list_items,
                [
                    "the explorer asks the user directly",
                    "select grill-me when a plan appears incomplete",
                ],
            ),
            TARGETS["skill"],
            "Orchestrator Protocol",
            (
                "Missing explicit trigger, mediation, or one-question contract "
                "in SKILL.md."
            ),
        ),
        result(
            "WWGM007",
            decision_log_section is not None
            and has_required_list_labels(
                decision_log_section.list_items,
                [
                    "Decision ID:",
                    "State:",
                    "Question:",
                    "User-Confirmed Answer:",
                    "Recommendation Offered:",
                    "Rationale Or Repository Evidence:",
                    "Dependencies Resolved:",
                    "Dependent Branches Unblocked:",
                ],
            )
            and contains_all(
                decision_log_section.text,
                [
                    "the orchestrator owns this log",
                    "the grill-me explorer remains read-only",
                    (
                        "create or update an entry only when grill-me is "
                        "explicitly active"
                    ),
                    (
                        "keep State: open until the user explicitly confirms "
                        "an answer"
                    ),
                    "do not treat the recommended answer as confirmation",
                    (
                        "record repository-resolved facts as evidence without "
                        "asking the user to decide them"
                    ),
                    (
                        "use confirmed entries as inputs to later design specs "
                        "and implementation plans"
                    ),
                    (
                        "keep round approval and runtime lifecycle state in "
                        "dispatch-plan.md"
                    ),
                ],
            ),
            TARGETS["brief"],
            "Decision Persistence",
            "Missing durable orchestrator-owned Grill-Me Decision Log.",
        ),
        result(
            "WWGM008",
            contains_all(
                registry_plain,
                [
                    "grill-me",
                    "explicitly requests",
                    "runtime_role: explorer",
                    "must not enter the worker candidate set",
                ],
            ),
            TARGETS["registry"],
            "Persona Selection Guidance",
            "Missing grill-me eligibility and role-boundary guidance.",
        ),
        result(
            "WWGM009",
            contains_all(
                readme_plain,
                [
                    "$ww grill me",
                    "one question at a time",
                    "recommended answer",
                ],
            ),
            TARGETS["readme"],
            "User Guidance",
            "Missing user-facing grill-me trigger and interaction guidance.",
        ),
    ]
    return checks


def emit_human(results: list[RuleResult]) -> None:
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


def emit_json(results: list[RuleResult]) -> None:
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
        results = validate_repository(args.repo_root.resolve())
    except Exception as exc:  # pragma: no cover - operational safeguard
        if args.as_json:
            print(
                json.dumps(
                    {
                        "ok": False,
                        "rule_failures": 0,
                        "results": [],
                        "error": str(exc),
                    },
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

    return 0 if all(item.passed for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
