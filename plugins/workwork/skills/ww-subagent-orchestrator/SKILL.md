---
name: ww-subagent-orchestrator
description: Use when a task should start with `$ww` to estimate work, choose an orchestrator persona, build a persisted working brief, create a tracked dispatch plan file, and coordinate persona-bound subagents with Superpowers workflows across coding, product, or creative work.
---

# WW Subagent Orchestrator

## Overview

Use this skill to turn `$ww` into a disciplined orchestration flow instead of ad hoc subagent dispatch. The skill estimates first, writes a persisted working brief, chooses the correct top-level orchestrator persona, writes a tracked dispatch plan file, and only then allows real subagent work.

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
- Persist the working brief before dispatch-plan creation. Runtime schema checks do not operate on chat-only summaries.
- Bind a Superpowers workflow at every stage and inside every subagent packet.
- Every `$ww` reply must end with a `Document Summary` block covering `working brief`, `dispatch plan`, `design spec`, and `implementation plan`.
- If any of those documents do not exist yet, say `not created yet` in the summary instead of omitting the item.
- Every section must have reviewer coverage, orchestrator synthesis, and human judgment.
- Reviewer subagents point out problems only. They do not rewrite the draft or make the final decision.
- Reviewer subagents must stay narrow and convergent: only inspect the assigned artifact against its stated scope, list the highest-signal issues, and stop.
- `runtime_state` is the single authoritative post-launch section state. `close_state` is derived from it and must never act as a parallel state machine.
- `failed` and `stopped` are distinct. User stop must not be conflated with execution failure.

## Required Stage Order

Follow this sequence every time:

1. Estimate the task
2. Build the working brief
3. Persist the working brief
4. Route to the correct orchestrator
5. Write the dispatch plan file
6. Render this approval block:
   1. `Approve`
   2. `Revise`
   3. `Stop`
7. Launch subagents only after `Approve`
8. Run section review loops
9. Synthesize results and close with verification

This numbered list is the required rendered approval prompt. Numeric replies map to the same decisions: `1` -> `Approve`, `2` -> `Revise`, `3` -> `Stop`. The words `Approve`, `Revise`, and `Stop` remain accepted aliases for the same decisions.

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
- scope preparation when packets or reviewers will reference artifacts

Its job is to capture context and recommendations, not runtime approval state. Do not dispatch from a rough idea or a quick summary.

Working brief persistence rules:

- a brief may temporarily exist in chat during raw estimation
- before dispatch-plan creation, the brief must be saved to `docs/superpowers/working-briefs/YYYY-MM-DD-topic-vN.md`
- schema checks, revision comparisons, and reviewer targeting must use the persisted brief artifact

Schema compatibility rules:

- pre-versioned artifacts are treated as `schema_version: 0`
- normalize persisted artifacts on load before planning or launch decisions
- write only the current schema version back to disk
- reject mixed in-memory schema versions within one dispatch round
- `runtime_status` is deprecated terminology and must not be reintroduced as a persisted field

Cross-artifact compatibility rules:

- working brief, dispatch plan, and subagent packet schemas must be compatible within one dispatch round after load-time normalization
- if a persisted working brief or dispatch plan cannot be normalized to the current schema version, halt launch and request revision instead of dispatching with a mixed schema set
- packet creation may only reference fields that exist in the normalized persisted working brief and dispatch plan
- if registry fallback is used, the target must resolve to a persisted `artifact_path` plus optional `section_anchor` before it can be treated as parallel-safe or review-target-eligible

State crosswalk:

| Layer | Owner | Canonical values | Notes |
|---|---|---|---|
| `plan_state` | dispatch round | `draft`, `awaiting-approval`, `approved`, `revising`, `dispatched`, `completed`, `stopped` | top-level rollup only; `blocked` is represented by section/runtime state, not plan state |
| `section_state` | dispatch section | `drafted`, `accepted`, `revision-requested`, `stopped` | derived from section review and controller outcomes |
| `runtime_state` | section runtime | `queued`, `running`, `review-pending`, `blocked`, `complete`, `failed`, `stopped` | single authoritative post-launch section state |
| `return_status` | subagent output | `DONE`, `DONE_WITH_CONCERNS`, `NEEDS_CONTEXT`, `BLOCKED`, `FAILED` | mapped through the transition table; stale returns do not advance state |

## Persona Planning

Check for project personas first at `docs/superpowers/personas/registry.yaml`. If that file does not exist or does not cover the need, fall back to built-in personas and rules from `references/persona-registry.md`.

For every chosen persona, write:

- the persona name
- the owned scope
- the reason it was selected from the working brief
- the workflow bindings for its current stage
- the `agents/openai.yaml` role binding used for prompt assembly
- the role prompt asset used for launch assembly:
  - `agents/orchestrator-prompt.md`
  - `agents/worker-prompt.md`
  - `agents/reviewer-prompt.md`
  - `agents/explorer-prompt.md`

Keep reviewers and implementers separate.

If a task spans multiple categories, choose the top-level orchestrator by the primary artifact being produced and the highest-risk decision area. Keep cross-category concerns as specialist personas instead of switching orchestrators mid-run.

## Artifact Resolution

When sections or reviewers reference `artifact_id`, resolve it in this order:

1. `docs/superpowers/artifact-registry.yaml`
2. inline artifact mapping in the working brief
3. inline artifact mapping in the dispatch plan

Rules:

- one `artifact_id` maps to exactly one canonical `artifact_path`
- aggregate multi-file work must use multiple `artifact_id` values, explicit `path_glob` scopes, or multiple sections
- if an artifact cannot be resolved into canonical targets, that section is not parallel-safe and may not be used as a reviewer target

## Subagent Packet Contract

Use the contract in `references/subagent-packet-contract.md`.

Packets are execution artifacts, not planning artifacts. Create them only from an approved dispatch plan section.

Every packet must encode:

- source dispatch metadata
- execution identity
- execution binding
- owned read/write scope
- success and handoff rules
- immutable reviewer target data when review is involved

Create reviewer packets only after the reviewed artifact snapshot is stable enough to generate `review_target_ref`.

## Dispatch Plan File

Before real dispatch, write a tracked Markdown file using `assets/dispatch-plan-template.md` to:

`docs/superpowers/dispatch-plans/YYYY-MM-DD-topic.md`

The dispatch plan is the canonical runtime state for the dispatch round. The dispatch plan must:

- reference the persisted working brief version it was derived from
- record the active approval state
- list planned sections and planned personas
- encode per-section review loops
- expose one canonical `plan_state`
- track per-section `runtime_state`
- keep active execution pointers plus execution history
- record `required_for_goal` so top-level aggregation can distinguish `failed` from `stopped`

If the user chooses `Stop`, preserve the working brief and the dispatch plan file, and do not dispatch any new subagents.

Approval semantics:

- `Approve` allows the next approved stage to proceed.
- `Revise` returns to orchestrator editing and requires approval again before launch.
- `Stop` preserves the working brief and dispatch plan and prevents new dispatch.

## Review Pipeline

Review depth depends on route type.

For `code/programming`:

1. implementer
2. spec reviewer
3. code quality reviewer
4. orchestrator synthesis
5. human judgment

For `design/ads/product`:

1. drafter
2. scope reviewer
3. orchestrator synthesis
4. human judgment

For `video/creative`:

1. creator
2. editorial reviewer
3. orchestrator synthesis
4. human judgment

For spec-light code tasks, reviewer target precedence is:

1. implementation plan if present
2. dispatch section contract
3. working brief excerpt

## Controller Update Procedure

The orchestrator must follow one deterministic runtime procedure.

On launch:

1. load and normalize persisted working brief and dispatch plan artifacts
2. verify schema compatibility and approval state
3. resolve scope declarations into canonical targets
4. build packet with `execution_id`, `packet_id`, `attempt_id`, and `review_target_ref` when applicable
5. assemble the final prompt payload from persona binding, runtime template, packet fields, and workflow bindings
6. persist `runtime_state: running` and active execution pointers

On subagent return:

1. verify that the result belongs to `active_attempt_id` or is explicitly allowed as a late result
2. apply the `return_status -> runtime_state` transition table
3. persist canonical `runtime_state`
4. persist summary, concerns, or blocker reason
5. derive `close_state`, section rollups, and top-level `plan_state`

Only the active attempt may advance canonical state. A return from any non-active attempt is stale unless `accepts_late_results: true` explicitly allows it to be recorded as history without changing the canonical `runtime_state`. Late results may be appended to attempt history, but they must not replace the active attempt pointer or advance the section state.

On reviewer return:

1. verify immutable `review_target_ref`
2. record findings against the reviewed artifact revision
3. apply the reviewer transition rules
4. queue synthesis or revision follow-up

On orchestrator synthesis:

1. summarize implementer or reviewer output
2. persist the synthesis note into the dispatch plan review record
3. keep `runtime_state: review-pending` while human judgment is still required
4. otherwise advance by the transition rule for the current lane

On human `Approve`, `Revise`, or `Stop`:

1. record decision and timestamp
2. apply the transition rule
3. preserve or rotate `execution_id` according to whether the logical work item changed

On retry:

1. confirm that the current state is retry-eligible
2. preserve or rotate identity layers according to controller semantics
3. create a new `attempt_id`
4. re-assemble the prompt payload with updated context
5. persist `runtime_state: running` plus the new active attempt pointer

On close:

1. confirm terminal `runtime_state` and no next action
2. set derived `close_state: closed`
3. record closure timestamp and final references

## Runtime Transition Table

Use this canonical controller transition table.

| Event Type | Input Event | Current `runtime_state` | Next canonical `runtime_state` | Required follow-up |
|---|---|---|---|---|
| subagent return | `DONE` | `running` | `review-pending` or `complete` | send to next required reviewer, or mark complete if no further review applies |
| subagent return | `DONE_WITH_CONCERNS` | `running` | `review-pending` | persist concerns and require orchestrator synthesis before proceeding |
| subagent return | `NEEDS_CONTEXT` | `running` | `blocked` | record missing context, keep `execution_id`, rotate `attempt_id` only on re-launch |
| subagent return | `BLOCKED` | `running` | `blocked` | classify blocker and choose retry, revise, or human escalation |
| subagent return | `FAILED` | `running` | `failed` | close current attempt and require explicit recovery decision before new launch |
| reviewer outcome | `PASS` | `review-pending` | `review-pending` or `complete` | advance to next reviewer or synthesis, then complete if review lane is finished |
| reviewer outcome | `REJECT` | `review-pending` | `blocked` | persist findings, require orchestrator synthesis, and relaunch only through explicit retry or revise path |
| orchestrator event | `SYNTHESIS_COMPLETE` | `review-pending` | `review-pending` or `complete` | wait for human decision when required, otherwise close completed lane |
| human decision | `APPROVE` | `review-pending` | `complete` | persist decision and close when no next action remains |
| human decision | `REVISE` | `review-pending` or `blocked` | `blocked` | create revision task and preserve `execution_id` only if the logical work item is unchanged |
| human decision | `STOP` | `running`, `review-pending`, or `blocked` | `stopped` | record explicit user stop, close active work, and prevent relaunch unless planning is explicitly reopened |
| controller action | `RETRY` | `blocked` or `failed` | `running` | create a new `attempt_id`, preserve or rotate higher identities per controller semantics |

## Document Summary Contract

At the end of every `$ww` response, output a short `Document Summary` section. This is mandatory during estimation, approval, revision, dispatch, review, and closure updates.

Always include exactly these four entries:

- `working brief`
- `dispatch plan`
- `design spec`
- `implementation plan`

Each entry should briefly report the current state and, when known, the active file path or version. Never omit an entry because the document has not been started.

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

- `working brief`: ready, version 2, `docs/superpowers/working-briefs/2026-04-27-topic-v2.md`
- `dispatch plan`: awaiting-approval, `docs/superpowers/dispatch-plans/2026-04-27-topic.md`
- `design spec`: not created yet
- `implementation plan`: not created yet
```

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

## Approval Lifecycle

Use this authoritative state crosswalk:

| State Surface | Purpose | Allowed Values | Authority Rule |
|---|---|---|---|
| `plan_state` | round-level summary | `draft`, `awaiting-approval`, `approved`, `revising`, `stopped`, `dispatched`, `completed` | derived from section outcomes and required-section criticality |
| `section_state` | human workflow tracking | `drafted`, `under-review`, `accepted`, `revision-requested`, `stopped` | records human review posture, not execution truth |
| `runtime_state` | canonical execution state | `queued`, `running`, `blocked`, `review-pending`, `complete`, `failed`, `stopped` | single authoritative post-launch section state |
| `return_status` | subagent event input | `DONE`, `DONE_WITH_CONCERNS`, `NEEDS_CONTEXT`, `BLOCKED`, `FAILED`, `PASS`, `REJECT` | event input only; never persisted as the canonical long-lived state |

Use one global plan state throughout the run:

- `draft`
- `awaiting-approval`
- `approved`
- `revising`
- `stopped`
- `dispatched`
- `completed`

`approved` is the only state that allows packet creation or real dispatch.

Use a separate section state for human workflow tracking:

- `drafted`
- `under-review`
- `accepted`
- `revision-requested`
- `stopped`

Use canonical per-section runtime states for execution tracking:

- `queued`
- `running`
- `blocked`
- `review-pending`
- `complete`
- `failed`
- `stopped`

Do not reuse section decisions as the global plan state.

Top-level aggregation rules:

- if any `required_for_goal: true` section enters `stopped`, top-level `plan_state` becomes `stopped`
- if a non-required section enters `stopped` while required sections remain active, top-level `plan_state` remains `dispatched`
- if all required sections are `complete` and only non-required sections are `stopped`, top-level `plan_state` becomes `completed`
- if any section is `running` or `review-pending`, top-level `plan_state` must not become `completed`

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
