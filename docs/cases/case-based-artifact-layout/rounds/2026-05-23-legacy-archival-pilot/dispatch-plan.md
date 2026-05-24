# Dispatch Plan: Legacy Archival Pilot

- Date: 2026-05-23
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: case-based-artifact-layout
- Round Slug: 2026-05-23-legacy-archival-pilot
- Case Root: `docs/cases/case-based-artifact-layout/`
- Round Root: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-archival-pilot/`
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
- archived legacy artifacts must not become active generation defaults

## Source Context

- User Request: `legacy archival pilot`
- Working Brief Reference: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-archival-pilot/working-brief.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: pilot a dedicated legacy archival move for pre-cutover type-based workflow documents while keeping `docs/cases/...` as the only active root for new rounds
- Relevant Context: the active workflow has already cut over to `docs/cases/...`; what remains is to gather older type-based artifacts into a clear archival surface
- Constraints:
  - do not widen into full historical repo cleanup
  - keep live `docs/cases/...` artifacts untouched
  - preserve active contract semantics unless the archival move exposes a concrete mismatch
- Risks:
  - overly broad moves could break historical references
  - an unclear legacy root could replace one ambiguity with another
  - active and archived material could blur if the archival rule is not explicit
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Legacy Archival Pilot

- Section ID: section-legacy-archival-pilot
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: staff-engineer-orchestrator
- Planned Reviewer Persona: pm-orchestrator
- Planned Specialist Personas: none
- Planned Scope:
  - `docs/legacy/**/*`
  - `README.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: active-path cutover is complete; the next bounded migration step is to classify and move the old type-based artifact families into a single obvious historical surface
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: validate-first
- Worker Mode Rationale: verify the archival boundary before moving files, then perform the smallest coherent archival slice
- Goal Tuning: validation-biased
- Constraint Interaction Rule: move historical type-based artifacts only; do not touch active `docs/cases/...` round files
- Planned Review Lanes:
  - Lane ID: lane-legacy-archival-pilot-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-archival-pilot/working-brief.md`
    - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-archival-pilot/dispatch-plan.md`
    - `path_glob`: `docs/legacy/**/*`
    - `path_glob`: `README.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `shared_read_scope`:
    - `path_glob`: `docs/cases/case-based-artifact-layout/**/*`
    - `path_glob`: `docs/legacy/superpowers/**/*`
    - `path_glob`: `tools/*.py`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: `ww_skill_contract`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `section_anchors`: `Document Summary Contract`
    - `artifact_id`: `case_layout_design`
    - `artifact_kind`: `doc`
    - `artifact_path`: `docs/legacy/superpowers/specs/2026-05-22-case-based-artifact-layout-design.md`
    - `section_anchors`: `Migration Strategy`, `Compatibility Rules`
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Legacy Archival Pilot

- Section ID: section-legacy-archival-pilot
- Runtime State: complete
- Active Execution ID: execution-legacy-archival-pilot
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
  - Execution ID: execution-legacy-archival-pilot
  - Role: orchestrator-implementation
  - Status: DONE
  - Owned Scope: `docs/legacy/superpowers/**/*`, `README.md`, `SKILL.md`, current round documents
  - Started At: 2026-05-23 America/Los_Angeles
  - Finished At: 2026-05-23 America/Los_Angeles
- Packet Records:
- Attempt Records:
  - Attempt ID: attempt-legacy-archival-pilot-1
  - Packet ID:
  - Agent ID:
  - Return Status: DONE
  - Runtime State After Return: complete
  - Launched At: 2026-05-23 America/Los_Angeles
  - Closed At: 2026-05-23 America/Los_Angeles
  - Result Summary: moved the old type-based workflow artifact families into `docs/legacy/superpowers/` and updated active references to the archived locations
  - Result Artifact Location: `docs/legacy/superpowers/`, `README.md`, `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`, `docs/superpowers/artifact-registry.yaml`
- Attempt Count: 1
- Last Update At: 2026-05-23 America/Los_Angeles
- Next Action: none
- Active Write Scope:
- Result Summary:
- Canonical Result Artifact Location:
- Concerns:
  - archived documents still contain many internal historical references to their old pre-archive paths, which is acceptable for this pilot but may merit a later normalization pass
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Legacy Archival Pilot

- Section ID: section-legacy-archival-pilot
- Review Target Strategy:
  - validate that archived artifacts are clearly separated from active case-based rounds
  - validate that only old type-based workflow artifact families are in scope
  - validate that active path guidance still points only to `docs/cases/...`
- Review Lane Records:
  - Lane ID: lane-legacy-archival-pilot-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Execution ID:
  - Packet ID:
  - Attempt ID:
  - Review Target Ref:
  - Reviewer Findings: no material findings
  - Orchestrator Synthesis: the archival boundary is now explicit, active rounds still point only to `docs/cases/...`, and the moved type-based families have one obvious historical home
  - Strict Review Outcome: none
  - Persistence rule: pre-approval plans must preserve this review-lane structure and outcome field pattern; `Review Status` must not reappear here, and durable review-lane data must retain `Reviewer Findings`, `Orchestrator Synthesis`, and the `Strict Review Outcome` field pattern.
  - Applicability rule: `Strict Review Outcome` is required when a strict-review target or durable strict-review result applies; otherwise keep the same field pattern without creating a second schema for valid non-strict lanes.
  - Invalid state note: `Review Status` reappears or durable strict-review outcome data is dropped when applicable.
- Human Decision: Approve
- Revision Notes:
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level `plan_state` is derived from `required_for_goal`

## Ordering And Parallelism

- Blocking work first: `section-legacy-archival-pilot`
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
- Notes: this pilot is scoped to defining and moving a bounded legacy artifact set only
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial legacy archival pilot round
- Supersedes Revision:

## Dispatch Log

- Agents Launched: none
- Retry Events:
- Close Events:
- Review Lane Transitions:
  - active `docs/cases/...` cutover confirmed
  - legacy archival identified as the next bounded migration step
  - working brief persisted
  - dispatch plan drafted
  - legacy type-based workflow artifact families moved under `docs/legacy/superpowers/`
  - active references updated to archived locations where needed
  - verification completed
- Launch Time: 2026-05-23 America/Los_Angeles
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
