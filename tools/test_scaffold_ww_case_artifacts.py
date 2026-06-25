from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools import validate_ww_repo


REPO_ROOT = Path(__file__).resolve().parent.parent
SCAFFOLD = REPO_ROOT / "tools" / "scaffold_ww_case_artifacts.py"


class ScaffoldWwCaseArtifactsTests(unittest.TestCase):
    def test_empty_json_child_marks_repo_check_failed(self) -> None:
        result = validate_ww_repo.run_check(
            "empty json check",
            [sys.executable, "-c", "pass"],
            as_json=True,
            supports_json=True,
        )

        self.assertFalse(result["ok"])
        self.assertIsNotNone(result["error"])

    def test_child_payload_ok_false_marks_repo_check_failed(self) -> None:
        result = validate_ww_repo.run_check(
            "negative json check",
            [sys.executable, "-c", "print('{\"ok\": false}')"],
            as_json=True,
            supports_json=True,
        )

        self.assertFalse(result["ok"])
        self.assertEqual(result["payload"], {"ok": False})
        self.assertIsNotNone(result["error"])

    def test_invalid_json_child_marks_repo_check_failed(self) -> None:
        result = validate_ww_repo.run_check(
            "invalid json check",
            [sys.executable, "-c", "print('not-json')"],
            as_json=True,
            supports_json=True,
        )

        self.assertFalse(result["ok"])
        self.assertIsNotNone(result["error"])

    def test_plain_text_repo_check_does_not_report_json_parse_error(self) -> None:
        result = validate_ww_repo.run_check(
            "plain text check",
            [sys.executable, "-c", "print('ok')"],
            as_json=True,
            supports_json=False,
        )

        self.assertTrue(result["ok"])
        self.assertIsNone(result["payload"])
        self.assertIsNone(result["error"])

    def test_repo_validation_suite_runs_scaffold_regression_tests(self) -> None:
        build_checks = getattr(validate_ww_repo, "build_checks", lambda _python: [])
        commands = [command for _, command, _ in build_checks(sys.executable)]

        self.assertIn(
            [
                sys.executable,
                "-m",
                "unittest",
                "tools.test_scaffold_ww_case_artifacts",
                "-v",
            ],
            commands,
        )

    def test_new_round_defaults_to_schema_v2_legacy_lifecycle_protocol(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_root = Path(temporary_directory) / "cases"
            result = subprocess.run(
                [
                    sys.executable,
                    str(SCAFFOLD),
                    "--case-slug",
                    "runtime-case",
                    "--round-slug",
                    "2026-06-20-runtime-round",
                    "--title",
                    "Runtime Round",
                    "--user-request",
                    "Create a runtime round.",
                    "--output-root",
                    str(output_root),
                    "--json",
                ],
                cwd=REPO_ROOT,
                capture_output=True,
                check=False,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            self.assertTrue(payload["ok"])

            round_root = (
                output_root
                / "runtime-case"
                / "rounds"
                / "2026-06-20-runtime-round"
            )
            brief = (round_root / "working-brief.md").read_text(encoding="utf-8")
            dispatch = (round_root / "dispatch-plan.md").read_text(encoding="utf-8")

            self.assertIn("- `schema_version`: 2", brief)
            self.assertIn("- `lifecycle_protocol_recommendation`: legacy", brief)
            self.assertIn("- Schema Version: 2", dispatch)
            self.assertIn("- Lifecycle Protocol: legacy", dispatch)
            self.assertNotIn("## Lifecycle Snapshot", dispatch)
            self.assertNotIn("## Lifecycle Event History", dispatch)
            self.assertNotIn("\nlifecycle:\n", dispatch)
            self.assertNotIn("\nlifecycle_event_history:\n", dispatch)


if __name__ == "__main__":
    unittest.main()
