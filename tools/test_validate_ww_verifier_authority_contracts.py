from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from validate_ww_verifier_authority_contracts import validate_repository


SKILL_ROOT = Path("plugins/workwork/skills/ww-subagent-orchestrator")
VALIDATOR_PATH = Path(__file__).with_name(
    "validate_ww_verifier_authority_contracts.py"
)


def write_text(root: Path, relative: Path, content: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def make_valid_repo(root: Path) -> None:
    write_text(
        root,
        SKILL_ROOT / "references/task-runtime-verification.md",
        """# Task Runtime Verification Contract

This dormant contract defines verifier authority, verification lanes,
evidence records, lane selection, and model capability resolution.

Legacy rounds must not persist or consult these records as lifecycle authority.
""",
    )
    write_text(
        root,
        SKILL_ROOT / "SKILL.md",
        """# WW Subagent Orchestrator

`task-runtime-v1` verifier authority, verifier lane schema, evidence records,
baseline/risk-triggered lane selection, and model capability profile/floor/resolution
are defined in `references/task-runtime-verification.md`.

Dormant verifier fields in templates, references, packets, or planning notes
must not be consumed as lifecycle authority while `lifecycle_protocol: legacy`.
""",
    )
    write_text(
        root,
        Path("README.md"),
        """# WorkWork

Treat `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
as the dormant verifier authority, lane schema, evidence, lane selection, and
model capability contract.

Do not treat dormant verifier fields or references as active lifecycle authority
while a round uses `Lifecycle Protocol: legacy`.
""",
    )
    write_text(
        root,
        SKILL_ROOT / "assets/dispatch-plan-template.md",
        """# Dispatch Plan

- Lifecycle Protocol: legacy | task-runtime-v1

### Section Verification Lanes: Example (`task-runtime-v1` only)

Render this block only when the approved round protocol is `task-runtime-v1`.
Omit the entire block for `legacy` rounds.

```yaml
worker_lanes: []
verifier_lanes:
  - lane_id:
    lane_type: test-verification | artifact-verification | deployment-verification | configuration-verification
    runtime_role: verifier
    required: true
    selection:
      sources: []
    verification_target_ref:
      target_id:
      target_kind: single | aggregate
    verification_commands: []
    evidence_requirements: []
    freshness_policy:
      target_bound: true
    model_capability_profile:
    model_capability_profile_schema_version: 1
    model_capability_profile_hash:
    minimum_capability_floor:
    minimum_capability_floor_schema_version: 1
    minimum_capability_floor_hash:
model_resolutions: []
```
""",
    )
    write_text(
        root,
        SKILL_ROOT / "references/subagent-packet-contract.md",
        """# Subagent Packet Contract

`persona_binding` contract:

- `runtime_role` must be exactly one of `orchestrator`, `worker`, `reviewer`, or `explorer`
- future `task-runtime-v1` verifier packets require `runtime_role: verifier` only after a separately approved verifier role binding exists

Future verifier packets additionally require, after a separately approved
verifier binding exists:

- `source_verifier_lane`
- `authority_subject`
- `verification_target_ref`
- `verification_commands[]`
- `evidence_requirements[]`
- `freshness_policy`
- `model_capability_profile`
- `minimum_capability_floor`
- `model_resolution`

These fields are dormant contract fields until `task-runtime-v1` activation.
They do not authorize verifier packet creation while the source protocol is
`legacy` or while no approved verifier role binding exists.
""",
    )
    write_text(
        root,
        SKILL_ROOT / "references/working-brief-template.md",
        """# Working Brief Template

- `verification_authority_notes` when a future `task-runtime-v1` round will need formal verifier lanes

## Runtime Preparation

- `verification_lane_preparation` when `lifecycle_protocol_recommendation: task-runtime-v1`

`verification_lane_preparation` is dormant planning analysis unless the approved
dispatch plan selects `task-runtime-v1`.

- candidate baseline verifier lanes by task profile
- candidate risk-triggered verifier lanes with rationale
- expected evidence kinds: command, artifact, and/or environment
- expected model capability profile and minimum floor
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

This legacy plan may mention verifier authority in historical prose, but it does
not render verifier lane authority blocks.
""",
    )


class VerifierAuthorityContractValidatorTests(unittest.TestCase):
    def assert_rule_fails(self, results: list, rule_id: str) -> None:
        failures = [result.rule_id for result in results if not result.passed]
        self.assertEqual([rule_id], failures, results)

    def mutate(
        self,
        relative: Path,
        old: str,
        new: str,
    ) -> list:
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
                / "references/task-runtime-verification.md"
            ).unlink()
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWVA001")

    def test_rejects_skill_without_reference_link(self) -> None:
        results = self.mutate(
            SKILL_ROOT / "SKILL.md",
            "references/task-runtime-verification.md",
            "references/task-runtime-lifecycle.md",
        )
        self.assert_rule_fails(results, "WWVA002")

    def test_rejects_readme_without_legacy_non_authority_note(self) -> None:
        results = self.mutate(
            Path("README.md"),
            "Do not treat dormant verifier fields or references as active lifecycle authority",
            "Verifier fields are lifecycle authority",
        )
        self.assert_rule_fails(results, "WWVA003")

    def test_rejects_dispatch_template_missing_model_resolutions(self) -> None:
        results = self.mutate(
            SKILL_ROOT / "assets/dispatch-plan-template.md",
            "model_resolutions: []",
            "model_resolution_notes: []",
        )
        self.assert_rule_fails(results, "WWVA004")

    def test_rejects_packet_contract_without_active_legacy_role_gate(self) -> None:
        results = self.mutate(
            SKILL_ROOT / "references/subagent-packet-contract.md",
            "`runtime_role` must be exactly one of `orchestrator`, `worker`, `reviewer`, or `explorer`",
            "`runtime_role` must be exactly one of `orchestrator`, `worker`, `reviewer`, `explorer`, or `verifier`",
        )
        self.assert_rule_fails(results, "WWVA005")

    def test_rejects_working_brief_without_verification_preparation(self) -> None:
        results = self.mutate(
            SKILL_ROOT / "references/working-brief-template.md",
            "candidate baseline verifier lanes by task profile",
            "candidate implementation notes",
        )
        self.assert_rule_fails(results, "WWVA006")

    def test_rejects_legacy_dispatch_with_active_verifier_lanes(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            path = (
                root
                / "docs/cases/example/rounds/2026-06-01-example/dispatch-plan.md"
            )
            path.write_text(
                path.read_text(encoding="utf-8")
                + "\n## Section Verification Lanes\n\n```yaml\nverifier_lanes: []\n```\n",
                encoding="utf-8",
            )
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWVA007")

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
        self.assertEqual("WWVA003", next(
            result for result in payload["results"] if not result["passed"]
        )["rule_id"])


if __name__ == "__main__":
    unittest.main()
