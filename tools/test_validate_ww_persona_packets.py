from __future__ import annotations

import hashlib
import tempfile
import unittest
from pathlib import Path

import yaml

from validate_ww_persona_packets import validate_repository


WORKER_PRINCIPLES = [
    "prefer deterministic packet evidence over broad but weak coverage",
    "when tradeoffs are close, bias toward explicit fixture boundaries",
]
PERSONA_RATIONALE = (
    "baseline required-field fit is strong; built-in fallback selected "
    "because no stronger eligible project persona covers this fixture"
)
SOURCE_PLAN = (
    "docs/cases/example/rounds/2026-05-31-packet-validator-fixture/"
    "dispatch-plan.md"
)


def write_yaml(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")


def write_packet(path: Path, title: str, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    yaml_body = yaml.safe_dump(payload, sort_keys=False)
    path.write_text(f"# {title}\n\n{yaml_body}", encoding="utf-8")


def read_packet(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    return yaml.safe_load("\n".join(lines[1:]))


def update_packet(path: Path, title: str, **updates) -> None:
    packet = read_packet(path)
    packet.update(updates)
    write_packet(path, title, packet)


def common_packet(persona: str, source_plan: str, runtime_role: str) -> dict:
    return {
        "schema_version": 1,
        "source_dispatch_plan": source_plan,
        "source_plan_revision": 1,
        "source_section_id": "section-packet-validator-fixture",
        "orchestrator_type": "staff-engineer-orchestrator",
        "stage": {
            "reviewer": "review",
            "explorer": "investigate",
        }.get(runtime_role, "implement"),
        "execution_id": f"exec-{runtime_role}-01",
        "packet_id": f"packet-{runtime_role}-01",
        "attempt_id": f"attempt-{runtime_role}-01",
        "supersedes_attempt_id": None,
        "accepts_late_results": False,
        "subagent_persona": persona,
        "persona_source": "built-in",
        "persona_rationale": PERSONA_RATIONALE,
        "persona_binding": {
            "runtime_role": runtime_role,
            "template_path": f"agents/{runtime_role}-prompt.md",
        },
        "derived_from_working_brief": "packet validator regression fixture",
        "task_mode": {
            "reviewer": "review",
            "explorer": "investigate",
        }.get(runtime_role, "implement"),
        "workflow_bindings": ["superpowers:verification-before-completion"],
        "working_brief_excerpt": "validate a minimal packet fixture",
        "owned_scope": "fixture only",
        "read_scope": [{"path_glob": "fixture/**"}],
        "write_scope": [],
        "non_goals": "do not widen fixture scope",
        "success_criteria": "return packet validator evidence",
        "output_contract": "findings only",
        "handoff_rule": "return to orchestrator",
        "retry_policy": "relaunch through orchestrator decision",
        "close_policy": "close after findings",
        "result_artifact_location": "not created yet",
        "expected_return_status": ["PASS", "REJECT"],
        "execution_binding": {
            "agent_type": {
                "reviewer": "default",
                "explorer": "explorer",
            }.get(runtime_role, "worker"),
            "context_mode": "curated-only",
            "fork_context": False,
            "model_tier": "strong",
            "reasoning_effort": "high",
            "template_path": f"agents/{runtime_role}-prompt.md",
            "prompt_inputs": {"focus": "packet validator fixture"},
        },
        "requires_human_judgment": runtime_role == "reviewer",
    }


def make_repo(
    root: Path,
    *,
    worker_template: str = "agents/worker-prompt.md",
    worker_principles: list[str] | None = None,
    reviewer_hash: str | None = None,
    reviewer_revision: str | None = None,
    reviewer_content_hash: str | None = None,
    dispatch_snapshot_principles: list[str] | None = None,
) -> None:
    round_root = root / "docs/cases/example/rounds/2026-05-31-packet-validator-fixture"
    worker_path = round_root / "packets/worker-packet.md"
    reviewer_path = round_root / "packets/reviewer-packet.md"

    built_in = {
        "personas": [
            {
                "id": "fixture-worker",
                "role_type": "specialist",
                "review_only": False,
                "implementation_principles": WORKER_PRINCIPLES,
            },
            {
                "id": "fixture-reviewer",
                "role_type": "reviewer",
                "review_only": True,
            },
            {
                "id": "fixture-secondary-reviewer",
                "role_type": "reviewer",
                "review_only": True,
            },
            {
                "id": "fixture-explorer",
                "role_type": "specialist",
                "review_only": False,
            },
        ]
    }
    write_yaml(
        root
        / "plugins/workwork/skills/ww-subagent-orchestrator/references/"
        "built-in-personas.yaml",
        built_in,
    )
    write_yaml(root / "docs/superpowers/personas/registry.yaml", {"personas": []})

    snapshot = dispatch_snapshot_principles or WORKER_PRINCIPLES
    dispatch = f"""# Dispatch Plan: Packet Validator Fixture

- Plan Revision: 1
- Plan State: approved

### Section: Packet Validator Fixture

- Section ID: section-packet-validator-fixture
- Planned Reviewer Persona: fixture-reviewer
- Planned Reviewer Persona Source: built-in
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: {PERSONA_RATIONALE}
- Planned Reviewer Template Path: agents/reviewer-prompt.md
- Planned Specialist Personas:
  - Persona ID: fixture-worker
    - Source: built-in
    - Runtime Role: worker
    - Selection Rationale: {PERSONA_RATIONALE}
    - Template Path: agents/worker-prompt.md
    - Implementation Principles:
      - {snapshot[0]}
      - {snapshot[1]}
"""
    round_root.mkdir(parents=True, exist_ok=True)
    (round_root / "dispatch-plan.md").write_text(dispatch, encoding="utf-8")

    worker = common_packet("fixture-worker", SOURCE_PLAN, "worker")
    worker["persona_binding"]["template_path"] = worker_template
    worker["execution_binding"]["template_path"] = worker_template
    worker["implementation_principles"] = worker_principles or WORKER_PRINCIPLES
    worker.update(
        {
            "work_mode": "validate-first",
            "work_mode_rationale": "prove packet behavior before integration",
            "goal_tuning": "validation-biased",
            "constraint_precedence_note": (
                "packet constraints, user limits, and non-goals take precedence "
                "over work mode"
            ),
        }
    )
    write_packet(worker_path, "Worker Packet Fixture", worker)

    worker_hash = hashlib.sha256(worker_path.read_bytes()).hexdigest()
    reviewer = common_packet("fixture-reviewer", SOURCE_PLAN, "reviewer")
    reviewer.update(
        {
            "review_target_ref": {
                "artifact_path": str(worker_path.relative_to(root)).replace("\\", "/"),
                "artifact_kind": "worker_packet",
                "artifact_revision": reviewer_revision or f"sha256:{reviewer_hash or worker_hash}",
                "schema_version": 1,
                "section_anchor": "full-file worker packet fixture",
                "content_hash": f"sha256:{reviewer_content_hash or reviewer_hash or worker_hash}",
            },
            "review_type": "spec-review",
            "pass_condition": "packet fixture is contract complete",
            "reject_condition": "packet fixture drifts",
        }
    )
    write_packet(reviewer_path, "Reviewer Packet Fixture", reviewer)


def add_explorer_packet(root: Path) -> None:
    round_root = root / "docs/cases/example/rounds/2026-05-31-packet-validator-fixture"
    dispatch_path = round_root / "dispatch-plan.md"
    dispatch = dispatch_path.read_text(encoding="utf-8")
    dispatch += f"""  - Persona ID: fixture-explorer
    - Source: built-in
    - Runtime Role: explorer
    - Selection Rationale: {PERSONA_RATIONALE}
    - Template Path: agents/explorer-prompt.md
"""
    dispatch_path.write_text(dispatch, encoding="utf-8")
    explorer = common_packet("fixture-explorer", SOURCE_PLAN, "explorer")
    write_packet(round_root / "packets/explorer-packet.md", "Explorer Packet Fixture", explorer)


class PersonaPacketValidatorTests(unittest.TestCase):
    def run_fixture(self, **kwargs) -> list:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_repo(root, **kwargs)
            return validate_repository(root)

    def assert_rule_fails(self, results: list, rule_id: str) -> None:
        self.assertTrue(
            any(result.rule_id == rule_id and not result.passed for result in results),
            f"expected {rule_id} failure, got {results}",
        )

    def test_accepts_valid_worker_and_reviewer_packets(self) -> None:
        results = self.run_fixture()
        self.assertTrue(all(result.passed for result in results), results)

    def test_rejects_worker_principle_drift(self) -> None:
        results = self.run_fixture(
            worker_principles=["drifted hard rule", WORKER_PRINCIPLES[1]]
        )
        self.assert_rule_fails(results, "WWPP005")

    def test_rejects_role_prompt_mismatch(self) -> None:
        results = self.run_fixture(worker_template="agents/reviewer-prompt.md")
        self.assert_rule_fails(results, "WWPP004")

    def test_rejects_reviewer_target_hash_drift(self) -> None:
        results = self.run_fixture(reviewer_hash="0" * 64)
        self.assert_rule_fails(results, "WWPP007")

    def test_rejects_dispatch_snapshot_drift_when_snapshot_exists(self) -> None:
        results = self.run_fixture(
            dispatch_snapshot_principles=["drifted snapshot", WORKER_PRINCIPLES[1]]
        )
        self.assert_rule_fails(results, "WWPP008")

    def test_accepts_explorer_specialist_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_repo(root)
            add_explorer_packet(root)
            results = validate_repository(root)
        self.assertTrue(all(result.passed for result in results), results)

    def test_accepts_reviewer_explicit_document_revision(self) -> None:
        results = self.run_fixture(reviewer_revision="design-spec-revision-1")
        self.assertTrue(all(result.passed for result in results), results)

    def test_accepts_excerpt_hash_with_explicit_document_revision(self) -> None:
        results = self.run_fixture(
            reviewer_revision="design-spec-revision-1",
            reviewer_content_hash="1" * 64,
        )
        self.assertTrue(all(result.passed for result in results), results)

    def test_uses_source_section_snapshot_in_multi_section_plan(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_repo(root)
            dispatch_path = (
                root
                / "docs/cases/example/rounds/2026-05-31-packet-validator-fixture/"
                "dispatch-plan.md"
            )
            dispatch = dispatch_path.read_text(encoding="utf-8")
            earlier_section = """### Section: Earlier Fixture

- Section ID: section-earlier-fixture
- Planned Reviewer Persona: wrong-reviewer
- Planned Reviewer Persona Source: project
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: wrong earlier rationale
- Planned Reviewer Template Path: agents/reviewer-prompt.md

"""
            dispatch_path.write_text(
                dispatch.replace(
                    "### Section: Packet Validator Fixture\n",
                    earlier_section + "### Section: Packet Validator Fixture\n",
                ),
                encoding="utf-8",
            )
            results = validate_repository(root)
        self.assertTrue(all(result.passed for result in results), results)

    def test_rejects_absolute_dispatch_plan_path(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_repo(root)
            round_root = (
                root / "docs/cases/example/rounds/2026-05-31-packet-validator-fixture"
            )
            update_packet(
                round_root / "packets/worker-packet.md",
                "Worker Packet Fixture",
                source_dispatch_plan=str((round_root / "dispatch-plan.md").resolve()),
            )
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWPP002")

    def test_rejects_absolute_reviewer_target_path(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_repo(root)
            round_root = (
                root / "docs/cases/example/rounds/2026-05-31-packet-validator-fixture"
            )
            reviewer_path = round_root / "packets/reviewer-packet.md"
            reviewer = read_packet(reviewer_path)
            reviewer["review_target_ref"]["artifact_path"] = str(
                (round_root / "packets/worker-packet.md").resolve()
            )
            write_packet(reviewer_path, "Reviewer Packet Fixture", reviewer)
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWPP007")

    def test_reports_malformed_nested_binding_as_rule_failure(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_repo(root)
            worker_path = (
                root
                / "docs/cases/example/rounds/2026-05-31-packet-validator-fixture/"
                "packets/worker-packet.md"
            )
            update_packet(
                worker_path,
                "Worker Packet Fixture",
                persona_binding="worker",
            )
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWPP004")

    def test_accepts_secondary_reviewer_lane_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_repo(root)
            round_root = (
                root / "docs/cases/example/rounds/2026-05-31-packet-validator-fixture"
            )
            dispatch_path = round_root / "dispatch-plan.md"
            dispatch = dispatch_path.read_text(encoding="utf-8")
            dispatch += f"""- Planned Review Lanes:
  - Lane ID: lane-secondary-review
  - Lane Type: other
  - Reviewer Persona: fixture-secondary-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: {PERSONA_RATIONALE}
  - Required: true
"""
            dispatch_path.write_text(dispatch, encoding="utf-8")
            reviewer_path = round_root / "packets/reviewer-packet.md"
            reviewer = read_packet(reviewer_path)
            reviewer["subagent_persona"] = "fixture-secondary-reviewer"
            write_packet(reviewer_path, "Reviewer Packet Fixture", reviewer)
            results = validate_repository(root)
        self.assertTrue(all(result.passed for result in results), results)


if __name__ == "__main__":
    unittest.main()
