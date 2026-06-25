# Task Runtime Lifecycle Contract

This reference defines the dormant `task-runtime-v1` lifecycle protocol. Schema
version 2 makes the protocol selectable, but new and ordinary rounds default to
`legacy`. Do not select `task-runtime-v1` until every mandatory phase capability
listed under **Activation Boundary** is implemented and approved.

## State Ownership

| Surface | Owner | Purpose | Authority |
|---|---|---|---|
| `plan_state` | round | approval and required-section rollup | derived by the orchestrator |
| `section_state` | section workflow | human review disposition | derived from review and human decisions |
| `lifecycle_protocol` | round | compatibility discriminator | selected only by an approved dispatch revision |
| `lifecycle_phase` | section runtime | kind of work that owns the next action | advanced only by the orchestrator through a legal event |
| `runtime_state` | section runtime | operational condition | canonical post-launch execution state |
| `return_status` | one attempt return | worker, reviewer, or future verifier input | event input only |

`lifecycle_phase` answers what kind of work is current or next.
`runtime_state` answers whether that work is queued, running, awaiting synthesis,
blocked, complete, failed, or stopped. `runtime_state: complete` remains terminal
and is valid only in `lifecycle_phase: close`.

Workers, reviewers, future verifiers, guards, and humans may produce evidence or
decisions. Only the orchestrator may validate those inputs and persist a phase
change.

## Protocol And Schema

The current write schema is version 2.

```yaml
lifecycle_protocol: legacy | task-runtime-v1
```

- `lifecycle_protocol` is round-owned metadata, not a runtime state.
- `legacy` uses the existing controller and must not persist or consult a
  canonical lifecycle snapshot, event history, or lifecycle rollup.
- `task-runtime-v1` requires every required section to persist the snapshot and
  events in this contract.
- Required sections in one active round may not mix protocols.
- Presence of schema version 2 or lifecycle-capable templates does not activate
  `task-runtime-v1`.
- Schema version 2 dispatch plans must persist an explicit approved protocol;
  absence is invalid and resume must never infer or silently upgrade it.
- A schema version 0 or 1 dispatch plan that predates the discriminator and has
  no lifecycle snapshot or event history normalizes deterministically to
  `lifecycle_protocol: legacy` in memory. This compatibility default does not
  activate or persist a protocol upgrade.
- Historical schema version 0 or 1 artifacts remain readable through that
  explicit compatibility rule and are not rewritten merely to add lifecycle
  fields.
- Mixed normalized schema versions inside one active round remain invalid.

The working brief may recommend a protocol, but it does not own the protocol.
The approved dispatch plan is authoritative.

## Activation Boundary

`task-runtime-v1` may be selected only after all of these mandatory capabilities
are implemented, verified end to end, and approved:

- verifier authority and minimum required verification lanes
- review progression and stale-target handling
- repair authorization and re-verification
- score production and blocker evaluation
- close-gate handling and final human judgment

Approved contracts or templates alone are insufficient activation evidence.

Until then, scaffolded and ordinary rounds must persist
`Lifecycle Protocol: legacy`. This implementation does not add verifier roles,
hooks, quality scoring, repair limits, routing, personas, or lifecycle validator
rules.

## Canonical Phase Vocabulary

```text
plan -> execute -> verify -> review -> fix -> re-verify -> score -> close
```

Every normal path includes `plan`, `execute`, `verify`, `review`, `score`, and
`close`. `fix` and `re-verify` are conditional, but both are mandatory when an
accepted finding causes the target artifact to change. A task profile may not
rename or bypass canonical phases.

| Phase | Meaning |
|---|---|
| `plan` | scope, authority, lanes, and approval are being established |
| `execute` | the primary producer performs the planned work |
| `verify` | first formal verification of the stable execution target |
| `review` | independent quality review and required synthesis |
| `fix` | an authorized producer addresses accepted findings |
| `re-verify` | formal verification of the repaired target |
| `score` | accepted evidence is aggregated into a quality result |
| `close` | final close preconditions and human judgment |

## Phase And Runtime Compatibility

Only the combinations marked `yes` are valid.

| Phase | queued | running | review-pending | blocked | complete | failed | stopped |
|---|---:|---:|---:|---:|---:|---:|---:|
| `plan` | yes |  |  |  |  |  | yes |
| `execute` | yes | yes | yes | yes |  | yes | yes |
| `verify` | yes | yes | yes | yes |  | yes | yes |
| `review` | yes | yes | yes | yes |  | yes | yes |
| `fix` | yes | yes | yes | yes |  | yes | yes |
| `re-verify` | yes | yes | yes | yes |  | yes | yes |
| `score` | yes | yes | yes | yes |  | yes | yes |
| `close` | yes |  | yes | yes | yes |  | yes |

Rules:

- `queued` means the phase owns `next_action.code`, but no attempt is active.
- `running` means the phase has active controller work or an active attempt.
- `review-pending` means a result returned and requires synthesis or human
  judgment before progression.
- `blocked`, `failed`, and `stopped` preserve the phase where progress ended.
- `close/complete` requires `next_action.code: none`.
- Recovery from `blocked` or `failed` preserves phase unless a separate legal
  transition authorizes a phase change.

## Initial Snapshot

A newly initialized `task-runtime-v1` required section begins as:

```yaml
Runtime State: queued
lifecycle:
  phase: plan
  phase_entered_at: <section-created-at>
  event_head: null
  next_action:
    code: await-plan-approval
    detail: dispatch revision requires human approval
```

The null event head is valid only for this exact genesis snapshot. Existing
packet and approval gates still apply.

## Canonical Phase Transitions

Each event maps one exact source pair to one destination pair. Any unlisted
source is rejected.

| Event | Exact source | Exact destination | Required foundation condition |
|---|---|---|---|
| `PLAN_APPROVED` | `plan/queued` | `execute/queued` | referenced dispatch revision is approved |
| `EXECUTION_RESULT_ACCEPTED` | `execute/review-pending` | `verify/queued` | active execution result is accepted and target identity is stable |
| `VERIFICATION_ACCEPTED` | `verify/review-pending` | `review/queued` | formal verification outcome is accepted for the current target |
| `REVIEW_ACCEPTED_NO_REMEDIATION` | `review/review-pending` | `score/queued` | required review lanes and synthesis are accepted with no required artifact change |
| `REVIEW_ACCEPTED_FOR_REMEDIATION` | `review/review-pending` | `fix/queued` | accepted findings require an authorized artifact change |
| `FIX_RESULT_ACCEPTED` | `fix/review-pending` | `re-verify/queued` | repaired artifact revision and producer result are accepted |
| `REVERIFICATION_ACCEPTED` | `re-verify/review-pending` | `review/queued` | formal verification is accepted for the repaired target revision |
| `SCORE_ACCEPTED` | `score/review-pending` | `close/queued` | quality result and blocker evaluation are persisted |
| `CLOSE_APPROVED` | `close/review-pending` | `close/complete` | final human decision permits normal terminal completion |

Later capability contracts may strengthen a transition guard. They may not
change phase ownership, skip a required phase, or complete outside `close`.

## State-Only Events

State-only events never change phase. `<producer-phase>` means `execute`, `fix`,
or `score`; `<lane-phase>` means `verify`, `review`, or `re-verify`;
`<work-phase>` is their union; `<active-phase>` is a work phase or `close`.

| Event | Exact source | Exact destination |
|---|---|---|
| `PHASE_STARTED` | `<work-phase>/queued` | `<work-phase>/running` |
| `ATTEMPT_RESULT_RETURNED` | `<producer-phase>/running` | `<producer-phase>/review-pending` |
| `LANE_RESULT_RECORDED_ACTIVE` | `<lane-phase>/running` | `<lane-phase>/running` |
| `LANE_RESULT_RECORDED_PENDING` | `<lane-phase>/running` | `<lane-phase>/queued` |
| `REQUIRED_LANES_RETURNED` | `<lane-phase>/running` | `<lane-phase>/review-pending` |
| `CLOSE_JUDGMENT_REQUESTED` | `close/queued` | `close/review-pending` |
| `CLOSE_RETRY_REQUESTED` | `close/blocked` | `close/queued` |
| `SECTION_BLOCKED_FROM_QUEUED` | `<active-phase>/queued` | `<active-phase>/blocked` |
| `SECTION_BLOCKED_FROM_RUNNING` | `<work-phase>/running` | `<work-phase>/blocked` |
| `SECTION_BLOCKED_FROM_REVIEW` | `<active-phase>/review-pending` | `<active-phase>/blocked` |
| `SECTION_FAILED_FROM_QUEUED` | `<work-phase>/queued` | `<work-phase>/failed` |
| `SECTION_FAILED_FROM_RUNNING` | `<work-phase>/running` | `<work-phase>/failed` |
| `PLAN_STOPPED` | `plan/queued` | `plan/stopped` |
| `SECTION_STOPPED_FROM_QUEUED` | `<active-phase>/queued` | `<active-phase>/stopped` |
| `SECTION_STOPPED_FROM_RUNNING` | `<work-phase>/running` | `<work-phase>/stopped` |
| `SECTION_STOPPED_FROM_REVIEW` | `<active-phase>/review-pending` | `<active-phase>/stopped` |
| `SECTION_STOPPED_FROM_BLOCKED` | `<active-phase>/blocked` | `<active-phase>/stopped` |
| `SECTION_STOPPED_FROM_FAILED` | `<work-phase>/failed` | `<work-phase>/stopped` |
| `RETRY_BLOCKED` | `<work-phase>/blocked` | `<work-phase>/running` |
| `RETRY_FAILED` | `<work-phase>/failed` | `<work-phase>/running` |
| `REVISION_REQUESTED_FROM_REVIEW` | `<active-phase>/review-pending` | `<active-phase>/blocked` |
| `REVISION_REQUESTED_FROM_BLOCKED` | `<active-phase>/blocked` | `<active-phase>/blocked` |

Revision-request events also set the round plan to `revising`, freeze new
dispatch, and derive `next_action.code: regenerate-plan`.

`close` never enters `running` or `failed`.

## Multi-Lane Aggregation

`verify`, `review`, and `re-verify` are section-level aggregate phases.
Individual lane attempts do not own section state. After recording one lane
return, the orchestrator computes required lanes for the same immutable target:

- if any required lane remains active, emit `LANE_RESULT_RECORDED_ACTIVE`
- if none is active but a required lane remains unlaunched or lacks a terminal
  outcome, emit `LANE_RESULT_RECORDED_PENDING`
- if all required lanes returned, emit `REQUIRED_LANES_RETURNED`

Only the final condition enters `review-pending`. Stale or mismatched-target
returns remain history and do not satisfy required-lane aggregation.

## Snapshot And Event Persistence

Every required `task-runtime-v1` section persists one current lifecycle block,
the existing canonical `Runtime State`, and an append-only event list. The
lifecycle block must not duplicate `runtime_state`, `section_state`, or
`plan_state`:

```yaml
lifecycle:
  phase: plan | execute | verify | review | fix | re-verify | score | close
  phase_entered_at: <timestamp>
  event_head: <event-id-or-null>
  next_action:
    code: <canonical-code>
    detail: <non-authoritative-explanation>
```

Event comparison uses a transition projection containing `lifecycle_phase`,
canonical `runtime_state`, and `next_action`. `phase_entered_at` and `event_head`
are snapshot metadata. State-only events do not rewrite `phase_entered_at`.

Each accepted event contains:

```yaml
- event_id: <immutable-id>
  sequence: <positive-integer>
  section_id: <section-id>
  event_type: <canonical-event>
  occurred_at: <timestamp>
  actor:
    runtime_role: orchestrator
    persona_id: <orchestrator-persona-id>
    execution_id: <execution-id-or-null>
  causation:
    dispatch_revision: <revision>
    previous_event_id: <event-id-or-null>
  previous:
    lifecycle_phase: <phase-or-null>
    runtime_state: <state>
    next_action:
      code: <code>
      detail: <detail>
  next:
    lifecycle_phase: <phase>
    runtime_state: <state>
    next_action:
      code: <code>
      detail: <detail>
  artifact_refs: []
  evidence_refs: []
  guard_results: []
  rationale: <decision-explanation>
```

Events are append-only, monotonically sequenced, linked by
`causation.previous_event_id`, and accepted only when `previous` exactly matches
the persisted transition projection. Phase-changing events require
`actor.runtime_role: orchestrator`; `actor.execution_id` is required when an
execution result caused the event and null for pure planning or human-decision
transitions. The accepted event becomes the new head and its `next` projection
becomes current state in one logical update.

## Deterministic Next Actions

`next_action.code` is derived controller data. The canonical codes are:

| Phase/state | Code |
|---|---|
| `plan/queued` | `await-plan-approval` |
| `execute/queued` | `launch-producer` |
| `execute/running` | `await-active-attempt` |
| `execute/review-pending` | `synthesize-execution-return` |
| `verify/queued` | `launch-verifier` |
| `verify/running` | `await-active-attempt` |
| `verify/review-pending` | `synthesize-verification-return` |
| `review/queued` | `launch-reviewer` |
| `review/running` | `await-active-attempt` |
| `review/review-pending` | `synthesize-review-return` |
| `fix/queued` | `launch-fix` |
| `fix/running` | `await-active-attempt` |
| `fix/review-pending` | `synthesize-fix-return` |
| `re-verify/queued` | `launch-re-verifier` |
| `re-verify/running` | `await-active-attempt` |
| `re-verify/review-pending` | `synthesize-reverification-return` |
| `score/queued` | `compute-score` |
| `score/running` | `await-score-computation` |
| `score/review-pending` | `synthesize-score` |
| `close/queued` | `request-close-judgment` |
| `close/review-pending` | `await-close-judgment` |
| `close/complete` | `none` |
| any valid `blocked` | `resolve-blocker` or `regenerate-plan` after an accepted revision request |
| any valid `failed` | `decide-retry-or-stop` |
| any valid `stopped` | `none` |

The `detail` field may explain context but may not change the code's meaning.

## Round Rollup

Any round lifecycle summary is derived from required section snapshots. It must
never be a writable phase authority or packet source. Existing `plan_state`
aggregation remains authoritative. Under `task-runtime-v1`, a round cannot be
completed until every required section is `close/complete` with next action
`none`. Legacy rounds continue using the existing aggregation rules.

## Resume And Recovery

On resume, the orchestrator:

1. normalizes the dispatch schema
2. loads required section snapshots and runtime states
3. finds each final accepted event
4. verifies event head, sequence, previous snapshot, and current snapshot
5. verifies phase/state compatibility and derived next action
6. reconciles active execution and attempt identities
7. blocks unknown active attempts until reconciliation completes
8. recomputes any derived round rollup
9. resumes only from persisted `next_action`

Snapshot/event disagreement freezes packet creation and phase advancement. The
orchestrator records a durable reconciliation requirement. If durable evidence
cannot resolve the disagreement, the round returns to human `Revise`; the
runtime must not replay completed artifact writes merely because execution was
interrupted.

## Legacy Migration

Migration requires a separately approved dispatch revision, complete mandatory
phase capabilities, and a safe checkpoint with no active agent, active attempt,
or unresolved late result. A round containing a required `running`, `complete`,
or `stopped` section remains legacy.

The exact source contract is:

```yaml
lifecycle_protocol: legacy
lifecycle_snapshot: absent
lifecycle_event_history: absent
active_agent_id: null
active_attempt_id: null
pending_late_results: []
```

Migration is round-atomic. Against one immutable source plan revision and hash,
the orchestrator prepares:

- one migration manifest with source plan revision, source content hash,
  destination schema version, required section IDs, and each section's
  bootstrap event ID
- one `LEGACY_LIFECYCLE_BOOTSTRAPPED` event per required section
- one resulting snapshot per required section
- one round protocol switch to `task-runtime-v1`

All records persist together and pass post-write validation, or none persist.
If the logical write or post-write validation fails, dispatch remains frozen
and the last approved legacy revision remains the rollback baseline. If a
section's phase cannot be derived without guessing, migration halts for human
revision. Legacy review evidence never substitutes for matching formal
verification. Existing `running` attempts must be reconciled under the legacy
controller before migration can be considered.

The bootstrap event has sequence `1`, null `previous_event_id`, a `previous`
projection with `lifecycle_phase: null`, and a legal evidence-derived `next`
snapshot. `legacy-unmapped` may appear only as the bootstrap event's previous
next-action code; it may never appear in the current snapshot.

Destination selection is strict:

1. reject migration when any required section is `running`, `complete`, or `stopped`
2. for `blocked`, preserve the one evidence-derived active phase and do not evaluate milestones
3. for `failed`, preserve the one evidence-derived work phase and do not evaluate milestones
4. for only `queued` or `review-pending`, select the furthest fully satisfied cumulative milestone
5. if zero destinations or multiple destinations at one milestone match, halt for human revision

| Durable legacy evidence | Exact destination and next action |
|---|---|
| `blocked` with one evidence-derived active phase | `<active-phase>/blocked`, `resolve-blocker` |
| `failed` with one evidence-derived work phase | `<work-phase>/failed`, `decide-retry-or-stop` |
| verification and complete review for current target, no remediation outstanding, accepted score awaiting judgment | `close/queued`, `request-close-judgment` |
| verification and complete review for current target, no remediation required, no accepted score | `score/queued`, `compute-score` |
| accepted repaired result after verified and reviewed pre-fix target, repaired target lacks re-verification | `re-verify/queued`, `launch-re-verifier` |
| verification and complete review for current target with accepted remediation required | `fix/queued`, `launch-fix` |
| verification and all required review lanes returned for the same target, synthesis pending | `review/review-pending`, `synthesize-review-return` |
| verification exists but a required review lane is unlaunched, active, stale, or non-terminal | `review/queued`, `launch-reviewer` |
| stable producer result with no matching formal verification | `verify/queued`, `launch-verifier` |
| unapproved plan in `queued` | `plan/queued`, `await-plan-approval` |
| approved plan in `queued` with no accepted producer result | `execute/queued`, `launch-producer` |

Later milestones are cumulative and require all earlier mandatory gates for the
same target lineage. For any non-blocked, non-failed source with a stable target
but no matching formal verification, `verify/queued` takes precedence over
legacy review, score, or close labels.

## Invalid States

Examples that later validator rounds must reject include:

- lifecycle snapshot or event history while protocol is `legacy`
- lifecycle-aware execution before mandatory capabilities are available
- `execute/complete`, `plan/running`, `plan/review-pending`, or `close/running`
- `close/complete` with a next action other than `none`
- phase change by a non-orchestrator actor or without an appended event
- event sequence gaps, duplicate IDs, broken previous snapshots, or head drift
- `fix -> review` without `re-verify`
- `review -> close` without `score`
- a writable round-level `lifecycle_phase`
- partial multi-section migration or mixed lifecycle protocols
- active legacy migration whose phase requires guessing

Dedicated validator rule IDs and negative fixtures belong to a later validator
round. This contract defines the semantics they will enforce.
