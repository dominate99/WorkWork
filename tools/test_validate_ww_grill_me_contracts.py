from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

from validate_ww_grill_me_contracts import validate_repository


SKILL_ROOT = Path("plugins/workwork/skills/ww-subagent-orchestrator")
VALIDATOR_PATH = Path(__file__).with_name("validate_ww_grill_me_contracts.py")
SCAFFOLD_PATH = Path("tools/scaffold_ww_case_artifacts.py")
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

## Grill-Me Conditional Protocol

This protocol defines the read-only `grill-me` explorer viewpoint used inline by
the orchestrator during planning. Do not assemble or launch an explorer packet
for the interview. Otherwise ordinary explorer packet behavior remains unchanged.

- investigate the codebase and current artifacts before asking
- ask exactly one unresolved question per user turn
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
It uses the `runtime_role: explorer` viewpoint inline during planning, must not enter the worker candidate set, and must not be selected for packet assembly.
""",
    )
    write_text(
        root,
        SKILL_ROOT / "references/working-brief-template.md",
        """# Working Brief

## Grill-Me Decision Log

The orchestrator owns this log. The `grill-me` explorer remains read-only and
is applied inline during planning.

Use one entry per decision:

- Decision ID:
- State: open | confirmed | deferred
- Question:
- User-Confirmed Answer:
- Recommendation Offered:
- Rationale Or Repository Evidence:
- Dependencies Resolved:
- Dependent Branches Unblocked:

Rules:

- create or update an entry only when `grill-me` is explicitly active
- keep `State: open` until the user explicitly confirms an answer
- do not treat the recommended answer as confirmation
- record repository-resolved facts as evidence without asking the user to decide them
- use confirmed entries as inputs to later design specs and implementation plans
- keep round approval and runtime lifecycle state in `dispatch-plan.md`
- when the user stops grilling, mark the current unresolved branch `deferred`
""",
    )
    write_text(
        root,
        SKILL_ROOT / "SKILL.md",
        """# WorkWork

## Persona Planning

### Grill-Me Explorer

Select `grill-me` only when the user explicitly requests the interview.
For each turn, the orchestrator asks the user exactly one unresolved question.
The orchestrator must not select `grill-me` merely because a plan appears incomplete.

Run the interview inline during working-brief finalization before dispatch-plan
approval. Do not create a subagent packet for the interview. Do not launch an
explorer execution for the interview. Do not enter the runtime controller for
the interview.

When no dispatch plan exists, investigate repository-answerable facts first,
persist confirmed decisions in the working brief, confirm shared understanding,
then finalize the brief and create the dispatch plan.

When a dispatch plan already exists, freeze new dispatch, set `plan_state` to
`revising`, run the interview as planning work, update and increment
`brief_version`, regenerate the dispatch plan against that brief version, and
require approval again before any worker or reviewer dispatch.

`stop grilling` marks the current unresolved branch `deferred`; it does not set
dispatch plan, section, or runtime state to `stopped`. Canonical `$ww` `Stop`
remains an approval or controller decision. Use canonical `Stop` separately
when the user wants to stop the round.

During an active grill question, use lettered options (`A`, `B`, `C`) or
descriptive answers. Numeric `1/2/3` approval aliases apply only when the
dispatch plan is awaiting an approval decision, not during an active grill
question.
""",
    )
    write_text(
        root,
        SCAFFOLD_PATH,
        '''def render_working_brief(context):
    return """# Working Brief

## Grill-Me Decision Log

The orchestrator owns this log. The `grill-me` explorer remains read-only and
is applied inline during planning.

Use one entry per decision:

- Decision ID:
- State: open | confirmed | deferred
- Question:
- User-Confirmed Answer:
- Recommendation Offered:
- Rationale Or Repository Evidence:
- Dependencies Resolved:
- Dependent Branches Unblocked:

Rules:

- create or update an entry only when `grill-me` is explicitly active
- keep `State: open` until the user explicitly confirms an answer
- do not treat the recommended answer as confirmation
- record repository-resolved facts as evidence without asking the user to decide them
- use confirmed entries as inputs to later design specs and implementation plans
- keep round approval and runtime lifecycle state in `dispatch-plan.md`
- when the user stops grilling, mark the current unresolved branch `deferred`
"""
''',
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

    def run_append(self, relative_name: str, addition: str) -> list:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            path = root / SKILL_ROOT / relative_name
            content = path.read_text(encoding="utf-8")
            path.write_text(f"{content.rstrip()}\n\n{addition}\n", encoding="utf-8")
            return validate_repository(root)

    def run_scaffold_mutation(self, old: str, new: str) -> list:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            path = root / SCAFFOLD_PATH
            content = path.read_text(encoding="utf-8")
            self.assertEqual(1, content.count(old), old)
            path.write_text(content.replace(old, new, 1), encoding="utf-8")
            return validate_repository(root)

    def run_cli(
        self,
        root: Path,
        *,
        as_json: bool = False,
        cwd: Path,
    ) -> subprocess.CompletedProcess[str]:
        command = [
            sys.executable,
            str(VALIDATOR_PATH),
            "--repo-root",
            str(root),
        ]
        if as_json:
            command.append("--json")
        return subprocess.run(
            command,
            cwd=cwd,
            check=False,
            capture_output=True,
            text=True,
        )

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
            "used inline by\nthe orchestrator during planning",
            "used by every explorer packet",
        )
        self.assert_rule_fails(results, "WWGM003")

    def test_rejects_changed_ordinary_explorer_behavior(self) -> None:
        results = self.run_text_mutation(
            "agents/explorer-prompt.md",
            "Otherwise ordinary explorer packet behavior remains unchanged",
            "Otherwise ordinary explorer behavior uses the interview protocol",
        )
        self.assert_rule_fails(results, "WWGM003")

    def test_rejects_grill_me_packet_launch(self) -> None:
        results = self.run_text_mutation(
            "agents/explorer-prompt.md",
            "Do not assemble or launch an explorer packet",
            "Assemble and launch an explorer packet",
        )
        self.assert_rule_fails(results, "WWGM003")

    def test_rejects_protocol_phrase_found_only_in_four_backtick_fence(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            path = root / SKILL_ROOT / "agents/explorer-prompt.md"
            content = path.read_text(encoding="utf-8")
            content = content.replace(
                "ask exactly one unresolved question per user turn",
                "ask about one unresolved decision",
                1,
            )
            content += (
                "\n````text\n"
                "```\n"
                "ask exactly one unresolved question per user turn\n"
                "```\n"
                "````\n"
            )
            path.write_text(content, encoding="utf-8")
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWGM004")

    def test_rejects_multiple_questions_per_turn(self) -> None:
        results = self.run_text_mutation(
            "agents/explorer-prompt.md",
            "ask exactly one unresolved question per user turn",
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

    def test_rejects_contradictory_multiple_questions_statement(self) -> None:
        results = self.run_append(
            "agents/explorer-prompt.md",
            "- return multiple unresolved questions at once",
        )
        self.assert_rule_fails(results, "WWGM004")

    def test_rejects_prefixed_multiple_questions_instruction(self) -> None:
        results = self.run_append(
            "agents/explorer-prompt.md",
            "- always return multiple unresolved questions at once",
        )
        self.assert_rule_fails(results, "WWGM004")

    def test_rejects_unrelated_negation_before_multiple_questions(self) -> None:
        results = self.run_append(
            "agents/explorer-prompt.md",
            (
                "- do not hesitate; always return multiple unresolved "
                "questions at once"
            ),
        )
        self.assert_rule_fails(results, "WWGM004")

    def test_rejects_recommendation_as_approval_or_branch_closure(self) -> None:
        results = self.run_append(
            "agents/explorer-prompt.md",
            "- the recommended answer counts as user approval",
        )
        self.assert_rule_fails(results, "WWGM004")

    def test_accepts_historical_multiple_questions_prose(self) -> None:
        results = self.run_append(
            "agents/explorer-prompt.md",
            (
                "Historical guidance once said return multiple unresolved "
                "questions at once, which caused poor outcomes."
            ),
        )
        self.assertTrue(all(result.passed for result in results), results)

    def test_accepts_protective_multiple_questions_negation(self) -> None:
        results = self.run_append(
            "agents/explorer-prompt.md",
            "- do not return multiple unresolved questions at once",
        )
        self.assertTrue(all(result.passed for result in results), results)

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

    def test_rejects_retained_contract_with_direct_explorer_user_channel(
        self,
    ) -> None:
        results = self.run_append(
            "SKILL.md",
            "- the explorer asks the user directly",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_retained_contract_with_incomplete_plan_auto_select(
        self,
    ) -> None:
        results = self.run_append(
            "SKILL.md",
            "- select grill-me when a plan appears incomplete",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_prefixed_incomplete_plan_selection(self) -> None:
        results = self.run_append(
            "SKILL.md",
            "- you should select grill-me when a plan appears incomplete",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_accepts_protective_incomplete_plan_negation(self) -> None:
        results = self.run_append(
            "SKILL.md",
            "- must not select grill-me when a plan appears incomplete",
        )
        self.assertTrue(all(result.passed for result in results), results)

    def test_rejects_interview_after_dispatch_approval(self) -> None:
        results = self.run_text_mutation(
            "SKILL.md",
            "before dispatch-plan\napproval",
            "after dispatch-plan approval",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_missing_inline_planning_rule(self) -> None:
        results = self.run_text_mutation(
            "SKILL.md",
            "Run the interview inline during working-brief finalization",
            "Launch an explorer execution during working-brief finalization",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_packet_assembly_for_interview(self) -> None:
        results = self.run_text_mutation(
            "SKILL.md",
            "Do not create a subagent packet",
            "Create a subagent packet",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_runtime_controller_entry(self) -> None:
        results = self.run_text_mutation(
            "SKILL.md",
            "enter the runtime controller",
            "remain outside the runtime controller",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_missing_pre_plan_flow(self) -> None:
        results = self.run_text_mutation(
            "SKILL.md",
            "then finalize the brief and create the dispatch plan",
            "then launch a worker packet",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_missing_existing_plan_freeze(self) -> None:
        results = self.run_text_mutation(
            "SKILL.md",
            "freeze new dispatch",
            "continue new dispatch",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_missing_revising_transition(self) -> None:
        results = self.run_text_mutation(
            "SKILL.md",
            "set `plan_state` to\n`revising`",
            "leave `plan_state` approved",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_missing_brief_version_increment(self) -> None:
        results = self.run_text_mutation(
            "SKILL.md",
            "update and increment\n`brief_version`",
            "keep the existing `brief_version`",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_missing_plan_regeneration_and_reapproval(self) -> None:
        results = self.run_text_mutation(
            "SKILL.md",
            "regenerate the dispatch plan against that brief version, and\nrequire approval again",
            "reuse the original dispatch plan without approval",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_stop_grilling_as_runtime_stop(self) -> None:
        results = self.run_text_mutation(
            "SKILL.md",
            "`deferred`; it does not set",
            "`stopped`; it also sets",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_missing_canonical_stop_separation(self) -> None:
        results = self.run_text_mutation(
            "SKILL.md",
            "remains an approval or controller decision",
            "Stopping the interview always stops the round",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_numeric_grill_question_options(self) -> None:
        results = self.run_text_mutation(
            "SKILL.md",
            "Numeric `1/2/3` approval aliases apply only when the",
            "use numeric `1/2/3` options for every grill question",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_retained_contract_with_packet_launch(self) -> None:
        results = self.run_append(
            "SKILL.md",
            "- create an explorer packet for the grill-me interview",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_retained_contract_with_runtime_entry(self) -> None:
        results = self.run_append(
            "SKILL.md",
            "- grill-me enters the runtime controller during the interview",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_retained_contract_with_post_approval_interview(self) -> None:
        results = self.run_append(
            "SKILL.md",
            "- run the grill-me interview after dispatch approval",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_retained_contract_with_numeric_grill_options(self) -> None:
        results = self.run_append(
            "SKILL.md",
            "- use numeric 1/2/3 options during active grill questions",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_retained_contract_with_stop_invoking_round_stop(
        self,
    ) -> None:
        results = self.run_append(
            "SKILL.md",
            "- stop grilling invokes canonical Stop and stops the round",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_normative_paragraph_packet_launch(self) -> None:
        results = self.run_append(
            "SKILL.md",
            "Create an explorer packet for the grill-me interview.",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_normative_paragraph_explorer_execution(self) -> None:
        results = self.run_append(
            "SKILL.md",
            "Launch an explorer execution for the interview.",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_normative_paragraph_runtime_entry(self) -> None:
        results = self.run_append(
            "SKILL.md",
            "Enter the runtime controller for the interview.",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_packet_assembly_synonym(self) -> None:
        results = self.run_append(
            "SKILL.md",
            "Build a subagent packet for the grill-me interview.",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_explorer_execution_synonym(self) -> None:
        results = self.run_append(
            "SKILL.md",
            "Execute the grill-me interview as an explorer job.",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_packet_synonym_with_indirect_interview_reference(
        self,
    ) -> None:
        results = self.run_append(
            "SKILL.md",
            (
                "Build a subagent packet and run the grill-me interview "
                "through it."
            ),
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_modal_explorer_job_synonym(self) -> None:
        results = self.run_append(
            "SKILL.md",
            "The interview must execute as an explorer job.",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_rejects_normative_paragraph_stale_plan_reuse(self) -> None:
        results = self.run_append(
            "SKILL.md",
            "Reuse the original dispatch plan without approval.",
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_accepts_protective_inline_negations(self) -> None:
        results = self.run_append(
            "SKILL.md",
            "\n".join(
                [
                    "- do not create an explorer packet for the grill-me interview",
                    "- grill-me does not enter the runtime controller",
                    "- do not run the grill-me interview after dispatch approval",
                    (
                        "- do not use numeric 1/2/3 options during active grill "
                        "questions"
                    ),
                    (
                        "- stop grilling does not invoke canonical Stop or stop "
                        "the round"
                    ),
                    "- do not reuse the original dispatch plan without approval",
                ]
            ),
        )
        self.assertTrue(all(result.passed for result in results), results)

    def test_accepts_historical_inline_contradiction_prose(self) -> None:
        results = self.run_append(
            "SKILL.md",
            (
                "Historical guidance said to create an explorer packet for the "
                "grill-me interview, which is no longer the protocol."
            ),
        )
        self.assertTrue(all(result.passed for result in results), results)

    def test_accepts_extended_protective_negation(self) -> None:
        results = self.run_append(
            "SKILL.md",
            "Do not ever create an explorer packet for the grill-me interview.",
        )
        self.assertTrue(all(result.passed for result in results), results)

    def test_rejects_unprotected_directive_after_protective_directive(
        self,
    ) -> None:
        results = self.run_append(
            "SKILL.md",
            (
                "Do not create a subagent packet for the interview. "
                "Build a subagent packet and run the interview through it."
            ),
        )
        self.assert_rule_fails(results, "WWGM006")

    def test_accepts_former_contract_history(self) -> None:
        results = self.run_append(
            "SKILL.md",
            (
                "The former contract said to create an explorer packet for the "
                "grill-me interview; that rule is obsolete."
            ),
        )
        self.assertTrue(all(result.passed for result in results), results)

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

    def test_rejects_missing_decision_log_confirmation_rule(self) -> None:
        results = self.run_text_mutation(
            "references/working-brief-template.md",
            "- do not treat the recommended answer as confirmation",
            "- recommendations provide context",
        )
        self.assert_rule_fails(results, "WWGM007")

    def test_rejects_incomplete_decision_log_fields(self) -> None:
        results = self.run_text_mutation(
            "references/working-brief-template.md",
            "- Dependent Branches Unblocked:",
            "- Notes:",
        )
        self.assert_rule_fails(results, "WWGM007")

    def test_rejects_decision_log_without_state(self) -> None:
        results = self.run_text_mutation(
            "references/working-brief-template.md",
            "- State: open | confirmed | deferred",
            "- Status: open | confirmed | deferred",
        )
        self.assert_rule_fails(results, "WWGM007")

    def test_rejects_old_stopped_decision_state(self) -> None:
        results = self.run_text_mutation(
            "references/working-brief-template.md",
            "- State: open | confirmed | deferred",
            "- State: open | confirmed | stopped",
        )
        self.assert_rule_fails(results, "WWGM007")

    def test_rejects_duplicate_stopped_decision_state(self) -> None:
        results = self.run_append(
            "references/working-brief-template.md",
            "- State: open | confirmed | stopped",
        )
        self.assert_rule_fails(results, "WWGM007")

    def test_rejects_decision_log_without_question(self) -> None:
        results = self.run_text_mutation(
            "references/working-brief-template.md",
            "- Question:",
            "- Topic:",
        )
        self.assert_rule_fails(results, "WWGM007")

    def test_rejects_decision_log_without_rationale_or_repository_evidence(
        self,
    ) -> None:
        results = self.run_text_mutation(
            "references/working-brief-template.md",
            "- Rationale Or Repository Evidence:",
            "- Notes:",
        )
        self.assert_rule_fails(results, "WWGM007")

    def test_rejects_decision_log_field_found_only_in_prose(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            path = (
                root
                / SKILL_ROOT
                / "references/working-brief-template.md"
            )
            content = path.read_text(encoding="utf-8")
            content = content.replace(
                "- Question:",
                "- Topic:",
                1,
            )
            content += "\nQuestion: this prose is not a decision-log field.\n"
            path.write_text(content, encoding="utf-8")
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWGM007")

    def test_rejects_decision_log_field_found_only_in_four_backtick_fence(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            path = (
                root
                / SKILL_ROOT
                / "references/working-brief-template.md"
            )
            content = path.read_text(encoding="utf-8")
            content = content.replace("- Question:", "- Topic:", 1)
            content += "\n````text\n```\n- Question:\n```\n````\n"
            path.write_text(content, encoding="utf-8")
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWGM007")

    def test_rejects_scaffold_without_decision_log(self) -> None:
        results = self.run_scaffold_mutation(
            "## Grill-Me Decision Log",
            "## Interview Notes",
        )
        self.assert_rule_fails(results, "WWGM007")

    def test_rejects_scaffold_old_stopped_decision_state(self) -> None:
        results = self.run_scaffold_mutation(
            "- State: open | confirmed | deferred",
            "- State: open | confirmed | stopped",
        )
        self.assert_rule_fails(results, "WWGM007")

    def test_rejects_scaffold_duplicate_stopped_decision_state(self) -> None:
        results = self.run_scaffold_mutation(
            "- when the user stops grilling, mark the current unresolved branch `deferred`",
            (
                "- when the user stops grilling, mark the current unresolved "
                "branch `deferred`\n"
                "- State: open | confirmed | stopped"
            ),
        )
        self.assert_rule_fails(results, "WWGM007")

    def test_rejects_scaffold_without_orchestrator_ownership(self) -> None:
        results = self.run_scaffold_mutation(
            "The orchestrator owns this log",
            "The explorer owns this log",
        )
        self.assert_rule_fails(results, "WWGM007")

    def test_rejects_scaffold_without_confirmation_rule(self) -> None:
        results = self.run_scaffold_mutation(
            "- do not treat the recommended answer as confirmation",
            "- recommendations provide context",
        )
        self.assert_rule_fails(results, "WWGM007")

    def test_rejects_scaffold_contract_found_only_in_function_docstring(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            path = root / SCAFFOLD_PATH
            content = path.read_text(encoding="utf-8")
            content = content.replace(
                '    return """# Working Brief',
                '    """# Working Brief',
                1,
            )
            content = content.replace(
                '"""\n',
                '"""\n    return "# Working Brief\\n\\n## Interview Notes\\n"\n',
                1,
            )
            path.write_text(content, encoding="utf-8")
            results = validate_repository(root)
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

    def test_rejects_non_list_personas_shape(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            write_yaml(
                root,
                SKILL_ROOT / "references/built-in-personas.yaml",
                {"personas": {"id": "grill-me"}},
            )
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWGM001")
        failure = next(result for result in results if not result.passed)
        self.assertIn("must be a list", failure.message)

    def test_rejects_non_mapping_persona_entry(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            write_yaml(
                root,
                SKILL_ROOT / "references/built-in-personas.yaml",
                {"personas": ["grill-me"]},
            )
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWGM001")
        failure = next(result for result in results if not result.passed)
        self.assertIn("entries must be mappings", failure.message)

    def test_rejects_non_mapping_role_bindings(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            write_yaml(
                root,
                SKILL_ROOT / "agents/openai.yaml",
                {"role_bindings": ["explorer"]},
            )
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWGM005")
        failure = next(result for result in results if not result.passed)
        self.assertIn("role_bindings", failure.message)

    def test_rejects_non_mapping_explorer_binding(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            write_yaml(
                root,
                SKILL_ROOT / "agents/openai.yaml",
                {"role_bindings": {"explorer": "agents/explorer-prompt.md"}},
            )
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWGM005")
        failure = next(result for result in results if not result.passed)
        self.assertIn("explorer", failure.message)

    def test_cli_human_success_from_non_repo_cwd(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            workspace = Path(temp_dir)
            root = workspace / "fixture"
            cwd = workspace / "elsewhere"
            cwd.mkdir()
            make_valid_repo(root)
            completed = self.run_cli(root, cwd=cwd)
        self.assertEqual(0, completed.returncode, completed)
        self.assertEqual("PASS: 9 rules checked\n", completed.stdout)
        self.assertEqual("", completed.stderr)

    def test_cli_human_failure_exit_and_output(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            workspace = Path(temp_dir)
            root = workspace / "fixture"
            cwd = workspace / "elsewhere"
            cwd.mkdir()
            make_valid_repo(root)
            readme = root / "README.md"
            readme.write_text("# WorkWork\n", encoding="utf-8")
            completed = self.run_cli(root, cwd=cwd)
        self.assertEqual(1, completed.returncode, completed)
        self.assertIn("FAIL: 1 rule violations", completed.stdout)
        self.assertIn("[WWGM009] README.md", completed.stdout)

    def test_cli_json_success_schema(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            workspace = Path(temp_dir)
            root = workspace / "fixture"
            cwd = workspace / "elsewhere"
            cwd.mkdir()
            make_valid_repo(root)
            completed = self.run_cli(root, as_json=True, cwd=cwd)
        payload = json.loads(completed.stdout)
        self.assertEqual(0, completed.returncode, completed)
        self.assertEqual(
            {"ok", "rule_failures", "results"},
            set(payload),
        )
        self.assertTrue(payload["ok"])
        self.assertEqual(0, payload["rule_failures"])
        self.assertEqual(9, len(payload["results"]))

    def test_cli_json_failure_schema(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            workspace = Path(temp_dir)
            root = workspace / "fixture"
            cwd = workspace / "elsewhere"
            cwd.mkdir()
            make_valid_repo(root)
            readme = root / "README.md"
            readme.write_text("# WorkWork\n", encoding="utf-8")
            completed = self.run_cli(root, as_json=True, cwd=cwd)
        payload = json.loads(completed.stdout)
        self.assertEqual(1, completed.returncode, completed)
        self.assertFalse(payload["ok"])
        self.assertEqual(1, payload["rule_failures"])
        failure = next(
            result for result in payload["results"] if not result["passed"]
        )
        self.assertEqual("WWGM009", failure["rule_id"])


if __name__ == "__main__":
    unittest.main()
