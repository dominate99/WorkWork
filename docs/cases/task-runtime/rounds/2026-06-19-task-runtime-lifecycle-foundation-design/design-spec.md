# Task Runtime Lifecycle Foundation Design

- Date: 2026-06-19
- Status: review-pending
- Artifact Revision: 11
- Working Brief Version: 1
- Dispatch Plan Revision: 1
- Upstream Design: `docs/superpowers/specs/2026-06-19-workwork-task-runtime-design.md`

## Goal

Define the lifecycle foundation that lets a WorkWork section persist what kind
of work is active without weakening the existing authority of `runtime_state`.
The foundation must be deterministic enough for a later implementation round to
update contracts and templates without re-deciding state ownership, transition
semantics, event identity, migration, or recovery behavior.

This round defines design only. It does not update active contracts, templates,
packets, validators, personas, role bindings, hooks, verifier lanes, model
profiles, repair policy, or quality scoring.

## State Ownership

WorkWork keeps its existing state layers and adds one section-owned semantic
phase:

| Surface | Owner | Purpose | Authority |
|---|---|---|---|
| `plan_state` | round | approval and required-section rollup | derived by the orchestrator from section outcomes |
| `section_state` | section workflow | human review disposition | derived from review and human decisions |
| `lifecycle_phase` | section runtime | kind of work that is current or next | advanced only by the orchestrator through a legal lifecycle event |
| `runtime_state` | section runtime | operational condition of the section | remains the canonical post-launch execution state |
| `return_status` | one attempt return | worker/reviewer/verifier input | event input only; never canonical long-lived state |

`lifecycle_phase` and `runtime_state` are orthogonal, but they are not peers with
overlapping authority:

- `lifecycle_phase` answers **what stage owns the next action**.
- `runtime_state` answers **whether the section is queued, running, waiting,
  blocked, complete, failed, or stopped**.
- Phase completion is represented by a lifecycle transition event.
- `runtime_state: complete` continues to mean the section is terminal. It must
  not be reused to mean that an intermediate phase completed.
- A phase transition does not automatically imply a terminal runtime-state
  transition.

The orchestrator is the only writer allowed to change `lifecycle_phase`.
Workers, reviewers, future verifiers, transition guards, and humans produce
inputs or decisions; the orchestrator validates those inputs and persists the
legal transition.

## Protocol Activation Boundary

Adding schema and template support does not immediately activate the new phase
machine. Each round records one compatibility discriminator:

```yaml
lifecycle_protocol: legacy | task-runtime-v1
```

Rules:

- `legacy` uses the current WorkWork controller and does not persist or consult a
  canonical lifecycle snapshot.
- `task-runtime-v1` requires every required section to persist the lifecycle
  snapshot and events defined here.
- One active round may not mix lifecycle protocols across required sections.
- The lifecycle foundation implementation round may add dormant schema,
  templates, normalization, and validation support, but defaults all ordinary
  rounds to `legacy`.
- `task-runtime-v1` cannot be selected until verifier authority, minimum required
  verification lanes, review progression, score production, and close-gate
  handling exist for every mandatory phase.
- Protocol activation is explicit in an approved dispatch plan. It must not be
  inferred from the presence of new fields or silently enabled during resume.
- Migrating an active legacy round requires a separately approved migration
  revision and a safe checkpoint with no active agent, packet attempt, or
  unresolved late result.
- The protocol switch, bootstrap event, lifecycle snapshot, schema version, and
  normalized `next_action` persist as one logical update. Before that update the
  artifact remains fully `legacy`; after it, the artifact is fully
  `task-runtime-v1`. No mixed intermediate state may be written.
- `lifecycle_protocol` is round-owned compatibility metadata. Migrating a
  multi-section round evaluates every required section from the same immutable
  legacy dispatch snapshot, prepares one bootstrap event and snapshot per
  section, and commits all section bootstraps plus the one round protocol switch
  in a single logical write.
- The migration manifest records the source plan revision, source content hash,
  destination schema version, required section IDs, and bootstrap event ID for
  each section. If any required section cannot bootstrap deterministically, none
  of the section snapshots or protocol changes may persist.
- If the migration write or post-write validation fails, dispatch remains frozen
  and the last approved legacy revision remains the rollback baseline.
- The first end-to-end dogfood round is the earliest allowed activation unless a
  preceding approved round proves the same capability set.

This discriminator controls which controller contract is active; it is not a
second runtime state or phase authority.

## Phase Vocabulary

The canonical ordered vocabulary is:

```text
plan -> execute -> verify -> review -> fix -> re-verify -> score -> close
```

Phase definitions:

| Phase | Meaning | Completion evidence owned by later layers |
|---|---|---|
| `plan` | section scope, authority, lanes, and approval are being established | approved dispatch revision |
| `execute` | the planned producer performs the section's primary work | accepted producer result and stable artifact identity |
| `verify` | the first formal verification of execution output is active or next | verification outcome bound to the target revision |
| `review` | independent quality review or its required human synthesis is active or next | reviewer outcomes and orchestrator synthesis |
| `fix` | an authorized producer addresses accepted findings | accepted repaired artifact revision |
| `re-verify` | formal verification of a changed artifact is active or next | verification outcome bound to the repaired revision |
| `score` | persisted evidence is being aggregated into a quality result | accepted score and blocker evaluation |
| `close` | final close preconditions and human judgment are active or complete | final human decision and terminal section state |

`execute` is intentionally task-neutral. It covers code implementation, document
production, design creation, audits, data work, and operational changes.

No task profile may rename or bypass canonical phases. Every normal path includes
`plan`, `execute`, `verify`, `review`, `score`, and `close`. The foundation
defines two legal review branches:

- `review -> score` when accepted review evidence has no required remediation
- `review -> fix` when accepted findings require artifact changes

`fix` and `re-verify` are conditional phases: they are absent when no remediation
is required, and both are mandatory whenever remediation changes the target.

## Phase And Runtime-State Compatibility

The following matrix defines valid combinations for new lifecycle-aware
artifacts. A blank combination is invalid.

| `lifecycle_phase` | `queued` | `running` | `review-pending` | `blocked` | `complete` | `failed` | `stopped` |
|---|---:|---:|---:|---:|---:|---:|---:|
| `plan` | yes | no | no | no | no | no | yes |
| `execute` | yes | yes | yes | yes | no | yes | yes |
| `verify` | yes | yes | yes | yes | no | yes | yes |
| `review` | yes | yes | yes | yes | no | yes | yes |
| `fix` | yes | yes | yes | yes | no | yes | yes |
| `re-verify` | yes | yes | yes | yes | no | yes | yes |
| `score` | yes | yes | yes | yes | no | yes | yes |
| `close` | yes | no | yes | yes | yes | no | yes |

Normative rules:

- `complete` is valid only with `close`.
- `review-pending` means an attempt or lane returned and orchestrator synthesis
  or human judgment is required before the phase can advance. It is valid in
  production, verification, review, repair, scoring, and close phases, but not
  during unapproved `plan`.
- `queued` means the named phase owns `next_action.code` but has not started an active
  attempt.
- `running` means the named phase has active controller work or an active attempt.
- `blocked`, `failed`, and `stopped` preserve the phase in which progress ended.
- Recovery from `blocked` or `failed` does not change phase unless the recovery
  decision separately authorizes a legal phase transition.
- A section may not persist `lifecycle_phase: close` and
  `runtime_state: complete` while `next_action.code` is anything other than
  `none`.

## Initial Snapshot

A newly scaffolded, unapproved required section starts as:

```yaml
lifecycle_phase: plan
runtime_state: queued
next_action:
  code: await-plan-approval
  detail: dispatch revision requires human approval
lifecycle_event_head: null
```

Approval of the dispatch revision completes planning for that section and emits
the first phase transition:

```text
plan/queued --PLAN_APPROVED--> execute/queued
```

Packet creation and real work remain forbidden until existing `plan_state`
approval gates are also satisfied. `lifecycle_phase` does not replace or bypass
those gates.

## Transition Model

Every phase change requires one legal event. State-only events may change
`runtime_state` without changing phase.

### Canonical Phase Transitions

Each event maps one exact source pair to one exact destination pair. An event
received in any unlisted source pair is rejected.

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

`CLOSE_APPROVED` is a same-phase terminal event. It changes
`runtime_state: review-pending` to `runtime_state: complete`; it does not invent a
phase after `close`.

Later rounds own the detailed verifier evidence, review findings, repair limits,
score schema, blocker policy, and exception-close semantics referenced by these
conditions. Those later contracts may strengthen a transition guard but may not
change phase ownership or bypass the required event.

### State-Only Events

In this table, `<producer-phase>` means exactly `execute`, `fix`, or `score`.
`<lane-phase>` means exactly `verify`, `review`, or `re-verify`.
`<work-phase>` is the union of producer and lane phases. `<active-phase>` means a
work phase or `close`. None of these placeholders includes `plan`.

| Event | Exact source | Exact destination | Phase behavior |
|---|---|---|---|
| `PHASE_STARTED` | `<work-phase>/queued` | `<work-phase>/running` | unchanged; `work-phase` is exactly `execute`, `verify`, `review`, `fix`, `re-verify`, or `score` |
| `ATTEMPT_RESULT_RETURNED` | `<producer-phase>/running` | `<producer-phase>/review-pending` | unchanged; producer/scoring result requires synthesis before phase advancement |
| `LANE_RESULT_RECORDED_ACTIVE` | `<lane-phase>/running` | `<lane-phase>/running` | record one lane result while at least one other required lane attempt remains active |
| `LANE_RESULT_RECORDED_PENDING` | `<lane-phase>/running` | `<lane-phase>/queued` | record one lane result when no attempt remains active but another required lane still needs launch |
| `REQUIRED_LANES_RETURNED` | `<lane-phase>/running` | `<lane-phase>/review-pending` | final required lane returned; no required lane remains active or unlaunched |
| `CLOSE_JUDGMENT_REQUESTED` | `close/queued` | `close/review-pending` | unchanged |
| `CLOSE_RETRY_REQUESTED` | `close/blocked` | `close/queued` | close-specific recovery; never enters `close/running` |
| `SECTION_BLOCKED_FROM_QUEUED` | `<active-phase>/queued` | `<active-phase>/blocked` | preserve current phase |
| `SECTION_BLOCKED_FROM_RUNNING` | `<work-phase>/running` | `<work-phase>/blocked` | preserve current phase |
| `SECTION_BLOCKED_FROM_REVIEW` | `<active-phase>/review-pending` | `<active-phase>/blocked` | preserve current phase |
| `SECTION_FAILED_FROM_QUEUED` | `<work-phase>/queued` | `<work-phase>/failed` | preserve current phase |
| `SECTION_FAILED_FROM_RUNNING` | `<work-phase>/running` | `<work-phase>/failed` | preserve current phase |
| `PLAN_STOPPED` | `plan/queued` | `plan/stopped` | preserve planning phase when the user chooses Stop before dispatch |
| `SECTION_STOPPED_FROM_QUEUED` | `<active-phase>/queued` | `<active-phase>/stopped` | preserve current phase before an attempt starts |
| `SECTION_STOPPED_FROM_RUNNING` | `<work-phase>/running` | `<work-phase>/stopped` | preserve current phase |
| `SECTION_STOPPED_FROM_REVIEW` | `<active-phase>/review-pending` | `<active-phase>/stopped` | preserve current phase |
| `SECTION_STOPPED_FROM_BLOCKED` | `<active-phase>/blocked` | `<active-phase>/stopped` | preserve current phase |
| `SECTION_STOPPED_FROM_FAILED` | `<work-phase>/failed` | `<work-phase>/stopped` | preserve current phase after the human chooses not to retry |
| `RETRY_BLOCKED` | `<work-phase>/blocked` | `<work-phase>/running` | preserve phase and rotate attempt identity as required |
| `RETRY_FAILED` | `<work-phase>/failed` | `<work-phase>/running` | preserve phase and rotate attempt identity as required |
| `REVISION_REQUESTED_FROM_REVIEW` | `<active-phase>/review-pending` | `<active-phase>/blocked` | preserve phase, set round plan to revising, freeze new dispatch, and set next action to regenerate the plan |
| `REVISION_REQUESTED_FROM_BLOCKED` | `<active-phase>/blocked` | `<active-phase>/blocked` | preserve phase and blocked state, set round plan to revising, freeze new dispatch, and set next action to regenerate the plan |

The implementation contract may add narrower event names, but aliases must map
to one canonical event before validation and persistence.

## Existing Controller Event Crosswalk

Lifecycle-aware sections must not apply the legacy transition table directly.
They first normalize existing inputs into the lifecycle event model:

| Existing input | Lifecycle-aware handling |
|---|---|
| worker `DONE` or `DONE_WITH_CONCERNS` in `execute/running` | append `ATTEMPT_RESULT_RETURNED` to reach `execute/review-pending`; orchestrator acceptance separately emits `EXECUTION_RESULT_ACCEPTED` |
| worker `DONE` or `DONE_WITH_CONCERNS` in `fix/running` | append `ATTEMPT_RESULT_RETURNED` to reach `fix/review-pending`; orchestrator acceptance separately emits `FIX_RESULT_ACCEPTED` |
| `NEEDS_CONTEXT` or `BLOCKED` | append the exact `SECTION_BLOCKED_*` event and preserve phase |
| `FAILED` | append the exact `SECTION_FAILED_*` event and preserve phase |
| verifier or reviewer lane outcome returned from a lane phase | persist the lane result, then emit exactly one of `LANE_RESULT_RECORDED_ACTIVE`, `LANE_RESULT_RECORDED_PENDING`, or `REQUIRED_LANES_RETURNED` from the aggregate lane state |
| reviewer outcome `PASS` after return normalization | preserve `review/review-pending` until required lanes and synthesis finish, then emit `REVIEW_ACCEPTED_NO_REMEDIATION` |
| reviewer outcome `REJECT` after return normalization | preserve findings in `review/review-pending`; emit `REVIEW_ACCEPTED_FOR_REMEDIATION` only after remediation is authorized, otherwise block in `review` |
| `SYNTHESIS_COMPLETE` | remain `review/review-pending` when human judgment is required; otherwise emit the applicable review acceptance event |
| human `APPROVE` during `review` | emit the applicable review acceptance event; never set section `runtime_state: complete` |
| human `APPROVE` during `close/review-pending` | emit `CLOSE_APPROVED` and only then set `runtime_state: complete` |
| human `REVISE` from `review-pending` or `blocked` | append the matching `REVISION_REQUESTED_*` event, freeze dispatch, and follow existing plan regeneration and reapproval rules |
| human `STOP` or controller `RETRY` | use existing stop/retry authority plus the exact state-only lifecycle event; close retries use `CLOSE_RETRY_REQUESTED` and never `close/running` |

The old `DONE -> review-pending or complete` and
`APPROVE -> runtime_state: complete` rules remain valid only for legacy sections
that have not adopted the lifecycle-aware schema. Once a section is upgraded,
this crosswalk is mandatory and direct completion outside `close` is invalid.

## Multi-Lane Phase Aggregation

`verify`, `review`, and `re-verify` are section-level aggregate phases. Individual
lane attempts do not own section `runtime_state`.

For every lane return, the orchestrator first closes the matching active attempt
and persists its immutable target and outcome. It then computes:

- `active_required_lanes`: required lanes with an active attempt
- `pending_required_lanes`: required lanes not launched or lacking a terminal
  outcome for the current target revision
- `returned_required_lanes`: required lanes with a terminal outcome for the
  current target revision

The aggregate event is deterministic:

| Aggregate after recording one return | Event | Resulting state and action |
|---|---|---|
| `active_required_lanes` non-empty | `LANE_RESULT_RECORDED_ACTIVE` | remain `running`; `await-active-attempt` |
| no active lanes, `pending_required_lanes` non-empty | `LANE_RESULT_RECORDED_PENDING` | move to `queued`; launch the next required verifier, reviewer, or re-verifier lane |
| no active or pending lanes, all required lanes returned | `REQUIRED_LANES_RETURNED` | move to `review-pending`; synthesize the phase result |

Optional lane returns may append history but cannot make a required lane appear
returned. A stale, superseded, or wrong-target outcome does not enter any of the
three sets. Parallel lane returns are serialized by the orchestrator into one
event sequence; each event re-evaluates the aggregate from the latest persisted
lane records.

Phase advancement events such as `VERIFICATION_ACCEPTED`,
`REVIEW_ACCEPTED_NO_REMEDIATION`, and `REVERIFICATION_ACCEPTED` are legal only
after `REQUIRED_LANES_RETURNED` and phase synthesis have completed.

### Forbidden Transitions

The following are invalid:

- any worker, reviewer, verifier, hook, or packet directly writing
  `lifecycle_phase`
- any phase change without an appended lifecycle event
- `execute -> review` without the required `verify` phase
- `fix -> review` without `re-verify`
- `review -> close` without `score`
- `score -> close` when the score or blocker decision is absent
- `close -> complete` represented as a new phase rather than a runtime-state
  transition
- moving backward from `score` or `close` by editing the snapshot in place
- treating retry, blocked recovery, or human revision as permission to erase
  prior events

If a material plan revision changes the logical work item, existing WorkWork
revision rules apply. The new approved revision establishes new lifecycle events
or a superseding section identity rather than rewriting prior history.

## Snapshot Model

Each lifecycle-aware section runtime ledger adds this current snapshot:

```yaml
lifecycle:
  phase: execute
  phase_entered_at: 2026-06-19T00:00:00Z
  event_head: EVT-LIFECYCLE-DESIGN-001-0002
  next_action:
    code: launch-producer
    detail: launch the approved producer packet
```

The existing section `Runtime State` field remains outside this block and
canonical for operational state. The lifecycle block must not duplicate
`runtime_state`, `section_state`, or `plan_state`.

For event comparison, define the canonical transition projection as:

```yaml
transition_projection:
  lifecycle_phase:
  runtime_state:
  next_action:
    code:
    detail:
```

`event_head` and `phase_entered_at` are snapshot metadata, not members of the
transition projection. `next_action.code` is authoritative and validated;
`next_action.detail` is optional explanatory text and carries no transition
authority.

### Next-Action Derivation

The controller derives `next_action.code` from the exact phase/state pair:

| Exact phase/state | Required action code |
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
| any allowed `<phase>/blocked` | `resolve-blocker` or `regenerate-plan` after an accepted revision request |
| any allowed `<work-phase>/failed` | `decide-retry-or-stop` |
| any allowed `<phase>/stopped` | `none` |
| `close/complete` | `none` |

No other action code is valid. Event definitions may further narrow a code, such
as requiring `regenerate-plan` after `REVISION_REQUESTED_*`. Validators compare
the persisted code to this derivation table; free-text detail cannot make an
otherwise invalid code valid.

Snapshot rules:

- Except for the genesis snapshot defined below, `phase` equals
  `next.lifecycle_phase` of `event_head`.
- `phase_entered_at` equals the transition time of the event that most recently
  changed phase; state-only events do not rewrite it.
- `next_action` must be compatible with the phase/state matrix.
- `event_head` identifies the newest accepted event for the section.
- An event's `previous` projection must equal the pre-update snapshot projection.
- After persistence, the snapshot projection must equal the event's `next`
  projection, `event_head` must equal the event ID, and `phase_entered_at` changes
  only when the event changes phase.
- Event append plus projection and metadata updates form one logical controller
  update; a persisted mismatch blocks further dispatch.

Genesis exception:

- allowed only for a newly created `task-runtime-v1` section before its dispatch
  plan is approved
- exact snapshot is `plan/queued`, `event_head: null`, and
  `next_action.code: await-plan-approval`
- lifecycle event history must be empty
- the first accepted event must be `PLAN_APPROVED` with sequence `1`
- any other null event head is invalid

## Lifecycle Event Schema

Each section owns an append-only lifecycle event list. Every event records:

```yaml
- event_id: EVT-LIFECYCLE-DESIGN-001-0001
  sequence: 1
  section_id: LIFECYCLE-DESIGN-001
  event_type: PLAN_APPROVED
  occurred_at: 2026-06-19T00:00:00Z
  actor:
    runtime_role: orchestrator
    persona_id: pm-orchestrator
    execution_id: null
  causation:
    dispatch_revision: 1
    previous_event_id: null
  previous:
    lifecycle_phase: plan
    runtime_state: queued
    next_action:
      code: await-plan-approval
      detail: dispatch revision requires human approval
  next:
    lifecycle_phase: execute
    runtime_state: queued
    next_action:
      code: launch-producer
      detail: launch the approved producer packet
  artifact_refs: []
  evidence_refs: []
  guard_results: []
  rationale: dispatch revision 1 received explicit human approval
```

Required semantics:

- `event_id` is unique within the round and stable after persistence.
- `sequence` is monotonic and contiguous per section.
- `previous_event_id` equals the preceding accepted event for the section.
- `previous` must exactly match the current persisted transition projection
  before the event.
- `next` must be a valid phase/state combination and legal transition.
- `actor.runtime_role` records who supplied transition authority; phase-changing
  events require `orchestrator`.
- `execution_id` is required when an execution result caused the event and null
  for pure planning or human-decision transitions.
- `artifact_refs`, `evidence_refs`, and `guard_results` may be empty only when the
  event type does not require them under the later owning contract.
- `rationale` explains decisions and exceptions; it may not replace required
  structured evidence.

Events are append-only. The first adoption layer does not define automatic
reconciliation or supersession events. If accepted history and the snapshot
disagree, the controller blocks and requires human `Revise`; the revised
dispatch artifact preserves the inconsistent prior revision as history rather
than editing accepted events in place.

## Snapshot And Event Update Procedure

The future controller implementation must process one transition as a single
logical update:

1. load and normalize the current section snapshot
2. verify that `event_head` matches the final accepted event
3. validate actor authority
4. validate the requested event against the transition table
5. validate the proposed phase/state pair
6. validate required artifact, evidence, and guard references
7. allocate the next event sequence and stable event ID
8. append the event
9. update the transition projection, `event_head`, `phase_entered_at` when the
   phase changed, and existing `runtime_state`
10. persist the updated dispatch plan
11. re-read or validate the persisted snapshot/event agreement before dispatch

The contract does not require full event sourcing. Resume reads the current
snapshot first and uses events to validate and explain it. Validators may replay
events for consistency checks, but runtime operation need not rebuild all state
on every load.

## Round Rollup

The round must not own a writable `lifecycle_phase`. Concurrent sections may be
in different phases.

A round may expose a derived informational rollup:

```yaml
round_lifecycle_rollup:
  active_required_phases:
    - execute
    - review
  required_section_counts:
    execute: 1
    review: 1
    close: 0
  blocked_required_sections: []
  next_required_gate: review completion
```

Rollup rules:

- derive only from required section snapshots and current runtime states
- sort phase lists by canonical phase order
- never use the rollup as packet, transition, or closure authority
- if persisted as a cache, mark it derived and require recomputation validation
- prohibit a single manually writable round `lifecycle_phase`

Existing `plan_state` aggregation remains authoritative for round approval and
completion. For `task-runtime-v1`, a round cannot become `completed` until every
required section is `lifecycle_phase: close` with `runtime_state: complete` and
`next_action.code: none`. A `legacy` round continues to use the existing
`plan_state` aggregation contract and is not required to carry lifecycle fields.

## Rollup And Recovery

On resume, the orchestrator performs:

1. normalize the dispatch schema
2. load each required section's lifecycle snapshot and existing runtime state
3. find the final accepted event for each section
4. verify event head, sequence, previous snapshot, and current snapshot agreement
5. verify the phase/state compatibility matrix
6. reconcile active execution and attempt identities using existing controller
   rules
7. block sections with unknown active attempts until reconciliation completes
8. recompute the derived round lifecycle rollup
9. resume only from persisted `next_action`

Recovery must not replay completed artifact writes merely because the runtime was
interrupted. If the snapshot and event history disagree, new packet creation and
phase advancement halt. The orchestrator records a reconciliation requirement
and returns to human revision when the discrepancy cannot be resolved from
durable evidence.

## Schema Compatibility And Migration

Adopting required lifecycle fields changes the persisted dispatch schema and
therefore requires a coordinated schema-version increment in the implementation
round. The implementation round must assign the concrete next version based on
the repository's version at that time and update normalization rules atomically.

Legacy rules:

- historical completed or stopped artifacts remain readable and are not
  rewritten merely to add lifecycle fields
- an active legacy round must normalize and persist an upgraded lifecycle
  snapshot plus bootstrap event before any new packet or transition
- `runtime_state: review-pending` maps to `review` only when formal verification
  evidence exists for the same immutable target revision and durable review
  records identify the active target; without matching verification evidence,
  map to `verify/queued` when the target is stable, otherwise halt for revision
- `runtime_state: running` is not directly migratable; the legacy controller
  must first reconcile every active or late attempt to a durable non-running
  state under the legacy protocol, then request an approved migration revision
- `runtime_state: queued` maps to `plan` before approval and `execute` after
  approval when no later durable stage exists
- `blocked` and `failed` preserve the last phase derivable from active
  execution, attempt, review, or result records
- if an active artifact cannot be normalized without guessing its phase, halt
  launch and require revision rather than inventing a phase

The first persisted lifecycle event for an upgraded active section is:

```yaml
event_type: LEGACY_LIFECYCLE_BOOTSTRAPPED
sequence: 1
previous_event_id: null
previous:
  lifecycle_phase: null
  runtime_state: <existing runtime state>
  next_action:
    code: legacy-unmapped
    detail: <existing next action as non-authoritative context>
next:
  lifecycle_phase: <deterministically derived phase>
  runtime_state: <destination runtime state from the bootstrap transition table>
  next_action:
    code: <derived code for the normalized phase/state pair>
    detail: <normalized non-authoritative explanation>
```

Only the orchestrator may write this event. Its evidence references identify the
legacy execution, attempt, review, approval, or result records used to derive the
phase. The upgraded snapshot and bootstrap event must be persisted under the new
schema and pass validation before packet creation. In-memory normalization alone
never authorizes launch.

`legacy-unmapped` is valid only inside the `previous` projection of
`LEGACY_LIFECYCLE_BOOTSTRAPPED`. It may never appear in a persisted current
snapshot or in the event's `next` projection.

Bootstrap normalization may change `runtime_state` when the exact destination
table requires a safer state. In particular, legacy `review-pending` without
matching formal verification becomes `verify/queued`; the event preserves the
legacy state only in `previous.runtime_state` and records the normalized state in
`next.runtime_state`.

### Bootstrap Transition Contract

`LEGACY_LIFECYCLE_BOOTSTRAPPED` is the only event allowed to change
one section from lifecycle-absent to lifecycle-aware as part of the round-atomic
protocol migration. No individual section event may switch the round protocol by
itself. Its exact source contract is:

```yaml
lifecycle_protocol: legacy
lifecycle_snapshot: absent
lifecycle_event_history: absent
active_agent_id: null
active_attempt_id: null
pending_late_results: []
```

It requires an approved migration revision, complete protocol capabilities, and
durable evidence sufficient to select exactly one destination. Destination
selection uses this strict algorithm:

1. reject migration when any required section is `running`, `complete`, or
   `stopped`
2. when source state is `blocked`, preserve the evidence-derived active phase and
   choose `<active-phase>/blocked`; do not evaluate milestone rows
3. when source state is `failed`, preserve the evidence-derived work phase and
   choose `<work-phase>/failed`; do not evaluate milestone rows
4. for only `queued` or `review-pending`, select the furthest fully satisfied
   durable milestone in the ordered table below
5. if evidence satisfies zero rows or more than one row at the same milestone,
   halt for human revision

Every milestone row includes the implicit condition that no later milestone is
fully satisfied. Milestones are cumulative: a later milestone is satisfied only
when every earlier mandatory gate for the same current target or repaired target
lineage has matching durable evidence. Legacy labels such as "reviewed" or
"scored" never substitute for missing formal verification.

| Legacy evidence and state | Exact destination |
|---|---|
| source is `blocked` with one evidence-derived active phase | `task-runtime-v1`, `<active-phase>/blocked`, `resolve-blocker` |
| source is `failed` with one evidence-derived work phase | `task-runtime-v1`, `<work-phase>/failed`, `decide-retry-or-stop` |
| matching formal verification and complete required review evidence for the current target, no remediation outstanding, and an accepted score for that evidence set awaiting final judgment | `task-runtime-v1`, `close/queued`, `request-close-judgment` |
| matching formal verification and complete required review evidence for the current target, no remediation required, and no accepted score | `task-runtime-v1`, `score/queued`, `compute-score` |
| accepted repaired result in a lineage whose pre-fix target had matching formal verification and complete required review evidence, but the repaired target lacks matching re-verification | `task-runtime-v1`, `re-verify/queued`, `launch-re-verifier` |
| matching formal verification and complete required review evidence for the current target with accepted remediation required | `task-runtime-v1`, `fix/queued`, `launch-fix` |
| matching formal verification and all required reviewer lanes returned for the same target, with synthesis pending | `task-runtime-v1`, `review/review-pending`, `synthesize-review-return` |
| matching formal verification but any required reviewer lane is unlaunched, active, stale, or missing a terminal outcome for the same target | `task-runtime-v1`, `review/queued`, `launch-reviewer` |
| stable producer result with no matching formal verification | `task-runtime-v1`, `verify/queued`, `launch-verifier` |
| unapproved plan and `runtime_state: queued` | `task-runtime-v1`, `plan/queued`, `await-plan-approval` |
| approved plan, no accepted producer result, and `runtime_state: queued` | `task-runtime-v1`, `execute/queued`, `launch-producer` |

For any non-blocked, non-failed source with a stable current target but no
matching formal verification, `verify/queued` takes precedence over every
legacy review, score, or close marker. Those later markers are treated as stale
context until task-runtime verification and downstream evidence are rebuilt.

The event actor must be the orchestrator. Its `previous` projection uses
`lifecycle_phase: null` and `next_action.code: legacy-unmapped`; its `next`
projection must exactly match one row above. The event receives sequence `1`, a
null `previous_event_id`, and evidence references proving the selected row.

All required-section bootstrap events are prepared against the same source plan
revision and source hash recorded by the migration manifest. The controller
persists the destination schema, round `lifecycle_protocol: task-runtime-v1`,
migration manifest, all required-section bootstrap events, and all corresponding
snapshots together. Post-write validation must succeed for the complete set
before dispatch resumes.

Legacy `running` state is not migratable because it implies active or
unreconciled work. A round containing any required section in terminal
`complete` or `stopped` remains on the legacy protocol through closure; terminal
sections are not backfilled merely to migrate other sections. Any source that
matches zero or multiple destinations halts for human revision.

Bootstrap into `review` requires a matching formal verification evidence
reference. Legacy review alone never proves verification. If the runtime cannot
produce a legal bootstrap snapshot under the activated `task-runtime-v1`
capability set, it must remain `legacy` or require human revision.

Normalization is an in-memory compatibility step until the artifact is revised
or written under the new schema. Mixed normalized schema versions inside one
active round remain invalid under the existing WorkWork contract.

## Integration Boundaries For Later Rounds

This foundation deliberately leaves these details to their owning rounds:

- verifier runtime role, identity separation, and verification evidence schema
- worker, reviewer, and verifier lane mappings
- model capability profiles and fallback policy
- named transition guards and hook result schemas
- repair-cycle limits and no-improvement policy
- finding severity and stale-target invalidation
- score components, thresholds, blockers, and exception closure
- validator rule IDs and negative fixtures

Later designs may populate `artifact_refs`, `evidence_refs`, and `guard_results`
or strengthen transition preconditions. They may not add a second phase owner,
allow a skipped canonical phase, redefine `runtime_state: complete`, or make a
round rollup authoritative.

## Invalid-State Examples

The future implementation and validator rounds must reject at least:

- `lifecycle_phase: execute` with `runtime_state: complete`
- `lifecycle_phase: plan` with `runtime_state: review-pending`
- `lifecycle_phase: plan` with `runtime_state: running`, `blocked`, or `failed`
- `lifecycle_phase: close` with `runtime_state: complete` and a non-empty
  `next_action`
- `lifecycle_phase: close` with `runtime_state: running` or `failed`
- phase transition by a non-orchestrator actor
- phase change with no appended event
- event sequence gap or duplicate event ID
- event `previous` snapshot that differs from the persisted current head
- lifecycle snapshot whose phase differs from its event head
- null lifecycle event head outside the exact genesis exception
- multi-section migration whose bootstrap events reference different source
  revisions or hashes
- partial persistence of a protocol switch or required-section bootstrap set
- lifecycle-aware execution while `lifecycle_protocol: legacy`
- `lifecycle_protocol: task-runtime-v1` before all mandatory phase capabilities
  are available
- `next_action.code` that does not match the phase/state derivation table
- `fix -> review` without `re-verify`
- `review -> close` without `score`
- a writable round-level `lifecycle_phase`
- active legacy dispatch whose phase cannot be normalized without guessing

## Acceptance Criteria

- The design preserves `runtime_state` as the canonical section execution state.
- The design defines one section-owned canonical `lifecycle_phase` vocabulary.
- Lifecycle schema support can land dormant without activating an incomplete
  phase machine.
- `task-runtime-v1` activation is explicit and requires all mandatory phase
  capabilities.
- Intermediate phase completion uses events rather than
  `runtime_state: complete`.
- Every phase and runtime-state combination is explicitly valid or invalid.
- Every forward phase transition has one canonical event and prerequisite.
- State-only block, fail, stop, retry, review-wait, and close-wait events are
  distinguished from phase changes.
- Reviewer `PASS` and `REJECT` returns deterministically enter
  the multi-lane aggregate, and only the final required lane return enters
  `review/review-pending` before outcome processing.
- Close judgment and close retry never enter `close/running`.
- Human revision from review-pending or blocked has an exact persisted event.
- Only the orchestrator may authorize and persist a phase change.
- The current snapshot references one immutable append-only event head.
- Event identity, ordering, causation, previous/next snapshots, and evidence
  reference semantics are implementation-ready.
- Round lifecycle information is derived and cannot become a competing authority.
- Multi-section protocol migration is round-atomic and uses one immutable source
  snapshot for all required-section bootstraps.
- Recovery detects snapshot/event disagreement and halts unsafe continuation.
- Every persisted `next_action.code` is deterministically derived and testable.
- Active legacy rounds normalize deterministically or require revision.
- Historical terminal artifacts do not require backfill.
- Later verifier, hook, repair, scoring, validator, and implementation details
  remain explicitly out of scope.

## Out Of Scope

- editing `SKILL.md`, templates, packet contracts, prompts, or README
- assigning the concrete next schema version
- implementing controller code or validators
- adding verifier personas or `runtime_role: verifier`
- adding worker, reviewer, or verifier lane mappings
- defining model capability profiles
- defining hook predicates beyond lifecycle event integration points
- defining quality scores, thresholds, blockers, or exception terminal states
- writing an implementation plan
