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
- Review Status: not-started
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
  - Review Status:
  - Reviewer Findings:
  - Orchestrator Synthesis:
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

- Required Human Choice:
  - `1. Approve`
  - `2. Revise`
  - `3. Stop`
- Accepted Aliases: `Approve` | `Revise` | `Stop`
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
