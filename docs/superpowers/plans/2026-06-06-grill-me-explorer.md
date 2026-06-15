# Grill-Me Explorer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an explicitly triggered, read-only `grill-me` explorer persona/viewpoint that investigates the repository first, asks one recommended question at a time through the orchestrator during planning, and persists confirmed decisions in the working brief.

**Architecture:** Keep the existing `explorer` role vocabulary and `agents/explorer-prompt.md` as the source of the read-only viewpoint. Add `grill-me` as a non-worker-capable built-in specialist persona, but apply it inline during working-brief finalization instead of assembling a packet or entering runtime control. Keep the orchestrator responsible for user interaction and decision persistence. Protect the behavior with a focused validator registered in the repository suite.

**Design revision:** The initial packet-resume design conflicted with WorkWork's packet closure, plan revision, and controller semantics. The approved implementation uses a planning-time inline interview. When a plan already exists, dispatch freezes, `plan_state` becomes `revising`, `brief_version` increments, the plan is regenerated, and approval is requested again.

**Tech Stack:** Markdown contracts, YAML persona records, Python 3, PyYAML, `unittest`, existing WorkWork repository validators.

---

## File Structure

- Create `tools/validate_ww_grill_me_contracts.py`
  - Validate the built-in persona, conditional explorer protocol, explicit trigger boundary, decision-log ownership, README guidance, and existing explorer role binding.
- Create `tools/test_validate_ww_grill_me_contracts.py`
  - Build isolated positive and negative fixtures for every protected `grill-me` contract.
- Modify `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - Add the portable `grill-me` persona record without worker capability.
- Modify `plugins/workwork/skills/ww-subagent-orchestrator/agents/explorer-prompt.md`
  - Add an inline planning viewpoint while preserving ordinary explorer packet behavior.
- Modify `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - Define explorer eligibility and the explicit-trigger selection rule.
- Modify `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - Add the durable `Grill-Me Decision Log` owned by the orchestrator.
- Modify `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - Define selection, mediation, persistence, completion, and stop behavior.
- Modify `README.md`
  - Add user-facing trigger examples and maintainer validation guidance.
- Modify `tools/validate_ww_repo.py`
  - Register the focused validator in the full repository suite.

### Task 1: Build The Focused Contract Validator

**Files:**
- Create: `tools/test_validate_ww_grill_me_contracts.py`
- Create: `tools/validate_ww_grill_me_contracts.py`

- [ ] **Step 1: Write the failing validator tests**

Create `tools/test_validate_ww_grill_me_contracts.py` with a temporary repository fixture containing the six target files. The valid fixture must use this persona:

```python
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
```

The test module must include:

```python
class GrillMeContractValidatorTests(unittest.TestCase):
    def test_accepts_complete_contract(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            results = validate_repository(root)
        self.assertTrue(all(result.passed for result in results), results)

    def test_rejects_worker_capable_grill_me(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            make_valid_repo(root)
            mutate_persona(root, implementation_principles=["hard rule", "soft rule"])
            results = validate_repository(root)
        self.assert_rule_fails(results, "WWGM002")

    def test_rejects_missing_explicit_trigger_boundary(self) -> None:
        results = self.run_text_mutation(
            "SKILL.md",
            "only when the user explicitly requests",
            "when the plan appears incomplete",
        )
        self.assert_rule_fails(results, "WWGM006")

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

    def test_rejects_missing_decision_log(self) -> None:
        results = self.run_text_mutation(
            "references/working-brief-template.md",
            "## Grill-Me Decision Log",
            "## Interview Notes",
        )
        self.assert_rule_fails(results, "WWGM007")

    def test_rejects_direct_explorer_user_channel(self) -> None:
        results = self.run_text_mutation(
            "SKILL.md",
            "the orchestrator asks the user",
            "the explorer asks the user directly",
        )
        self.assert_rule_fails(results, "WWGM006")
```

Use helper methods that write UTF-8 files, mutate one exact fragment, load YAML with `yaml.safe_load`, and assert a named rule failed. Keep every negative fixture valid except for the one contract it targets.

- [ ] **Step 2: Run the tests to verify RED**

Run:

```powershell
python tools/test_validate_ww_grill_me_contracts.py
```

Expected: FAIL with `ModuleNotFoundError: No module named 'validate_ww_grill_me_contracts'`.

- [ ] **Step 3: Implement the minimal validator**

Create `tools/validate_ww_grill_me_contracts.py` using the repository validator result shape:

```python
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_ROOT = Path("plugins/workwork/skills/ww-subagent-orchestrator")
TARGETS = {
    "personas": SKILL_ROOT / "references/built-in-personas.yaml",
    "prompt": SKILL_ROOT / "agents/explorer-prompt.md",
    "registry": SKILL_ROOT / "references/persona-registry.md",
    "brief": SKILL_ROOT / "references/working-brief-template.md",
    "skill": SKILL_ROOT / "SKILL.md",
    "openai": SKILL_ROOT / "agents/openai.yaml",
    "readme": Path("README.md"),
}


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


def normalized(text: str) -> str:
    return " ".join(text.split()).casefold()


def contains_all(text: str, fragments: list[str]) -> bool:
    value = normalized(text)
    return all(normalized(fragment) in value for fragment in fragments)


def result(
    rule_id: str,
    passed: bool,
    path: Path,
    section: str,
    message: str,
) -> RuleResult:
    return RuleResult(
        rule_id=rule_id,
        passed=passed,
        file=path.as_posix(),
        section=section,
        message="ok" if passed else message,
    )


def validate_repository(repo_root: Path = REPO_ROOT) -> list[RuleResult]:
    paths = {name: repo_root / relative for name, relative in TARGETS.items()}
    texts = {
        name: path.read_text(encoding="utf-8")
        for name, path in paths.items()
        if name != "personas"
    }
    payload = yaml.safe_load(paths["personas"].read_text(encoding="utf-8")) or {}
    personas = payload.get("personas", [])
    grill = next(
        (persona for persona in personas if persona.get("id") == "grill-me"),
        {},
    )

    role_binding = yaml.safe_load(texts["openai"]) or {}
    explorer_binding = role_binding.get("role_bindings", {}).get("explorer", {})

    checks = [
        result(
            "WWGM001",
            bool(grill),
            TARGETS["personas"],
            "Built-In Persona",
            "Missing built-in persona `grill-me`.",
        ),
        result(
            "WWGM002",
            grill.get("role_type") == "specialist"
            and grill.get("review_only") is False
            and "implementation_principles" not in grill,
            TARGETS["personas"],
            "Worker Capability Boundary",
            "`grill-me` must be a non-reviewer specialist without implementation principles.",
        ),
        result(
            "WWGM003",
            contains_all(
                texts["prompt"],
                [
                    "used inline by the orchestrator during planning",
                    "do not assemble or launch an explorer packet",
                    "ordinary explorer packet behavior remains unchanged",
                ],
            ),
            TARGETS["prompt"],
            "Conditional Protocol",
            "Missing persona-conditional activation or ordinary-explorer preservation.",
        ),
        result(
            "WWGM004",
            contains_all(
                texts["prompt"],
                [
                    "investigate the codebase and current artifacts before asking",
                    "ask exactly one unresolved question per user turn",
                    "include one recommended answer and a concise reason",
                    "keep the branch open until the user explicitly confirms",
                    "resolve prerequisite decisions before dependent decisions",
                    "allow the user to stop",
                    "shared-understanding summary",
                ],
            ),
            TARGETS["prompt"],
            "Interview Protocol",
            "The grill-me interview protocol is incomplete.",
        ),
        result(
            "WWGM005",
            explorer_binding.get("runtime_role") == "explorer"
            and explorer_binding.get("template_path") == "agents/explorer-prompt.md"
            and contains_all(texts["prompt"], ["do not write files"]),
            TARGETS["openai"],
            "Read-Only Explorer Binding",
            "`grill-me` must use the existing read-only explorer role binding.",
        ),
        result(
            "WWGM006",
            contains_all(
                texts["skill"],
                [
                    "only when the user explicitly requests",
                    "the orchestrator asks the user",
                    "exactly one unresolved question",
                    "must not select `grill-me` merely because a plan appears incomplete",
                ],
            ),
            TARGETS["skill"],
            "Orchestrator Protocol",
            "Missing explicit trigger, mediation, or one-question contract in SKILL.md.",
        ),
        result(
            "WWGM007",
            contains_all(
                texts["brief"],
                [
                    "## Grill-Me Decision Log",
                    "Decision ID",
                    "User-Confirmed Answer",
                    "Recommendation Offered",
                    "Dependencies Resolved",
                    "Dependent Branches Unblocked",
                    "the orchestrator owns this log",
                ],
            ),
            TARGETS["brief"],
            "Decision Persistence",
            "Missing durable orchestrator-owned Grill-Me Decision Log.",
        ),
        result(
            "WWGM008",
            contains_all(
                texts["registry"],
                [
                    "`grill-me`",
                    "explicitly requests",
                    "runtime_role: explorer",
                    "must not enter the worker candidate set",
                ],
            ),
            TARGETS["registry"],
            "Persona Selection Guidance",
            "Missing grill-me eligibility and role-boundary guidance.",
        ),
        result(
            "WWGM009",
            contains_all(
                texts["readme"],
                [
                    "$ww grill me",
                    "one question at a time",
                    "recommended answer",
                ],
            ),
            TARGETS["readme"],
            "User Guidance",
            "Missing user-facing grill-me trigger and interaction guidance.",
        ),
    ]
    return checks
```

Add the same `--json`, human `PASS: N rules checked`, failure reporting, and exit-code conventions used by `validate_ww_role_contracts.py`.

- [ ] **Step 4: Run focused tests**

Run:

```powershell
python tools/test_validate_ww_grill_me_contracts.py
```

Expected: all focused tests PASS.

- [ ] **Step 5: Confirm the current repository fails the new contract**

Run:

```powershell
python tools/validate_ww_grill_me_contracts.py
```

Expected: FAIL because the active persona, conditional protocol, decision log, and guidance have not been added yet.

- [ ] **Step 6: Commit the validator and tests**

```powershell
git add tools/validate_ww_grill_me_contracts.py tools/test_validate_ww_grill_me_contracts.py
git commit -m "Add grill-me contract validator"
```

### Task 2: Add The Built-In Persona And Conditional Explorer Protocol

**Files:**
- Modify: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
- Modify: `plugins/workwork/skills/ww-subagent-orchestrator/agents/explorer-prompt.md`
- Modify: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`

- [ ] **Step 1: Add the built-in persona record**

Append the `VALID_PERSONA` YAML equivalent from Task 1 to `built-in-personas.yaml`. Preserve these hard boundaries:

```yaml
  - id: grill-me
    title: Grill-Me Explorer
    category: product
    role_type: specialist
    domains:
      - planning
      - design
      - requirements
      - decision-analysis
    languages: []
    strengths:
      - decision-tree interrogation
      - dependency resolution
      - assumption surfacing
      - codebase-first investigation
    use_when:
      - the user explicitly asks to be grilled about a plan or design
      - the user explicitly asks to stress-test decisions one question at a time
    avoid_when:
      - the user did not explicitly request an intensive interview
      - the task is implementation or a simple factual investigation
    preferred_workflows:
      - superpowers:brainstorming
    decision_style: dependency-first
    quality_bar: shared-understanding quality
    tradeoff_bias: explicit user decisions over premature closure
    failure_modes_to_watch:
      - asking questions the repository can answer
      - closing branches without user confirmation
      - asking multiple unresolved questions at once
    escalation_triggers:
      - a prerequisite decision remains unresolved
      - the user answer conflicts with repository evidence
    collaboration_posture: relentless but bounded interviewer
    taste_criteria:
      - resolve dependencies before downstream preferences
      - keep each question narrow enough for one explicit answer
    review_only: false
    priority: 85
```

Do not add `implementation_principles`.

- [ ] **Step 2: Add the conditional prompt section**

Append this section to `agents/explorer-prompt.md`:

```markdown
## Grill-Me Conditional Protocol

This section defines the read-only `grill-me` viewpoint used inline by the orchestrator during planning. Do not assemble or launch an explorer packet for the interview. Otherwise ordinary explorer packet behavior remains unchanged.

- investigate the codebase and current artifacts before asking anything they can answer
- use repository-resolved evidence instead of turning it into a user question
- ask exactly one unresolved question per user turn
- prefer bounded options when they accurately represent the decision
- include one recommended answer and a concise reason with every question
- treat the recommendation as advice, never as user approval
- keep the branch open until the user explicitly confirms an answer or supplies a replacement
- resolve prerequisite decisions before dependent decisions
- continue until material branches, dependencies, tradeoffs, and risks are resolved
- allow the user to stop at any time
- finish with a compact shared-understanding summary for user confirmation

The orchestrator applies the viewpoint directly. It owns user interaction and decision persistence.
```

- [ ] **Step 3: Add registry selection guidance**

Under the explorer taxonomy and runtime selection guidance in `persona-registry.md`, add:

```markdown
`grill-me` is a built-in specialist persona that may resolve only to `runtime_role: explorer`. Select it only when the user explicitly requests an intensive plan or design interview, stress test, or equivalent one-question-at-a-time challenge. It must not enter the worker candidate set because it has no `implementation_principles`, and it must not be auto-selected merely because a plan appears incomplete.
```

- [ ] **Step 4: Run focused and existing role validation**

Run:

```powershell
python tools/test_validate_ww_grill_me_contracts.py
python tools/validate_ww_role_contracts.py
python tools/validate_ww_persona_packets.py
```

Expected:

- focused unit tests PASS
- existing reviewer/explorer role contracts PASS
- packet artifact validation PASS
- the focused repository validator still fails only for missing SKILL, working-brief, and README guidance

- [ ] **Step 5: Commit persona and prompt contracts**

```powershell
git add plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml plugins/workwork/skills/ww-subagent-orchestrator/agents/explorer-prompt.md plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md
git commit -m "Add grill-me explorer persona"
```

### Task 3: Add Inline Planning Mediation And Decision Persistence

**Files:**
- Modify: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
- Modify: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`

- [ ] **Step 1: Add the working-brief decision log**

Insert this section after `Persona And Workflow Guidance` and before `Runtime Preparation`:

```markdown
## Grill-Me Decision Log

The orchestrator owns this log. The `grill-me` explorer remains read-only and returns evidence or one unresolved question at a time.

Use one entry per decision:

- Decision ID:
- State: open | confirmed | stopped
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
```

- [ ] **Step 2: Add SKILL selection and interaction rules**

Add a `Grill-Me Explorer` subsection under `Persona Planning`:

```markdown
### Grill-Me Explorer

Select built-in persona `grill-me` only when the user explicitly requests to be grilled, interviewed relentlessly, or to stress-test a plan or design one decision at a time. The orchestrator must not select `grill-me` merely because a plan appears incomplete.

Use the `runtime_role: explorer` viewpoint defined by `agents/explorer-prompt.md`. It is read-only, has no `implementation_principles`, and is never eligible for worker or reviewer authority.

During the interview:

1. apply the grill-me viewpoint inline while finalizing the working brief
2. investigate repository-answerable questions first
3. briefly report material repository evidence
4. the orchestrator asks the user exactly one unresolved question
5. include the explorer's recommended answer and concise reason
6. require explicit user confirmation, another option, or a custom answer before closing the branch
7. persist the result in the working brief `Grill-Me Decision Log`
8. advance to the next newly unblocked branch

Do not create a packet, launch an explorer execution, or enter the runtime controller for the interview. If a dispatch plan already exists, freeze dispatch, set it to `revising`, increment the brief version, regenerate the plan, and require approval again.

Allow the user to stop at any time. Otherwise finish only when material branches and dependencies are resolved and the user confirms the shared-understanding summary.
```

- [ ] **Step 3: Run the focused validator**

Run:

```powershell
python tools/validate_ww_grill_me_contracts.py
```

Expected: only the README rule remains failing.

- [ ] **Step 4: Run persona-selection and skill validation**

Run:

```powershell
python tools/quick_validate.py plugins/workwork/skills/ww-subagent-orchestrator
python tools/validate_ww_persona_selection_contracts.py
python tools/validate_ww_role_contracts.py
```

Expected: all three validators PASS.

- [ ] **Step 5: Commit mediation and persistence contracts**

```powershell
git add plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md
git commit -m "Record grill-me interview decisions"
```

### Task 4: Add User Guidance And Repository-Suite Integration

**Files:**
- Modify: `README.md`
- Modify: `tools/validate_ww_repo.py`

- [ ] **Step 1: Add the user-facing example**

Add this example under `Example Prompts`:

```text
$ww grill me on this migration plan until every material decision is resolved.
```

Add this concise explanation after the example block:

```markdown
When the user explicitly asks for `grill-me`, WorkWork uses a read-only explorer to investigate repository facts first and then asks one question at a time through the orchestrator. Every question includes a recommended answer, but the decision remains open until the user confirms or replaces it.
```

- [ ] **Step 2: Document the validator**

Add to the maintainer command block:

```powershell
python tools/validate_ww_grill_me_contracts.py --json
python tools/test_validate_ww_grill_me_contracts.py
```

Update the repository-suite description to include `grill-me` explorer contract checks.

- [ ] **Step 3: Register the validator**

Add this check after the existing reviewer/explorer role-contract validator in `tools/validate_ww_repo.py`:

```python
(
    "Grill-me explorer contract validation",
    [python, "tools/validate_ww_grill_me_contracts.py"],
),
```

- [ ] **Step 4: Run focused validation**

Run:

```powershell
python tools/test_validate_ww_grill_me_contracts.py
python tools/validate_ww_grill_me_contracts.py
python tools/validate_ww_grill_me_contracts.py --json
```

Expected:

- unit tests PASS
- human validator reports `PASS: 9 rules checked`
- JSON reports `"ok": true` and `"rule_failures": 0`

- [ ] **Step 5: Commit docs and suite registration**

```powershell
git add README.md tools/validate_ww_repo.py
git commit -m "Integrate grill-me validation"
```

### Task 5: Full Verification And Contract Review

**Files:**
- Verify: all files changed in Tasks 1-4

- [ ] **Step 1: Run Python compilation**

Run:

```powershell
python -m py_compile tools/validate_ww_grill_me_contracts.py tools/test_validate_ww_grill_me_contracts.py tools/validate_ww_repo.py
```

Expected: exit code `0` with no output.

- [ ] **Step 2: Run the focused regression suite**

Run:

```powershell
python tools/test_validate_ww_grill_me_contracts.py
```

Expected: all tests PASS.

- [ ] **Step 3: Run the complete repository validator**

Run:

```powershell
python tools/validate_ww_repo.py
```

Expected: every child validator passes and the final line is `WW repository validation passed.`

- [ ] **Step 4: Run JSON aggregation**

Run:

```powershell
python tools/validate_ww_repo.py --json
```

Expected: valid JSON with `"ok": true` and `"check_failures": 0`.

- [ ] **Step 5: Check formatting and unintended scope**

Run:

```powershell
git diff --check
git status --short
git diff --stat HEAD~4
```

Expected:

- no whitespace errors
- only the files listed in this plan are changed
- no packet contract, project registry, routing category, or new prompt asset changes

- [ ] **Step 6: Review the final contract manually**

Confirm all of the following from the diff:

- ordinary explorer instructions remain the default
- the inline protocol activates only for an explicit grill-me request
- the persona has no `implementation_principles`
- the explorer never writes artifacts or speaks directly to the user
- the orchestrator asks one unresolved question per turn
- every question includes a recommendation but requires explicit user confirmation
- repository-answerable questions are investigated first
- confirmed decisions persist in the working brief
- the interview never assembles a packet or enters runtime control
- an existing plan is revised, regenerated, and reapproved
- dispatch-plan lifecycle ownership is unchanged
- no standalone skill, new runtime role, new prompt binding, routing expansion, or project-registry change was introduced

- [ ] **Step 7: Create a final verification commit only if verification required fixes**

If verification required edits, stage only those corrections and commit:

```powershell
git add README.md tools/validate_ww_repo.py tools/validate_ww_grill_me_contracts.py tools/test_validate_ww_grill_me_contracts.py plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md plugins/workwork/skills/ww-subagent-orchestrator/agents/explorer-prompt.md plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md
git commit -m "Fix grill-me contract verification"
```

If no corrections were needed, do not create an empty commit.
