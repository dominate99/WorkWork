# Dispatch Plan: {{topic}}

- Date: {{date}}
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: {{brief_version}}
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

- `strict_review` is a target-specific gate record owned by the dispatch plan for `$www`.
- `strict_review.target`, `state`, and `cycle_count` apply to the active strict-review target only.
- When a new target is allowed to start, initialize the live gate record for that target with `target`, `state: idle`, and `cycle_count: 0`, then enter `self-review` through `STRICT_TARGET_STARTED`.
- A blocked target may not be overwritten by switching `strict_review.target` in the same round; it must follow the existing human `Revise` path into a new approved round or revision.
- `strict_review` does not replace section-level `runtime_state`; `runtime_state` remains the single authoritative post-launch section state.
- `strict_review.target` is only the strict-review target-kind discriminator: `none` | `design-spec` | `implementation-plan`.
- Concrete artifact identity and artifact revision continue to come from persisted artifact paths and reviewer `review target` references elsewhere in the controller model.
- Durable per-target strict-review outcomes remain in `Review Lane Records` keyed by `Review Target Ref`, so switching the live gate record to a later target does not erase whether an earlier target revision already passed or blocked.

## Preconditions

- Estimation Complete: {{true_or_false}}
- Working Brief Status: ready|draft

> Do not launch any real subagent until the preconditions are satisfied and `Plan State: approved`.

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
- Planned Specialist Personas: {{specialist_personas}}
- Planned Scope: {{owned_scope}}
- Planning Rationale: {{persona_rationale}}
- Planned Workflow Bindings: {{workflow_bindings}}
- Planned Review Lanes:
  - Lane ID:
  - Lane Type: spec-review | code-quality-review | scope-review | editorial-review | other
  - Reviewer Persona:
  - Required: true|false
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
- Packet Created: false

## Section Runtime Ledger

### Section: {{section_name}}

- Section ID: {{section_id}}
- Runtime State: queued
- Active Execution ID:
- Active Packet ID:
- Active Agent ID:
- Active Attempt ID:
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
