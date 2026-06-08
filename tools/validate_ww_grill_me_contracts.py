from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

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


def markdown_without_fences(text: str) -> str:
    lines: list[str] = []
    fence_marker = ""
    for line in text.splitlines():
        stripped = line.lstrip()
        if fence_marker:
            if stripped.startswith(fence_marker):
                fence_marker = ""
            continue
        if stripped.startswith("```"):
            fence_marker = "```"
            continue
        if stripped.startswith("~~~"):
            fence_marker = "~~~"
            continue
        lines.append(line)
    return "\n".join(lines)


def markdown_heading(line: str) -> tuple[int, str] | None:
    stripped = line.lstrip()
    hashes = len(stripped) - len(stripped.lstrip("#"))
    if hashes == 0 or hashes > 6:
        return None
    if len(stripped) <= hashes or stripped[hashes] != " ":
        return None
    return hashes, stripped[hashes + 1 :].strip()


def markdown_section(text: str, heading: str, level: int = 2) -> str | None:
    content = markdown_without_fences(text)
    collecting = False
    lines: list[str] = []
    for line in content.splitlines():
        parsed = markdown_heading(line)
        if parsed:
            current_level, current_heading = parsed
            if collecting and current_level <= level:
                break
            if current_level == level and current_heading == heading:
                collecting = True
                continue
        if collecting:
            lines.append(line)
    if not collecting:
        return None
    return "\n".join(lines)


def is_negated(statement: str) -> bool:
    return any(
        marker in statement
        for marker in [
            "must not",
            "may not",
            "cannot",
            "can not",
            "does not",
            "do not",
            "never",
            "forbid",
        ]
    )


def has_prompt_contradiction(text: str) -> bool:
    for raw_line in markdown_without_fences(text).splitlines():
        statement = normalized(raw_line)
        if not statement or is_negated(statement):
            continue
        if (
            "multiple unresolved questions" in statement
            or "more than one unresolved question" in statement
        ):
            return True
        if (
            "recommendation" in statement
            and (
                "count as approval" in statement
                or "close the branch without" in statement
                or "close branch without" in statement
            )
        ):
            return True
    return False


def has_skill_contradiction(text: str) -> bool:
    for raw_line in markdown_without_fences(text).splitlines():
        statement = normalized(raw_line)
        if not statement or is_negated(statement):
            continue
        if "explorer asks the user directly" in statement:
            return True
        if (
            (
                "auto-select `grill-me`" in statement
                or "automatically select `grill-me`" in statement
                or "may select `grill-me`" in statement
            )
            and "plan appears incomplete" in statement
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

    prompt_plain = markdown_without_fences(texts["prompt"])
    skill_plain = markdown_without_fences(texts["skill"])
    registry_plain = markdown_without_fences(texts["registry"])
    readme_plain = markdown_without_fences(texts["readme"])
    protocol_section = markdown_section(
        texts["prompt"],
        "Grill-Me Conditional Protocol",
    )
    decision_log_section = markdown_section(
        texts["brief"],
        "Grill-Me Decision Log",
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
                protocol_section,
                [
                    "only when `subagent_persona` is `grill-me`",
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
                protocol_section,
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
            and not has_prompt_contradiction(prompt_plain),
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
            and contains_all(prompt_plain, ["do not write files"]),
            TARGETS["openai"],
            "Read-Only Explorer Binding",
            role_binding_shape_error
            or "`grill-me` must use the existing read-only explorer role binding.",
        ),
        result(
            "WWGM006",
            contains_all(
                skill_plain,
                [
                    "only when the user explicitly requests",
                    "the orchestrator asks the user",
                    "exactly one unresolved question",
                    (
                        "must not select `grill-me` merely because a plan "
                        "appears incomplete"
                    ),
                ],
            )
            and not has_skill_contradiction(skill_plain),
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
            and contains_all(
                decision_log_section,
                [
                    "Decision ID",
                    "State",
                    "Question",
                    "User-Confirmed Answer",
                    "Recommendation Offered",
                    "Rationale Or Repository Evidence",
                    "Dependencies Resolved",
                    "Dependent Branches Unblocked",
                    "the orchestrator owns this log",
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
                    "`grill-me`",
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
