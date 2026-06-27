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
    "verification_reference": SKILL_ROOT / "references/task-runtime-verification.md",
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
        description=(
            "Validate dormant WorkWork verifier/lane authority contract surfaces."
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
            if name == "verification_reference":
                return texts, "Missing `references/task-runtime-verification.md`."
            return texts, f"Missing required contract file `{relative.as_posix()}`."
        texts[name] = path.read_text(encoding="utf-8")
    return texts, ""


def legacy_dispatch_authority_violations(repo_root: Path) -> list[Path]:
    docs_root = repo_root / "docs" / "cases"
    if not docs_root.exists():
        return []
    violations: list[Path] = []
    for path in docs_root.rglob("dispatch-plan.md"):
        text = path.read_text(encoding="utf-8")
        if "Lifecycle Protocol: legacy" not in text:
            continue
        normalized_text = normalize(text)
        if (
            "## section verification lanes" in normalized_text
            or "verifier_lanes:" in normalized_text
            or "evidence_bundles:" in normalized_text
            or "model_resolutions:" in normalized_text
        ):
            violations.append(path.relative_to(repo_root))
    return violations


def validate_repository(repo_root: Path = REPO_ROOT) -> list[RuleResult]:
    repo_root = repo_root.resolve()
    texts, load_error = read_required_texts(repo_root)
    verification_path = TARGETS["verification_reference"]
    if load_error:
        return [
            result(
                "WWVA001",
                False,
                verification_path,
                "Dormant Verification Reference",
                load_error,
            )
        ]

    reference_fragments = [
        "# Task Runtime Verification Contract",
        "dormant",
        "verifier authority",
        "verification lanes",
        "evidence records",
        "lane selection",
        "model capability resolution",
        "Legacy rounds must not persist or consult these records as lifecycle authority",
    ]
    skill_fragments = [
        "references/task-runtime-verification.md",
        "verifier authority",
        "verifier lane schema",
        "evidence records",
        "baseline/risk-triggered lane selection",
        "model capability profile/floor/resolution",
        "dormant verifier fields",
        "must not be consumed as lifecycle authority",
        "lifecycle_protocol: legacy",
    ]
    readme_fragments = [
        "references/task-runtime-verification.md",
        "dormant verifier authority",
        "lane schema",
        "model capability contract",
        "do not treat dormant verifier fields or references as active lifecycle authority",
        "Lifecycle Protocol: legacy",
    ]
    dispatch_fragments = [
        "Section Verification Lanes",
        "`task-runtime-v1` only",
        "Omit the entire block for `legacy` rounds",
        "verifier_lanes:",
        "verification_target_ref:",
        "evidence_requirements:",
        "freshness_policy:",
        "model_capability_profile:",
        "minimum_capability_floor:",
        "model_resolutions:",
    ]
    packet_fragments = [
        "`runtime_role` must be exactly one of `orchestrator`, `worker`, `reviewer`, or `explorer`",
        "future `task-runtime-v1` verifier packets require `runtime_role: verifier` only after a separately approved verifier role binding exists",
        "Future verifier packets additionally require",
        "`source_verifier_lane`",
        "`authority_subject`",
        "`verification_target_ref`",
        "`evidence_requirements[]`",
        "`model_capability_profile`",
        "`minimum_capability_floor`",
        "`model_resolution`",
        "These fields are dormant contract fields until `task-runtime-v1` activation",
        "They do not authorize verifier packet creation while the source protocol is `legacy`",
    ]
    brief_fragments = [
        "`verification_authority_notes`",
        "`verification_lane_preparation`",
        "candidate baseline verifier lanes by task profile",
        "candidate risk-triggered verifier lanes with rationale",
        "expected evidence kinds: command, artifact, and/or environment",
        "expected model capability profile and minimum floor",
        "explicit note that legacy rounds do not use these records as lifecycle authority",
    ]
    legacy_violations = legacy_dispatch_authority_violations(repo_root)

    return [
        result(
            "WWVA001",
            contains_all(texts["verification_reference"], reference_fragments),
            verification_path,
            "Dormant Verification Reference",
            (
                "`task-runtime-verification.md` must exist and define the "
                "dormant verifier authority, lane, evidence, selection, model "
                "capability, and legacy non-authority contract."
            ),
        ),
        result(
            "WWVA002",
            contains_all(texts["skill"], skill_fragments),
            TARGETS["skill"],
            "SKILL Reference Linkage",
            (
                "SKILL.md must link to task-runtime-verification and state "
                "that dormant verifier fields are not legacy lifecycle authority."
            ),
        ),
        result(
            "WWVA003",
            contains_all(texts["readme"], readme_fragments),
            TARGETS["readme"],
            "README Guidance",
            (
                "README.md must document the verifier authority reference and "
                "the legacy non-authority boundary."
            ),
        ),
        result(
            "WWVA004",
            contains_all(texts["dispatch_template"], dispatch_fragments),
            TARGETS["dispatch_template"],
            "Dispatch Template Verifier Lane Block",
            (
                "Dispatch plan template must carry the dormant task-runtime-v1 "
                "verifier lane block and required verifier/evidence/model fields."
            ),
        ),
        result(
            "WWVA005",
            contains_all(texts["packet_contract"], packet_fragments),
            TARGETS["packet_contract"],
            "Packet Contract Dormant Verifier Gate",
            (
                "Packet contract must preserve the active legacy runtime_role "
                "gate and mark verifier packet fields as dormant/non-authorizing."
            ),
        ),
        result(
            "WWVA006",
            contains_all(texts["working_brief"], brief_fragments),
            TARGETS["working_brief"],
            "Working Brief Verification Preparation",
            (
                "Working brief template must record verification preparation "
                "fields and the legacy non-authority note."
            ),
        ),
        result(
            "WWVA007",
            not legacy_violations,
            Path("docs/cases"),
            "Legacy Round Non-Authority",
            (
                "Legacy dispatch plans must not render active verifier lane, "
                f"evidence, or model-resolution authority blocks: "
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
