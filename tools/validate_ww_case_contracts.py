from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
CASES_ROOT = REPO_ROOT / "docs" / "cases"
CASE_TEMPLATE = (
    REPO_ROOT
    / "plugins"
    / "workwork"
    / "skills"
    / "ww-subagent-orchestrator"
    / "references"
    / "case-template.md"
)
SCAFFOLD_HELPER = REPO_ROOT / "tools" / "scaffold_ww_case_artifacts.py"
REQUIRED_TEMPLATE_SECTIONS = [
    "## Purpose",
    "## Required Layout",
    "## Required Fields",
    "## Rules",
]
REQUIRED_FIELD_MARKERS = [
    "# Case: <case-slug>",
    "Status",
    "Canonical Root",
    "Current Round",
    "Goal",
    "Legacy Status",
    "## Round Index",
    "## Notes",
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
        description="Validate WorkWork case and round artifact contract surfaces."
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


def extract_section(text: str, heading: str) -> str:
    pattern = rf"{re.escape(heading)}\n(.*?)(?:\n## |\Z)"
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1) if match else ""


def parse_case_md(case_path: Path) -> dict:
    text = case_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    heading = ""
    bullets: dict[str, str] = {}
    current_round = ""
    round_index_entries: list[str] = []
    notes_section_present = "## Notes" in text
    round_index_present = "## Round Index" in text
    in_round_index = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# Case: "):
            heading = stripped
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
    canonical_root = bullets.get("Canonical Root", "").strip("`")

    return {
        "heading": heading,
        "bullets": bullets,
        "current_round": current_round,
        "canonical_root": canonical_root,
        "round_index_present": round_index_present,
        "round_index_entries": round_index_entries,
        "notes_present": notes_section_present,
    }


def case_structure_issues(parsed: dict, case_slug: str, expected_root: str) -> list[str]:
    required_checks = {
        "# Case: <case-slug>": parsed["heading"] == f"# Case: {case_slug}",
        "Status": "Status" in parsed["bullets"],
        "Canonical Root": "Canonical Root" in parsed["bullets"],
        "Current Round": "Current Round" in parsed["bullets"],
        "Goal": "Goal" in parsed["bullets"],
        "Legacy Status": "Legacy Status" in parsed["bullets"],
        "## Round Index": parsed["round_index_present"],
        "## Notes": parsed["notes_present"],
    }
    issues = [label for label, passed in required_checks.items() if not passed]
    if parsed["canonical_root"] != expected_root:
        issues.append(f"Canonical Root != `{expected_root}`")
    if not parsed["current_round"] or parsed["current_round"] not in parsed["round_index_entries"]:
        issues.append("Current Round missing from Round Index")
    return issues


def validate_case_template(results: list[RuleResult]) -> list[str]:
    required_fields = REQUIRED_FIELD_MARKERS.copy()
    if not CASE_TEMPLATE.exists():
        results.append(
            RuleResult(
                "WWCC001",
                False,
                rel(CASE_TEMPLATE),
                "Template Presence",
                "Missing dedicated case template.",
            )
        )
        return required_fields

    text = CASE_TEMPLATE.read_text(encoding="utf-8")
    results.append(
        make_result("WWCC001", True, CASE_TEMPLATE, "Template Presence", "case-template.md exists.")
    )

    missing_sections = [section for section in REQUIRED_TEMPLATE_SECTIONS if section not in text]
    results.append(
        make_result(
            "WWCC002",
            not missing_sections,
            CASE_TEMPLATE,
            "Template Sections",
            "Template contains all required sections."
            if not missing_sections
            else f"Missing required template section(s): {', '.join(missing_sections)}",
        )
    )

    required_fields_section = extract_section(text, "## Required Fields")
    template_markers = [
        line.strip()[2:].strip().strip("`")
        for line in required_fields_section.splitlines()
        if line.strip().startswith("- ")
    ]
    missing_markers = [marker for marker in required_fields if marker not in template_markers]
    results.append(
        make_result(
            "WWCC003",
            not missing_markers,
            CASE_TEMPLATE,
            "Template Field Markers",
            "Template enumerates all required case markers."
            if not missing_markers
            else f"Missing required marker(s) in case template: {', '.join(missing_markers)}",
        )
    )
    return required_fields


def validate_case_roots(results: list[RuleResult]) -> None:
    case_dirs = [path for path in CASES_ROOT.iterdir() if path.is_dir()]
    missing_case_md = [path.name for path in case_dirs if not (path / "case.md").exists()]
    results.append(
        RuleResult(
            "WWCC004",
            not missing_case_md,
            rel(CASES_ROOT),
            "Case Root Presence",
            "Every case root has a case.md entrypoint."
            if not missing_case_md
            else f"Missing case.md for case root(s): {', '.join(sorted(missing_case_md))}",
        )
    )

    for case_dir in case_dirs:
        case_md = case_dir / "case.md"
        if not case_md.exists():
            continue
        parsed = parse_case_md(case_md)
        expected_root = f"docs/cases/{case_dir.name}/"
        failed_keys = case_structure_issues(parsed, case_dir.name, expected_root)
        results.append(
            make_result(
                "WWCC005",
                not failed_keys,
                case_md,
                "Case Required Fields",
                "case.md contains the required headings and fields."
                if not failed_keys
                else f"case.md is missing required field(s): {', '.join(failed_keys)}",
            )
        )

        results.append(
            make_result(
                "WWCC006",
                parsed["canonical_root"] == expected_root,
                case_md,
                "Canonical Root",
                "case.md canonical root matches the case directory."
                if parsed["canonical_root"] == expected_root
                else f"Expected Canonical Root `{expected_root}`, found `{parsed['canonical_root']}`.",
            )
        )

        round_in_index = parsed["current_round"] and parsed["current_round"] in parsed["round_index_entries"]
        results.append(
            make_result(
                "WWCC007",
                round_in_index,
                case_md,
                "Current Round Index",
                "Current Round is present in Round Index."
                if round_in_index
                else "Current Round is missing from Round Index.",
            )
        )

        rounds_dir = case_dir / "rounds"
        missing_round_files: list[str] = []
        if rounds_dir.exists():
            for round_dir in [path for path in rounds_dir.iterdir() if path.is_dir()]:
                required_files = ["working-brief.md", "dispatch-plan.md"]
                for filename in required_files:
                    if not (round_dir / filename).exists():
                        missing_round_files.append(f"{round_dir.name}/{filename}")
        results.append(
            make_result(
                "WWCC008",
                not missing_round_files,
                rounds_dir if rounds_dir.exists() else case_dir,
                "Round Minimum Files",
                "Every round contains working-brief.md and dispatch-plan.md."
                if not missing_round_files
                else f"Missing required round artifact(s): {', '.join(missing_round_files)}",
            )
        )


def run_helper(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCAFFOLD_HELPER), *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


def validate_helper_output(results: list[RuleResult]) -> None:
    tmp_root_base = REPO_ROOT / ".tmp"
    tmp_root_base.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(dir=tmp_root_base) as tmp_dir:
        tmp_root = Path(tmp_dir)

        default_round = "2026-05-24-helper-default"
        default_case = "helper-default-case"
        default_result = run_helper(
            [
                "--case-slug",
                default_case,
                "--round-slug",
                default_round,
                "--title",
                "Helper Default Smoke",
                "--user-request",
                "helper default smoke",
                "--output-root",
                str(tmp_root),
            ]
        )
        results.append(
            RuleResult(
                "WWCC009",
                default_result.returncode == 0,
                rel(SCAFFOLD_HELPER),
                "Helper Default Scaffold",
                "Default helper scaffold completed successfully."
                if default_result.returncode == 0
                else f"Default helper scaffold failed: {default_result.stderr.strip() or default_result.stdout.strip()}",
            )
        )
        if default_result.returncode == 0:
            default_case_root = tmp_root / default_case
            default_round_root = default_case_root / "rounds" / default_round
            default_required = [
                default_case_root / "case.md",
                default_round_root / "working-brief.md",
                default_round_root / "dispatch-plan.md",
            ]
            default_optional = [
                default_round_root / "design-spec.md",
                default_round_root / "implementation-plan.md",
            ]
            default_ok = all(path.exists() for path in default_required) and not any(
                path.exists() for path in default_optional
            )
            results.append(
                RuleResult(
                    "WWCC010",
                    default_ok,
                    rel(SCAFFOLD_HELPER),
                    "Helper Default Outputs",
                    "Default helper output includes case.md, working-brief.md, and dispatch-plan.md only."
                    if default_ok
                    else "Default helper output does not match the required minimum artifact set.",
                )
            )
            if default_case_root.joinpath("case.md").exists():
                parsed_default_case = parse_case_md(default_case_root / "case.md")
                default_expected_root = f"{rel(default_case_root)}/"
                default_issues = case_structure_issues(
                    parsed_default_case, default_case, default_expected_root
                )
                results.append(
                    RuleResult(
                        "WWCC011",
                        not default_issues,
                        rel(SCAFFOLD_HELPER),
                        "Helper Default Case Contract",
                        "Default helper-generated case.md satisfies the case contract."
                        if not default_issues
                        else f"Default helper-generated case.md issues: {', '.join(default_issues)}",
                    )
                )

        optional_round = "2026-05-24-helper-optional"
        optional_case = "helper-optional-case"
        optional_result = run_helper(
            [
                "--case-slug",
                optional_case,
                "--round-slug",
                optional_round,
                "--title",
                "Helper Optional Smoke",
                "--user-request",
                "helper optional smoke",
                "--with-design-spec",
                "--with-implementation-plan",
                "--output-root",
                str(tmp_root),
            ]
        )
        results.append(
            RuleResult(
                "WWCC012",
                optional_result.returncode == 0,
                rel(SCAFFOLD_HELPER),
                "Helper Optional Scaffold",
                "Optional helper scaffold completed successfully."
                if optional_result.returncode == 0
                else f"Optional helper scaffold failed: {optional_result.stderr.strip() or optional_result.stdout.strip()}",
            )
        )
        if optional_result.returncode == 0:
            optional_case_root = tmp_root / optional_case
            optional_round_root = optional_case_root / "rounds" / optional_round
            optional_expected = [
                optional_case_root / "case.md",
                optional_round_root / "working-brief.md",
                optional_round_root / "dispatch-plan.md",
                optional_round_root / "design-spec.md",
                optional_round_root / "implementation-plan.md",
            ]
            optional_ok = all(path.exists() for path in optional_expected)
            results.append(
                RuleResult(
                    "WWCC013",
                    optional_ok,
                    rel(SCAFFOLD_HELPER),
                    "Helper Optional Outputs",
                    "Optional helper output includes design-spec.md and implementation-plan.md when requested."
                    if optional_ok
                    else "Optional helper output is missing one or more requested artifacts.",
                )
            )


def main() -> int:
    args = parse_args()
    results: list[RuleResult] = []
    validate_case_template(results)
    validate_case_roots(results)
    validate_helper_output(results)

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
