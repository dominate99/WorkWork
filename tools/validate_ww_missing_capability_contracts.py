from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_ROOT = Path("plugins/workwork/skills/ww-subagent-orchestrator")
TARGETS = {
    "skill": SKILL_ROOT / "SKILL.md",
    "readme": Path("README.md"),
    "dispatch_template": SKILL_ROOT / "assets/dispatch-plan-template.md",
    "working_brief": SKILL_ROOT / "references/working-brief-template.md",
    "packet_contract": SKILL_ROOT / "references/subagent-packet-contract.md",
    "missing_capability_reference": (
        SKILL_ROOT / "references/task-runtime-missing-capabilities.md"
    ),
}

RECORD_FAMILIES = [
    "internal_hook_records",
    "quality_gate_records",
    "score_records",
    "repair_records",
    "review_synthesis_records",
    "reverification_requirements",
    "close_gate_records",
    "final_judgment_records",
    "recovery_requirement_records",
    "checkpoint_records",
]

SOURCE_CONTEXT_FIELDS = [
    "`source_internal_hook_refs[]`",
    "`source_quality_gate_ref`",
    "`source_score_ref`",
    "`source_repair_ref`",
    "`source_reverification_requirement_ref`",
    "`source_close_gate_ref`",
    "`source_final_judgment_ref`",
    "`source_recovery_requirement_ref`",
    "`source_checkpoint_ref`",
]


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
        description=(
            "Validate dormant WorkWork missing-capability contract surfaces."
        )
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


def normalize(text: str) -> str:
    return " ".join(text.split()).casefold()


def contains_all(text: str, fragments: list[str]) -> bool:
    value = normalize(text)
    return all(normalize(fragment) in value for fragment in fragments)


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


def read_required_texts(repo_root: Path) -> tuple[dict[str, str], str]:
    texts: dict[str, str] = {}
    for name, relative in TARGETS.items():
        path = repo_root / relative
        if not path.is_file():
            if name == "missing_capability_reference":
                return (
                    texts,
                    "Missing `references/task-runtime-missing-capabilities.md`.",
                )
            return texts, f"Missing required contract file `{relative.as_posix()}`."
        texts[name] = path.read_text(encoding="utf-8")
    return texts, ""


def legacy_dispatch_authority_violations(repo_root: Path) -> list[Path]:
    docs_root = repo_root / "docs" / "cases"
    if not docs_root.exists():
        return []
    violations: list[Path] = []
    block_markers = [
        "## section missing capability records",
        "### section missing capability records",
    ]
    record_markers = [f"{record}:" for record in RECORD_FAMILIES]
    for path in docs_root.rglob("dispatch-plan.md"):
        text = path.read_text(encoding="utf-8")
        if "Lifecycle Protocol: legacy" not in text:
            continue
        normalized_text = normalize(text)
        if any(marker in normalized_text for marker in block_markers):
            violations.append(path.relative_to(repo_root))
            continue
        matched_records = sum(
            1 for marker in record_markers if normalize(marker) in normalized_text
        )
        if matched_records >= 2:
            violations.append(path.relative_to(repo_root))
    return violations


def validate_repository(repo_root: Path = REPO_ROOT) -> list[RuleResult]:
    repo_root = repo_root.resolve()
    texts, load_error = read_required_texts(repo_root)
    reference_path = TARGETS["missing_capability_reference"]
    if load_error:
        return [
            result(
                "WWMC001",
                False,
                reference_path,
                "Dormant Missing Capability Reference",
                load_error,
            )
        ]

    reference_fragments = [
        "# Task Runtime Missing Capability Contract",
        "dormant",
        "internal hooks",
        "quality gates",
        "scoring",
        "repair authorization",
        "re-verification",
        "close gates",
        "final human judgment",
        "recovery requirements",
        "checkpoints",
        "Legacy rounds must not persist or consult these records as lifecycle authority",
        *[f"{record}: []" for record in RECORD_FAMILIES],
    ]
    skill_fragments = [
        "references/task-runtime-missing-capabilities.md",
        "missing capability records",
        "internal hooks",
        "quality gates/scoring",
        "repair authorization/re-verification",
        "close gates",
        "final human judgment",
        "recovery requirements",
        "checkpoints",
        "dormant missing-capability fields",
        "must not be consumed as lifecycle authority",
        "lifecycle_protocol: legacy",
    ]
    readme_fragments = [
        "references/task-runtime-missing-capabilities.md",
        "dormant internal hook",
        "quality gate/scoring",
        "repair/re-verification",
        "close gate",
        "final human judgment",
        "recovery requirement",
        "checkpoint contract",
        "do not treat dormant missing-capability fields or references as active lifecycle authority",
        "Lifecycle Protocol: legacy",
    ]
    dispatch_fragments = [
        "Section Missing Capability Records",
        "`task-runtime-v1` only",
        "Omit the entire block for `legacy` rounds",
        *[f"{record}: []" for record in RECORD_FAMILIES],
        "legacy rounds must omit this entire authority block",
    ]
    packet_fragments = [
        "Future task-runtime packets may additionally carry",
        *SOURCE_CONTEXT_FIELDS,
        "These fields are dormant source-context fields until `task-runtime-v1` activation",
        "They do not authorize packet creation",
        "runtime-state changes while the source protocol is `legacy`",
    ]
    brief_fragments = [
        "`missing_capability_preparation`",
        "expected internal hooks by lifecycle phase",
        "expected quality gate profile and hard blockers",
        "expected score dimensions and required evidence inputs",
        "expected repair authorization triggers and target-lineage rules",
        "expected re-verification requirements after repair",
        "expected close-gate inputs and final human judgment package",
        "expected recovery requirement and checkpoint triggers",
        "explicit note that legacy rounds do not use these records as lifecycle authority",
    ]
    legacy_violations = legacy_dispatch_authority_violations(repo_root)

    return [
        result(
            "WWMC001",
            contains_all(texts["missing_capability_reference"], reference_fragments),
            reference_path,
            "Dormant Missing Capability Reference",
            (
                "`task-runtime-missing-capabilities.md` must exist and define "
                "the dormant hook, gate, score, repair, re-verification, close, "
                "final judgment, recovery, checkpoint, record-family, and legacy "
                "non-authority contract."
            ),
        ),
        result(
            "WWMC002",
            contains_all(texts["skill"], skill_fragments),
            TARGETS["skill"],
            "SKILL Reference Linkage",
            (
                "SKILL.md must link to task-runtime-missing-capabilities and "
                "state that dormant missing-capability fields are not legacy "
                "lifecycle authority."
            ),
        ),
        result(
            "WWMC003",
            contains_all(texts["readme"], readme_fragments),
            TARGETS["readme"],
            "README Guidance",
            (
                "README.md must document the missing-capability reference and "
                "the legacy non-authority boundary."
            ),
        ),
        result(
            "WWMC004",
            contains_all(texts["dispatch_template"], dispatch_fragments),
            TARGETS["dispatch_template"],
            "Dispatch Template Missing Capability Block",
            (
                "Dispatch plan template must carry the dormant task-runtime-v1 "
                "missing capability block, all record families, and the legacy "
                "omission rule."
            ),
        ),
        result(
            "WWMC005",
            contains_all(texts["packet_contract"], packet_fragments),
            TARGETS["packet_contract"],
            "Packet Contract Dormant Source Context",
            (
                "Packet contract must include missing-capability source-context "
                "fields and mark them dormant/non-authorizing under legacy."
            ),
        ),
        result(
            "WWMC006",
            contains_all(texts["working_brief"], brief_fragments),
            TARGETS["working_brief"],
            "Working Brief Missing Capability Preparation",
            (
                "Working brief template must record missing_capability_preparation "
                "fields and the legacy non-authority note."
            ),
        ),
        result(
            "WWMC007",
            not legacy_violations,
            Path("docs/cases"),
            "Legacy Round Non-Authority",
            (
                "Legacy dispatch plans must not render active missing-capability "
                f"authority blocks or record families: "
                f"{', '.join(path.as_posix() for path in legacy_violations)}"
            ),
        ),
    ]


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
        results = validate_repository(args.repo_root)
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

    return 0 if all(result.passed for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
