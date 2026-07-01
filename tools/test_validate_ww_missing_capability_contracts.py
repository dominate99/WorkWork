from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from validate_ww_missing_capability_contracts import validate_repository


SKILL_ROOT = Path("plugins/workwork/skills/ww-subagent-orchestrator")
VALIDATOR_PATH = Path(__file__).with_name(
    "validate_ww_missing_capability_contracts.py"
)


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


SOURCE_FIELDS = [
    "source_internal_hook_refs[]",
    "source_quality_gate_ref",
    "source_score_ref",
    "source_repair_ref",
    "source_reverification_requirement_ref",
    "source_close_gate_ref",
    "source_final_judgment_ref",
    "source_recovery_requirement_ref",
    "source_checkpoint_ref",
]


def write_text(root: Path, relative: Path, content: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def make_valid_repo(root: Path) -> None:
    write_text(
        root,
        SKILL_ROOT / "references/task-runtime-missing-capabilities.md",
        f"""# Task Runtime Missing Capability Contract

This dormant contract defines internal hooks, quality gates, scoring, repair
authorization, re-verification, close gates, final human judgment, recovery
requirements, and checkpoints.

Legacy rounds must not persist or consult these records as lifecycle authority.

```yaml
{chr(10).join(f"{record}: []" for record in RECORD_FAMILIES)}
```
""",
    )
    write_text(
        root,
        SKILL_ROOT / "SKILL.md",
        """# WW Subagent Orchestrator

`task-runtime-v1` missing capability records for internal hooks, quality
gates/scoring, repair authorization/re-verification, close gates, final human
judgment, recovery requirements, and checkpoints are defined in
`references/task-runtime-missing-capabilities.md`.

Dormant missing-capability fields in templates, references, packets, or
planning notes must not be consumed as lifecycle authority while
`lifecycle_protocol: legacy`.
""",
    )
    write_text(
        root,
        Path("README.md"),
        """# WorkWork

Treat `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`
as the dormant internal hook, quality gate/scoring, repair/re-verification,
close gate, final human judgment, recovery requirement, and checkpoint
contract.

Do not treat dormant missing-capability fields or references as active
lifecycle authority while a round uses `Lifecycle Protocol: legacy`.
""",
    )
    write_text(
        root,
        SKILL_ROOT / "assets/dispatch-plan-template.md",
        f"""# Dispatch Plan

- Lifecycle Protocol: legacy | task-runtime-v1

### Section Missing Capability Records: Example (`task-runtime-v1` only)

Render this block only when the approved round protocol is `task-runtime-v1`.
Omit the entire block for `legacy` rounds.

```yaml
{chr(10).join(f"{record}: []" for record in RECORD_FAMILIES)}
```

Missing capability record rules:

- these records are section-scoped guard, gate, recovery, or decision records
- legacy rounds must omit this entire authority block
""",
    )
    write_text(
        root,
        SKILL_ROOT / "references/subagent-packet-contract.md",
        f"""# Subagent Packet Contract

Future task-runtime packets may additionally carry, after a separately approved
activation round implements the corresponding runtime behavior:

{chr(10).join(f"- `{field}`" for field in SOURCE_FIELDS)}

These fields are dormant source-context fields until `task-runtime-v1`
activation. They do not authorize packet creation, target mutation, evidence
acceptance, scoring, repair, close, final judgment, lifecycle phase changes, or
runtime-state changes while the source protocol is `legacy`.
""",
    )
    write_text(
        root,
        SKILL_ROOT / "references/working-brief-template.md",
        """# Working Brief Template

- `missing_capability_preparation` when a future `task-runtime-v1` round will need internal hooks, quality gates/scoring, repair/re-verification, close gates, final human judgment, recovery requirements, or checkpoints

`missing_capability_preparation` is dormant planning analysis unless the
approved dispatch plan selects `task-runtime-v1`.

- expected internal hooks by lifecycle phase
- expected quality gate profile and hard blockers
- expected score dimensions and required evidence inputs
- expected repair authorization triggers and target-lineage rules
- expected re-verification requirements after repair
- expected close-gate inputs and final human judgment package
- expected recovery requirement and checkpoint triggers
- explicit note that legacy rounds do not use these records as lifecycle authority
""",
    )
    write_text(
        root,
        Path("docs/cases/example/rounds/2026-06-01-example/dispatch-plan.md"),
        """# Dispatch Plan

- Lifecycle Protocol: legacy
- Plan State: completed

## Notes

This legacy plan may mention internal hooks or close gates in historical prose,
but it does not render missing-capability authority blocks.
""",
    )


class MissingCapabilityContractValidatorTests(unittest.TestCase):
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
            (
                root
                / SKILL_ROOT
                / "references/task-runtime-missing-capabilities.md"
            ).unlink()
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWMC001")

    def test_rejects_skill_without_reference_link(self) -> None:
        results = self.mutate(
            SKILL_ROOT / "SKILL.md",
            "references/task-runtime-missing-capabilities.md",
            "references/task-runtime-lifecycle.md",
        )
        self.assert_rule_fails(results, "WWMC002")

    def test_rejects_readme_without_legacy_non_authority_note(self) -> None:
        results = self.mutate(
            Path("README.md"),
            "Do not treat dormant missing-capability fields or references as active",
            "Missing capability fields are active",
        )
        self.assert_rule_fails(results, "WWMC003")

    def test_rejects_dispatch_template_missing_record_family(self) -> None:
        results = self.mutate(
            SKILL_ROOT / "assets/dispatch-plan-template.md",
            "review_synthesis_records: []",
            "review_records: []",
        )
        self.assert_rule_fails(results, "WWMC004")

    def test_rejects_packet_contract_without_source_context_dormant_gate(self) -> None:
        results = self.mutate(
            SKILL_ROOT / "references/subagent-packet-contract.md",
            "These fields are dormant source-context fields until `task-runtime-v1`",
            "These fields are active source-context fields during `legacy`",
        )
        self.assert_rule_fails(results, "WWMC005")

    def test_rejects_working_brief_without_missing_capability_preparation(self) -> None:
        results = self.mutate(
            SKILL_ROOT / "references/working-brief-template.md",
            "expected internal hooks by lifecycle phase",
            "expected runtime notes by lifecycle phase",
        )
        self.assert_rule_fails(results, "WWMC006")

    def test_rejects_legacy_dispatch_with_active_missing_capability_block(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            path = (
                root
                / "docs/cases/example/rounds/2026-06-01-example/dispatch-plan.md"
            )
            path.write_text(
                path.read_text(encoding="utf-8")
                + "\n### Section Missing Capability Records\n\n"
                + "```yaml\ninternal_hook_records: []\nquality_gate_records: []\n```\n",
                encoding="utf-8",
            )
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWMC007")

    def test_rejects_legacy_dispatch_with_heading_only_missing_capability_block(
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
                + "\n### Section Missing Capability Records\n\n"
                + "This heading is reserved for task-runtime-v1 authority records.\n",
                encoding="utf-8",
            )
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWMC007")

    def test_rejects_legacy_dispatch_with_single_record_family_assignment(
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
                + "\n```yaml\ninternal_hook_records: []\n```\n",
                encoding="utf-8",
            )
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWMC007")

    def test_rejects_legacy_dispatch_with_multiple_record_family_assignments(
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
                + "\n```yaml\ninternal_hook_records: []\nclose_gate_records: []\n```\n",
                encoding="utf-8",
            )
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWMC007")

    def test_allows_legacy_dispatch_prose_with_raw_record_family_names(
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
                + "A later task-runtime-v1 plan may discuss `internal_hook_records:` "
                + "and `close_gate_records:` as reference field names, but this "
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
            "WWMC003",
            next(result for result in payload["results"] if not result["passed"])[
                "rule_id"
            ],
        )


if __name__ == "__main__":
    unittest.main()
