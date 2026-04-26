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
  - `working_brief_ready: true`
  - `dispatch_decision: approved`
- Bind a Superpowers workflow at every stage and inside every subagent packet.
- Every section must have a reviewer subagent, then orchestrator synthesis, then human judgment.
- Reviewer subagents point out problems only. They do not rewrite the draft or make the final decision.

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

The working brief is the only valid basis for:

- orchestrator choice
- persona selection
- workflow bindings
- dispatch recommendation

Do not dispatch from a rough idea or a quick summary.

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

The dispatch plan must:

- record the active gate state
- list proposed subagents and rationales
- encode per-section review loops
- expose one approval state aligned to `Approve / Revise / Stop`
- record whether real dispatch has started

If the user chooses `Stop`, preserve the working brief and the dispatch plan file, and do not dispatch any new subagents.

If the user chooses `Revise`, return to orchestrator editing, update the working brief and dispatch plan, keep `Real Dispatch Started: false`, and request `Approve / Revise / Stop` again before any launch.

## Review Loop

For each section:

1. Orchestrator drafts the section
2. Reviewer subagent returns findings only
3. Orchestrator outputs:
   - `section draft`
   - `reviewer findings`
   - `recommendation`
4. Human chooses `Approve`, `Revise`, or `Stop`

Never skip the orchestrator synthesis step.

## Approval Lifecycle

Use one approval path throughout the run:

- `pending` while the plan is under review
- `approved` after `Approve`
- `revise-requested` after `Revise`
- `stopped` after `Stop`

`approved` is the only state that allows packet creation or real dispatch.

## References

- `references/working-brief-template.md`
- `references/persona-registry.md`
- `references/subagent-packet-contract.md`
- `assets/dispatch-plan-template.md`
