# Dispatch Plan: {{topic}}

- Date: {{date}}
- Schema Version: 2
- Plan Revision: 1
- Working Brief Version: {{brief_version}}
- Case Slug: {{case_slug}}
- Round Slug: {{round_slug}}
- Case Root: {{case_root}}
- Round Root: {{round_root}}
- Plan State: awaiting-approval
- Last Approved Revision: none
- Rollback Baseline Revision: none
- Task Routing: {{task_routing}}
- Main Orchestrator: {{main_orchestrator}}
- Lifecycle Protocol: legacy | task-runtime-v1

Lifecycle protocol rules:

- `Lifecycle Protocol` is round-owned compatibility metadata and is selected only by an approved dispatch revision.
- New and ordinary rounds must render `legacy`.
- Schema version 2 support does not activate `task-runtime-v1`.
- A `legacy` plan must not render or consult section lifecycle snapshots, lifecycle event histories, or a writable round-level lifecycle phase.
- Required sections in one active round may not mix protocols.
- `task-runtime-v1` may be selected only after every activation prerequisite in `references/task-runtime-lifecycle.md` is implemented and approved.
- Verifier authority, verifier lanes, evidence records, baseline/risk-triggered lane selection, and model capability profile/floor/resolution are defined in `references/task-runtime-verification.md`.
- Internal hooks, quality gates/scoring, repair authorization/re-verification, close gates, final human judgment, recovery requirements, and checkpoints are defined in `references/task-runtime-missing-capabilities.md`.
- Dormant verifier/lane and missing-capability fields must not be treated as lifecycle authority while `Lifecycle Protocol: legacy`.

## Strict Review Runtime State

```yaml
strict_review:
  mode: standard | strict
  target: none | design-spec | implementation-plan
  state: idle | self-review | reviewer-review | patching | re-review | passed | blocked
  cycle_count: 0
```

Rules:

- The `strict_review` block is a required top-level runtime-state surface in every round; omission is invalid even when no strict target is active.
- Standard `$ww` rounds must still render `mode: standard`, `target: none`, `state: idle`, and `cycle_count: 0`.
- When a strict-review target is active, `strict_review` also serves as the live target-specific gate record for that target.
- `strict_review.target`, `state`, and `cycle_count` apply to the active strict-review target only.
- When a new target is allowed to start, initialize the live gate record for that target with `target`, `state: idle`, and `cycle_count: 0`, then enter `self-review` through `STRICT_TARGET_STARTED`.
- A blocked target may not be overwritten by switching `strict_review.target` in the same round; it must follow the existing human `Revise` path into a new approved round or revision.
- `strict_review` does not replace section-level `runtime_state`; `runtime_state` remains the single authoritative post-launch section state.
- `strict_review.target` is only the strict-review target-kind discriminator: `none` | `design-spec` | `implementation-plan`.
- Concrete artifact identity and artifact revision continue to come from persisted artifact paths and reviewer `review target` references elsewhere in the controller model.
- Durable per-target strict-review outcomes remain in `Review Lane Records` keyed by `Review Target Ref`, so switching the live gate record to a later target does not erase whether an earlier target revision already passed or blocked.
- Invalid state note: omitting the `strict_review` runtime block is invalid.

## Preconditions

- Estimation Complete: {{true_or_false}}
- Working Brief Status: ready|draft

> Do not launch any real subagent until the preconditions are satisfied and `Plan State: approved`.

Path identity rules:

- `Case Root` must resolve to `docs/cases/<case_slug>/`
- `Round Root` must resolve to `docs/cases/<case_slug>/rounds/<round_slug>/`
- new dispatch-round artifacts are canonically written under `Round Root`
- legacy type-based paths are legacy history only; they are not canonical targets or ongoing generation defaults

## Source Context

- User Request: {{user_request}}
- Working Brief Reference: {{working_brief_reference}}
- Artifact Registry Reference: {{artifact_registry_reference}}

## Dispatch Summary

- Goal: {{goal}}
- Relevant Context: {{relevant_context}}
- Constraints: {{constraints}}
- Risks: {{risks}}
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: {{section_name}}

- Section ID: {{section_id}}
- Section State: drafted
- Runtime State: queued
- Required For Goal: true|false
- Draft Author Role: {{draft_author}}
- Planned Reviewer Persona: {{reviewer_persona}}
- Planned Reviewer Persona Source: project | built-in
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: {{reviewer_persona_rationale}}
- Planned Specialist Personas: {{specialist_personas}}
- Planned Specialist Persona Sources:
  - Persona ID:
  - Source: project | built-in
  - Runtime Role: worker | explorer | none
  - Selection Rationale:
- Planned Scope: {{owned_scope}}
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: {{persona_rationale}}
- Planned Workflow Bindings: {{workflow_bindings}}
- Planned Worker Mode: {{planned_worker_mode}}
- Worker Mode Rationale: {{worker_mode_rationale}}
- Goal Tuning: {{goal_tuning}}
- Constraint Interaction Rule: {{constraint_interaction_rule}}
- `Planned Worker Mode` is the section-level execution posture chosen for worker launches.
- `Planned Worker Mode` must align with the working brief recommendation unless an explicit override rationale is recorded.
- `task_mode` remains the role-task field (`implement` | `review` | `investigate`) and must not be reused as `worker mode`.
- `Goal Tuning` may modify execution emphasis, but it must not replace or contradict `Planned Worker Mode`.
- `Constraint Interaction Rule` must state how user constraints bound the planned worker mode for the section.
- Planned Review Lanes:
  - Lane ID:
  - Lane Type: spec-review | code-quality-review | scope-review | editorial-review | other
  - Reviewer Persona:
  - Reviewer Source: project | built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale:
  - Required: true|false
- Review lane mapping rule: default built-in reviewer mapping is `spec-review` -> `spec-reviewer`, `code-quality-review` -> `code-quality-reviewer`, `scope-review` -> `product-scope-reviewer`, `editorial-review` -> `editorial-reviewer`, and `other` -> explicit rationale only.
- Cross-cutting reviewer rule: add `secure-software-engineer`, `accessibility-ux-reviewer`, or `documentation-clarity-reviewer` as a second review lane when that risk surface is independently material, or use one for `other` only with explicit rationale that no durable lane type fits.
- Worker specialist mapping rule: select worker specialists by owned scope and dominant implementation risk, not top-level `task_routing` alone.
- Persona source rule: project personas win only after role-gate and required-field eligibility, and only when stronger or project-specific; otherwise record built-in fallback rationale.
- Scope Declarations:
  - `exclusive_write_scope`:
  - `shared_read_scope`:
  - `depends_on_sections`:
  - `parallel_safe_with_sections`:
  - `artifact_mappings`:
    - `artifact_id`:
    - `artifact_kind`:
    - `artifact_path`:
    - `section_anchors`:
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Invalid state note: `Planned Scope` includes a writable file not mirrored in `exclusive_write_scope`.
- Packet Created: false

## Section Runtime Ledger

### Section: {{section_name}}

- Section ID: {{section_id}}
- Runtime State: queued
- Active Execution ID:
- Active Packet ID:
- Active Agent ID:
- Active Attempt ID:
- Active Worker Mode:
- Active Persona IDs:
- Active Persona Sources:
- Active Persona Role Bindings:
- Mode Change History:
  - Previous Mode:
  - New Mode:
  - Trigger Evidence:
  - Approved By:
  - Changed At:
- `Active Worker Mode` is the launch-time or currently effective mode for the active section execution.
- Any worker-mode change caused by new evidence must be recorded in `Mode Change History` before a new worker packet is created.
- An unrecorded worker-mode change is invalid and must not be treated as controller-approved execution state.
- Execution Records:
  - Execution ID:
  - Role:
  - Status:
  - Owned Scope:
  - Started At:
  - Finished At:
- Packet Records:
  - Packet ID:
  - Execution ID:
  - Stage:
  - Template Path:
  - Review Target Ref:
  - Supersedes Attempt ID:
  - Accepts Late Results:
- Attempt Records:
  - Attempt ID:
  - Packet ID:
  - Agent ID:
  - Return Status:
  - Runtime State After Return:
  - Launched At:
  - Closed At:
  - Result Summary:
  - Result Artifact Location:
- Attempt Count: 0
- Last Update At:
- Next Action:
- Active Write Scope:
- Result Summary:
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns:
- Blocker Reason:
- Close State: open
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

### Section Lifecycle Record: {{section_name}} (`task-runtime-v1` only)

Render this block only when the approved round protocol is `task-runtime-v1`.
Omit the entire block for `legacy` rounds.

```yaml
lifecycle:
  phase: plan | execute | verify | review | fix | re-verify | score | close
  phase_entered_at: <timestamp>
  event_head: <event-id-or-null>
  next_action:
    code: <canonical-code>
    detail: <non-authoritative-explanation>
lifecycle_event_history:
  - event_id:
    sequence:
    section_id:
    event_type:
    occurred_at:
    actor:
      runtime_role: orchestrator
      persona_id:
      execution_id:
    causation:
      dispatch_revision:
      previous_event_id:
    previous:
      lifecycle_phase:
      runtime_state:
      next_action:
        code:
        detail:
    next:
      lifecycle_phase:
      runtime_state:
      next_action:
        code:
        detail:
    artifact_refs: []
    evidence_refs: []
    guard_results: []
    rationale:
```

Lifecycle record rules:

- canonical `runtime_state` remains only in the section runtime ledger and must not be duplicated inside `lifecycle`
- only the orchestrator may append an accepted lifecycle event or change `lifecycle_phase`
- the event `previous` projection must match the current lifecycle phase, canonical runtime state, and next action before its `next` projection is persisted
- `next_action.code` is derived from the canonical phase/state table in `references/task-runtime-lifecycle.md`
- the null event head is valid only for the exact `plan/queued` genesis state
- `phase_entered_at` changes only when an accepted event changes phase
- a round lifecycle rollup, when present, is derived and never writable authority

### Section Verification Lanes: {{section_name}} (`task-runtime-v1` only)

Render this block only when the approved round protocol is `task-runtime-v1`.
Omit the entire block for `legacy` rounds. These records follow
`references/task-runtime-verification.md`.

```yaml
worker_lanes: []
verifier_lanes:
  - lane_id:
    lane_type: test-verification | artifact-verification | deployment-verification | configuration-verification
    runtime_role: verifier
    required: true
    selection:
      sources: []
      task_profile_ids: []
      risk_trigger_ids: []
      rationale:
      exclusion_ref:
    target_selector:
      artifact_ids: []
      path_globs: []
      environment_ids: []
    verification_target_ref:
      target_id:
      target_kind: single | aggregate
      artifact_path:
      artifact_kind:
      artifact_revision:
      schema_version:
      section_anchor:
      content_hash:
      target_set_members: []
      target_set_hash:
    verification_commands: []
    evidence_requirements: []
    freshness_policy:
      target_bound: true
      environment_bound: false
      max_age_seconds:
      environment_change_token_id:
    model_capability_profile:
    model_capability_profile_schema_version: 1
    model_capability_profile_hash:
    minimum_capability_floor:
    minimum_capability_floor_schema_version: 1
    minimum_capability_floor_hash:
    selected_verifier:
      persona_id:
      persona_source:
      selection_rationale:
    active_execution_id:
    active_attempt_id:
    attempt_history: []
    accepted_outcome_ref:
reviewer_lanes: []
evidence_bundles: []
evidence_applicability_records: []
model_resolutions: []
```

Verification lane rules:

- verifier lane records do not own `runtime_state` or `lifecycle_phase`
- baseline and risk-triggered lane selection must record durable source and rationale
- every verifier lane must resolve to one frozen `verification_target_ref` before packet creation
- required lanes pass only through current accepted `PASS` evidence for the exact frozen target
- stale, wrong-target, identity-conflicted, superseded, skipped, failed, blocked, or below-floor evidence cannot authorize verification acceptance
- model capability profile, minimum floor, and model resolution are separate from persona identity and concrete model labels
- `runtime_role: verifier` requires a later approved verifier binding before any packet can be launched

### Section Missing Capability Records: {{section_name}} (`task-runtime-v1` only)

Render this block only when the approved round protocol is `task-runtime-v1`.
Omit the entire block for `legacy` rounds. These records follow
`references/task-runtime-missing-capabilities.md`.

```yaml
internal_hook_records: []
quality_gate_records: []
score_records: []
repair_records: []
review_synthesis_records: []
reverification_requirements: []
close_gate_records: []
final_judgment_records: []
recovery_requirement_records: []
checkpoint_records: []
```

Missing capability record rules:

- these records are section-scoped guard, gate, recovery, or decision records; they do not own `runtime_state`, `lifecycle_phase`, `plan_state`, or `section_state`
- internal hooks are invocation-scoped WorkWork guard points, not operating-system hooks, git hooks, background daemons, scheduled tasks, or passive listeners
- quality gates and score records summarize accepted evidence but cannot override non-waivable hard blockers
- repair records require explicit authorization and a stable pre-repair target; repaired targets require fresh re-verification before returning to review, score, or close
- review synthesis records must reject stale reviewer targets as coverage for the current target lineage
- close gates package verification, review, repair, score, blocker, and waiver state before final judgment; they recommend close but do not approve it
- final judgment records must preserve the user decision and cannot relabel missing, stale, wrong-target, below-floor, or failed verifier evidence as valid PASS evidence
- recovery requirements and checkpoints are resume aids; they must not override lifecycle snapshots or event history
- legacy rounds must omit this entire authority block

## Section Review Record

### Section: {{section_name}}

- Section ID: {{section_id}}
- Review Target Strategy:
- Review Lane Records:
  - Lane ID:
  - Lane Type:
  - Reviewer Persona:
  - Reviewer Source:
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale:
  - Execution ID:
  - Packet ID:
  - Attempt ID:
  - Review Target Ref:
    - Artifact Path:
    - Artifact Kind:
    - Artifact Revision:
    - Schema Version:
    - Section Anchor:
    - Content Hash:
  - Reviewer Findings:
  - Orchestrator Synthesis:
  - Strict Review Outcome: none | passed | blocked
  - Persistence rule: pre-approval plans must preserve this review-lane structure and outcome field pattern; `Review Status` must not reappear here, and durable review-lane data must retain `Reviewer Findings`, `Orchestrator Synthesis`, and the `Strict Review Outcome` field pattern.
  - Applicability rule: `Strict Review Outcome` is required when a strict-review target or durable strict-review result applies; otherwise keep the same field pattern without creating a second schema for valid non-strict lanes.
  - Invalid state note: `Review Status` reappears or durable strict-review outcome data is dropped when applicable.
- Human Decision: none
- Revision Notes:
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level `plan_state` is derived from `required_for_goal`

## Ordering And Parallelism

- Blocking work first: {{blocking_order}}
- Parallel sections: {{parallel_sections}}
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
- Current Choice: none
- Approved By:
- Approval Time:
- Notes:
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: {{brief_version}}
- Revision Reason:
- Supersedes Revision:

## Dispatch Log

- Agents Launched:
- Retry Events:
- Close Events:
- Review Lane Transitions:
- Launch Time:
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
