# Dispatch Plan: Round Lifecycle Validator Pilot

- Date: 2026-05-25
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: case-based-artifact-layout
- Round Slug: 2026-05-25-round-lifecycle-validator-pilot
- Case Root: `docs/cases/case-based-artifact-layout/`
- Round Root: `docs/cases/case-based-artifact-layout/rounds/2026-05-25-round-lifecycle-validator-pilot/`
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

- User Request: `round lifecycle validator pilot`
- Working Brief Reference: `docs/cases/case-based-artifact-layout/rounds/2026-05-25-round-lifecycle-validator-pilot/working-brief.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: add repo-local validation for the lifecycle ownership rules so stale `Current Round` drift and state-surface duplication become machine-detectable
- Relevant Context: lifecycle ownership was defined in the prior round, but current validation only checks structure and case-path identity
- Constraints:
  - keep the validator structural
  - do not change helper behavior in this round
  - do not add a second lifecycle state surface to `case.md`
- Risks:
  - lifecycle checks could drift into content/prose linting
  - validator rules could accidentally require `case.md` to mirror round runtime state
  - weak checks could miss stale `Current Round` or bad state ownership
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Scaffold Draft

- Section ID: section-round-lifecycle-validator
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: staff-engineer-orchestrator
- Planned Reviewer Persona: pm-orchestrator
- Planned Specialist Personas: none
- Planned Scope:
  - `README.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `docs/cases/case-based-artifact-layout/case.md`
  - `docs/cases/case-based-artifact-layout/rounds/2026-05-25-round-lifecycle-validator-pilot/**/*`
  - `tools/validate_ww_repo.py`
  - `tools/validate_ww_round_lifecycle.py`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: the lifecycle ownership model is already defined, so the highest-leverage next step is to encode the bounded rules into repo-local validation
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: validate-first
- Worker Mode Rationale: verify the established ownership model first, then implement only the validator rules needed to catch stale pointers and ownership drift
- Goal Tuning: validation-biased
- Constraint Interaction Rule: new checks may tighten determinism, but they must preserve `case.md` as a navigational surface only
- Planned Review Lanes:
  - Lane ID: lane-round-lifecycle-validator-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `README.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `docs/cases/case-based-artifact-layout/case.md`
    - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-25-round-lifecycle-validator-pilot/working-brief.md`
    - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-25-round-lifecycle-validator-pilot/dispatch-plan.md`
    - `path_glob`: `tools/validate_ww_repo.py`
    - `path_glob`: `tools/validate_ww_round_lifecycle.py`
  - `shared_read_scope`:
    - `path_glob`: `docs/cases/**/*`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/**/*`
    - `path_glob`: `tools/scaffold_ww_case_artifacts.py`
    - `path_glob`: `tools/validate_ww_case_contracts.py`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: `case_entrypoint`
    - `artifact_kind`: `doc`
    - `artifact_path`: `docs/cases/case-based-artifact-layout/case.md`
    - `section_anchors`: `Current Round`, `Round Index`, `Notes`
    - `artifact_id`: `lifecycle_design`
    - `artifact_kind`: `doc`
    - `artifact_path`: `docs/cases/case-based-artifact-layout/rounds/2026-05-24-round-lifecycle-pilot/design-spec.md`
    - `section_anchors`: `Decisions`, `Ownership Model`, `Lifecycle Rules`
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Scaffold Draft

- Section ID: section-round-lifecycle-validator
- Runtime State: complete
- Active Execution ID: execution-round-lifecycle-validator-pilot
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
  - Execution ID: execution-round-lifecycle-validator-pilot
  - Role: orchestrator-implementation
  - Status: DONE
  - Owned Scope: `README.md`, `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`, `plugins/workwork/skills/ww-subagent-orchestrator/references/case-template.md`, `tools/validate_ww_round_lifecycle.py`, `tools/validate_ww_repo.py`, current round documents
  - Started At: 2026-05-25 America/Los_Angeles
  - Finished At: 2026-05-25 America/Los_Angeles
- Packet Records:
- Attempt Records:
  - Attempt ID: attempt-round-lifecycle-validator-pilot-1
  - Packet ID:
  - Agent ID:
  - Return Status: DONE
  - Runtime State After Return: complete
  - Launched At: 2026-05-25 America/Los_Angeles
  - Closed At: 2026-05-25 America/Los_Angeles
  - Result Summary: added a dedicated round lifecycle validator, wired it into repo validation, and tightened active lifecycle contract wording
  - Result Artifact Location: `tools/validate_ww_round_lifecycle.py`, `tools/validate_ww_repo.py`, `README.md`, `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`, `plugins/workwork/skills/ww-subagent-orchestrator/references/case-template.md`
- Attempt Count: 1
- Last Update At: 2026-05-25
- Next Action: none
- Active Write Scope:
- Result Summary:
- Canonical Result Artifact Location:
- Concerns:
  - lifecycle ownership is now machine-checkable, but further rounds may still choose to expand lifecycle validation if more state surfaces are introduced later
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Scaffold Draft

- Section ID: section-round-lifecycle-validator
- Review Target Strategy:
  - verify lifecycle checks match the prior round's ownership model
  - verify `case.md` is not required to mirror runtime state
  - verify stale `Current Round` and bad ownership patterns become detectable
- Review Lane Records:
  - Lane ID: lane-round-lifecycle-validator-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Execution ID:
  - Packet ID:
  - Attempt ID:
  - Review Target Ref:
  - Reviewer Findings: no material findings
  - Orchestrator Synthesis: the validator stays structural, enforces stale-pointer and authority-boundary rules, and does not turn `case.md` into a second state machine
  - Strict Review Outcome: none
- Human Decision: Approve
- Revision Notes:

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
- Approval Time: 2026-05-25 America/Los_Angeles
- Notes: lifecycle validator pilot approved and completed after full repo validation passed
