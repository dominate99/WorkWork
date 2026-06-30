# Task Runtime Missing Capability Contract

This reference defines dormant `task-runtime-v1` contract surfaces for internal
hooks, quality gates, scoring, repair authorization, re-verification, close
gates, final human judgment, recovery requirements, and checkpoints.

It extends `task-runtime-lifecycle.md` and `task-runtime-verification.md`. It
does not activate `task-runtime-v1`. Legacy rounds must not persist or consult
these records as lifecycle authority. Presence of these fields, examples,
templates, or references is contract scaffolding only until a later approved
activation round implements runtime behavior, validator coverage, verifier
binding, command execution, packet assembly, and end-to-end pilots.

## Authority Boundary

The missing capability layer adds guard and decision records. It does not add a
new state owner.

| Surface | Produces | Must Not Do |
|---|---|---|
| worker | execution result and optional self-check notes | approve verification, review, score, close, or its own repair acceptance |
| verifier | bounded verifier evidence and one lane outcome | mutate target, repair, review, score, close, or change lifecycle state |
| reviewer | findings and disposition for a frozen review target | mutate target, accept verifier evidence, score, or close |
| orchestrator | hook evaluations, evidence applicability, synthesis, score proposal, close recommendation, lifecycle events | bypass hard blockers or convert missing evidence into PASS |
| human | approval, revision, stop, exceptional authorization, final close judgment | relabel missing, stale, wrong-target, below-floor, or failed evidence as valid PASS |

`lifecycle_phase` remains orchestrator-owned through accepted lifecycle events.
`runtime_state` remains the canonical operational state. Missing capability
records may be referenced from lifecycle event `guard_results`, `artifact_refs`,
or `evidence_refs`, but they do not replace lifecycle events.

## Dormant Record Families

Future active `task-runtime-v1` sections may persist:

```yaml
internal_hook_records: []
quality_gate_records: []
score_records: []
repair_records: []
review_synthesis_records: []
reverification_requirements: []
close_gate_records: []
final_judgment_records: []
recovery_requirement_records: []
checkpoint_records: []
```

Rules:

- Records are section-scoped unless a later approved contract says otherwise.
- Records are append-only unless explicitly marked as a current snapshot by a
  later implementation contract.
- Records do not own `lifecycle_phase`, `runtime_state`, `plan_state`, or
  `section_state`.
- Legacy rounds omit these authority records entirely.

## Internal Hooks

Internal hooks are invocation-scoped guard points inside `$ww` or `$www`. They
are not operating-system hooks, git hooks, background daemons, scheduled tasks,
or passive listeners.

Canonical dormant hook names:

| Hook | Trigger Point | Primary Purpose |
|---|---|---|
| `BeforePhaseLaunch` | before launching `execute`, `verify`, `review`, `fix`, `re-verify`, or `score` work | confirm phase prerequisites and launch identity |
| `AfterWorkerReturn` | after producer or repair attempt returns | confirm stable result artifact identity and handoff readiness |
| `BeforeReview` | before reviewer launch | confirm review target is frozen and verifier prerequisites are satisfied when required |
| `AfterReview` | after required review lanes return | classify findings and decide no-remediation vs remediation path |
| `BeforeRepair` | before repair launch | confirm repair is authorized and scoped to accepted findings |
| `AfterRepairReturn` | after repair attempt returns | freeze repaired target and invalidate stale evidence |
| `BeforeScore` | before score computation | confirm verification and review evidence is current for the target lineage |
| `BeforeClose` | before requesting close judgment | confirm quality gate, blockers, score, evidence, review, and repair rules are satisfied |
| `OnBlocked` | when a phase enters `blocked` | persist recovery requirement and next action |
| `OnCompactRisk` | before long phases, after phase transitions, or when compaction risk is detected | checkpoint current state and recovery summary |

Dormant record shape:

```yaml
internal_hook_record:
  hook_id: <stable-id-within-section>
  hook_name: BeforeClose
  hook_schema_version: 1
  section_id: <section-id>
  lifecycle_phase: close
  runtime_state_at_evaluation: queued
  trigger_event_ref: <event-id-or-null>
  target_ref: <verification-or-review-target-ref-or-null>
  inputs:
    artifact_refs: []
    evidence_refs: []
    review_refs: []
    score_ref: <score-record-id-or-null>
    repair_ref: <repair-record-id-or-null>
  guard_results:
    - guard_id: <stable-id>
      guard_name: <canonical-guard-name>
      result: pass | fail | blocked | not-applicable
      severity: info | warning | blocker
      rationale: <short-explanation>
  outcome: pass | blocked
  blocked_reason_code: <code-or-null>
  recovery_requirement_ref: <record-id-or-null>
  evaluated_by:
    runtime_role: orchestrator
    persona_id: <orchestrator-persona-id>
  evaluated_at: <timestamp>
```

Hook integration rules:

- `AfterWorkerReturn` must pass before `EXECUTION_RESULT_ACCEPTED`.
- `BeforeReview` must pass before reviewer lanes launch.
- `AfterReview` must pass before `REVIEW_ACCEPTED_NO_REMEDIATION` or
  `REVIEW_ACCEPTED_FOR_REMEDIATION`.
- `BeforeRepair` must pass before `PHASE_STARTED` for `fix/queued`.
- `AfterRepairReturn` must pass before `FIX_RESULT_ACCEPTED`.
- `BeforeScore` must pass before `PHASE_STARTED` for `score/queued`.
- `BeforeClose` must pass before `CLOSE_JUDGMENT_REQUESTED`.
- `OnBlocked` must write a recovery requirement before or with a blocked-state
  lifecycle event.
- `OnCompactRisk` may checkpoint state but must not change phase by itself.

## Quality Gates And Scoring

A quality gate is a declared close policy for a section. It defines thresholds,
required evidence, scoring dimensions, and hard blockers before scoring occurs.

```yaml
quality_gate_record:
  quality_gate_id: <stable-id-within-section>
  gate_schema_version: 1
  section_id: <section-id>
  gate_profile_id: <profile-id>
  close_threshold: 80
  pr_threshold: 90
  excellence_threshold: 95
  required_evidence:
    verifier_lane_ids: []
    review_lane_ids: []
    artifact_refs: []
  hard_blockers:
    - blocker_code: missing-verification
      waivable: false
      rationale: formal verification is mandatory before close
  soft_blockers: []
  scoring_dimensions: []
  selected_by:
    runtime_role: orchestrator
    persona_id: <orchestrator-persona-id>
  selected_at: <timestamp>
```

```yaml
score_record:
  score_id: <stable-id-within-section>
  score_schema_version: 1
  section_id: <section-id>
  target_ref: <complete-current-target-ref>
  quality_gate_id: <quality-gate-id>
  lifecycle_phase: score
  score_value: <0-100-or-null>
  score_status: pass | fail | blocked
  dimension_results: []
  blocker_evaluation:
    hard_blockers_present: []
    soft_blockers_present: []
    waived_blockers: []
    non_waivable_blockers_present: []
  evidence_applicability_refs: []
  review_synthesis_refs: []
  repair_refs: []
  computed_by:
    runtime_role: orchestrator
    persona_id: <orchestrator-persona-id>
  computed_at: <timestamp>
```

Rules:

- Gate thresholds are policy inputs, not evidence.
- A high score cannot override a non-waivable hard blocker.
- Missing required evidence makes the score `blocked`, not zero-filled.
- `score_status: pass` requires `score_value >= close_threshold` and no
  non-waivable blockers.
- `SCORE_ACCEPTED` is legal only when the orchestrator accepts a score record
  for the current target lineage.

## Repair And Re-Verification

Repair is a controlled response to accepted review findings or verifier
failures. It is not a general second implementation pass.

```yaml
repair_record:
  repair_id: <stable-id-within-section>
  repair_schema_version: 1
  section_id: <section-id>
  source_target_ref: <pre-repair-target-ref>
  authorization:
    authorized_by:
      runtime_role: orchestrator | human
      persona_id: <persona-id-or-null>
    authorized_at: <timestamp>
    authorization_reason: accepted-review-findings | failed-verification | human-revision
    approved_plan_revision: <revision>
  accepted_findings: []
  repair_scope:
    allowed_artifact_refs: []
    disallowed_changes: []
    success_conditions: []
  assigned_worker:
    persona_id: <worker-persona-id>
    persona_source: project | built-in
    runtime_role: worker
    execution_id: <execution-id-or-null-before-launch>
  repair_attempt_refs: []
  repaired_target_ref: <target-ref-or-null-until-return>
  invalidated_evidence_refs: []
  invalidated_review_refs: []
  status: authorized | running | returned | accepted | blocked | superseded
```

```yaml
reverification_requirement:
  reverification_id: <stable-id-within-section>
  repair_id: <repair-record-id>
  repaired_target_ref: <complete-repaired-target-ref>
  required_verifier_lane_ids: []
  inherited_lane_ids: []
  new_lane_ids: []
  stale_evidence_refs: []
  required_current_pass_refs: []
  status: pending | satisfied | blocked
  rationale: <why these lanes are required after repair>
```

Rules:

- Repair requires explicit authorization before `fix` work starts.
- Repair scope must map to accepted findings or failed verifier evidence.
- Any target artifact mutation creates a repaired target lineage.
- `FIX_RESULT_ACCEPTED` leads to `re-verify/queued`, never directly to
  `review`, `score`, or `close`.
- `REVERIFICATION_ACCEPTED` requires current accepted PASS evidence for every
  required re-verifier lane.
- Stale pre-fix evidence cannot satisfy re-verification.

## Review Synthesis And Stale Targets

```yaml
review_synthesis_record:
  review_synthesis_id: <stable-id-within-section>
  section_id: <section-id>
  review_target_ref: <complete-current-target-ref>
  required_review_lane_ids: []
  returned_review_lane_ids: []
  stale_review_lane_ids: []
  accepted_findings: []
  rejected_findings: []
  remediation_required: true | false
  critical_findings_present: true | false
  target_changed_since_review: true | false
  outcome: no-remediation | remediation-required | blocked
  synthesized_by:
    runtime_role: orchestrator
    persona_id: <orchestrator-persona-id>
  synthesized_at: <timestamp>
```

Rules:

- Required review lanes must target the same current target lineage.
- Stale reviewer returns remain history and cannot satisfy review coverage.
- Review findings are not verifier evidence, but they may become repair inputs
  and scoring inputs.

## Close Gates And Final Judgment

```yaml
close_gate_record:
  close_gate_id: <stable-id-within-section>
  close_gate_schema_version: 1
  section_id: <section-id>
  target_ref: <complete-current-target-ref>
  quality_gate_id: <quality-gate-id>
  score_id: <score-record-id>
  required_verification:
    required_lane_ids: []
    accepted_pass_evidence_refs: []
    missing_or_invalid_lane_ids: []
  required_review:
    required_lane_ids: []
    accepted_review_synthesis_ref: <review-synthesis-id>
    stale_or_missing_lane_ids: []
  repair_status:
    repairs_required: true | false
    open_repair_ids: []
    accepted_repair_ids: []
    required_reverification_ids: []
  blocker_status:
    non_waivable_blockers: []
    waivable_blockers: []
    waiver_records: []
  close_recommendation: approve-close | request-revision | blocked | stop
  outcome: pass | blocked
  evaluated_by:
    runtime_role: orchestrator
    persona_id: <orchestrator-persona-id>
  evaluated_at: <timestamp>
```

```yaml
final_judgment_record:
  judgment_id: <stable-id-within-section>
  judgment_schema_version: 1
  section_id: <section-id>
  close_gate_id: <close-gate-id>
  score_id: <score-record-id>
  target_ref: <complete-current-target-ref>
  presented_summary:
    score_value: <0-100>
    non_waivable_blockers: []
    waivable_blockers: []
    waived_blockers: []
    verification_summary_ref: <ref-or-null>
    review_summary_ref: <ref-or-null>
    repair_summary_ref: <ref-or-null>
  decision: approve-close | request-revision | stop
  decided_by: user
  decided_at: <timestamp>
  rationale: <optional-human-rationale>
```

Rules:

- `BeforeClose` must produce a passing close gate before
  `CLOSE_JUDGMENT_REQUESTED`.
- `CLOSE_JUDGMENT_REQUESTED` requires `close_gate_record.outcome: pass`.
- Any non-waivable blocker blocks close.
- Waivable blockers require explicit waiver records and must be visible in the
  final judgment package.
- `CLOSE_APPROVED` is legal only with final human judgment
  `decision: approve-close`.
- A human may approve close, request revision, or stop. A human may not turn
  invalid verifier evidence into valid PASS evidence.

## Recovery And Checkpointing

```yaml
recovery_requirement_record:
  recovery_requirement_id: <stable-id-within-section>
  section_id: <section-id>
  lifecycle_phase: <phase>
  runtime_state: blocked
  blocker_code: <canonical-code>
  blocker_summary: <short-summary>
  required_next_input: <human-decision | artifact-change | evidence | plan-revision | tool-access>
  resume_instructions: <short-instructions>
  created_by:
    runtime_role: orchestrator
    persona_id: <orchestrator-persona-id>
  created_at: <timestamp>
```

```yaml
checkpoint_record:
  checkpoint_id: <stable-id-within-section>
  section_id: <section-id>
  lifecycle_phase: <phase>
  runtime_state: <state>
  event_head: <event-id-or-null>
  active_execution_id: <id-or-null>
  active_attempt_id: <id-or-null>
  pending_next_action: <next-action-code>
  summary: <resume-safe-summary>
  created_reason: before-long-phase | after-phase-transition | context-compaction-risk
  created_at: <timestamp>
```

Rules:

- Checkpoints are resume aids, not lifecycle authorities.
- A checkpoint cannot override the current lifecycle snapshot or event history.
- Recovery requirements should guide resume without replaying completed artifact
  writes.

## Lifecycle Event Integration

| Lifecycle Event | Required Missing-Capability Inputs |
|---|---|
| `EXECUTION_RESULT_ACCEPTED` | passing `AfterWorkerReturn` hook and stable target ref |
| `VERIFICATION_ACCEPTED` | accepted current verifier PASS evidence for all required lanes |
| `REVIEW_ACCEPTED_NO_REMEDIATION` | review synthesis outcome `no-remediation` and no accepted remediation-required findings |
| `REVIEW_ACCEPTED_FOR_REMEDIATION` | review synthesis outcome `remediation-required` and repair authorization plan |
| `FIX_RESULT_ACCEPTED` | accepted repair return, repaired target ref, stale evidence invalidation, and re-verification requirement |
| `REVERIFICATION_ACCEPTED` | current accepted verifier PASS evidence for the repaired target |
| `SCORE_ACCEPTED` | accepted score record tied to current target and quality gate |
| `CLOSE_JUDGMENT_REQUESTED` | passing close gate and final judgment package prepared |
| `CLOSE_APPROVED` | final human judgment `approve-close` |

State-only blocked events should include `OnBlocked` guard results and recovery
requirements in the lifecycle event's `guard_results` or `evidence_refs`.

## Verifier Evidence Integration

- Verifier evidence remains the only formal verification authority.
- Worker self-checks may inform scoring but cannot satisfy verification.
- Reviewer findings may inform repair and score dimensions but cannot satisfy
  verification.
- Score records reference verifier evidence but do not validate it.
- Close gates depend on current accepted verifier PASS evidence and evidence
  applicability records.
- Repair invalidates target-bound verifier evidence unless the orchestrator
  records current applicability for unchanged target members.
- Re-verification requires verifier evidence for the repaired target lineage.

## Invalid States For Later Validators

Later validator rounds should reject at least:

- active hook, score, repair, close, or final judgment records under
  `Lifecycle Protocol: legacy`
- phase transition records that lack required hook or gate inputs once
  `task-runtime-v1` is active
- `SCORE_ACCEPTED` without a score record for the current target
- `CLOSE_JUDGMENT_REQUESTED` without a passing close gate
- `CLOSE_APPROVED` without final human judgment `approve-close`
- close gates with non-waivable blockers
- scores that pass despite missing required evidence dimensions
- repairs without authorization or accepted findings
- `FIX_RESULT_ACCEPTED` without a repaired target ref
- `REVERIFICATION_ACCEPTED` using stale pre-repair evidence
- review synthesis using stale reviewer targets
- hook records that claim to own `runtime_state` or `lifecycle_phase`
- checkpoints used as lifecycle authority

Dedicated validator rule IDs, fixtures, and enforcement code belong to a later
approved validator-expansion round.
