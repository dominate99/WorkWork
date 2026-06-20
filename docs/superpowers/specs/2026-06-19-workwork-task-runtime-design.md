# WorkWork Invocation-Scoped Task Runtime Design

## Goal

Evolve WorkWork from a subagent dispatcher into an invocation-scoped task
runtime. A `$ww` or `$www` round should persist and coordinate the complete work
lifecycle:

```text
plan -> execute -> verify -> review -> fix -> re-verify -> score -> close
```

The runtime starts only when the user invokes `$ww` or `$www`. It is not a
daemon, background listener, or continuous process.

## Design Principles

- Persist lifecycle authority in round artifacts rather than chat history.
- Separate production, verification, review, orchestration, and human approval.
- Use one canonical phase owner and one canonical execution-state owner.
- Treat verification and review evidence as revision-bound records.
- Prevent normal closure when required evidence, coverage, or quality is absent.
- Keep automatic repair bounded and return exhausted or stagnant loops to a human.
- Resolve agent models by declared capability instead of hard-coded model names.
- Adopt the runtime incrementally so existing WorkWork state contracts remain
  understandable and testable throughout the migration.

## System Boundary

The task runtime exists only inside an active `$ww` or `$www` round. The
dispatch plan is the durable runtime record. Context compaction, process restart,
or thread resumption must not require reconstructing canonical state from chat.

The design does not introduce:

- an operating-system service
- a repository watcher
- a Git hook framework
- an arbitrary shell-hook plugin system
- silent continuation after a blocking human gate

## Canonical State Model

Each dispatch section owns two orthogonal fields:

```yaml
lifecycle_phase: plan | execute | verify | review | fix | re-verify | score | close
runtime_state: queued | running | review-pending | blocked | complete | failed | stopped
```

`lifecycle_phase` answers what kind of work is currently active.
`runtime_state` answers how that phase is progressing.

Both are canonical at section level. Round-level phase and state are derived from
required sections; the round does not maintain an independent competing phase
machine.

Only the orchestrator may advance `lifecycle_phase`. Workers, reviewers, and
verifiers return results and evidence. Transition guards compute pass or block.
The orchestrator validates those results, persists the event, and updates the
canonical snapshot.

## Lifecycle Flow

The default section flow is:

```text
plan -> execute -> verify -> review
                         |-> no findings -> score -> close
                         `-> findings -> fix -> re-verify -> review
```

The first verification follows `execute`. Any artifact-changing repair follows
`fix -> re-verify`. Review evidence bound to an older target revision cannot
authorize scoring or closure.

Repair is bounded:

- default maximum: two repair cycles
- a task profile may lower the maximum
- a profile may not silently raise the maximum
- two consecutive cycles without measurable improvement block early
- cycle exhaustion enters `runtime_state: blocked` and requires human judgment

After initial dispatch approval, passing guards advance automatically. Human
judgment is required for:

- plan revision
- blocked recovery
- material scope drift
- removal of a required lane
- model fallback below the declared capability floor
- external-state or destructive verification commands
- final close

## Authority Model

### Worker

- produces or modifies artifacts
- performs self-checks
- may not satisfy the formal verification gate for its own output
- may not review or approve its own target

### Verifier

- uses `runtime_role: verifier`
- runs declared verification commands and safe supplemental checks
- binds evidence to artifact path, revision, and content hash
- must use a different `agent_id` and `execution_id` from the worker whose output
  it verifies
- does not modify the target artifact while fulfilling verification authority

### Reviewer

- finds quality, correctness, scope, domain, security, layout, or editorial issues
- records stable findings against target references
- does not modify the review target
- does not advance lifecycle phase or approve closure

### Orchestrator

- selects profiles, lanes, personas, and model capability profiles
- validates transition guards
- persists snapshots and lifecycle events
- aggregates verifier and reviewer evidence
- computes the quality score from persisted outcomes
- requests human decisions at required gates

### Human

- approves the initial dispatch plan and material revisions
- decides blocked recovery
- approves final normal closure
- may accept non-critical score shortfall through an exception path
- may not override hard blockers into normal completion

## Agent Lanes

The dispatch schema separates authority classes:

```yaml
worker_lanes: []
reviewer_lanes: []
verifier_lanes: []
```

Baseline reviewer lanes include:

- `proofread-review`
- `layout-review`
- `domain-review`
- `ops-reliability-review`
- `security-review`
- `code-quality-review`
- `spec-review`

Baseline verifier lanes include:

- `test-verification`
- `artifact-verification`
- `deployment-verification`
- `configuration-verification`

Task profiles supply required baseline lanes. Working-brief risk lenses append
additional lanes. Project personas retain priority only after role and capability
eligibility; built-in personas remain the fallback.

The dispatch plan records why every selected lane applies. It also records why a
plausible risk lane was excluded when that exclusion is material. Users may add
lanes. Removing a profile-required lane is a material revision and requires
reapproval.

## Model Capability Profiles

Persona, runtime role, and model selection are separate concerns:

- persona defines professional judgment and working style
- runtime role defines authority
- model profile defines required execution capability

The dispatch plan stores a capability label such as `deep-review`,
`code-execution`, or `tool-verification`. At launch, the controller resolves the
profile to an available model and records:

- requested model profile
- actual model
- fallback, if any
- fallback rationale
- capability-floor result

Fallback within the declared capability tier is allowed. A fallback below the
minimum capability blocks and requires human approval; it must not happen
silently.

## Internal Transition Guards

First-version internal hooks are named transition guards, not arbitrary scripts.
They evaluate persisted conditions and write pass/block evidence.

Core guards are mandatory:

### `AfterWorkerReturn`

Confirm result artifact existence, revision, write-scope compliance, return
status, and worker self-check evidence.

### `BeforeVerify`

Confirm a stable target, declared verification commands, and verifier identity
separation from the worker.

### `BeforeReview`

Confirm target path, artifact kind, revision, content hash, and required reviewer
coverage.

### `AfterReview`

Persist findings, severity, category, evidence, required action, and target
identity.

### `BeforeClose`

Require completed formal verification, complete required reviewer coverage, no
stale evidence, no hard blocker, and a sufficient quality score.

### `OnBlocked`

Persist blocker identity, recovery prerequisites, safe suggested commands,
next action, and required human decision.

### `OnCompactRisk`

Write a best-effort resume snapshot before long phases, after phase transitions,
and when the runtime exposes a compaction-risk signal. Correct recovery does not
depend on a precise token threshold.

Task profiles may add domain-specific guards but may not remove core guards.
Shell commands belong to verifier `verification_commands`, not hook definitions.

## Verification Commands And Evidence

Planning declares baseline verification commands. A verifier may add safe,
read-only, or local commands when new evidence requires them and must record the
rationale. Commands that modify external state, deploy, migrate, delete, or
perform destructive operations require renewed human approval.

Each command record includes:

- command identity and normalized command
- verifier execution identity
- target artifact revision and hash
- start and finish time
- exit code
- bounded output summary or result artifact reference
- pass, fail, blocked, or skipped disposition
- skip rationale when applicable

Worker self-checks remain useful execution evidence but do not satisfy the
formal verification gate.

## Findings And Stale Evidence

Findings use a stable schema:

```yaml
finding_id:
severity: critical | high | medium | low
category:
target_ref:
evidence:
required_action:
status: open | fixed | accepted-risk | invalid
```

Unresolved critical findings are global blockers. Task profiles may elevate
specific high-severity categories to blockers. Critical findings cannot be
accepted as risk.

Every verification and review result is bound to target path, revision, and
content hash. When `fix` modifies an artifact, overlapping verifier and reviewer
lanes become stale. Required stale lanes must run again before scoring. Aggregate
lanes become stale when any artifact in their declared target set changes.

## Quality Gates

Global thresholds have consistent meaning across profiles:

```yaml
close_threshold: 80
pr_threshold: 90
excellence_threshold: 95
```

Task profiles define component weights, required evidence, and profile-specific
blockers. The orchestrator computes the score mechanically from persisted gate
outcomes. No scoring agent assigns a holistic subjective number.

Example:

```yaml
quality_gate:
  profile: ops-platform
  score: 88
  components:
    verification: 30/30
    reviewer_coverage: 22/25
    correctness: 26/30
    recovery_readiness: 10/15
  blockers: []
```

Hard blockers override the score. At minimum they include:

- missing required verification
- incomplete required reviewer coverage
- unresolved critical finding
- stale required review or verification target

Normal closure requires no hard blocker and `score >= close_threshold`.

A human may accept a non-critical score shortfall. That path ends as
`closed-with-exception`, records the accepted risk, and must not be represented as
normal `completed`. Hard blockers cannot use this exception path.

## Persistence Model

The dispatch plan stores both a current snapshot and append-only events.

Current section snapshot:

```yaml
current:
  lifecycle_phase:
  runtime_state:
  active_execution_id:
  repair_cycle:
  next_action:
  resume_snapshot:
```

Lifecycle event:

```yaml
- event_id:
  event_type:
  occurred_at:
  actor_role:
  persona_id:
  execution_id:
  actual_model:
  previous_phase:
  new_phase:
  previous_state:
  new_state:
  artifact_refs: []
  evidence_refs: []
  guard_results: []
  rationale:
```

The snapshot makes resume efficient. Events explain why the snapshot changed.
The first version does not require rebuilding all state through event sourcing.

## Recovery

On resume, the orchestrator:

1. loads the current snapshot
2. verifies that the latest event agrees with the snapshot
3. reconciles active execution and attempt identities
4. marks unknown interrupted attempts as reconciliation-required
5. checks whether referenced artifact identities changed
6. marks overlapping evidence stale when required
7. resumes from persisted `next_action` without replaying completed writes

`resume_snapshot` is a recovery aid, not a second state authority.

## Incremental Rollout

Each item is a separate `$ww` round:

1. **Task runtime lifecycle foundation design**
   Define phases, states, transitions, authority, and lifecycle events.
2. **Lifecycle foundation implementation**
   Adopt lifecycle fields and event records in active contracts and templates.
3. **Verifier and lane authority design**
   Define verifier permissions, identity isolation, lane schemas, evidence, and
   model capability profiles.
4. **Verifier and lane implementation**
   Add bindings, personas, profile baseline selection, and risk-triggered lanes.
5. **Internal transition guards design**
   Define core guards, blocked recovery, compact checkpoints, and stale evidence.
6. **Internal transition guards implementation**
   Adopt guard records and recovery semantics in active runtime surfaces.
7. **Quality gate and scoring design**
   Define global thresholds, task profiles, weights, findings, blockers, and
   exception closure.
8. **Quality gate and scoring implementation**
   Adopt scoring records, repair limits, close gates, and terminal outcomes.
9. **Runtime validator expansion**
   Validate phases, events, authority separation, lane coverage, guard evidence,
   stale targets, verification records, and quality gates.
10. **End-to-end runtime dogfood pilot**
    Run a real task through the complete lifecycle and classify evidence and gaps.

## Acceptance Criteria

- Every required section exposes one canonical `lifecycle_phase` and one
  canonical `runtime_state`.
- Round-level lifecycle state is derived rather than independently advanced.
- Only the orchestrator advances lifecycle phase.
- Worker, verifier, and reviewer authority is separated and persisted.
- Formal verification uses a different execution identity from artifact production.
- Required lanes derive from task profile plus risk triggers.
- Model capability requirements and actual model resolution are durable.
- Every phase transition emits a stable lifecycle event.
- Core transition guards cannot be removed by a task profile.
- Artifact changes invalidate overlapping review and verification evidence.
- Repair loops are bounded and return exhausted work to a human.
- Quality scores derive from persisted component outcomes.
- Hard blockers prevent normal close regardless of score.
- Non-critical score exceptions are distinguishable from normal completion.
- Restart or context compaction can resume from persisted state and `next_action`.
- No daemon, background watcher, or arbitrary hook scripting is introduced.
