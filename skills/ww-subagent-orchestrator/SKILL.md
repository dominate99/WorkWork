---
name: ww-subagent-orchestrator
description: Use when a task should start with `$ww` to estimate work, choose an orchestrator persona, build a working brief, create a tracked dispatch plan file, and coordinate persona-bound subagents with Superpowers workflows across coding, product, or creative work.
---

# WW Subagent Orchestrator

## Overview

Use this skill to turn `$ww` into a disciplined orchestration flow instead of ad hoc subagent dispatch. The skill estimates first, writes a working brief, chooses the correct top-level orchestrator persona, writes a tracked dispatch plan file, and only then allows real subagent work.

## Core Rules

- Treat `$ww` as an estimation trigger, not a dispatch command.
- Choose the top-level orchestrator from task context:
  - `code/programming` -> `staff engineer orchestrator`
  - `design/ads/product` -> `PM orchestrator`
  - `video/creative` -> `creative director orchestrator`
- Do not assign personas from keywords alone. Derive them from the working brief.
- Do not create any subagent packet until all three gates are true:
  - `estimation_complete: true`
  - `brief_status: ready`
  - dispatch plan `plan_state: approved`
- Bind a Superpowers workflow at every stage and inside every subagent packet.
- Every `$ww` reply must follow the `User-Facing Reply Contract`.
- If any of those documents do not exist yet, say `not created yet` in the summary instead of omitting the item.
- Every section must have a reviewer subagent, then orchestrator synthesis, then human judgment.
- Reviewer subagents point out problems only. They do not rewrite the draft or make the final decision.
- Reviewer subagents must stay narrow and convergent: only inspect the assigned artifact against its stated scope, list the highest-signal issues, and stop.

## Required Stage Order

Follow this sequence every time:

1. Estimate the task
2. Build the working brief
3. Route to the correct orchestrator
4. Write the dispatch plan file
5. Ask for `Approve / Revise / Stop`
6. Launch subagents only after `Approve`
7. Run section review loops
8. Synthesize results and close with verification

## Stage Bindings

- Estimation and framing: `superpowers:brainstorming`
- Planning: `superpowers:writing-plans`
- Independent workstreams: `superpowers:dispatching-parallel-agents`
- Implementation execution: `superpowers:subagent-driven-development`
- Code changes: `superpowers:test-driven-development`
- Debugging: `superpowers:systematic-debugging`
- Review: `superpowers:requesting-code-review`
- Closure: `superpowers:verification-before-completion`

## Working Brief

Use the template in `references/working-brief-template.md`.

The working brief is the analysis snapshot for one dispatch round. It is the only valid basis for:

- orchestrator choice
- persona selection
- workflow bindings
- dispatch recommendation

Its job is to capture context and recommendations, not runtime approval state. Do not dispatch from a rough idea or a quick summary.

## Persona Planning

Check for project personas first at `docs/superpowers/personas/registry.yaml`. If that file does not exist or does not cover the need, fall back to built-in personas and rules from `references/persona-registry.md`.

For every chosen persona, write:

- the persona name
- the owned scope
- the reason it was selected from the working brief
- the workflow bindings for its current stage

Keep reviewers and implementers separate.

If a task spans multiple categories, choose the top-level orchestrator by the primary artifact being produced and the highest-risk decision area. Keep cross-category concerns as specialist personas instead of switching orchestrators mid-run.

## Subagent Packet Contract

Use the contract in `references/subagent-packet-contract.md`.

Packets are execution artifacts, not planning artifacts. Create them only from an approved dispatch plan section.

Required packet fields:

- `orchestrator_type`
- `stage`
- `subagent_persona`
- `persona_rationale`
- `derived_from_working_brief`
- `task_mode`
- `workflow_bindings[]`
- `working_brief_excerpt`
- `owned_scope`
- `non_goals`
- `success_criteria`
- `output_contract`
- `handoff_rule`
- `requires_human_judgment`

## Dispatch Plan File

Before real dispatch, write a tracked Markdown file using `assets/dispatch-plan-template.md` to:

`docs/superpowers/dispatch-plans/YYYY-MM-DD-topic.md`

The dispatch plan is the canonical runtime state for the dispatch round. The dispatch plan must:

- reference the working brief version it was derived from
- record the active approval state
- list planned sections and planned personas
- encode per-section review loops
- expose one canonical plan state
- let `plan_state` represent whether dispatch has started

If the user chooses `Stop`, preserve the working brief and the dispatch plan file, and do not dispatch any new subagents.

If the user chooses `Revise`, return to orchestrator editing, keep the last approved revision as the rollback baseline, increment the plan revision, and request `Approve / Revise / Stop` again before any launch.

## User-Facing Reply Contract

Every `$ww` reply must use these four sections in this order:

1. `Status Summary`
2. `Subagent Progress`
3. `Decision Block`
4. `Document Summary`

The dispatch plan is the canonical runtime state source. Update the dispatch plan first, then render the chat reply from the updated persisted state in the same turn.

### Status Summary

- Always include:
  - `current stage`
  - `primary owner`
  - `waiting on`
  - `next action`
  - `user decision needed`
- Derive all five fields from the critical-path workstream recorded in the dispatch plan.

### Subagent Progress

- Always include the section, even when no subagents are active.
- If no subagents have launched, output `no subagents launched`.
- Otherwise render each workstream from the dispatch plan `Progress Board`.

### Decision Block

- Always include the section.
- If `user decision needed` is `yes`, enumerate the available choice set.
- If `user decision needed` is `no`, output `No decision required right now`.

### Document Summary

- Always include:
  - `working brief`
  - `dispatch plan`
  - `design spec`
  - `implementation plan`
- Use `not created yet` for missing documents.

Default document references:

- `working brief`: current brief artifact for the dispatch round; if no saved file exists yet, report the current brief state and say file is `not created yet`
- `dispatch plan`: `docs/superpowers/dispatch-plans/YYYY-MM-DD-topic.md`
- `design spec`: `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`
- `implementation plan`: `docs/superpowers/plans/YYYY-MM-DD-<feature-name>.md`

Missing-document rule:

- If a document has not been created yet, write `not created yet`
- Do not replace that phrase with softer wording such as `pending`, `later`, or `to be created`

Preferred format:

```markdown
## Document Summary

- `working brief`: ready, version 2, file `not created yet`
- `dispatch plan`: awaiting-approval, `docs/superpowers/dispatch-plans/2026-04-27-topic.md`
- `design spec`: not created yet
- `implementation plan`: not created yet
```

## Runtime Rendering Rules

- `current stage`, `waiting on`, and `next action` must all derive from the same critical-path workstream.
- `waiting on` precedence:
  - human choice
  - orchestrator synthesis or routing
  - blocker owner or unresolved dependency
  - active workstream owner
  - queue gate
  - `nobody`
- `Decision Block` must derive from the same dispatch-plan state as `user decision needed`.
- Do not emit a rendered state that is more advanced than the persisted dispatch plan.

## Reviewer Convergence Rules

Reviewer subagents exist to reduce decision noise, not to expand the work. Make reviewers strict, narrow, and easy to synthesize.

Reviewer requirements:

- Review only the assigned artifact or section, not the whole project
- Compare against the declared scope, stated goals, and current stage requirements
- Return findings only; no rewrites, no speculative redesign, no new scope creation
- Report at most `5` findings, ordered by severity
- Prefer blockers, contradictions, missing requirements, unsafe assumptions, and likely regressions
- If there are no material findings, explicitly say `no material findings`
- Keep findings short enough that the orchestrator can synthesize them inline without a second condensation pass

Reviewer anti-patterns:

- brainstorming new features
- proposing alternate architectures when the current one is in-scope and viable
- rewriting the draft
- adding implementation details that belong to a later stage
- widening the review surface beyond the assigned artifact
- returning verbose review essays

Preferred reviewer output shape:

```markdown
## Reviewer Findings

- Severity: high | Scope: requirement mismatch | Finding: ...
- Severity: medium | Scope: missing edge case | Finding: ...
```

## Review Loop

For each section:

1. Orchestrator drafts the section
2. Reviewer subagent returns a narrow findings-only review under the convergence rules
3. Orchestrator outputs:
   - `section draft`
   - `reviewer findings`
   - `recommendation`
4. Human chooses `Approve`, `Revise`, or `Stop`

Never skip the orchestrator synthesis step.

## Approval Lifecycle

Use one global plan state throughout the run:

- `draft`
- `awaiting-approval`
- `approved`
- `revising`
- `stopped`
- `dispatched`
- `completed`

`approved` is the only state that allows packet creation or real dispatch.

Use a separate section state for each section review:

- `drafted`
- `under-review`
- `accepted`
- `revision-requested`
- `stopped`

Do not reuse section decisions as the global plan state.

## Rollback Rules

On `Revise`:

- freeze real dispatch for the affected plan revision
- preserve the last approved revision as the rollback baseline
- update the working brief if the analysis changed
- regenerate the dispatch plan against the new working brief version
- re-request approval before creating any packet for the new revision

If a section enters `revision-requested`, the global plan state returns to `revising` until a revised plan is approved again.

## References

- `references/working-brief-template.md`
- `references/persona-registry.md`
- `references/subagent-packet-contract.md`
- `assets/dispatch-plan-template.md`
