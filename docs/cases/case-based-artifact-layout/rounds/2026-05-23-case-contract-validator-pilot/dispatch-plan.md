# Dispatch Plan: Case Contract Validator Pilot

- Date: 2026-05-24
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: case-based-artifact-layout
- Round Slug: 2026-05-23-case-contract-validator-pilot
- Case Root: `docs/cases/case-based-artifact-layout/`
- Round Root: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-case-contract-validator-pilot/`
- Plan State: completed
- Last Approved Revision: 1
- Rollback Baseline Revision: none
- Task Routing: code/programming
- Main Orchestrator: staff-engineer-orchestrator

## Strict Review Runtime State

```yaml
strict_review:
  mode: standard
  target: none
  state: idle
  cycle_count: 0
```

## Preconditions

- Estimation Complete: true
- Working Brief Status: ready

> Do not launch any real subagent until the preconditions are satisfied and `Plan State: approved`.

Path identity rules:

- `Case Root` must resolve to `docs/cases/<case_slug>/`
- `Round Root` must resolve to `docs/cases/<case_slug>/rounds/<round_slug>/`
- new dispatch-round artifacts are canonically written under `Round Root`
- legacy type-based paths are legacy history only; they are not canonical targets or ongoing generation defaults

## Source Context

- User Request: `case contract validator pilot`
- Working Brief Reference: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-case-contract-validator-pilot/working-brief.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: turn the current case/round structure from convention into a machine-checked contract
- Relevant Context: active case-based paths and a scaffold helper already exist; the missing pieces are a dedicated `case.md` template and a validator for `case.md` plus minimum round files
- Constraints:
  - keep the validator structural
  - add a formal `case.md` template to the contract surface
  - avoid broad content-quality checks
  - wire the validator into the repo-level entrypoint
- Risks:
  - the validator could overshoot into semantic review
  - helper expectations and contract expectations could drift
  - weak field rules could still leave ambiguity
  - without a dedicated template, `case.md` field rules could be encoded only in validator logic
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Case Contract Validator Pilot

- Section ID: section-case-contract-validator-pilot
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: staff-engineer-orchestrator
- Planned Reviewer Persona: pm-orchestrator
- Planned Specialist Personas: none
- Planned Scope:
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/case-template.md`
  - `tools/validate_ww_case_contracts.py`
  - `tools/validate_ww_repo.py`
  - `README.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `docs/cases/case-based-artifact-layout/rounds/2026-05-23-case-contract-validator-pilot/**/*`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: the highest-leverage next step is to define the `case.md` template and make the case/round structure deterministic and machine-validated
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: validate-first
- Worker Mode Rationale: define the hard case contract first, then implement only the narrow validator needed to enforce it
- Goal Tuning: validation-biased
- Constraint Interaction Rule: validator should enforce structure only and must not expand into workflow-content judgment
- Planned Review Lanes:
  - Lane ID: lane-case-contract-validator-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/case-template.md`
    - `path_glob`: `tools/validate_ww_case_contracts.py`
    - `path_glob`: `tools/validate_ww_repo.py`
    - `path_glob`: `README.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-case-contract-validator-pilot/**/*`
  - `shared_read_scope`:
    - `path_glob`: `docs/cases/**/*`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/**/*`
    - `path_glob`: `tools/*.py`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: `case_entrypoint`
    - `artifact_kind`: `doc`
    - `artifact_path`: `docs/cases/case-based-artifact-layout/case.md`
    - `section_anchors`: `Round Index`, `Notes`
    - `artifact_id`: `brief_template`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `section_anchors`: `Artifact Metadata`, `Artifact-layout rules`
    - `artifact_id`: `dispatch_template`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `section_anchors`: `Path identity rules`, `Approval Block`
- Planned contract additions:
  - dedicated `case.md` template
  - validator rules for `case.md` presence and required fields
  - validator rules for minimum round artifacts
  - helper conformance checks against the same contract
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Case Contract Validator Pilot

- Section ID: section-case-contract-validator-pilot
- Runtime State: complete
- Active Execution ID: execution-case-contract-validator-pilot
- Active Packet ID:
- Active Agent ID:
- Active Attempt ID:
- Active Worker Mode: validate-first
- Mode Change History:
  - Previous Mode:
  - New Mode:
  - Trigger Evidence:
  - Approved By:
  - Changed At:
- Execution Records:
  - Execution ID: execution-case-contract-validator-pilot
  - Role: orchestrator-implementation
  - Status: DONE
  - Owned Scope: `plugins/workwork/skills/ww-subagent-orchestrator/references/case-template.md`, `tools/validate_ww_case_contracts.py`, `tools/validate_ww_repo.py`, `README.md`, `SKILL.md`, current round documents
  - Started At: 2026-05-24 America/Los_Angeles
  - Finished At: 2026-05-24 America/Los_Angeles
- Packet Records:
- Attempt Records:
  - Attempt ID: attempt-case-contract-validator-pilot-1
  - Packet ID:
  - Agent ID:
  - Return Status: DONE
  - Runtime State After Return: complete
  - Launched At: 2026-05-24 America/Los_Angeles
  - Closed At: 2026-05-24 America/Los_Angeles
  - Result Summary: added a dedicated `case.md` template, a repo-local case contract validator, repo validator wiring, and helper conformance checks against the same structure rules
  - Result Artifact Location: `plugins/workwork/skills/ww-subagent-orchestrator/references/case-template.md`, `tools/validate_ww_case_contracts.py`, `tools/validate_ww_repo.py`, `README.md`, `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- Attempt Count: 1
- Last Update At: 2026-05-24 America/Los_Angeles
- Next Action: none
- Active Write Scope:
- Result Summary:
- Canonical Result Artifact Location:
- Concerns:
  - field minimums must be strict enough to be useful without turning into prose linting
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Case Contract Validator Pilot

- Section ID: section-case-contract-validator-pilot
- Review Target Strategy:
  - validate that the contract is structural and deterministic
  - validate that `case.md` requirements are documented in a template, not only in validator code
  - validate that helper output is covered by the same rules
  - validate that active case-based paths remain canonical
- Review Lane Records:
  - Lane ID: lane-case-contract-validator-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Execution ID:
  - Packet ID:
  - Attempt ID:
  - Review Target Ref:
  - Reviewer Findings: no material findings
  - Orchestrator Synthesis: the contract is now template-backed, helper output is checked against the same rules, and the validator stays structural rather than drifting into prose-quality review
  - Strict Review Outcome: none
- Human Decision: Approve
- Revision Notes:

## Ordering And Parallelism

- Blocking work first: `section-case-contract-validator-pilot`
- Parallel sections: none
- Review loop per section: draft -> reviewer findings -> orchestrator synthesis -> human judgment

## Approval Block

- Required Human Choice (rendered labels):
  - `1. Approve`
  - `2. Revise`
  - `3. Stop`
- Numeric Reply Mapping:
  - `1` -> `Approve`
  - `2` -> `Revise`
  - `3` -> `Stop`
- Canonical Decision Values: `Approve` | `Revise` | `Stop`
- Accepted Word Replies: `Approve` | `Revise` | `Stop`
- Current Choice: Approve
- Approved By: user
- Approval Time: 2026-05-24 America/Los_Angeles
- Notes: this pilot is scoped to structural case/round validation and includes a dedicated `case.md` template
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`
- Revision History:
  - Revision 1 Created From Brief Version: 1
  - Revision Reason: initial case contract validator pilot round
  - Supersedes Revision:
- Dispatch Log:
  - Agents Launched: none
  - Retry Events:
  - Close Events:
  - Review Lane Transitions:
    - `case.md` template requirement added during approval revision
    - working brief persisted
    - dispatch plan drafted
    - `case-template.md` created
    - case contract validator implemented
    - repo-level validator wired to the new case contract validator
    - helper conformance validated with temporary scaffold output
    - verification completed
  - Launch Time: 2026-05-24 America/Los_Angeles
  - Revisions Since Approval:
  - Stop State Preserves Files: true
  - No Launch Before Approval: true
  - Result Artifact Location Source: latest active attempt record
