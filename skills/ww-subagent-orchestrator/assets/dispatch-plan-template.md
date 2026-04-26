# Dispatch Plan: {{topic}}

- Date: {{date}}
- Plan Status: awaiting-review
- Human Approval Choice: pending
- Task Routing: {{task_routing}}
- Main Orchestrator: {{main_orchestrator}}
- Real Dispatch Started: false

## Gate Checks

- Estimation Complete: {{true_or_false}}
- Working Brief Ready: {{true_or_false}}
- Dispatch Decision Approved: {{true_or_false}}

> Do not launch any real subagent until all three gate checks are `true` and the human approval choice is `Approve`.

## Source Context

- User Request: {{user_request}}
- Working Brief Reference: {{working_brief_reference}}

## Dispatch Summary

- Goal: {{goal}}
- Relevant Context: {{relevant_context}}
- Constraints: {{constraints}}
- Risks: {{risks}}
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Proposed Subagents

### Section: {{section_name}}

- Draft Author: {{draft_author}}
- Reviewer Persona: {{reviewer_persona}}
- Specialist Personas: {{specialist_personas}}
- Stage: {{stage}}
- Owned Scope: {{owned_scope}}
- Persona Rationale: {{persona_rationale}}
- Workflow Bindings: {{workflow_bindings}}
- Success Criteria: {{success_criteria}}
- Non Goals: {{non_goals}}
- Handoff Rule: return to orchestrator, then human judgment required
- Human Judgment Required: true

## Section Review Record

### Section: {{section_name}}

- Section Status: pending
- Reviewer Findings:
- Orchestrator Synthesis:
- Human Decision: pending
- Revision Notes:

## Ordering And Parallelism

- Blocking work first: {{blocking_order}}
- Parallel sections: {{parallel_sections}}
- Review loop per section: draft -> reviewer findings -> orchestrator synthesis -> human judgment

## Approval Block

- Required Human Choice: `Approve` | `Revise` | `Stop`
- Current Choice: pending
- Approved By:
- Approval Time:
- Notes:

## Dispatch Log

- Dispatch Round State: not-started
- Agents Launched:
- Launch Time:
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
