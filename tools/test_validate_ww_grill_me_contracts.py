from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import yaml

from validate_ww_grill_me_contracts import validate_repository


SKILL_ROOT = Path("plugins/workwork/skills/ww-subagent-orchestrator")
VALID_PERSONA = {
    "id": "grill-me",
    "title": "Grill-Me Explorer",
    "category": "product",
    "role_type": "specialist",
    "domains": ["planning", "design", "requirements", "decision-analysis"],
    "languages": [],
    "strengths": [
        "decision-tree interrogation",
        "dependency resolution",
        "assumption surfacing",
        "codebase-first investigation",
    ],
    "use_when": [
        "the user explicitly asks to be grilled about a plan or design",
        "the user explicitly asks to stress-test decisions one question at a time",
    ],
    "avoid_when": [
        "the user did not explicitly request an intensive interview",
        "the task is implementation or a simple factual investigation",
    ],
    "preferred_workflows": ["superpowers:brainstorming"],
    "decision_style": "dependency-first",
    "quality_bar": "shared-understanding quality",
    "tradeoff_bias": "explicit user decisions over premature closure",
    "failure_modes_to_watch": [
        "asking questions the repository can answer",
        "closing branches without user confirmation",
        "asking multiple unresolved questions at once",
    ],
    "escalation_triggers": [
        "a prerequisite decision remains unresolved",
        "the user answer conflicts with repository evidence",
    ],
    "collaboration_posture": "relentless but bounded interviewer",
    "taste_criteria": [
        "resolve dependencies before downstream preferences",
        "keep each question narrow enough for one explicit answer",
    ],
    "review_only": False,
    "priority": 85,
}


def write_text(root: Path, relative: Path, content: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_yaml(root: Path, relative: Path, payload: dict) -> None:
    write_text(root, relative, yaml.safe_dump(payload, sort_keys=False))


def make_valid_repo(root: Path) -> None:
    write_yaml(
        root,
        SKILL_ROOT / "references/built-in-personas.yaml",
        {"personas": [VALID_PERSONA]},
    )
    write_text(
        root,
        SKILL_ROOT / "agents/explorer-prompt.md",
        """# Explorer Prompt

Ordinary explorer behavior remains unchanged.

## Grill-Me Protocol

Activate this protocol only when `subagent_persona` is `grill-me`.

- investigate the codebase and current artifacts before asking
- return exactly one unresolved question
- include one recommended answer and a concise reason
- keep the branch open until the user explicitly confirms
- resolve prerequisite decisions before dependent decisions
- allow the user to stop
- finish with a shared-understanding summary
- do not write files
""",
    )
    write_text(
        root,
        SKILL_ROOT / "references/persona-registry.md",
        """# Persona Registry

`grill-me` is eligible when the user explicitly requests the interview.
It resolves to `runtime_role: explorer` and must not enter the worker candidate set.
""",
    )
    write_text(
        root,
        SKILL_ROOT / "references/working-brief-template.md",
        """# Working Brief

## Grill-Me Decision Log

The orchestrator owns this log.

| Decision ID | User-Confirmed Answer | Recommendation Offered | Dependencies Resolved | Dependent Branches Unblocked |
| --- | --- | --- | --- | --- |
""",
    )
    write_text(
        root,
        SKILL_ROOT / "SKILL.md",
        """# WorkWork

Select `grill-me` only when the user explicitly requests the interview.
For each turn, the orchestrator asks the user exactly one unresolved question.
The orchestrator must not select `grill-me` merely because a plan appears incomplete.
""",
    )
    write_yaml(
        root,
        SKILL_ROOT / "agents/openai.yaml",
        {
            "role_bindings": {
                "explorer": {
                    "runtime_role": "explorer",
                    "template_path": "agents/explorer-prompt.md",
                }
            }
        },
    )
    write_text(
        root,
        Path("README.md"),
        """# WorkWork

Use `$ww grill me` for one question at a time with a recommended answer.
""",
    )


def mutate_persona(root: Path, **updates) -> None:
    path = root / SKILL_ROOT / "references/built-in-personas.yaml"
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    payload["personas"][0].update(updates)
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")


class GrillMeContractValidatorTests(unittest.TestCase):
    def assert_rule_fails(self, results: list, rule_id: str) -> None:
        failures = [
            result.rule_id
            for result in results
            if not result.passed
        ]
        self.assertEqual([rule_id], failures, results)

    def run_text_mutation(
        self,
        relative_name: str,
        old: str,
        new: str,
    ) -> list:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            path = root / SKILL_ROOT / relative_name
            if relative_name == "README.md":
                path = root / relative_name
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

    def test_rejects_missing_grill_me_persona(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            mutate_persona(root, id="ordinary-explorer")
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWGM001")

    def test_rejects_worker_capable_grill_me(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            mutate_persona(
                root,
                implementation_principles=["hard rule", "soft rule"],
            )
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWGM002")

    def test_rejects_non_specialist_grill_me(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            mutate_persona(root, role_type="reviewer")
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWGM002")

    def test_rejects_unconditional_protocol(self) -> None:
        results = self.run_text_mutation(
            "agents/explorer-prompt.md",
            "only when `subagent_persona` is `grill-me`",
            "for every explorer",
        )
        self.assert_rule_fails(results, "WWGM003")

    def test_rejects_changed_ordinary_explorer_behavior(self) -> None:
        results = self.run_text_mutation(
            "agents/explorer-prompt.md",
            "Ordinary explorer behavior remains unchanged",
            "Ordinary explorer behavior uses the interview protocol",
        )
        self.assert_rule_fails(results, "WWGM003")

    def test_rejects_multiple_questions_per_turn(self) -> None:
        results = self.run_text_mutation(
            "agents/explorer-prompt.md",
            "return exactly one unresolved question",
            "return unresolved questions",
        )
        self.assert_rule_fails(results, "WWGM004")

    def test_rejects_missing_recommended_answer(self) -> None:
        results = self.run_text_mutation(
            "agents/explorer-prompt.md",
            "include one recommended answer and a concise reason",
            "include useful context",
        )
        self.assert_rule_fails(results, "WWGM004")

    def test_rejects_silent_recommendation_acceptance(self) -> None:
        results = self.run_text_mutation(
            "agents/explorer-prompt.md",
            "keep the branch open until the user explicitly confirms",
            "close the branch after making a recommendation",
        )
        self.assert_rule_fails(results, "WWGM004")

    def test_rejects_missing_codebase_first_rule(self) -> None:
        results = self.run_text_mutation(
            "agents/explorer-prompt.md",
            "investigate the codebase and current artifacts before asking",
            "ask the user for repository facts",
        )
        self.assert_rule_fails(results, "WWGM004")

    def test_rejects_dependent_decisions_before_prerequisites(self) -> None:
        results = self.run_text_mutation(
            "agents/explorer-prompt.md",
            "resolve prerequisite decisions before dependent decisions",
            "resolve decisions in any order",
        )
        self.assert_rule_fails(results, "WWGM004")

    def test_rejects_missing_stop_support(self) -> None:
        results = self.run_text_mutation(
            "agents/explorer-prompt.md",
            "allow the user to stop",
            "continue until every branch closes",
        )
        self.assert_rule_fails(results, "WWGM004")

    def test_rejects_missing_shared_understanding_summary(self) -> None:
        results = self.run_text_mutation(
            "agents/explorer-prompt.md",
            "shared-understanding summary",
            "completion note",
        )
        self.assert_rule_fails(results, "WWGM004")

    def test_rejects_wrong_explorer_runtime_role(self) -> None:
        results = self.run_text_mutation(
            "agents/openai.yaml",
            "runtime_role: explorer",
            "runtime_role: worker",
        )
        self.assert_rule_fails(results, "WWGM005")

    def test_rejects_wrong_explorer_template(self) -> None:
        results = self.run_text_mutation(
            "agents/openai.yaml",
            "template_path: agents/explorer-prompt.md",
            "template_path: agents/worker-prompt.md",
        )
        self.assert_rule_fails(results, "WWGM005")

    def test_rejects_writable_explorer_prompt(self) -> None:
        results = self.run_text_mutation(
            "agents/explorer-prompt.md",
            "do not write files",
            "write files when useful",
        )
        self.assert_rule_fails(results, "WWGM005")

    def test_rejects_missing_explicit_trigger_boundary(self) -> None:
        results = self.run_text_mutation(
            "SKILL.md",
            "only when the user explicitly requests",
            "when the plan appears incomplete",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_skill_multiple_questions(self) -> None:
        results = self.run_text_mutation(
            "SKILL.md",
            "exactly one unresolved question",
            "all unresolved questions",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_auto_selection_for_incomplete_plan(self) -> None:
        results = self.run_text_mutation(
            "SKILL.md",
            "must not select `grill-me` merely because a plan appears incomplete",
            "may select `grill-me` when a plan appears incomplete",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_direct_explorer_user_channel(self) -> None:
        results = self.run_text_mutation(
            "SKILL.md",
            "the orchestrator asks the user",
            "the explorer asks the user directly",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_missing_decision_log(self) -> None:
        results = self.run_text_mutation(
            "references/working-brief-template.md",
            "## Grill-Me Decision Log",
            "## Interview Notes",
        )
        self.assert_rule_fails(results, "WWGM007")

    def test_rejects_explorer_owned_decision_log(self) -> None:
        results = self.run_text_mutation(
            "references/working-brief-template.md",
            "The orchestrator owns this log",
            "The explorer owns this log",
        )
        self.assert_rule_fails(results, "WWGM007")

    def test_rejects_incomplete_decision_log_fields(self) -> None:
        results = self.run_text_mutation(
            "references/working-brief-template.md",
            "Dependent Branches Unblocked",
            "Notes",
        )
        self.assert_rule_fails(results, "WWGM007")

    def test_rejects_registry_without_explicit_request(self) -> None:
        results = self.run_text_mutation(
            "references/persona-registry.md",
            "explicitly requests",
            "has an incomplete plan",
        )
        self.assert_rule_fails(results, "WWGM008")

    def test_rejects_registry_worker_candidate(self) -> None:
        results = self.run_text_mutation(
            "references/persona-registry.md",
            "must not enter the worker candidate set",
            "may enter the worker candidate set",
        )
        self.assert_rule_fails(results, "WWGM008")

    def test_rejects_readme_without_trigger(self) -> None:
        results = self.run_text_mutation(
            "README.md",
            "$ww grill me",
            "$ww interview",
        )
        self.assert_rule_fails(results, "WWGM009")

    def test_rejects_readme_without_recommendation(self) -> None:
        results = self.run_text_mutation(
            "README.md",
            "recommended answer",
            "context",
        )
        self.assert_rule_fails(results, "WWGM009")


if __name__ == "__main__":
    unittest.main()
