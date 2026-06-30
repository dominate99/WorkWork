# Design Spec: Task Runtime V1 Activation Readiness Audit

## Artifact Metadata

- `schema_version`: 1
- `spec_status`: approved
- `case_slug`: task-runtime
- `round_slug`: 2026-06-27-workwork-task-runtime-v1-activation-readiness-audit
- `created_at`: 2026-06-27
- `updated_at`: 2026-06-28
- `source_dispatch_plan`: `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/dispatch-plan.md`
- `primary_lifecycle_reference`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
- `primary_verification_reference`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`

## Summary

WorkWork is not ready to activate `task-runtime-v1`.

The lifecycle and verifier/lane authority foundations are strong enough for the current dormant stage. They define the phase vocabulary, protocol boundary, state ownership, verifier authority, verification lane schema, target identity, evidence freshness, model capability floors, and legacy non-authority rules. The existing validators also protect key dormant surfaces.

That is not the same as activation readiness. Real activation still lacks several mandatory capabilities named by the lifecycle boundary: review progression and stale-target handling as runtime behavior, repair authorization and re-verification, score production and blocker evaluation, close-gate handling and final human judgment, verifier runtime binding, command execution, packet assembly for verifier lanes, and end-to-end dogfood evidence.

Recommendation: the next round should be design, not implementation foundation or dogfood. The highest-value next round is a missing-capability design that defines dormant contracts for internal hooks, quality gates/scoring, repair authorization/re-verification, close gates, and final human judgment before any activation implementation begins.

## Audit Scope

This audit classified readiness across:

- `lifecycle_phase` authority
- verifier lane authority
- internal hooks
- quality gates
- worker/reviewer/verifier isolation
- packet assembly
- evidence freshness
- close gates
- dormant contract sufficiency
- missing contract, validator, runtime behavior, and dogfood evidence

Out of scope:

- activating `task-runtime-v1`
- modifying validators, runtime code, templates, packet contract, README, or SKILL
- adding verifier personas or runtime bindings
- implementing hooks, repair, scoring, close gates, command execution, routing, or packet assembly
- converting any active or historical round to `task-runtime-v1`

## Readiness Matrix

| Surface | Current Evidence | Classification | Activation Gap |
|---|---|---|---|
| Lifecycle protocol boundary | `task-runtime-lifecycle.md` defines `legacy` vs `task-runtime-v1`, activation boundary, phase vocabulary, state ownership, snapshots, events, migration, recovery, and invalid states. | Sufficient dormant contract | Needs activation validators and runtime controller behavior before selection is allowed. |
| `lifecycle_phase` authority | Contract says only the orchestrator advances phase through accepted events, and `runtime_state: complete` is valid only in `close`. | Sufficient dormant semantics | No validator/runtime yet proves phase-state compatibility, event head integrity, legal transitions, or no non-orchestrator phase changes in active rounds. |
| Verifier lane authority | `task-runtime-verification.md` defines verifier role authority, lane schema, target identity, evidence requirements, freshness, capability profiles, floors, and model resolution. | Sufficient dormant contract | No verifier binding, launch path, command execution, evidence acceptance runtime, or semantic validator for active evidence. |
| Dormant verifier validator | `validate_ww_verifier_authority_contracts.py` protects reference linkage, template fields, legacy non-authority, packet dormant fields, and repo-suite integration. | Sufficient dormant sentinel | Not a semantic activation validator; it does not validate actual verifier lanes, evidence bundles, identity isolation, freshness, or model resolution records. |
| Worker/reviewer/verifier isolation | Verification reference defines pairwise distinct authority subjects and prohibits verifier mutation, repair, scoring, and close approval. | Sufficient design baseline | No runtime binding or packet assembly enforces distinct agent/execution/attempt IDs for real `task-runtime-v1` target lineages. |
| Packet assembly | Packet contract requires `source_lifecycle_snapshot` for future `task-runtime-v1` packets and dormant verifier packet fields. Existing packet validation covers legacy worker/reviewer packet identities. | Partially sufficient | No active verifier packet generator, no verifier prompt binding, no lifecycle snapshot copy test for active packets, and no acceptance path for verifier evidence. |
| Evidence freshness | Verification reference defines frozen target refs, applicability records, stale/wrong-target/conflicted/superseded states, and current accepted `PASS` requirements. | Sufficient dormant semantics | No implementation captures evidence, computes freshness, rejects stale evidence, or blocks scoring/close from stale or wrong-target bundles. |
| Internal hooks | The lifecycle foundation names that current implementation does not add hooks. User design calls for BeforeReview, AfterReview, BeforeClose, OnBlocked, and OnCompactRisk style hooks. | Missing design | Need a dormant hook contract before implementation: hook names, trigger moments, guard inputs, allowed writes, blocker semantics, checkpoint rules, and interaction with lifecycle events. |
| Quality gates and scoring | Lifecycle contract requires score production and blocker evaluation before close. User design proposes score thresholds and blockers. | Missing design | Need a quality gate contract defining score record shape, blocker classes, threshold semantics, lane evidence aggregation, task-profile gates, and who may accept/override results. |
| Repair and re-verification | Lifecycle contract includes `fix` and `re-verify`, and verification contract says repaired targets need fresh formal verification. | Missing design | Need repair authorization rules, finding-to-repair mapping, repair attempt ownership, stale review handling, re-verification target lineage, and how fixes re-enter review/score. |
| Review progression and stale-target handling | Lifecycle and verification references require same-target lane aggregation and stale target rejection. | Partially designed | Need explicit review lane progression contract for required reviewer coverage, stale reviewer targets, finding disposition, and remediation vs no-remediation synthesis. |
| Close gates and final human judgment | Lifecycle contract requires `SCORE_ACCEPTED` before `close/queued` and `CLOSE_APPROVED` before `close/complete`. | Missing design | Need close-gate contract for required verification evidence, reviewer coverage, unresolved critical findings, score thresholds, blocker override limits, and final human decision records. |
| Runtime activation behavior | Current SKILL says ordinary rounds remain `legacy` and contracts/templates alone are insufficient activation evidence. | Correctly blocked | Need controller implementation for lifecycle transitions, verifier launches, hooks, scoring, repair loops, close gates, resume/recovery, and migration. |
| Dogfood evidence | Prior dogfood audited dormant verifier validator coverage. Current rounds remain legacy. | Insufficient for activation | Need at least one controlled task-runtime pilot after missing contracts and implementation foundations exist; current evidence does not prove end-to-end activation. |

## Sufficient Dormant Surfaces

The following surfaces are strong enough to remain unchanged before the next design round:

- The protocol discriminator: `Lifecycle Protocol: legacy | task-runtime-v1`.
- The canonical phase vocabulary: `plan -> execute -> verify -> review -> fix -> re-verify -> score -> close`.
- The rule that `lifecycle_phase` does not replace `runtime_state`.
- The orchestrator-only phase-change authority.
- Snapshot plus append-only lifecycle event persistence.
- The activation boundary that forbids selecting `task-runtime-v1` until mandatory capabilities are implemented, verified end to end, and approved.
- The verifier authority boundary: verifier may inspect and produce bounded evidence, but may not mutate, repair, review, score, or approve close.
- Frozen verification target identity and evidence freshness/applicability semantics.
- Model capability profile, floor, and resolution concepts.
- The active legacy packet role gate that excludes verifier packets until a later approved binding exists.
- Dormant verifier authority validator coverage for current reference/template/linkage drift.

These are contract scaffolds. They should not be relaxed, but they also should not be mistaken for runtime readiness.

## Blocking Activation Gaps

### Gap 1: Internal Hooks Are Named But Not Contracted

The user design requires workflow-internal hooks such as worker-return checks, review preconditions, review finding recording, close preflight, blocked recovery notes, and compaction-risk checkpointing. Current lifecycle text explicitly says hooks are not implemented, and there is no dormant hook reference.

Activation risk: without hook semantics, `task-runtime-v1` cannot reliably know when to freeze targets, checkpoint state, prevent premature close, or persist recovery instructions.

Needed next: a dormant internal hook contract.

### Gap 2: Quality Gate And Score Semantics Are Missing

The lifecycle contract requires `SCORE_ACCEPTED` before close, but no contract defines score inputs, blocker classes, score thresholds, lane weighting, required verification evidence, or override rules.

Activation risk: the runtime could move to `close` with a score record that is arbitrary, incomplete, or not tied to accepted lane evidence.

Needed next: a quality gate and score contract.

### Gap 3: Repair Authorization And Re-Verification Need Their Own Contract

The lifecycle contract defines `fix` and `re-verify`, while the verification contract says stale pre-fix evidence cannot satisfy re-verification. It does not define who authorizes repair, how findings map to repair tasks, how repaired targets are frozen, or when review must repeat.

Activation risk: a future controller could repair without authority, skip re-verification, or reuse stale verifier/reviewer evidence.

Needed next: a repair and re-verification contract.

### Gap 4: Close Gates And Final Human Judgment Are Not Yet Concrete

The lifecycle contract says close requires gate handling and final human judgment, but the close preconditions are not yet operationally specified.

Activation risk: the orchestrator could complete a section without current verification, required review coverage, accepted score, blocker disposition, or explicit close judgment.

Needed next: a close-gate and final judgment contract.

### Gap 5: Verifier Runtime Binding And Command Execution Are Absent

Verifier authority is well specified as dormant contract, but there is no launchable verifier runtime role, no verifier persona binding, no command execution contract implementation, and no accepted evidence bundle path.

Activation risk: `verify` and `re-verify` phases would be unlaunchable or would rely on legacy self-checks/reviewer findings that the contract explicitly rejects as formal evidence.

Needed later: implementation foundation after missing contract design is approved.

### Gap 6: Activation Validators Do Not Exist

Current validators protect legacy lifecycle surfaces and dormant verifier authority references. They do not validate active `task-runtime-v1` lifecycle snapshots, event sequences, phase/runtime compatibility, verifier evidence, model resolution, hook records, score records, close gates, or migration manifests.

Activation risk: malformed active runtime artifacts could pass repo validation.

Needed later: validator expansion after the missing contract shapes are settled.

### Gap 7: End-To-End Dogfood Evidence Is Not Yet Possible

Existing dogfood rounds prove pieces of the contract/validator story, not a complete lifecycle run. Because hooks, repair, scoring, close gates, verifier binding, command execution, and activation validators are absent, a meaningful `task-runtime-v1` dogfood pilot would be premature.

Activation risk: dogfood would either stay legacy or simulate important controller behavior in prose.

Needed later: dogfood only after implementation foundation and validators exist.

## Validator Gap Classification

Activation-time validators should eventually cover at least:

- `task-runtime-v1` selected only when activation prerequisites are marked available by approved contract/runtime evidence.
- No lifecycle snapshot or event history appears under `legacy`.
- Every required section under `task-runtime-v1` has a current lifecycle snapshot and append-only event history.
- Snapshot/event head, sequence, previous projection, and next projection agree.
- Phase/runtime combinations are legal.
- Phase changes are authored by the orchestrator and backed by a legal event.
- Verifier lane records are structurally valid and do not own `runtime_state` or `lifecycle_phase`.
- Required verifier lanes have accepted current `PASS` evidence before verification acceptance.
- Stale, wrong-target, conflicted, skipped, blocked, failed, below-floor, or superseded evidence does not authorize verification, scoring, or close.
- Worker, reviewer, verifier, and orchestrator authority subjects are isolated for one target lineage.
- Score records include blocker evaluation and satisfy the declared quality gate.
- Close records include required verification, review coverage, score, blocker disposition, and final human judgment.
- Repair records are authorized and force fresh re-verification before returning to review/score/close.
- Migration from legacy is atomic and never guesses phase.

These validators should not be implemented before the hook, score, repair, and close-gate contracts define their record shapes.

## Runtime Behavior Gap Classification

Real activation requires controller behavior for:

- protocol selection and migration safety checks
- phase launch and transition control
- target freezing
- verifier lane resolution and launch
- command execution and result capture
- evidence applicability and freshness decisions
- review lane aggregation and stale-target rejection
- finding disposition and repair authorization
- repair execution and re-verification routing
- score calculation and blocker evaluation
- close-gate synthesis and final judgment request
- checkpointing before long phases and after phase transitions
- resume/recovery from snapshots and event history

None of these should be inferred from current templates alone.

## Dogfood Gap Classification

Future dogfood should happen in this order:

1. Contract dogfood: create sample `task-runtime-v1` lifecycle, hook, score, repair, close, and verifier evidence records without activating runtime behavior.
2. Validator dogfood: prove validators catch malformed records and accept valid minimal fixtures.
3. Packet assembly dogfood: assemble worker, verifier, and reviewer packets from one frozen target lineage with distinct identities.
4. Runtime pilot: run a tiny controlled task through `plan -> execute -> verify -> review -> score -> close`, then a second task with `fix -> re-verify`.
5. Migration dogfood: migrate one eligible legacy round only after runtime pilot succeeds.

The current repository is not yet at step 1 for hooks, scoring, repair, or close gates.

## Next Round Recommendation

Open a design round next.

Recommended round:

`$ww round: task-runtime-v1 missing capability design. Based on the activation readiness audit, design the dormant contracts still required before task-runtime-v1 activation: internal hooks, quality gates/scoring, repair authorization/re-verification, close gates, final human judgment, and their relationship to lifecycle events and verifier evidence. Only produce design spec; do not implement activation, validators, personas, runtime bindings, command execution, routing, or packet assembly.`

Why design first:

- The remaining blockers are not just implementation work; several record shapes and authority rules do not exist yet.
- Validators need concrete hook, score, repair, and close-gate schemas before they can be meaningful.
- Dogfood would be artificial until those schemas exist.
- Implementation foundation should wait until the missing-capability design defines what must be persisted and blocked.

## Acceptance Criteria

- Every requested readiness surface is classified.
- The report distinguishes dormant contract sufficiency from activation readiness.
- The report identifies missing design, validator, runtime behavior, and dogfood evidence.
- The recommendation chooses design, implementation foundation, or dogfood as the next round type.
- No validator, active contract, template, packet contract, README, SKILL, persona, routing, project registry, or runtime code is modified.

## Conclusion

WorkWork has a solid dormant foundation for `task-runtime-v1`, especially around lifecycle ownership and verifier authority. It does not yet have enough contract, validator, runtime, or dogfood evidence to activate the protocol.

The next move should be a missing-capability design round for hooks, quality gates, repair/re-verification, close gates, and final human judgment. After that design is approved, WorkWork can move to implementation foundation, validator expansion, contract dogfood, and only then a real runtime pilot.
