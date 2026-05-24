# Dispatch Plan: Case Artifact Scaffolding Pilot

- Date: 2026-05-23
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: case-based-artifact-layout
- Round Slug: 2026-05-23-case-artifact-scaffolding-pilot
- Case Root: `docs/cases/case-based-artifact-layout/`
- Round Root: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-case-artifact-scaffolding-pilot/`
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

- User Request: `case artifact scaffolding pilot`
- Working Brief Reference: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-case-artifact-scaffolding-pilot/working-brief.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: add a repo-local scaffolding helper that creates case-based WW round skeletons under `docs/cases/...` and updates `case.md` without introducing workflow decision logic
- Relevant Context: the repo has stable case-based artifact paths and templates, but no helper to generate a new case/round structure consistently
- Constraints:
  - helper must stay structure-only
  - `working-brief.md` and `dispatch-plan.md` should be default outputs
  - `design-spec.md` and `implementation-plan.md` should remain opt-in outputs
- Risks:
  - helper could accidentally become a hidden workflow controller
  - helper could overwrite existing round files too easily
  - helper could rewrite `case.md` more aggressively than intended
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Case Artifact Scaffolding Pilot

- Section ID: section-case-artifact-scaffolding-pilot
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: staff-engineer-orchestrator
- Planned Reviewer Persona: pm-orchestrator
- Planned Specialist Personas: none
- Planned Scope:
  - `tools/scaffold_ww_case_artifacts.py`
  - `README.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `docs/cases/case-based-artifact-layout/case.md`
  - `docs/cases/case-based-artifact-layout/rounds/2026-05-23-case-artifact-scaffolding-pilot/**/*`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: now that case-based paths are stable, the highest-leverage next step is a minimal helper that makes new round setup deterministic
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: conservative-first
- Worker Mode Rationale: the helper should be the smallest coherent addition that reduces manual scaffolding without adding runtime behavior
- Goal Tuning: safety-biased
- Constraint Interaction Rule: generate structure and placeholders only; do not infer approval state or dispatch logic
- Planned Review Lanes:
  - Lane ID: lane-case-artifact-scaffolding-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `tools/scaffold_ww_case_artifacts.py`
    - `path_glob`: `README.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `docs/cases/case-based-artifact-layout/case.md`
    - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-case-artifact-scaffolding-pilot/**/*`
  - `shared_read_scope`:
    - `path_glob`: `docs/cases/**/*`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/**/*`
    - `path_glob`: `tools/*.py`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: `brief_template`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `section_anchors`: `Artifact Metadata`, `Artifact-layout rules`
    - `artifact_id`: `dispatch_template`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `section_anchors`: `Path identity rules`, `Approval Block`
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Case Artifact Scaffolding Pilot

- Section ID: section-case-artifact-scaffolding-pilot
- Runtime State: complete
- Active Execution ID: execution-case-artifact-scaffolding-pilot
- Active Packet ID:
- Active Agent ID:
- Active Attempt ID:
- Active Worker Mode: conservative-first
- Mode Change History:
  - Previous Mode:
  - New Mode:
  - Trigger Evidence:
  - Approved By:
  - Changed At:
- Execution Records:
  - Execution ID: execution-case-artifact-scaffolding-pilot
  - Role: orchestrator-implementation
  - Status: DONE
  - Owned Scope: `tools/scaffold_ww_case_artifacts.py`, `README.md`, `SKILL.md`, `docs/cases/case-based-artifact-layout/case.md`, current round documents
  - Started At: 2026-05-23 America/Los_Angeles
  - Finished At: 2026-05-23 America/Los_Angeles
- Packet Records:
- Attempt Records:
  - Attempt ID: attempt-case-artifact-scaffolding-pilot-1
  - Packet ID:
  - Agent ID:
  - Return Status: DONE
  - Runtime State After Return: complete
  - Launched At: 2026-05-23 America/Los_Angeles
  - Closed At: 2026-05-23 America/Los_Angeles
  - Result Summary: added a repo-local helper that scaffolds case/round artifacts, updates `case.md`, and keeps optional round documents opt-in
  - Result Artifact Location: `tools/scaffold_ww_case_artifacts.py`, `README.md`, `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- Attempt Count: 1
- Last Update At: 2026-05-23 America/Los_Angeles
- Next Action: none
- Active Write Scope:
- Result Summary:
- Canonical Result Artifact Location:
- Concerns:
  - helper output is only a starting point and still needs humans to fill in planning content
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Case Artifact Scaffolding Pilot

- Section ID: section-case-artifact-scaffolding-pilot
- Review Target Strategy:
  - validate that the helper creates only structural placeholders
  - validate that helper defaults stay aligned with the active case-based contract
  - validate that `case.md` updates are additive and navigational
- Review Lane Records:
  - Lane ID: lane-case-artifact-scaffolding-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Execution ID:
  - Packet ID:
  - Attempt ID:
  - Review Target Ref:
  - Reviewer Findings: no material findings
  - Orchestrator Synthesis: the helper stays narrow, defaults to the two required round artifacts, and leaves optional planning artifacts behind explicit flags
  - Strict Review Outcome: none
- Human Decision: Approve
- Revision Notes:

## Ordering And Parallelism

- Blocking work first: `section-case-artifact-scaffolding-pilot`
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
- Approval Time: 2026-05-23 America/Los_Angeles
- Notes: this pilot is scoped to helper-based scaffolding only

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial case artifact scaffolding pilot round
- Supersedes Revision:

## Dispatch Log

- Agents Launched: none
- Retry Events:
- Close Events:
- Review Lane Transitions:
  - case-based artifact generation and legacy cleanup completed
  - scaffold helper identified as the next bounded usability step
  - working brief persisted
  - dispatch plan drafted
  - helper implemented
  - helper usage documented
  - smoke test and validation completed
- Launch Time: 2026-05-23 America/Los_Angeles
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
