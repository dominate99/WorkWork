from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = REPO_ROOT / "plugins/workwork/skills/ww-subagent-orchestrator"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the full WorkWork repository validation suite."
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="as_json",
        help="Emit aggregate machine-readable JSON output.",
    )
    return parser.parse_args()


def run_check(
    label: str,
    command: list[str],
    as_json: bool,
    supports_json: bool = True,
) -> dict:
    effective_command = command + (["--json"] if as_json and supports_json else [])
    if not as_json:
        print(f"==> {label}", flush=True)

    completed = subprocess.run(
        effective_command,
        cwd=REPO_ROOT,
        capture_output=as_json,
        text=as_json,
    )

    if as_json:
        payload = None
        stdout = completed.stdout.strip()
        stderr = completed.stderr.strip()
        error = None
        if supports_json:
            if not stdout:
                error = stderr or "JSON-capable child validator returned no output."
            else:
                try:
                    payload = json.loads(stdout)
                except json.JSONDecodeError as exc:
                    error = f"Invalid JSON from child validator: {exc}"
                else:
                    if not isinstance(payload, dict):
                        error = "Child validator JSON payload must be an object."
                    elif payload.get("ok") is not True:
                        error = "Child validator JSON payload did not report ok: true."
        elif completed.returncode != 0 and stderr:
            error = stderr

        ok = completed.returncode == 0 and error is None
        return {
            "label": label,
            "ok": ok,
            "exit_code": completed.returncode,
            "payload": payload,
            "stdout": stdout,
            "stderr": stderr,
            "error": error,
        }

    if completed.returncode != 0:
        print(f"{label} failed with exit code {completed.returncode}.")

    return {
        "label": label,
        "ok": completed.returncode == 0,
        "exit_code": completed.returncode,
    }


def build_checks(python: str) -> list[tuple[str, list[str], bool]]:
    return [
        (
            "SKILL.md frontmatter validation",
            [python, "tools/quick_validate.py", str(SKILL_DIR)],
            False,
        ),
        (
            "Worker work-mode contract validation",
            [python, "tools/validate_ww_worker_work_mode.py"],
            True,
        ),
        (
            "Reviewer and explorer role-contract validation",
            [python, "tools/validate_ww_role_contracts.py"],
            True,
        ),
        (
            "Grill-me inline planning contract validation",
            [python, "tools/validate_ww_grill_me_contracts.py"],
            True,
        ),
        (
            "Persona runtime-selection recording contract validation",
            [python, "tools/validate_ww_persona_selection_contracts.py"],
            True,
        ),
        (
            "Runtime persona packet artifact validation",
            [python, "tools/validate_ww_persona_packets.py"],
            True,
        ),
        (
            "Case-based path identity contract validation",
            [python, "tools/validate_ww_case_path_identity.py"],
            True,
        ),
        (
            "Case artifact contract validation",
            [python, "tools/validate_ww_case_contracts.py"],
            True,
        ),
        (
            "Round lifecycle contract validation",
            [python, "tools/validate_ww_round_lifecycle.py"],
            True,
        ),
        (
            "Verifier/lane authority contract validation",
            [python, "tools/validate_ww_verifier_authority_contracts.py"],
            True,
        ),
        (
            "Missing-capability contract validation",
            [python, "tools/validate_ww_missing_capability_contracts.py"],
            True,
        ),
        (
            "Case scaffold regression tests",
            [
                python,
                "-m",
                "unittest",
                "tools.test_scaffold_ww_case_artifacts",
                "-v",
            ],
            False,
        ),
    ]


def main() -> int:
    args = parse_args()
    checks = build_checks(sys.executable)

    failed = False
    check_results = []
    for label, command, supports_json in checks:
        result = run_check(label, command, args.as_json, supports_json)
        check_results.append(result)
        if not result["ok"]:
            failed = True

    if args.as_json:
        payload = {
            "ok": not failed,
            "check_failures": sum(1 for result in check_results if not result["ok"]),
            "checks": check_results,
        }
        print(json.dumps(payload, indent=2))
        return 0 if not failed else 1

    if failed:
        print("WW repository validation failed.")
        return 1

    print("WW repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
