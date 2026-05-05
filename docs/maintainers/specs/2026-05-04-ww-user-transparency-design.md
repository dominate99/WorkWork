# WW User Transparency And Subagent Progress Design

**Date:** 2026-05-04

## Goal

Upgrade the `ww-subagent-orchestrator` skill so every `$ww` interaction makes the system state, the user decision state, and any subagent progress visible without forcing the user to inspect internal planning artifacts.

## Problem

The current skill is disciplined but operationally opaque. It tells the system what to produce, but not enough about what the user should understand at a glance.

Current gaps:

- the reply format emphasizes document existence more than runtime state
- the user cannot reliably tell what stage is active
- the user cannot reliably tell whether the system is waiting on the user or waiting on a subagent
- subagent progress is mostly hidden until a handoff completes
- internal lifecycle states are not translated into user-facing language

This reduces trust, increases cognitive load, and makes waits feel like dead time rather than active progress.

## Product Principles

1. Lead with state, not paperwork.
2. Show only the status the user can act on.
3. Translate internal workflow language into natural user language.
4. Make waiting states explicit.
5. Expose progress without turning the reply into a raw log stream.

## Scope

This redesign covers:

- the fixed reply contract for every `$ww` response
- the user-facing state model
- the subagent progress model
- the decision prompt model
- the mapping between internal workflow state and displayed language
- the minimum dispatch-plan fields needed to support visible progress

This redesign does not cover:

- new domain-specific personas
- implementation of live timers or telemetry
- a GUI dashboard outside the chat reply
- changes to the core approval lifecycle

## Recommended Interaction Model

Every `$ww` response should use four ordered sections:

1. `Status Summary`
2. `Subagent Progress`
3. `Decision Block`
4. `Document Summary`

This order is mandatory. The current `Document Summary` remains useful, but it should stop acting as the primary status surface.

The chat reply is a rendered view, not the canonical runtime store. The canonical runtime source remains the persisted orchestration artifacts:

- the dispatch plan is the canonical runtime state source
- the working brief is the canonical routing and analysis source
- the chat reply renders a concise view derived from those sources for the current turn

Render-order rule:

1. update the dispatch plan first
2. derive the rendered reply from the updated persisted state in the same turn
3. emit the reply only after the persisted state reflects the content being shown

If persistence fails, do not present a more advanced rendered state than the dispatch plan currently records.

## Section 1: Status Summary

`Status Summary` is the new top-level interface. It answers the user's first questions before anything else.

Required fields:

- `current stage`
- `primary owner`
- `waiting on`
- `next action`
- `user decision needed`

Rules:

- use natural language, not raw internal state names
- if the system is blocked, say what the blocker is
- if the system is waiting on the user, say exactly what decision is needed
- if the system is waiting on internal work, say who owns the next move
- when multiple workstreams are active, `primary owner` means the owner of the critical-path next move, not every active worker
- if ownership is split across parallel workstreams, call that out in `Subagent Progress` rather than overloading `Status Summary`
- `current stage` should describe the critical-path next handoff, not a generic aggregate of all active workstreams
- when multiple workstreams are active, select `current stage` using this precedence:
  - a user decision on the critical path
  - an orchestrator handoff on the critical path
  - an active blocker on the critical path
  - active execution on the critical path
  - queued work on the critical path
- when the round is complete, `current stage` should describe the completion handoff
- `waiting on` and `next action` must also be derived from the same critical-path workstream used to compute `current stage`
- `waiting on` should be computed with this precedence:
  - if the critical path requires a human choice -> the specific user decision owner and choice context
  - else if the critical path requires orchestrator synthesis or routing -> the orchestrator
  - else if a non-user blocker prevents progress -> the named blocker owner or unresolved dependency
  - else if execution is active -> the active workstream owner
  - else if work is queued -> the queue gate that must clear before start
  - else -> `nobody`
- `next action` should describe the next visible handoff on the critical path using persisted state only
- if there is no pending handoff because the round is complete, `next action` should describe the completion handoff or say that no further action is required

Example:

```md
## Status Summary

- Current stage: writing the PM design spec
- Primary owner: PM orchestrator
- Waiting on: nobody
- Next action: finish the written spec and hand it to you for review
- User decision needed: no
```

## Section 2: Subagent Progress

`Subagent Progress` is the live execution surface. It should exist in every reply, even when no subagents are active.

Rules:

- if no subagents have launched, explicitly say `no subagents launched`
- if subagents are active, list each by section or workstream, not by opaque internal ID
- each row or bullet must include:
  - `scope`
  - `display status`
  - `last update`
  - `blocker`
  - `next handoff`
- every displayed entry must be traceable back to one persisted runtime source in the dispatch plan
- `last update` changes only when one of these happens:
  - the workstream changes status
  - ownership changes
  - the blocker changes
  - the next handoff changes
  - materially new progress is made that affects user understanding
- the orchestrator is responsible for refreshing `last update` whenever it emits a reply that reflects one of those changes
- `display status` is derived deterministically using the precedence rules below; implementations must not choose ad hoc among multiple matching labels

Recommended display statuses:

- `not started`
- `queued`
- `running`
- `waiting on orchestrator`
- `waiting on user`
- `blocked`
- `completed`
- `failed`

Example with no active agents:

```md
## Subagent Progress

- no subagents launched
```

Example with active work:

```md
## Subagent Progress

- Section: authentication review | Display status: running | Last update: checking auth edge cases | Blocker: none | Next handoff: reviewer findings -> orchestrator
- Section: UI copy refinement | Display status: waiting on user | Last update: option set prepared | Blocker: pending direction on tone | Next handoff: user decision -> orchestrator
```

## Section 3: Decision Block

`Decision Block` is part of the fixed four-section reply shape. It must appear in every `$ww` response, but its content changes based on whether a real user decision is required.

Rules:

- keep the choices explicit and finite
- say what happens after each choice
- if no decision is needed, explicitly say `no decision required right now`
- do not omit the section, because the fixed reply shape should remain stable across all states
- `user decision needed` in `Status Summary` and the content of `Decision Block` must be derived from the same current dispatch-plan state
- if `user decision needed` is `yes`, `Decision Block` must enumerate the available choice set
- if `user decision needed` is `no`, `Decision Block` must show only `No decision required right now`

For plan approval, the block remains:

- `Approve`
- `Revise`
- `Stop`

But the copy should explain the consequence:

```md
## Decision Block

- `Approve`: I will proceed to the next approved stage.
- `Revise`: I will update the plan/spec and return with a revised version.
- `Stop`: I will stop this dispatch round and preserve the existing artifacts.
```

Example when no decision is needed:

```md
## Decision Block

- No decision required right now
```

## Section 4: Document Summary

`Document Summary` remains mandatory, but it becomes a secondary artifact index rather than the primary runtime surface.

Rules:

- always include:
  - `working brief`
  - `dispatch plan`
  - `design spec`
  - `implementation plan`
- if a document does not exist, write `not created yet`
- when a file exists, show the active path
- when helpful, show version or state, but do not repeat runtime status already covered above
- if the dispatch plan and rendered reply disagree, the dispatch plan is the source that must be fixed or re-rendered from

## State Translation Model

The skill should preserve internal states for process integrity, but it should translate them before showing them to the user.

Use a two-layer model:

- internal state: persisted workflow state used for gating and orchestration logic
- display state: user-facing wording derived from internal state for chat replies

Recommended mappings:

- `draft` -> `preparing the next artifact`
- `awaiting-approval` -> `waiting for your approval`
- `approved` -> `approved and ready to continue`
- `revising` -> `revising based on feedback`
- `dispatched` -> `subagents are running`
- `completed` -> `ready for final review`

Section-level states should also be translated:

- `drafted` -> `draft prepared`
- `under-review` -> `review in progress`
- `accepted` -> `accepted`
- `revision-requested` -> `revision requested`
- `stopped` -> `stopped`

Subagent progress uses display states derived from dispatch-plan data rather than introducing a separate independent runtime state machine.

Recommended derivation rules:

Definitions before precedence:

- `waiting on user` means the next required handoff is an explicit human choice
- `waiting on orchestrator` means the next required handoff is orchestrator synthesis or orchestrator routing
- `blocked` means progress is prevented by a non-user blocker that is not resolved by the normal next handoff

Display-status precedence, highest to lowest:

1. if the orchestrator records an unrecoverable failure -> `failed`
2. if the workstream has satisfied its handoff contract and has no remaining active handoff -> `completed`
3. if a non-user blocker is present and prevents progress -> `blocked`
4. if a human decision is the next required handoff -> `waiting on user`
5. if a handoff is pending orchestrator synthesis or orchestrator routing -> `waiting on orchestrator`
6. if work is active and no higher-precedence state matches -> `running`
7. if packet created but work has not begun -> `queued`
8. if packet not created and section not started -> `not started`

Only one display status may be shown for a workstream. If multiple conditions appear to match, apply the highest-precedence rule and suppress the rest.

## Dispatch Plan Changes

The dispatch plan template should gain a dedicated progress surface instead of relying on a minimal dispatch log.

Required additions:

- a `Progress Board` section
- exact per-workstream fields:
  - `workstream_id`
  - `source_section_id`
  - `source_plan_revision`
  - `workstream_type`
  - `scope`
  - `owner`
  - `internal_state_reference`
  - `display_status`
  - `last_update`
  - `blocker`
  - `next_handoff`
  - `review_pass_id` when the workstream is a reviewer pass

The `Progress Board` is the canonical store for rendered-progress inputs. The chat reply should not invent runtime values that are absent from this section.

The existing `Dispatch Log` can remain for audit purposes, but it should not be the only place where runtime movement is recorded.

Minimum template rule:

- the dispatch plan template must include a concrete `Progress Board` section with placeholders for every required per-workstream field
- the `Subagent Progress` reply section must be renderable from the template-backed persisted fields without inventing missing values

Reviewer-progress persistence rule:

- reviewer progress is persisted in the dispatch plan `Progress Board`
- the packet contract remains execution-oriented and does not become a second progress store
- packet fields should continue to identify scope and handoff contract, while the dispatch plan records live progress for rendering
- reviewer workstreams must be keyed by `source_section_id + review_pass_id` so repeated reviews for the same section remain distinguishable across revisions
- if more than one reviewer is used for the same section and review pass, append a stable reviewer-specific suffix to `workstream_id`

## Contract Synchronization Requirements

This design is not implementation-ready unless the dependent repo artifacts are updated in lockstep with the spec.

Required synchronized artifacts:

- `skills/ww-subagent-orchestrator/SKILL.md`
- `skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
- `skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`

Synchronization rules:

- `SKILL.md` must require the four-section reply shape, not only `Document Summary`
- `dispatch-plan-template.md` must include the canonical `Progress Board` schema defined in this spec
- `subagent-packet-contract.md` must remain execution-oriented, but it must still preserve the identifiers needed to connect packets to `Progress Board` workstreams
- if any of these three artifacts disagree with this design, the implementation plan must treat that as incomplete contract migration, not an acceptable partial rollout

Release-readiness rule:

- do not consider the design package implementation-ready until the spec and these dependent artifacts express the same reply contract and persisted progress schema

## Reviewer And Orchestrator Visibility Rules

Reviewer convergence stays intact. The change is in how the result is surfaced.

Rules:

- reviewer output remains findings-only
- orchestrator must translate reviewer output into a user-readable takeaway
- the user should see whether a reviewer has started, is running, is blocked, or has returned findings
- the user should not see raw reviewer verbosity dumped without synthesis

To support this, the dispatch plan should expose reviewer progress as a structured workstream, not just a narrative note.

## Failure And Wait States

The redesign must handle silent stalls explicitly.

If work is blocked:

- say what is blocked
- say why it is blocked
- say who must unblock it
- say the next visible step after unblock

If work fails:

- say which workstream failed
- say whether retry is possible
- say whether the user needs to choose a path forward

## Success Criteria

The redesign is successful when a user can read any `$ww` response and answer all of these without opening another file:

1. What stage is this in right now?
2. Who owns the current move?
3. Is the system waiting on me?
4. Are any subagents running?
5. If something is blocked, what is the blocker?
6. Which artifacts exist already?

It is also successful when an implementer can derive the reply from persisted state without inventing a second unsynchronized state machine.

## Testing Focus

When this design is implemented, validation should focus on:

- a no-subagent path
- an active parallel-subagent path
- a blocked subagent path
- a reviewer-returned-findings path
- a waiting-for-user-approval path
- a post-completion path

The key test is comprehension, not just formatting: the reply should make the orchestration legible at a glance.
