from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
CASES_ROOT = REPO_ROOT / "docs" / "cases"
FORBIDDEN_CASE_KEYS = {
    "Plan State",
    "Runtime State",
    "Section State",
    "Human Decision",
    "Current Choice",
    "Approval Time",
    "Close State",
    "Last Approved Revision",
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
        description="Validate WorkWork round lifecycle ownership rules."
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="as_json",
        help="Emit machine-readable JSON output.",
    )
    return parser.parse_args()


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def make_result(rule_id: str, passed: bool, file: Path, section: str, message: str) -> RuleResult:
    return RuleResult(rule_id=rule_id, passed=passed, file=rel(file), section=section, message=message)


def parse_case_md(case_path: Path) -> dict:
    text = case_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    bullets: dict[str, str] = {}
    round_index_entries: list[str] = []
    in_round_index = False

    for line in lines:
        stripped = line.strip()
        if stripped == "## Round Index":
            in_round_index = True
            continue
        if stripped.startswith("## ") and stripped != "## Round Index":
            in_round_index = False
        if in_round_index and stripped.startswith("- `") and stripped.endswith("`"):
            round_index_entries.append(stripped[3:-1])
        if stripped.startswith("- ") and ":" in stripped:
            key, value = stripped[2:].split(":", 1)
            bullets[key.strip()] = value.strip()

    current_round = bullets.get("Current Round", "").strip("`")
    return {
        "bullets": bullets,
        "current_round": current_round,
        "round_index_entries": round_index_entries,
    }


def parse_dispatch_plan(plan_path: Path) -> dict:
    text = plan_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    bullets: dict[str, str] = {}
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("- ") and ":" in stripped:
            key, value = stripped[2:].split(":", 1)
            bullets[key.strip()] = value.strip()
    return {
        "text": text,
        "bullets": bullets,
    }


def validate_case_lifecycle(case_dir: Path, results: list[RuleResult]) -> None:
    case_md = case_dir / "case.md"
    if not case_md.exists():
        return

    parsed_case = parse_case_md(case_md)
    rounds_dir = case_dir / "rounds"
    round_dirs = sorted(path.name for path in rounds_dir.iterdir() if path.is_dir()) if rounds_dir.exists() else []
    current_round = parsed_case["current_round"]

    latest_round = round_dirs[-1] if round_dirs else ""
    results.append(
        make_result(
            "WWRL001",
            current_round == latest_round,
            case_md,
            "Current Round Freshness",
            "Current Round points to the newest active round."
            if current_round == latest_round
            else f"Expected Current Round `{latest_round}`, found `{current_round}`.",
        )
    )

    results.append(
        make_result(
            "WWRL002",
            current_round in round_dirs,
            case_md,
            "Current Round Presence",
            "Current Round resolves to an existing round directory."
            if current_round in round_dirs
            else f"Current Round `{current_round}` does not resolve to an existing round directory.",
        )
    )

    results.append(
        make_result(
            "WWRL003",
            current_round in parsed_case["round_index_entries"],
            case_md,
            "Round Index Membership",
            "Current Round is present in Round Index."
            if current_round in parsed_case["round_index_entries"]
            else "Current Round is missing from Round Index.",
        )
    )

    forbidden_present = sorted(key for key in parsed_case["bullets"] if key in FORBIDDEN_CASE_KEYS)
    results.append(
        make_result(
            "WWRL004",
            not forbidden_present,
            case_md,
            "Case Lifecycle Authority",
            "case.md does not duplicate round approval or runtime state."
            if not forbidden_present
            else f"case.md contains forbidden lifecycle authority field(s): {', '.join(forbidden_present)}",
        )
    )

    for round_name in round_dirs:
        round_root = rounds_dir / round_name
        dispatch_plan = round_root / "dispatch-plan.md"
        if not dispatch_plan.exists():
            continue
        parsed_dispatch = parse_dispatch_plan(dispatch_plan)
        has_plan_state = "Plan State" in parsed_dispatch["bullets"]
        results.append(
            make_result(
                "WWRL005",
                has_plan_state,
                dispatch_plan,
                "Dispatch Plan State",
                "dispatch-plan.md declares Plan State."
                if has_plan_state
                else "dispatch-plan.md is missing Plan State.",
            )
        )

        has_human_decision = "Human Decision" in parsed_dispatch["bullets"]
        results.append(
            make_result(
                "WWRL006",
                has_human_decision,
                dispatch_plan,
                "Dispatch Human Decision",
                "dispatch-plan.md declares Human Decision."
                if has_human_decision
                else "dispatch-plan.md is missing Human Decision.",
            )
        )

        has_approval_block = "## Approval Block" in parsed_dispatch["text"]
        results.append(
            make_result(
                "WWRL007",
                has_approval_block,
                dispatch_plan,
                "Approval Block Presence",
                "dispatch-plan.md contains an Approval Block."
                if has_approval_block
                else "dispatch-plan.md is missing the Approval Block section.",
            )
        )


def main() -> int:
    args = parse_args()
    results: list[RuleResult] = []
    for case_dir in sorted(path for path in CASES_ROOT.iterdir() if path.is_dir()):
        validate_case_lifecycle(case_dir, results)

    failed = [result for result in results if not result.passed]
    if args.as_json:
        payload = {
            "ok": not failed,
            "rule_failures": len(failed),
            "results": [result.to_dict() for result in results],
        }
        print(json.dumps(payload, indent=2))
        return 0 if not failed else 1

    if failed:
        print(f"FAIL: {len(failed)} rule violations")
        print()
        for result in failed:
            print(f"[{result.rule_id}] {result.file}")
            print(result.message)
            print()
        return 1

    print(f"PASS: {len(results)} rules checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
