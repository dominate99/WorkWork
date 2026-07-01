from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from validate_ww_lifecycle_reference_contracts import validate_repository


SKILL_ROOT = Path("plugins/workwork/skills/ww-subagent-orchestrator")
VALIDATOR_PATH = Path(__file__).with_name(
    "validate_ww_lifecycle_reference_contracts.py"
)


def write_text(root: Path, relative: Path, content: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def make_valid_repo(root: Path) -> None:
    write_text(
        root,
        SKILL_ROOT / "references/task-runtime-lifecycle.md",
        """# Task Runtime Lifecycle Contract

This dormant contract defines lifecycle ownership, phase compatibility,
transitions, persistence, migration, and recovery for task-runtime-v1.

State Ownership separates lifecycle_phase from runtime_state.
Canonical Phase Vocabulary defines legal lifecycle phases.
Snapshot And Event Persistence defines lifecycle snapshots and event history.
Legacy Migration defines when legacy rounds may move to task-runtime-v1.
Invalid States reject writable round-level lifecycle_phase.

Legacy rounds must not persist or consult lifecycle snapshots, event history, or
lifecycle_phase as lifecycle authority.
""",
    )
    write_text(
        root,
        SKILL_ROOT / "SKILL.md",
        """# WW Subagent Orchestrator

`task-runtime-v1` lifecycle ownership, phase compatibility, transitions,
persistence, migration, and recovery are defined in
`references/task-runtime-lifecycle.md`.

Legacy rounds must not persist or consult lifecycle snapshots, event history,
or lifecycle_phase as lifecycle authority.

`lifecycle_phase` never replaces `runtime_state`.
""",
    )
    write_text(
        root,
        Path("README.md"),
        """# WorkWork

Treat `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
as the normative lifecycle ownership, transition, persistence, migration, and
recovery contract.

Do not select `task-runtime-v1` until every activation prerequisite is approved.
Legacy rounds must not treat lifecycle snapshots, event history, or
lifecycle_phase as active lifecycle authority.
""",
    )
    write_text(
        root,
        SKILL_ROOT / "assets/dispatch-plan-template.md",
        """# Dispatch Plan

- Lifecycle Protocol: legacy | task-runtime-v1

### Section Lifecycle Record: Example (`task-runtime-v1` only)

Render this block only when the approved round protocol is `task-runtime-v1`.
Omit the entire block for `legacy` rounds.

```yaml
lifecycle:
  lifecycle_phase:
  phase_entered_at:
  lifecycle_event_history:
    - event_id:
      event_type:
      lifecycle_phase:
      runtime_state:
```

Lifecycle record rules:

- canonical `runtime_state` remains only in the section runtime ledger and must not be duplicated inside `lifecycle`
- only the orchestrator may append an accepted lifecycle event or change `lifecycle_phase`
- `next_action.code` is derived from the canonical phase/state table in `references/task-runtime-lifecycle.md`
- legacy rounds must omit this entire authority block
""",
    )
    write_text(
        root,
        SKILL_ROOT / "references/subagent-packet-contract.md",
        """# Subagent Packet Contract

Lifecycle source context:

- packets from `legacy` rounds omit `source_lifecycle_snapshot` and must not infer a phase from legacy fields
- packets from `task-runtime-v1` rounds additionally require `source_lifecycle_snapshot` copied from the source section at packet creation time
- `source_lifecycle_snapshot` contains an immutable copy of the source section's `lifecycle` block plus its separately copied canonical `runtime_state`
- packet lifecycle data is read-only source context; packets never own phase transitions or append lifecycle events
""",
    )
    write_text(
        root,
        SKILL_ROOT / "references/working-brief-template.md",
        """# Working Brief Template

- `lifecycle_protocol_recommendation: legacy | task-runtime-v1`

Protocol recommendation guidance:

- recommend `task-runtime-v1` only when the round intends explicit activation and every mandatory capability in `task-runtime-lifecycle.md`, `task-runtime-verification.md`, and `task-runtime-missing-capabilities.md` is available
- default the recommendation to `legacy`
- working brief lifecycle recommendations are planning notes only and do not create lifecycle authority
""",
    )
    write_text(
        root,
        Path("docs/cases/example/rounds/2026-06-01-example/dispatch-plan.md"),
        """# Dispatch Plan

- Lifecycle Protocol: legacy
- Plan State: completed

## Notes

This legacy plan may mention lifecycle snapshots or event history in historical
prose, but it does not render lifecycle authority blocks.
""",
    )


class LifecycleReferenceContractValidatorTests(unittest.TestCase):
    def assert_rule_fails(self, results: list, rule_id: str) -> None:
        failures = [result.rule_id for result in results if not result.passed]
        self.assertEqual([rule_id], failures, results)

    def mutate(self, relative: Path, old: str, new: str) -> list:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            path = root / relative
            content = path.read_text(encoding="utf-8")
            self.assertEqual(1, content.count(old), old)
            path.write_text(content.replace(old, new, 1), encoding="utf-8")
            return validate_repository(root)

    def test_accepts_complete_contract(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            results = validate_repository(root)
        self.assertTrue(all(result.passed for result in results), results)

    def test_rejects_missing_reference_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            (root / SKILL_ROOT / "references/task-runtime-lifecycle.md").unlink()
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWLC001")

    def test_rejects_skill_without_lifecycle_reference_link(self) -> None:
        results = self.mutate(
            SKILL_ROOT / "SKILL.md",
            "references/task-runtime-lifecycle.md",
            "references/task-runtime-verification.md",
        )
        self.assert_rule_fails(results, "WWLC002")

    def test_rejects_readme_without_lifecycle_guidance(self) -> None:
        results = self.mutate(
            Path("README.md"),
            "normative lifecycle ownership, transition, persistence, migration, and\nrecovery contract",
            "normative runtime notes",
        )
        self.assert_rule_fails(results, "WWLC003")

    def test_rejects_dispatch_template_without_legacy_omission_rule(self) -> None:
        results = self.mutate(
            SKILL_ROOT / "assets/dispatch-plan-template.md",
            "legacy rounds must omit this entire authority block",
            "legacy rounds may render this authority block",
        )
        self.assert_rule_fails(results, "WWLC004")

    def test_rejects_packet_contract_without_source_context_gate(self) -> None:
        results = self.mutate(
            SKILL_ROOT / "references/subagent-packet-contract.md",
            "packets from `legacy` rounds omit `source_lifecycle_snapshot`",
            "packets from `legacy` rounds include `source_lifecycle_snapshot`",
        )
        self.assert_rule_fails(results, "WWLC005")

    def test_rejects_working_brief_without_protocol_recommendation(self) -> None:
        results = self.mutate(
            SKILL_ROOT / "references/working-brief-template.md",
            "`lifecycle_protocol_recommendation: legacy | task-runtime-v1`",
            "`runtime_protocol_recommendation: legacy | task-runtime-v1`",
        )
        self.assert_rule_fails(results, "WWLC006")

    def test_rejects_legacy_dispatch_with_active_lifecycle_block(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            path = (
                root
                / "docs/cases/example/rounds/2026-06-01-example/dispatch-plan.md"
            )
            path.write_text(
                path.read_text(encoding="utf-8")
                + "\n### Section Lifecycle Record\n\n"
                + "```yaml\nlifecycle:\n  lifecycle_phase: plan\n```\n",
                encoding="utf-8",
            )
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWLC007")

    def test_rejects_legacy_dispatch_with_heading_only_lifecycle_block(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            path = (
                root
                / "docs/cases/example/rounds/2026-06-01-example/dispatch-plan.md"
            )
            path.write_text(
                path.read_text(encoding="utf-8")
                + "\n### Section Lifecycle Record\n\n"
                + "This heading is reserved for task-runtime-v1 authority records.\n",
                encoding="utf-8",
            )
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWLC007")

    def test_rejects_legacy_dispatch_with_single_lifecycle_assignment(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            path = (
                root
                / "docs/cases/example/rounds/2026-06-01-example/dispatch-plan.md"
            )
            path.write_text(
                path.read_text(encoding="utf-8")
                + "\n```yaml\nlifecycle_snapshot: {}\n```\n",
                encoding="utf-8",
            )
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWLC007")

    def test_rejects_legacy_dispatch_with_multiple_lifecycle_assignments(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            path = (
                root
                / "docs/cases/example/rounds/2026-06-01-example/dispatch-plan.md"
            )
            path.write_text(
                path.read_text(encoding="utf-8")
                + "\n```yaml\nlifecycle_phase: verify\nlifecycle_event_history: []\n```\n",
                encoding="utf-8",
            )
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWLC007")

    def test_allows_legacy_dispatch_prose_with_raw_lifecycle_field_names(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            path = (
                root
                / "docs/cases/example/rounds/2026-06-01-example/dispatch-plan.md"
            )
            path.write_text(
                path.read_text(encoding="utf-8")
                + "\n## Historical Notes\n\n"
                + "A later task-runtime-v1 plan may discuss `lifecycle_snapshot:` "
                + "or `lifecycle_phase:` as reference field names, but this "
                + "legacy plan does not assign those fields.\n",
                encoding="utf-8",
            )
            results = validate_repository(root)
        self.assertTrue(all(result.passed for result in results), results)

    def test_cli_json_failure_schema(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            workspace = Path(temp_dir)
            root = workspace / "fixture"
            cwd = workspace / "elsewhere"
            cwd.mkdir()
            make_valid_repo(root)
            (root / "README.md").write_text("# WorkWork\n", encoding="utf-8")
            completed = subprocess.run(
                [
                    sys.executable,
                    str(VALIDATOR_PATH),
                    "--repo-root",
                    str(root),
                    "--json",
                ],
                cwd=cwd,
                check=False,
                capture_output=True,
                text=True,
            )
        payload = json.loads(completed.stdout)
        self.assertEqual(1, completed.returncode, completed)
        self.assertFalse(payload["ok"])
        self.assertEqual(1, payload["rule_failures"])
        self.assertEqual(
            "WWLC003",
            next(result for result in payload["results"] if not result["passed"])[
                "rule_id"
            ],
        )


if __name__ == "__main__":
    unittest.main()
