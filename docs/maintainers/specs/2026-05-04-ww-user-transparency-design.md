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

## Section 1: Status Summary

`Status Summary` is the new top-level interface. It answers the user's first questions before anything else.

Required fields:

- `current stage`
- `owner`
- `waiting on`
- `next action`
- `user decision needed`

Rules:

- use natural language, not raw internal state names
- if the system is blocked, say what the blocker is
- if the system is waiting on the user, say exactly what decision is needed
- if the system is waiting on internal work, say who owns the next move

Example:

```md
## Status Summary

- Current stage: writing the PM design spec
- Owner: PM orchestrator
- Waiting on: nobody
- Next action: finish the written spec and hand it to you for review
- User decision needed: not yet
```

## Section 2: Subagent Progress

`Subagent Progress` is the live execution surface. It should exist in every reply, even when no subagents are active.

Rules:

- if no subagents have launched, explicitly say `no subagents launched`
- if subagents are active, list each by section or workstream, not by opaque internal ID
- each row or bullet must include:
  - `scope`
  - `status`
  - `last update`
  - `blocker`
  - `next handoff`

Recommended statuses:

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

- Section: authentication review | Status: running | Last update: checking auth edge cases | Blocker: none | Next handoff: reviewer findings -> orchestrator
- Section: UI copy refinement | Status: waiting on user | Last update: option set prepared | Blocker: pending direction on tone | Next handoff: user decision -> orchestrator
```

## Section 3: Decision Block

`Decision Block` should appear only when a real user decision is required. It must not be used for generic progress chatter.

Rules:

- keep the choices explicit and finite
- say what happens after each choice
- if no decision is needed, omit the section

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

## State Translation Model

The skill should preserve internal states for process integrity, but it should translate them before showing them to the user.

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

## Dispatch Plan Changes

The dispatch plan template should gain a dedicated progress surface instead of relying on a minimal dispatch log.

Required additions:

- a `Progress Board` section
- per-workstream owner
- displayed status
- last update text
- blocker text
- next handoff

The existing `Dispatch Log` can remain for audit purposes, but it should not be the only place where runtime movement is recorded.

## Reviewer And Orchestrator Visibility Rules

Reviewer convergence stays intact. The change is in how the result is surfaced.

Rules:

- reviewer output remains findings-only
- orchestrator must translate reviewer output into a user-readable takeaway
- the user should see whether a reviewer has started, is running, is blocked, or has returned findings
- the user should not see raw reviewer verbosity dumped without synthesis

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

## Testing Focus

When this design is implemented, validation should focus on:

- a no-subagent path
- an active parallel-subagent path
- a blocked subagent path
- a reviewer-returned-findings path
- a waiting-for-user-approval path
- a post-completion path

The key test is comprehension, not just formatting: the reply should make the orchestration legible at a glance.
