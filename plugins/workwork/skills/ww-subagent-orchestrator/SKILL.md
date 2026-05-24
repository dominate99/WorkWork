---
name: ww-subagent-orchestrator
description: Use when a task should start with `$ww` to estimate work, choose an orchestrator persona, build a persisted working brief, create a tracked dispatch plan file, and coordinate persona-bound subagents with Superpowers workflows across coding, product, or creative work.
---

# WW Subagent Orchestrator

## Overview

Use this skill to turn `$ww` into a disciplined orchestration flow instead of ad hoc subagent dispatch. The skill estimates first, writes a persisted working brief, chooses the correct top-level orchestrator persona, writes a tracked dispatch plan file, and only then allows real subagent work.

- `$ww` = standard planning-and-dispatch workflow
- `$www` = strict mode layered on top of `$ww`
- `quality_mode` records round-level intent for whether the current dispatch round is `standard` or `strict`, and belongs in the persisted working brief for that round

## Core Rules

- Treat `$ww` as an estimation trigger, not a dispatch command.
- Treat `$www` as strict mode, not a separate orchestration system.
- Choose the top-level orchestrator from task context:
  - `code/programming` -> `staff-engineer-orchestrator`
  - `design/ads/product` -> `pm-orchestrator`
  - `video/creative` -> `creative-director-orchestrator`
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
- Worker execution order is `user constraints -> work_mode -> persona -> goal_tuning`.
- Keep `task_mode` separate from `work_mode`. `task_mode` describes the packet's role-task surface; `work_mode` describes the worker's execution posture.
- Reviewer subagents point out problems only. They do not rewrite the draft or make the final decision.
- Reviewer subagents must stay narrow and convergent: only inspect the assigned artifact against its stated scope, list the highest-signal issues, and stop.
- `$www` applies strict review only to the persisted `design spec` and `implementation plan` artifacts. `design-spec` and `implementation-plan` are shorthand target identifiers for those two artifact types only.
- For `$www` design/planning rounds, persisted `design spec` and/or `implementation plan` artifacts required by the round must be created and must pass strict review before the round can complete. `$www` must not degrade to ordinary `$ww` by skipping persistence of a required target.
- `$www` always runs `self-review -> reviewer-review`, and if material findings exist, it runs the only allowed `patching -> re-review` cycle.
- `$www` strict review passes only on `no material findings`.
- `$www` allows exactly one patch cycle per strict-review target.
- Strict review is per target, not latched across the whole round: `design-spec` and `implementation-plan` each run their own strict-review cycle.
- When a new strict-review target starts, initialize the live `strict_review` gate record for that target by setting `strict_review.target`, `strict_review.state: idle`, and `cycle_count: 0` before `STRICT_TARGET_STARTED` moves the new target into `self-review`.
- Each strict-review target is identified by its persisted artifact path plus immutable reviewer `review target` identity for one specific artifact revision.
- The one patch cycle limit is enforced per strict-review target artifact revision. The same unchanged artifact revision must not receive a second patch cycle through relabeling, redispatch, or a new review packet name.
- `re-review` must be a fresh independent reviewer pass against the patched artifact, not an orchestrator-only check or a relabeled synthesis step.
- If a strict-review target reaches canonical `runtime_state: blocked` and a human later chooses `Revise`, the revised `design spec` or `implementation plan` is a new strict-review target in a new approved round or revision. It does not reopen the old target or grant a second patch cycle.
- If a persisted `design spec` or `implementation plan` changes after a strict-review pass, that post-pass revision reopens strict review for the new artifact revision before dependent work or round completion can proceed.
- A strict-review pass does not bypass reviewer coverage, orchestrator synthesis, or human judgment. It only decides whether the strict-review target may advance without entering canonical `runtime_state: blocked`.
- Every applicable strict-review target is `required for goal` within that `$www` round. Dependent work and round completion must wait until each required strict-review target clears the strict-review gate.
- `strict_review` is the live gate record for the active target only. Durable per-target strict-review outcomes must remain persisted in the section's review lane records keyed by immutable `Review Target Ref` identity for that artifact revision.
- `passed` and `blocked` apply to the current target only. Starting a different strict-review target does not inherit the previous target's terminal gate result.
- `runtime_state` is the single authoritative post-launch section state. `close_state` is derived from it and must never act as a parallel state machine.
- `failed` and `stopped` are distinct. User stop must not be conflated with execution failure.

## Required Stage Order

Follow this sequence every time:

1. Estimate the task
2. Build the working brief
3. Persist the working brief
4. Route to the correct orchestrator
5. Write the dispatch plan file
6. Run the pre-approval self-audit on the just-written dispatch plan
7. Render this approval block:
   1. `Approve`
   2. `Revise`
   3. `Stop`
8. Launch subagents only after `Approve`
9. Run section review loops
10. Synthesize results and close with verification

This numbered list is the required rendered approval prompt. Numeric replies map to the same decisions: `1` -> `Approve`, `2` -> `Revise`, `3` -> `Stop`. The words `Approve`, `Revise`, and `Stop` remain accepted aliases for the same decisions.

The pre-approval self-audit is mandatory. If scope parity, required runtime-state surfaces, required review-lane outcome fields, or deprecated state-field removal fails validation, the dispatch plan stays in `draft` or `revising` and must not be shown for approval yet.

For `$www`, keep the same top-level stage order and diverge only after the persisted `design spec` or `implementation plan` artifact is produced.

For `$www` design/planning rounds, producing and persisting every required `design spec` and `implementation plan` artifact is mandatory before dependent work or the round can complete.

For `$www` on strict-review targets:

1. produce target artifact
2. run orchestrator `self-review`
3. run reviewer `reviewer-review`
4. if the reviewer reports `no material findings`, treat strict review as passed, map that result to reviewer outcome `PASS`, and continue under the normal lane rules for orchestrator synthesis and human judgment while canonical `runtime_state` stays in the existing review flow
5. if material findings exist, enter `patching`
6. run one independent reviewer `re-review`
7. if the `re-review` reports `no material findings`, treat strict review as passed, map that result to reviewer outcome `PASS`, and continue under the normal lane rules for orchestrator synthesis and human judgment while canonical `runtime_state` stays in the existing review flow
8. if the `re-review` still finds unresolved material issues, map that result to reviewer outcome `REJECT`, move the section to canonical `runtime_state: blocked`, and return it to the higher-level round for human judgment or revision
9. if a human later chooses `Revise`, restart strict review only for the newly revised artifact revision in the next approved round or revision
10. if the artifact changes after a strict-review pass, invalidate that pass and reopen strict review for the new artifact revision before dependent work or the round can complete

Artifacts outside the `design spec` and `implementation plan` strict-review targets continue through the normal `$ww` section review loops.
For `$www`, a blocked strict-review target is never optional or non-blocking: it blocks dependent work, blocks round completion, and remains `required for goal` until a newly revised target clears strict review in a later approved round or revision.

## Strict Review State Machine

Use this deterministic event-driven controller for `$www` strict-review targets:

| Event | From State | To State | Notes |
|---|---|---|---|
| `STRICT_TARGET_STARTED` | `idle` | `self-review` | after initializing the live gate record for the target, start strict review for that target |
| `SELF_REVIEW_COMPLETED` | `self-review` | `reviewer-review` | hand off to the independent reviewer |
| `REVIEW_FOUND_NO_MATERIAL_FINDINGS` | `reviewer-review` | `passed` | applies to the current target only |
| `REVIEW_FOUND_MATERIAL_FINDINGS` | `reviewer-review` | `patching` | first material finding enters the only patch cycle |
| `PATCH_COMPLETED` | `patching` | `re-review` | patching never completes the gate by itself |
| `REVIEW_FOUND_NO_MATERIAL_FINDINGS` | `re-review` | `passed` | requires an independent reviewer pass, not orchestrator synthesis alone |
| `REVIEW_FOUND_MATERIAL_FINDINGS` | `re-review` | `blocked` | unresolved material findings after the one patch cycle block the current target |

Rules:

- initialize a new target by setting `strict_review.target`, `strict_review.state: idle`, and `cycle_count: 0`, then apply `STRICT_TARGET_STARTED`
- only a `passed` target may allow the next strict-review target to start in the same round
- a `blocked` target may not be overwritten by switching `strict_review.target` in the same round; it must follow the existing human `Revise` path into a new approved round or revision
- entering `patching` increments `cycle_count` from `0` to `1`
- no direct `reviewer-review -> blocked` on the first material finding
- no direct `patching -> passed`
- no orchestrator-only shortcut from `re-review` to `passed`
- no second patch cycle

## Strict Review Outcomes

Use this objective contract for `$www` strict-review targets. `strict_review.state` is the live persisted gate state for the active target, and durable per-target results remain in review lane records keyed by `Review Target Ref`:

- `passed` means the active target's `strict_review.state` reaches `passed` because the reviewer or independent `re-review` reported `no material findings` for the current artifact revision; in controller terms, that gate result maps to reviewer outcome `PASS`, then the section continues through the existing synthesis and human-judgment flow
- `blocked` means the active target's `strict_review.state` reaches `blocked` and the section enters canonical `runtime_state: blocked` because the one allowed independent `re-review` still reports unresolved material findings; in controller terms, that gate result maps to reviewer outcome `REJECT`
- a post-pass artifact revision invalidates the earlier pass and reopens strict review for the new revision
- when the controller later initializes a new strict-review target, the previous target's pass/block outcome remains durably recorded in review lane records for that earlier `Review Target Ref`
- blocked strict-review targets return to the higher-level round for orchestrator synthesis plus human judgment or revision; they do not silently continue as passed, permit dependent work, or allow round completion

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
- section-level worker-mode recommendations
- workflow bindings
- dispatch recommendation
- scope preparation when packets or reviewers will reference artifacts

Its job is to capture context and recommendations, not runtime approval state. Do not dispatch from a rough idea or a quick summary.

Working brief persistence rules:

- a brief may temporarily exist in chat during raw estimation
- before dispatch-plan creation, the brief must be saved to `docs/cases/<case-slug>/rounds/<round-slug>/working-brief.md`
- the working brief may recommend `worker mode`, `worker-mode rationale`, `goal tuning`, and constraint-override notes by section, but it does not decide the final execution mode
- when `$www` is active, record `quality_mode` in that persisted working brief as the working brief's only strict-mode field and treat it as round-level intent, not as a dispatch gate boolean
- `design-spec` and `implementation-plan` artifacts stay content-focused and do not carry strict-mode headers or duplicate strict-mode metadata
- schema checks, revision comparisons, and reviewer targeting must use the persisted brief artifact
- each persisted working brief must carry explicit `case_slug`, `round_slug`, `case_root`, and `round_root` metadata so path identity is not re-derived ad hoc
- `case_slug` identifies the long-lived workstream; `round_slug` identifies one bounded `$ww` or `$www` cycle inside that case
- revisions within the same round update the same `round_root`; new rounds create a new `round_slug`
- pre-cutover type-based brief paths are legacy history only; they are not canonical write targets for new rounds
- archived historical type-based workflow artifacts live under `docs/legacy/superpowers/`

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

Check for project personas first at `docs/superpowers/personas/registry.yaml`. If that file does not exist or does not cover the need, fall back to built-in persona records from `references/built-in-personas.yaml` and the selection rules from `references/persona-registry.md`.

For this first worker-enforcement layer:

- `references/persona-registry.md` remains the rules layer
- `references/built-in-personas.yaml` is the built-in data-record layer
- project and built-in persona records must use the same top-level `personas:` schema shape
- built-in routing defaults and built-in fallback resolution should use canonical persona `id` values from the data file, not free-text labels
- worker-candidate filtering happens before persona selection is finalized
- a worker-capable persona must have `review_only: false`, `role_type` not equal to `orchestrator`, and exactly two `implementation_principles` before it may enter the worker selection set
- reviewer-only and orchestrator personas are not worker-capable in this layer

Runtime selection guidance:

- derive the initial candidate set from required fields first
- prefer the strongest project persona match before falling back to built-in personas
- use `strengths`, `use_when`, `domains`, and language fit to narrow the viable set
- once multiple candidates are still viable, use optional enrichment fields from `references/persona-registry.md` to rank and break ties
- use `decision_style` when the round's main ambiguity is how to frame or resolve the work
- use `quality_bar` when the main differentiator is the rigor level the round requires
- use `tradeoff_bias` and `failure_modes_to_watch` when two candidates are capable but protect different risks
- use `escalation_triggers` when the choice depends on who should stop and escalate under irreversible or high-blast-radius conditions
- use `collaboration_posture` and `taste_criteria` only when they materially improve specialist composition or quality judgment
- do not use optional enrichment fields to bypass role compatibility, worker-capability gates, or stronger required-field fit
- if enrichment meaningfully affected the choice, say so in the persona rationale after the required-field justification

For every chosen persona, write:

- the canonical persona `id`
- the persona `title` only when a human-facing display label is useful
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
- worker `work_mode`, `work_mode_rationale`, `goal_tuning`, and `constraint_precedence_note` when the packet is a worker packet
- worker persona implementation principles when the selected persona is worker-capable
- owned read/write scope
- success and handoff rules
- immutable reviewer target data when review is involved

Create reviewer packets only after the reviewed artifact snapshot is stable enough to generate `review_target_ref`.
Worker prompts consume packet state; they must not re-derive `work_mode` from the working brief.

## Dispatch Plan File

Before real dispatch, write a tracked Markdown file using `assets/dispatch-plan-template.md` to:

`docs/cases/<case-slug>/rounds/<round-slug>/dispatch-plan.md`

The dispatch plan is the canonical runtime state for the dispatch round. The dispatch plan must:

- reference the persisted working brief version it was derived from
- reference the active `case_slug`, `round_slug`, `case_root`, and `round_root`
- record the active approval state
- render the top-level `Strict Review Runtime State` block with `mode`, `target`, `state`, and `cycle_count`
- list planned sections and planned personas
- record the section-level effective `worker mode` and its rationale when worker execution applies
- encode per-section review loops
- expose one canonical `plan_state`
- track per-section `runtime_state`
- track `Active Worker Mode` plus `Mode Change History` when worker execution is active
- keep active execution pointers plus execution history
- record `required_for_goal` so top-level aggregation can distinguish `failed` from `stopped`

Dispatch-plan validation rules are mandatory before the approval block is rendered:

- every writable path listed in `Planned Scope` must also appear in `exclusive_write_scope`
- the dispatch plan must render the top-level `Strict Review Runtime State` block in every round; for standard rounds it must render `mode: standard`, `target: none`, `state: idle`, and `cycle_count: 0`, while active live strict-review gate semantics remain specific to strict-review targets
- deprecated state fields such as `Review Status` must not appear in new dispatch plans
- pre-approval plans must preserve the durable review-lane outcome fields and review-target structure, including `Strict Review Outcome` when applicable; once a stable reviewed artifact snapshot exists, the concrete durable record keyed by `Review Target Ref` and artifact revision must persist
- `task_mode` must not be reused as `worker mode`

If any of these validation rules fail, the dispatch plan remains in `draft` or `revising`, the orchestrator must correct the persisted plan, and the plan must not be shown for approval yet.

`strict_review` is rendered as top-level controller metadata inside every dispatch plan. It does not replace section-level `runtime_state`, which remains the single authoritative post-launch section state.
For worker execution, the authority chain is fixed: the working brief recommends, the dispatch plan decides and records, the packet freezes one execution snapshot, and the worker prompt consumes packet state only.
- new round artifacts are canonically written under `round_root`; pre-cutover type-based artifact locations are legacy history only and are not active write targets
- archived type-based workflow artifact families live under `docs/legacy/superpowers/`

For standard `$ww` rounds, render `strict_review` as `mode: standard`, `target: none`, `state: idle`, and `cycle_count: 0`. That required block is a runtime-state surface only and does not mean the round owns an active live `$www` strict-review gate.

`strict_review.target` is only the target-kind discriminator for the active strict-review target: `design-spec` or `implementation-plan`.

For strict-review targets, `strict_review.state` and `cycle_count` are scoped to the active live strict-review target only. When a new target is allowed to start, initialize the live gate record for that target with `state: idle` and `cycle_count: 0`, then advance it through the strict-review state machine.

Concrete artifact identity and artifact revision continue to come from persisted artifact paths, revision tracking, and reviewer `review target` references elsewhere in the controller model.

Durable per-target strict-review outcomes remain in the section review lane records keyed by `Review Target Ref`, so switching the live gate record to a later target does not erase whether an earlier target revision already passed or blocked.

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

Before approval rendering:

1. run a pre-approval self-audit on the just-written dispatch plan
2. verify scope parity so every writable path in `Planned Scope` must also appear in `exclusive_write_scope`
3. verify required runtime-state surfaces so the dispatch plan must render the top-level `Strict Review Runtime State` block in every round; for standard rounds it must render `mode: standard`, `target: none`, `state: idle`, and `cycle_count: 0`, while active live strict-review gate semantics remain specific to strict-review targets
4. verify review-lane completeness so pre-approval plans must preserve durable review-lane outcome fields and review-target structure, including `Strict Review Outcome` when applicable; once a stable reviewed artifact snapshot exists, the concrete durable record keyed by `Review Target Ref` and artifact revision must persist
5. verify deprecated state removal so fields such as `Review Status` must not appear
6. if any audit check fails, keep the dispatch plan in `draft` or `revising`, correct the persisted plan, and it must not be shown for approval yet

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
- `dispatch plan`: `docs/cases/<case-slug>/rounds/<round-slug>/dispatch-plan.md`
- `design spec`: `docs/cases/<case-slug>/rounds/<round-slug>/design-spec.md`
- `implementation plan`: `docs/cases/<case-slug>/rounds/<round-slug>/implementation-plan.md`

Missing-document rule:

- If a document has not been created yet, write `not created yet`
- Do not replace that phrase with softer wording such as `pending`, `later`, or `to be created`

Preferred format:

```markdown
## Document Summary

- `working brief`: ready, version 2, `docs/cases/example-case/rounds/2026-04-27-topic/working-brief.md`
- `dispatch plan`: awaiting-approval, `docs/cases/example-case/rounds/2026-04-27-topic/dispatch-plan.md`
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
| `section_state` | section-level workflow tracking | `drafted`, `accepted`, `revision-requested`, `stopped` | derived from section review and controller outcomes; do not use it as a parallel execution or review-status surface |
| `runtime_state` | canonical execution state | `queued`, `running`, `blocked`, `review-pending`, `complete`, `failed`, `stopped` | single authoritative post-launch section state |
| `return_status` | subagent event input | `DONE`, `DONE_WITH_CONCERNS`, `NEEDS_CONTEXT`, `BLOCKED`, `FAILED` | subagent-return input only; never persisted as the canonical long-lived state |
| reviewer outcome | review-lane event input | `PASS`, `REJECT` | separate event surface from `return_status`; used only when evaluating reviewer findings in the controller |

Use one global plan state throughout the run:

- `draft`
- `awaiting-approval`
- `approved`
- `revising`
- `stopped`
- `dispatched`
- `completed`

`approved` is the only state that allows packet creation or real dispatch.

Use one consistent section state set for workflow tracking:

- `drafted`
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
