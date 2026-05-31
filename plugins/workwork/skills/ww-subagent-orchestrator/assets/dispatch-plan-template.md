# Dispatch Plan: {{topic}}

- Date: {{date}}
- Schema Version: 1
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
