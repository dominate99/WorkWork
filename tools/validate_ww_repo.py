from __future__ import annotations

import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = REPO_ROOT / "plugins/workwork/skills/ww-subagent-orchestrator"


def run_check(label: str, command: list[str]) -> int:
    print(f"==> {label}", flush=True)
    completed = subprocess.run(command, cwd=REPO_ROOT)
    if completed.returncode != 0:
        print(f"{label} failed with exit code {completed.returncode}.")
    return completed.returncode


def main() -> int:
    python = sys.executable
    checks = [
        (
            "SKILL.md frontmatter validation",
            [python, "tools/quick_validate.py", str(SKILL_DIR)],
        ),
        (
            "Worker work-mode contract validation",
            [python, "tools/validate_ww_worker_work_mode.py"],
        ),
        (
            "Reviewer and explorer role-contract validation",
            [python, "tools/validate_ww_role_contracts.py"],
        ),
    ]

    failed = False
    for label, command in checks:
        if run_check(label, command) != 0:
            failed = True

    if failed:
        print("WW repository validation failed.")
        return 1

    print("WW repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
