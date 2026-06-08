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
    return parser.parse_args()


def normalized(text: str) -> str:
    return " ".join(text.split()).casefold()


def contains_all(text: str, fragments: list[str]) -> bool:
    value = normalized(text)
    return all(normalized(fragment) in value for fragment in fragments)


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
    payload = yaml.safe_load(paths["personas"].read_text(encoding="utf-8")) or {}
    personas = payload.get("personas", [])
    grill = next(
        (persona for persona in personas if persona.get("id") == "grill-me"),
        {},
    )

    role_binding = yaml.safe_load(texts["openai"]) or {}
    explorer_binding = role_binding.get("role_bindings", {}).get("explorer", {})

    checks = [
        result(
            "WWGM001",
            bool(grill),
            TARGETS["personas"],
            "Built-In Persona",
            "Missing built-in persona `grill-me`.",
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
            contains_all(
                texts["prompt"],
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
            contains_all(
                texts["prompt"],
                [
                    "investigate the codebase and current artifacts before asking",
                    "return exactly one unresolved question",
                    "include one recommended answer and a concise reason",
                    "keep the branch open until the user explicitly confirms",
                    "resolve prerequisite decisions before dependent decisions",
                    "allow the user to stop",
                    "shared-understanding summary",
                ],
            ),
            TARGETS["prompt"],
            "Interview Protocol",
            "The grill-me interview protocol is incomplete.",
        ),
        result(
            "WWGM005",
            explorer_binding.get("runtime_role") == "explorer"
            and explorer_binding.get("template_path")
            == "agents/explorer-prompt.md"
            and contains_all(texts["prompt"], ["do not write files"]),
            TARGETS["openai"],
            "Read-Only Explorer Binding",
            "`grill-me` must use the existing read-only explorer role binding.",
        ),
        result(
            "WWGM006",
            contains_all(
                texts["skill"],
                [
                    "only when the user explicitly requests",
                    "the orchestrator asks the user",
                    "exactly one unresolved question",
                    (
                        "must not select `grill-me` merely because a plan "
                        "appears incomplete"
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
            contains_all(
                texts["brief"],
                [
                    "## Grill-Me Decision Log",
                    "Decision ID",
                    "User-Confirmed Answer",
                    "Recommendation Offered",
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
                texts["registry"],
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
                texts["readme"],
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
        results = validate_repository()
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
