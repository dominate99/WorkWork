# Design Spec: Task Runtime V1 Activation Gate Validator

## Artifact Metadata

- `schema_version`: 1
- `design_status`: approved
- `case_slug`: task-runtime
- `round_slug`: 2026-07-01-task-runtime-v1-activation-gate-validator-design
- `created_at`: 2026-07-01
- `updated_at`: 2026-07-01
- `artifact_type`: validator_design_spec

## Purpose

The activation gate validator is a future repository validator that decides
whether WorkWork has enough contract coverage, runtime behavior, dogfood
evidence, and legacy non-authority protection to start a separate
`task-runtime-v1` activation round.

It must not activate `task-runtime-v1` by itself. Passing the activation gate
only means the repository is eligible to ask for an activation round. The
activation round still needs explicit human approval and its own migration or
runtime-change plan.

## Non-Goals

- Do not replace the existing lifecycle, verifier/lane authority,
  missing-capability, persona, packet, case, or repo validators.
- Do not infer runtime behavior from dormant reference text alone.
- Do not permit `task-runtime-v1` selection in ordinary rounds.
- Do not add personas, verifier runtime binding, command execution, routing,
  packet assembly, repair/scoring/hooks, or close-gate runtime behavior.
- Do not weaken legacy non-authority guards.

## Validator Shape

Recommended future file:

```text
tools/validate_ww_task_runtime_activation_gate.py
```

Recommended repo-suite label:

```text
Task runtime activation gate validation
```

The validator should support:

- human output with one PASS/FAIL summary
- `--json` output with `ok`, `rule_failures`, and per-rule `results`
- repo-root override for fixture tests
- deterministic rule IDs prefixed with `WWAG`
- read-only validation only

The validator should run after the existing individual contract validators in
`validate_ww_repo.py`, because it consumes their surfaces conceptually and
should fail closed when a prerequisite suite is absent or failing.

## Gate Model

The activation gate has three tiers.

### Tier 1: Dormant Contract Completeness

These suites must pass:

| Suite | Existing Validator | Required Evidence |
| --- | --- | --- |
| lifecycle authority | `validate_ww_round_lifecycle.py` plus a required future lifecycle-reference linkage validator | current rounds keep lifecycle state in dispatch plans; `case.md` stays navigational; lifecycle reference/SKILL/README/template linkage is explicitly checked before activation |
| verifier/lane authority | `validate_ww_verifier_authority_contracts.py` | verifier reference, SKILL/README/template/packet/working brief linkage, legacy non-authority |
| missing capabilities | `validate_ww_missing_capability_contracts.py` | missing-capability reference, SKILL/README/template/packet/working brief linkage, WWMC007 hardening |
| packet identity | `validate_ww_persona_packets.py` | packet target identity, path containment, prompt binding, worker principle snapshots |
| persona role gates | `validate_ww_persona_selection_contracts.py` and role-contract validators | worker/reviewer role gates, runtime role persistence, reviewer-only separation |
| case and round artifacts | case validators and round lifecycle validator | case/round identity, current round, plan state surfaces |

Activation gate rule: if any prerequisite validator is absent, not registered
in `validate_ww_repo.py`, not JSON-capable where expected, or failing, the gate
fails. This tier proves contract scaffold health only; it is not enough for
activation. The current repository has verifier and missing-capability
reference validators, but lifecycle reference linkage is only partially covered
through SKILL/README guidance and round lifecycle validation; a dedicated
lifecycle-reference linkage validator is therefore an activation prerequisite.

### Tier 2: Runtime Behavior Evidence

The gate must require explicit dogfood or pilot evidence for the capabilities
that the lifecycle contract names as mandatory before activation:

| Capability | Required Evidence Before Activation |
| --- | --- |
| verifier authority and minimum lanes | completed verifier packet or lane pilot showing `runtime_role: verifier` identity, frozen target, evidence bundle, model resolution, and orchestrator acceptance semantics |
| review progression and stale-target handling | dogfood evidence showing stale reviewer or verifier target returns remain history and cannot advance canonical state |
| repair authorization and re-verification | pilot evidence showing accepted finding -> authorized repair -> repaired target -> stale evidence invalidation -> required re-verification |
| score production and blocker evaluation | pilot evidence showing quality gate, score record, blocker evaluation, and blocked/pass outcomes |
| close-gate handling and final human judgment | pilot evidence showing `BeforeClose`, close gate, final judgment package, and human decision without evidence relabeling |
| lifecycle snapshot and events | pilot evidence showing current snapshot plus append-only events, event-head matching, legal phase transitions, and resume/recovery behavior |

Activation gate rule: dormant references and templates count only as design
evidence. A capability is activation-ready only when there is a completed,
approved, and repository-valid dogfood or pilot round proving the behavior.

### Tier 3: Cross-Suite Consistency

The gate must validate the relationships that no single current validator owns.

Required cross-suite checks:

- `lifecycle_phase` authority belongs only to orchestrator-accepted lifecycle
  events.
- `runtime_state` remains the canonical operational state and is not replaced
  by verifier lanes, score records, hooks, checkpoints, or close gates.
- worker, reviewer, verifier, and orchestrator subjects remain isolated for the
  same target lineage.
- verifier evidence is target-bound, freshness-bound, capability-floor checked,
  and accepted only by the orchestrator.
- worker self-checks and reviewer findings are never formal verifier evidence.
- repair invalidates stale target-bound verifier and reviewer evidence.
- close requires current accepted verifier PASS evidence, accepted review
  synthesis, accepted score, passing close gate, and final human judgment.
- legacy rounds still omit active lifecycle snapshots, event histories,
  verifier lane authority, and missing-capability authority records.

Activation gate rule: any missing cross-suite relationship blocks activation
even when every individual dormant contract validator passes.

## Proposed Rule Families

### WWAG001: Prerequisite Suite Inventory

Fail when any required validator file is missing, not called by
`validate_ww_repo.py`, not JSON-capable where applicable, or not represented by
a stable repo-suite label.

Minimum required suite labels:

- `Lifecycle reference contract validation`
- `Round lifecycle contract validation`
- `Verifier/lane authority contract validation`
- `Missing-capability contract validation`
- `Runtime persona packet artifact validation`
- `Persona runtime-selection recording contract validation`
- `Case artifact contract validation`
- `Case-based path identity contract validation`

### WWAG002: Dormant Reference Linkage

Fail when lifecycle, verification, or missing-capability references are absent
from SKILL/README/template/packet/working-brief guidance, or when the activation
gate cannot identify those individual suite results.

This rule should reference the existing validators rather than duplicating all
fragments. For lifecycle linkage, this rule should require either an existing
dedicated lifecycle-reference validator result or fail with a clear activation
prerequisite message.

### WWAG003: Legacy Non-Authority Preservation

Fail when any legacy dispatch plan renders active lifecycle snapshots, event
history, verifier lane authority, evidence/model resolution authority, or
missing-capability authority records.

This rule composes existing legacy guards:

- lifecycle snapshot/event-history absence from lifecycle validator work
- verifier non-authority guard from WWVA007
- missing-capability non-authority guard from WWMC007

The gate should verify that WWMC007's hardened assignment detection remains
present by requiring fixture names or equivalent negative fixture evidence in
the missing-capability test suite.

### WWAG004: Runtime Behavior Evidence Registry

Fail when no completed approved round evidence exists for each mandatory
activation capability.

The validator should look for an explicit activation evidence registry or
manifest rather than scraping prose from arbitrary rounds. Recommended future
manifest:

```text
docs/cases/task-runtime/activation-evidence.yaml
```

Recommended manifest fields:

```yaml
activation_evidence:
  lifecycle_snapshot_events:
    round: <round-slug>
    artifact_refs: []
    validation_commands: []
  verifier_authority:
    round: <round-slug>
    artifact_refs: []
    validation_commands: []
  stale_target_handling:
    round: <round-slug>
    artifact_refs: []
    validation_commands: []
  repair_reverification:
    round: <round-slug>
    artifact_refs: []
    validation_commands: []
  scoring_blockers:
    round: <round-slug>
    artifact_refs: []
    validation_commands: []
  close_gate_final_judgment:
    round: <round-slug>
    artifact_refs: []
    validation_commands: []
```

The activation gate should require every referenced round to be present in the
task-runtime case index, completed, and approved.

### WWAG005: Verifier Evidence Sufficiency

Fail when activation evidence lacks:

- verifier lane records with frozen target identity
- evidence requirements mapped to command, artifact, or environment evidence
- accepted PASS evidence for every required lane
- applicability records proving evidence is current
- wrong-target, stale, blocked, failed, skipped, and below-floor negative
  fixtures or pilot evidence
- model capability profile/floor/resolution records
- explicit worker self-check and reviewer finding non-substitution examples

This rule should not run commands or inspect external systems. It checks that
the future runtime's persisted evidence records and negative fixtures exist and
are validator-covered.

### WWAG006: Close Gate Sufficiency

Fail when activation evidence lacks:

- quality gate profile and hard blocker policy
- score record tied to current target and accepted evidence
- close gate record tied to score, current verifier evidence, review synthesis,
  repair status, and blocker status
- final judgment record that exposes score, blockers, verification summary,
  review summary, and repair summary
- negative fixtures for missing verification, stale review target, unresolved
  non-waivable blocker, and missing final judgment

This rule proves the close path can block false completion.

### WWAG007: Worker/Reviewer/Verifier Isolation

Fail when activation evidence lacks:

- distinct worker, reviewer, verifier, and orchestrator authority subjects for
  one target lineage
- distinct execution IDs and attempt IDs for producer, verifier, and reviewer
  roles
- verifier packet binding to a verifier runtime role only after approved role
  binding exists
- reviewer-only and worker-capability gates preserved
- negative fixture or pilot evidence for identity conflict

This rule proves that one actor cannot modify, verify, review, score, and close
its own work.

### WWAG008: Lifecycle Phase Authority

Fail when activation evidence lacks:

- initial `plan/queued` snapshot
- append-only lifecycle event list
- exact previous-to-next transition projection checks
- legal coverage for the normal path: plan -> execute -> verify -> review ->
  score -> close
- legal coverage for remediation path: review -> fix -> re-verify -> review
- resume/recovery check for event head, sequence, previous snapshot, and
  current snapshot
- negative fixtures for illegal phase completion, non-orchestrator phase
  change, skipped score, and close without final judgment

This rule proves that `lifecycle_phase` has one owner and one vocabulary.

### WWAG009: Activation Decision Boundary

Fail when the repository contains text or templates implying that passing
dormant validators alone activates `task-runtime-v1`.

The design should require wording that passing the activation gate only permits
opening a separate activation round.

## Output Contract

Human output:

```text
PASS: <N> activation gate rules checked
```

or:

```text
FAIL: <N> activation gate rule violations

[WWAG00X] <file-or-manifest>
Section: <section>
<message>
```

JSON output:

```json
{
  "ok": true,
  "rule_failures": 0,
  "results": [
    {
      "rule_id": "WWAG001",
      "passed": true,
      "file": "tools/validate_ww_repo.py",
      "section": "Prerequisite Suite Inventory",
      "message": "ok"
    }
  ]
}
```

Repo-suite wrapper behavior should match the existing child-validator JSON
contract in `validate_ww_repo.py`: a child payload must be an object and must
report `ok: true`, otherwise the aggregate suite fails.

## Fixture Strategy

Future implementation should include:

- one complete passing fixture repository
- one negative fixture per prerequisite suite omission
- one negative fixture for each legacy non-authority guard class
- one negative fixture per missing activation evidence family
- one negative fixture per cross-role identity conflict
- one negative fixture per stale or wrong-target evidence class
- one negative fixture for each illegal lifecycle phase shortcut
- one fixture proving dormant prose is allowed while active authority records
  in legacy dispatch plans are rejected
- JSON success and JSON failure schema tests
- repo-suite integration test or fixture that proves the activation gate is
  called by `validate_ww_repo.py`

Fixtures should use temporary repositories and repository-relative paths.
They should not depend on network, current wall-clock time, symlinks, or OS
path quirks unless the fixture explicitly tests path containment.

## Activation Entry Criteria

WorkWork may open a real activation round only when all of the following are
true:

1. Existing repo suite passes with lifecycle, verifier, missing-capability,
   persona, packet, case, and round validators enabled.
2. The future activation gate validator passes.
3. The activation evidence manifest exists and references completed approved
   rounds for every mandatory capability.
4. Required negative fixtures prove stale evidence, wrong targets, role
   conflicts, missing close gates, skipped score, and illegal phase changes are
   rejected.
5. Legacy rounds remain clean under lifecycle, verifier, and missing-capability
   non-authority guards.
6. A human explicitly approves a later activation round.

## Recommended Next Round

Next should be an implementation foundation round for the activation evidence
manifest, not the validator itself, unless the team prefers validator-first
development.

Recommended order:

1. lifecycle-reference linkage validator foundation, if not already present
2. activation evidence manifest design or implementation foundation
3. dogfood/pilot evidence gaps for missing runtime behavior families
4. activation gate validator implementation
5. activation gate validator dogfood audit
6. only then, a separate `task-runtime-v1` activation round
