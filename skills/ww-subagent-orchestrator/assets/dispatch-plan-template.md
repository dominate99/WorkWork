# Dispatch Plan: {{topic}}

- Date: {{date}}
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
- Draft Author Role: {{draft_author}}
- Planned Reviewer Persona: {{reviewer_persona}}
- Planned Specialist Personas: {{specialist_personas}}
- Planned Scope: {{owned_scope}}
- Planning Rationale: {{persona_rationale}}
- Planned Workflow Bindings: {{workflow_bindings}}
- Packet Created: false

## Section Review Record

### Section: {{section_name}}

- Section ID: {{section_id}}
- Review Status: not-started
- Reviewer Findings:
- Orchestrator Synthesis:
- Human Decision: none
- Revision Notes:
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped` and plan state becomes `stopped`

## Ordering And Parallelism

- Blocking work first: {{blocking_order}}
- Parallel sections: {{parallel_sections}}
- Review loop per section: draft -> reviewer findings -> orchestrator synthesis -> human judgment

## Progress Board

> The `Progress Board` is the canonical store for rendered-progress inputs. The reply must not invent values that are absent from this section.
>
> Allowed `Display Status` values: `not started`, `queued`, `running`, `waiting on orchestrator`, `waiting on user`, `blocked`, `completed`, `failed`.
>
> `Display Status` precedence, highest to lowest: `failed`, `completed`, `blocked`, `waiting on user`, `waiting on orchestrator`, `running`, `queued`, `not started`.
>
> Mark the single workstream used for `Status Summary` with `Critical Path: yes`. All other workstreams must use `Critical Path: no`.

### Workstream: {{workstream_label}}

- Workstream ID: {{workstream_id}}
- Source Section ID: {{source_section_id}}
- Source Plan Revision: {{source_plan_revision}}
- Workstream Type: {{workstream_type}}
- Critical Path: {{yes_or_no}}
- Scope: {{scope}}
- Owner: {{owner}}
- Internal State Reference: {{internal_state_reference}}
- Display Status: {{display_status}}
- Last Update: {{last_update}}
- Blocker: {{blocker}}
- Next Handoff: {{next_handoff}}
- Review Pass ID: {{review_pass_id_or_none}}

## Approval Block

- Required Human Choice: `Approve` | `Revise` | `Stop`
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
- Launch Time:
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
