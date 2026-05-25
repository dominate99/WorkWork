# Dispatch Plan: Round Lifecycle Pilot

- Date: 2026-05-24
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: case-based-artifact-layout
- Round Slug: 2026-05-24-round-lifecycle-pilot
- Case Root: `docs/cases/case-based-artifact-layout/`
- Round Root: `docs/cases/case-based-artifact-layout/rounds/2026-05-24-round-lifecycle-pilot/`
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

- User Request: `round lifecycle pilot`
- Working Brief Reference: `docs/cases/case-based-artifact-layout/rounds/2026-05-24-round-lifecycle-pilot/working-brief.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: define deterministic case/round lifecycle ownership so `case.md` stays current without becoming a second runtime state machine
- Relevant Context: current structure already has case-based paths, scaffold-first initialization, and case contract validation, but not lifecycle-state semantics across rounds
- Constraints:
  - keep scope on lifecycle semantics and bounded active documentation surfaces
  - do not widen helper responsibilities in this round
  - do not re-open legacy handling or packet/runtime contracts
- Risks:
  - lifecycle rules could accidentally turn `case.md` into an execution ledger
  - weak rules could still allow stale current-round pointers
  - duplicate lifecycle ownership across case and round files could reintroduce ambiguity
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Scaffold Draft

- Section ID: section-round-lifecycle
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: staff-engineer-orchestrator
- Planned Reviewer Persona: pm-orchestrator
- Planned Specialist Personas: none
- Planned Scope:
  - `docs/cases/case-based-artifact-layout/case.md`
  - `docs/cases/case-based-artifact-layout/rounds/2026-05-24-round-lifecycle-pilot/**/*`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: the highest-leverage next step is to define who owns lifecycle state between `case.md` and round dispatch artifacts before adding more automation
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: validate-first
- Worker Mode Rationale: inspect the current case/round contract surfaces first, then add only the minimal lifecycle rules needed to remove ambiguity
- Goal Tuning: validation-biased
- Constraint Interaction Rule: stronger lifecycle semantics may update ownership rules, but must preserve `case.md` as a lightweight case entrypoint
- Planned Review Lanes:
  - Lane ID: lane-round-lifecycle-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/case-based-artifact-layout/case.md`
    - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-24-round-lifecycle-pilot/working-brief.md`
    - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-24-round-lifecycle-pilot/dispatch-plan.md`
    - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-24-round-lifecycle-pilot/design-spec.md`
    - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-24-round-lifecycle-pilot/implementation-plan.md`
  - `shared_read_scope`:
    - `path_glob`: `docs/cases/**/*`
    - `path_glob`: `README.md`
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
    - `artifact_id`: `round_dispatch`
    - `artifact_kind`: `doc`
    - `artifact_path`: `docs/cases/case-based-artifact-layout/rounds/2026-05-24-round-lifecycle-pilot/dispatch-plan.md`
    - `section_anchors`: `Plan State`, `Section Runtime Ledger`, `Approval Block`
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Scaffold Draft

- Section ID: section-round-lifecycle
- Runtime State: complete
- Active Execution ID: execution-round-lifecycle-pilot
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
  - Execution ID: execution-round-lifecycle-pilot
  - Role: orchestrator-implementation
  - Status: DONE
  - Owned Scope: `docs/cases/case-based-artifact-layout/case.md`, current round documents
  - Started At: 2026-05-24 America/Los_Angeles
  - Finished At: 2026-05-24 America/Los_Angeles
- Packet Records:
- Attempt Records:
  - Attempt ID: attempt-round-lifecycle-pilot-1
  - Packet ID:
  - Agent ID:
  - Return Status: DONE
  - Runtime State After Return: complete
  - Launched At: 2026-05-24 America/Los_Angeles
  - Closed At: 2026-05-24 America/Los_Angeles
  - Result Summary: defined deterministic lifecycle ownership between `case.md` and per-round dispatch artifacts without expanding `case.md` into a runtime ledger
  - Result Artifact Location: `docs/cases/case-based-artifact-layout/rounds/2026-05-24-round-lifecycle-pilot/`
- Attempt Count: 1
- Last Update At: 2026-05-24
- Next Action: none
- Active Write Scope:
- Result Summary:
- Canonical Result Artifact Location:
- Concerns:
  - a later validator round may still be useful if stale `Current Round` drift becomes common in practice
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Scaffold Draft

- Section ID: section-round-lifecycle
- Review Target Strategy:
  - verify lifecycle ownership is deterministic
  - verify `case.md` stays navigational instead of becoming a runtime state machine
  - verify stale round pointers become detectable without requiring broad new metadata
- Review Lane Records:
  - Lane ID: lane-round-lifecycle-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Execution ID:
  - Packet ID:
  - Attempt ID:
  - Review Target Ref:
  - Reviewer Findings: no material findings
  - Orchestrator Synthesis: lifecycle ownership is now deterministic while `case.md` remains a navigational index rather than a duplicate runtime ledger
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
- Approval Time: 2026-05-24 America/Los_Angeles
- Notes: bounded lifecycle-definition pilot approved and completed without widening runtime semantics
