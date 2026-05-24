# Dispatch Plan: Legacy Normalization Pilot

- Date: 2026-05-23
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: case-based-artifact-layout
- Round Slug: 2026-05-23-legacy-normalization-pilot
- Case Root: `docs/cases/case-based-artifact-layout/`
- Round Root: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-normalization-pilot/`
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
- legacy normalization must not reactivate archived artifacts as generation defaults

## Source Context

- User Request: `legacy normalization pilot`
- Working Brief Reference: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-normalization-pilot/working-brief.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: normalize archived legacy workflow documents so the historical surface is easier to browse and less internally inconsistent, without changing the active workflow root
- Relevant Context: legacy archival is complete; what remains is a bounded cleanup of stale internal path references and legacy-surface guidance
- Constraints:
  - do not touch active `docs/cases/...` artifacts outside the current round
  - do not rewrite historical decisions beyond what normalization requires
  - keep the pass bounded and mechanically reviewable
- Risks:
  - normalization could sprawl into low-value historical editing
  - archived docs could accidentally be made to look active again
  - a weak stop condition could make this round much larger than intended
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Legacy Normalization Pilot

- Section ID: section-legacy-normalization-pilot
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: staff-engineer-orchestrator
- Planned Reviewer Persona: pm-orchestrator
- Planned Specialist Personas: none
- Planned Scope:
  - `docs/legacy/superpowers/**/*`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: archival created a clear historical home; the next bounded step is to reduce stale internal path drift and improve readability inside that archival surface
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: validate-first
- Worker Mode Rationale: define the normalization bar first, then apply only the smallest coherent cleanup that materially improves legacy consistency
- Goal Tuning: validation-biased
- Constraint Interaction Rule: normalize archived workflow docs only; do not widen into active workflow redesign or full historical rewriting
- Planned Review Lanes:
  - Lane ID: lane-legacy-normalization-pilot-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/case-based-artifact-layout/case.md`
    - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-normalization-pilot/working-brief.md`
    - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-normalization-pilot/dispatch-plan.md`
    - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-normalization-pilot/design-spec.md`
    - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-normalization-pilot/implementation-plan.md`
    - `path_glob`: `docs/legacy/superpowers/**/*`
  - `shared_read_scope`:
    - `path_glob`: `docs/cases/case-based-artifact-layout/**/*`
    - `path_glob`: `README.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/**/*`
    - `path_glob`: `tools/*.py`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: `legacy_index`
    - `artifact_kind`: `doc`
    - `artifact_path`: `docs/legacy/superpowers/README.md`
    - `section_anchors`: none
    - `artifact_id`: `legacy_archival_design`
    - `artifact_kind`: `doc`
    - `artifact_path`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-archival-pilot/design-spec.md`
    - `section_anchors`: `Goal`, `Legacy Surface`, `Decisions`
    - `artifact_id`: `legacy_normalization_design`
    - `artifact_kind`: `doc`
    - `artifact_path`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-normalization-pilot/design-spec.md`
    - `section_anchors`: `Goal`, `Normalization Rule`, `Decisions`
    - `artifact_id`: `legacy_normalization_plan`
    - `artifact_kind`: `doc`
    - `artifact_path`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-normalization-pilot/implementation-plan.md`
    - `section_anchors`: `Goal`, `Steps`, `Guardrails`
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Legacy Normalization Pilot

- Section ID: section-legacy-normalization-pilot
- Runtime State: complete
- Active Execution ID: execution-legacy-normalization-pilot
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
  - Execution ID: execution-legacy-normalization-pilot
  - Role: orchestrator-implementation
  - Status: DONE
  - Owned Scope: `docs/legacy/superpowers/**/*`, `docs/cases/case-based-artifact-layout/case.md`, current round documents
  - Started At: 2026-05-23 America/Los_Angeles
  - Finished At: 2026-05-23 America/Los_Angeles
- Packet Records:
- Attempt Records:
  - Attempt ID: attempt-legacy-normalization-pilot-1
  - Packet ID:
  - Agent ID:
  - Return Status: DONE
  - Runtime State After Return: complete
  - Launched At: 2026-05-23 America/Los_Angeles
  - Closed At: 2026-05-23 America/Los_Angeles
  - Result Summary: normalized archive-facing legacy path references to `docs/legacy/superpowers/...` where they function as navigational pointers, while preserving intentional historical source references
  - Result Artifact Location: `docs/legacy/superpowers/**/*`, `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-normalization-pilot/design-spec.md`, `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-normalization-pilot/implementation-plan.md`
- Attempt Count: 1
- Last Update At: 2026-05-23 America/Los_Angeles
- Next Action: none
- Active Write Scope:
- Result Summary:
- Canonical Result Artifact Location:
- Concerns:
  - intentional historical mentions of pre-archive `docs/superpowers/...` paths remain in a small number of design and migration-story passages
  - legacy readability improved, but the archive still intentionally preserves historical language rather than pretending it was always case-based
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Legacy Normalization Pilot

- Section ID: section-legacy-normalization-pilot
- Review Target Strategy:
  - validate that normalization stays inside the archived legacy surface
  - validate that active roots remain untouched
  - validate that the cleanup is mechanical and bounded
- Review Lane Records:
  - Lane ID: lane-legacy-normalization-pilot-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Execution ID:
  - Packet ID:
  - Attempt ID:
  - Review Target Ref:
  - Reviewer Findings: no material findings
  - Orchestrator Synthesis: the normalization stayed inside `docs/legacy/superpowers`, upgraded archive-facing path references to the archived root, and left only intentional historical source-path mentions behind
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

- Blocking work first: `section-legacy-normalization-pilot`
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
- Notes: this pilot is scoped to bounded legacy-surface normalization only
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial legacy normalization pilot round
- Supersedes Revision:

## Dispatch Log

- Agents Launched: none
- Retry Events:
- Close Events:
- Review Lane Transitions:
  - legacy archival completion reviewed
  - legacy normalization identified as optional follow-up work
  - working brief persisted
  - dispatch plan drafted
  - normalization rule defined
  - archive-facing legacy path references normalized to `docs/legacy/superpowers/...`
  - residual old-path mentions reviewed and bounded to historical-source context
  - verification completed
- Launch Time: 2026-05-23 America/Los_Angeles
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
