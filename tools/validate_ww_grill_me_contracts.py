from __future__ import annotations

import argparse
import json
import re
import runpy
from dataclasses import dataclass
from pathlib import Path
from types import SimpleNamespace
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
    "scaffold": Path("tools/scaffold_ww_case_artifacts.py"),
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


def render_scaffold_working_brief(
    scaffold_path: Path,
    repo_root: Path,
) -> tuple[str, str]:
    try:
        namespace = runpy.run_path(str(scaffold_path))
        renderer = namespace["render_working_brief"]
        cases_root = repo_root / "docs" / "cases"
        case_root = cases_root / "fixture-case"
        round_root = case_root / "rounds" / "2026-06-14-fixture-round"
        context = SimpleNamespace(
            case_slug="fixture-case",
            round_slug="2026-06-14-fixture-round",
            title="Fixture Round",
            user_request="Validate grill-me scaffold output",
            case_goal="Validate the rendered working brief",
            task_routing="code/programming",
            orchestrator="staff-engineer-orchestrator",
            quality_mode="standard",
            cases_root=cases_root,
            case_root=case_root,
            round_root=round_root,
            topic_slug="fixture-round",
            current_date="2026-06-14",
        )
        rendered = renderer(context)
    except Exception as exc:
        return "", f"Could not render scaffold working brief: {exc}"
    if not isinstance(rendered, str):
        return "", "Scaffold `render_working_brief` must return Markdown text."
    return rendered, ""


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


def has_forbidden_directive(
    section: MarkdownSection,
    forbidden_phrases: list[str],
) -> bool:
    historical_prefixes = [
        "historical guidance",
        "previous guidance",
        "older guidance",
        "the former contract",
        "former contract",
        "the old contract",
    ]
    lines = [*section.text.splitlines(), *section.list_items]
    for line in lines:
        normalized_line = normalized(line)
        if any(normalized_line.startswith(prefix) for prefix in historical_prefixes):
            continue
        for phrase in forbidden_phrases:
            normalized_phrase = normalized(phrase)
            for match in re.finditer(re.escape(normalized_phrase), normalized_line):
                prefix = normalized_line[: match.start()].rstrip()
                protective_pattern = (
                    r"(?:do not|must not|never|does not|should not|cannot|can't)"
                    r"(?:\s+\w+){0,2}\s*$"
                )
                if not re.search(protective_pattern, prefix):
                    return True
    return False


def has_forbidden_pattern(
    section: MarkdownSection,
    patterns: list[str],
) -> bool:
    historical_prefixes = (
        "historical guidance",
        "previous guidance",
        "older guidance",
        "the former contract",
        "former contract",
        "the old contract",
    )
    protective_pattern = re.compile(
        r"(?:do not|must not|never|does not|should not|cannot|can't)"
        r"(?:\s+\w+){0,2}\s*$"
    )
    for line in [*section.text.splitlines(), *section.list_items]:
        normalized_line = normalized(line)
        if normalized_line.startswith(historical_prefixes):
            continue
        for pattern in patterns:
            for match in re.finditer(pattern, normalized_line):
                if not protective_pattern.search(
                    normalized_line[: match.start()].rstrip()
                ):
                    return True
    return False


def has_stopped_decision_state(list_items: list[str]) -> bool:
    return any(
        normalized(item).startswith("state:")
        and "stopped" in normalized(item)
        for item in list_items
    )


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
    scaffold_brief, scaffold_error = render_scaffold_working_brief(
        paths["scaffold"],
        repo_root,
    )
    scaffold_tokens = md_cls().parse(scaffold_brief)
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
    scaffold_decision_log_section = extract_section(
        scaffold_tokens,
        "Grill-Me Decision Log",
        2,
    )
    decision_log_labels = [
        "Decision ID:",
        "State:",
        "Question:",
        "User-Confirmed Answer:",
        "Recommendation Offered:",
        "Rationale Or Repository Evidence:",
        "Dependencies Resolved:",
        "Dependent Branches Unblocked:",
    ]
    decision_log_fragments = [
        "the orchestrator owns this log",
        "the grill-me explorer remains read-only and is applied inline during planning",
        "State: open | confirmed | deferred",
        "create or update an entry only when grill-me is explicitly active",
        "keep State: open until the user explicitly confirms an answer",
        "do not treat the recommended answer as confirmation",
        (
            "record repository-resolved facts as evidence without asking the "
            "user to decide them"
        ),
        (
            "use confirmed entries as inputs to later design specs and "
            "implementation plans"
        ),
        "keep round approval and runtime lifecycle state in dispatch-plan.md",
        (
            "when the user stops grilling, mark the current unresolved branch "
            "deferred"
        ),
    ]

    def valid_decision_log(section: MarkdownSection | None) -> bool:
        return (
            section is not None
            and has_required_list_labels(section.list_items, decision_log_labels)
            and contains_all(section.text, decision_log_fragments)
            and not has_stopped_decision_state(section.list_items)
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
                    "used inline by the orchestrator during planning",
                    "do not assemble or launch an explorer packet",
                    "ordinary explorer packet behavior remains unchanged",
                ],
            )
            and not has_forbidden_directive(
                protocol_section,
                [
                    "assemble and launch an explorer packet",
                    "launch a grill-me explorer packet",
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
                    "ask exactly one unresolved question per user turn",
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
                    "run the interview inline during working-brief finalization",
                    "before dispatch-plan approval",
                    "do not create a subagent packet",
                    "launch an explorer execution",
                    "enter the runtime controller",
                    "when no dispatch plan exists",
                    "then finalize the brief and create the dispatch plan",
                    "when a dispatch plan already exists",
                    "freeze new dispatch",
                    "set plan_state to revising",
                    "update and increment brief_version",
                    "regenerate the dispatch plan against that brief version",
                    "require approval again",
                    "before any worker or reviewer dispatch",
                    "stop grilling",
                    "current unresolved branch deferred",
                    (
                        "does not set dispatch plan, section, or runtime state "
                        "to stopped"
                    ),
                    "canonical $ww Stop remains an approval or controller decision",
                    "use canonical Stop separately",
                    "stop the round",
                    "lettered options (A, B, C) or descriptive answers",
                    "numeric 1/2/3 approval aliases",
                    (
                        "only when the dispatch plan is awaiting an approval "
                        "decision"
                    ),
                    "not during an active grill question",
                ],
            )
            and not has_forbidden_directive(
                skill_section,
                [
                    "the explorer asks the user directly",
                    "select grill-me when a plan appears incomplete",
                    "create an explorer packet for the grill-me interview",
                    "build a subagent packet for the grill-me interview",
                    "launch an explorer execution for the interview",
                    "execute the grill-me interview as an explorer job",
                    "enter the runtime controller for the interview",
                    "grill-me enters the runtime controller",
                    "run the grill-me interview after dispatch approval",
                    "use numeric 1/2/3 options during active grill questions",
                    "stop grilling invokes canonical Stop",
                    "stop grilling stops the round",
                    "reuse the original dispatch plan without approval",
                ],
            )
            and not has_forbidden_pattern(
                skill_section,
                [
                    (
                        r"\b(?:create|build|assemble|generate|launch)\b"
                        r"(?:\s+\S+){0,5}\s+"
                        r"\b(?:subagent|explorer)\s+packet\b"
                    ),
                    (
                        r"\b(?:launch|execute|run)\b"
                        r"(?:\s+\S+){0,6}\s+\bexplorer\s+"
                        r"(?:execution|job)\b"
                    ),
                    (
                        r"(?:\b(?:enter|use|invoke)\b.*"
                        r"\bruntime controller\b|"
                        r"\brun\s+(?:through|inside)\b.*"
                        r"\bruntime controller\b)"
                    ),
                    (
                        r"\b(?:run|start|conduct)\b.*\bgrill-me interview\b"
                        r".*\bafter dispatch approval\b"
                    ),
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
            not scaffold_error
            and valid_decision_log(decision_log_section)
            and valid_decision_log(scaffold_decision_log_section),
            TARGETS["brief"],
            "Decision Persistence",
            (
                scaffold_error
                or "Missing durable orchestrator-owned Grill-Me Decision Log "
                "in the reference template or rendered scaffold output."
            ),
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
                    "must not be selected for packet assembly",
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
