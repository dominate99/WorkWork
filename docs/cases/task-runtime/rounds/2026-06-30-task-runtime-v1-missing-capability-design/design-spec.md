# Design Spec: Task Runtime V1 Missing Capability Design

## Artifact Metadata

- `schema_version`: 1
- `spec_status`: approved
- `case_slug`: task-runtime
- `round_slug`: 2026-06-30-task-runtime-v1-missing-capability-design
- `created_at`: 2026-06-30
- `updated_at`: 2026-06-30
- `source_dispatch_plan`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/dispatch-plan.md`
- `activation_readiness_source`: `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/design-spec.md`
- `primary_lifecycle_reference`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
- `primary_verification_reference`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`

## Summary

This design defines the dormant contracts still missing before WorkWork can activate `task-runtime-v1`: internal hooks, quality gates and scoring, repair authorization and re-verification, close gates, final human judgment, and their relationship to lifecycle events and verifier evidence.

The design remains dormant. It does not activate `task-runtime-v1`, does not add runtime bindings, does not execute commands, does not add personas, does not modify validators, and does not change packet assembly. Its purpose is to make the next implementation foundation and validator rounds concrete enough to build safely.

The central rule is simple: `task-runtime-v1` may only move forward when the orchestrator has current accepted evidence for the same target lineage, has evaluated required hooks and gates, has recorded any required repair path, and has an explicit final human close judgment. Scores may summarize quality, but hard blockers remain hard blockers.

## Design Goals

- Define invocation-scoped internal hooks that run only inside a `$ww` or `$www` workflow, not as background daemons.
- Define quality gate and scoring records that aggregate accepted evidence without hiding hard blockers.
- Define repair authorization and re-verification records so artifact changes after review cannot reuse stale verifier evidence.
- Define close-gate and final judgment records so `close/complete` is never reached automatically.
- Keep worker, reviewer, verifier, orchestrator, and human authorities separate.
- Make record shapes concrete enough for later template and validator rounds.
- Preserve the lifecycle foundation: `lifecycle_phase` remains orchestrator-owned, and `runtime_state` remains the canonical operational state.

## Non-Goals

- Do not activate `task-runtime-v1`.
- Do not implement runtime behavior.
- Do not modify validators.
- Do not add verifier personas or runtime bindings.
- Do not implement command execution.
- Do not expand routing, project registry, packet assembly, templates, README, SKILL, or packet contract in this round.
- Do not allow any hook, score, repair, close gate, or human judgment record to replace lifecycle events.

## Authority Model

The missing capability layer adds guard and decision records, not new owners for phase or runtime state.

| Surface | Produces | May Decide | Must Not Do |
|---|---|---|---|
| worker | execution result and optional self-check notes | whether its own attempt is ready to return | approve verification, review, score, close, or its own repair acceptance |
| verifier | bounded verifier evidence and lane outcome | one verifier lane result | mutate target, repair, review, score, close, or change lifecycle state |
| reviewer | findings and disposition for a frozen review target | reviewer lane outcome | mutate target, accept verifier evidence, score, or close |
| orchestrator | hook evaluations, evidence applicability, synthesis, score proposal, close recommendation, lifecycle events | whether guard inputs satisfy transition preconditions | bypass hard blockers or convert missing evidence into PASS |
| human | approval, revision, stop, exceptional authorization, final close judgment | final close approval or revision direction | relabel missing, stale, wrong-target, below-floor, or failed evidence as valid PASS |

Human judgment is final for closing or revising, but it does not falsify evidence. If evidence is missing or stale, the valid human choices are to revise, authorize a new path, stop, or approve an explicit exception only when the close-gate contract allows that blocker class to be waived.

## Dormant Record Families

Future `task-runtime-v1` sections should add five record families. They are dormant until activation.

```yaml
internal_hook_records: []
quality_gate_records: []
score_records: []
repair_records: []
close_gate_records: []
final_judgment_records: []
```

Rules:

- These records are section-scoped.
- They do not own `lifecycle_phase`, `runtime_state`, `plan_state`, or `section_state`.
- They may appear in lifecycle event `guard_results`, `artifact_refs`, or `evidence_refs`.
- Accepted phase changes remain legal only through lifecycle events from `task-runtime-lifecycle.md`.
- In legacy rounds, these records must not be rendered as active authority.

## Internal Hook Contract

Internal hooks are named, invocation-scoped guard points. They run during one WorkWork invocation or resume, and only when the orchestrator is already handling a `$ww` or `$www` round. They are not operating-system hooks, git hooks, background daemons, scheduled tasks, or passive listeners.

### Hook Purposes

| Hook | Trigger Point | Primary Purpose | Blocks When |
|---|---|---|---|
| `BeforePhaseLaunch` | before launching work for `execute`, `verify`, `review`, `fix`, `re-verify`, or `score` | confirm phase prerequisites and launch identity | required plan, target, lane, role, or identity input is missing |
| `AfterWorkerReturn` | after producer or repair attempt returns | confirm result artifact identity and handoff readiness | no stable target, wrong attempt, missing required artifact, or target cannot be frozen |
| `BeforeReview` | before reviewer launch | confirm review target is frozen and verifier prerequisites are satisfied when required | target is mutable, stale, missing, or not tied to accepted verifier evidence when required |
| `AfterReview` | after all required review lanes return | classify findings and decide no-remediation vs remediation path | required lane missing, stale, non-terminal, or synthesis cannot classify findings |
| `BeforeRepair` | before repair launch | confirm repair is authorized and scoped to accepted findings | no accepted repair authorization, repair would exceed scope, or target lineage is ambiguous |
| `AfterRepairReturn` | after repair attempt returns | freeze repaired target and invalidate stale evidence | repaired target cannot be identified or required invalidations cannot be recorded |
| `BeforeScore` | before score computation | confirm verification/review evidence is current for the target lineage | required accepted evidence or review synthesis is missing |
| `BeforeClose` | before requesting close judgment | confirm quality gate, blockers, score, evidence, review, and repair rules are satisfied | any non-waivable blocker remains or final judgment package is incomplete |
| `OnBlocked` | when a phase enters `blocked` | persist recovery requirement and next action | blocker lacks reason, owner, required evidence, or recovery route |
| `OnCompactRisk` | before long phases, after phase transitions, and when compaction risk is detected | checkpoint current state and recovery summary | checkpoint cannot be written or current state is internally inconsistent |

### Hook Record Shape

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

Hook records are append-only. If facts change, the orchestrator writes a new hook record rather than editing the old one.

### Hook And Lifecycle Integration

Hooks strengthen lifecycle transition guards but do not create new transitions.

- `AfterWorkerReturn` must pass before `EXECUTION_RESULT_ACCEPTED`.
- `BeforeReview` must pass before reviewer lanes launch.
- `AfterReview` must pass before either `REVIEW_ACCEPTED_NO_REMEDIATION` or `REVIEW_ACCEPTED_FOR_REMEDIATION`.
- `BeforeRepair` must pass before `PHASE_STARTED` for `fix/queued`.
- `AfterRepairReturn` must pass before `FIX_RESULT_ACCEPTED`.
- `BeforeScore` must pass before `PHASE_STARTED` for `score/queued`.
- `BeforeClose` must pass before `CLOSE_JUDGMENT_REQUESTED`.
- `OnBlocked` must write a recovery requirement before or with any blocked-state lifecycle event.
- `OnCompactRisk` may checkpoint state but must not change phase by itself.

## Quality Gate Contract

A quality gate is a declared close policy for a section. It defines thresholds and hard blockers before scoring occurs.

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
    - blocker_code: unresolved-critical-finding
      waivable: false
      rationale: critical review findings require remediation or explicit stop/revision
    - blocker_code: stale-review-target
      waivable: false
      rationale: review must apply to the current target
  soft_blockers:
    - blocker_code: low-confidence-evidence
      waivable: true
      waiver_requires: human-judgment
  scoring_dimensions:
    - dimension_id: verification
      weight: 30
      required: true
    - dimension_id: review-coverage
      weight: 25
      required: true
    - dimension_id: requirement-fit
      weight: 25
      required: true
    - dimension_id: maintainability-or-clarity
      weight: 20
      required: true
  selected_by:
    runtime_role: orchestrator
    persona_id: <orchestrator-persona-id>
  selected_at: <timestamp>
```

Rules:

- Gate thresholds are policy inputs, not evidence.
- A high score cannot override a non-waivable hard blocker.
- A missing required dimension makes the score blocked, not zero-filled.
- Gate profiles may vary by task profile later, but this round does not define routing or task-profile selection.
- Gate records are frozen before score computation for the target lineage.

## Score Contract

A score record aggregates current accepted evidence into a quality result.

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
  dimension_results:
    - dimension_id: verification
      score: <0-100-or-null>
      status: pass | fail | blocked
      evidence_refs: []
      rationale: <short-explanation>
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

- `score_status: pass` requires `score_value >= close_threshold` and no non-waivable blockers.
- `score_status: fail` means evidence is current and sufficient to score, but thresholds or blockers fail.
- `score_status: blocked` means required evidence, review synthesis, repair lineage, or gate inputs are missing or inconsistent.
- `SCORE_ACCEPTED` is legal only when the orchestrator accepts a `score_record` for the current target lineage.
- A score is stale if the target, verifier evidence, review target, repair result, quality gate, or blocker disposition changes.

## Repair Authorization Contract

Repair is a controlled response to accepted review findings or verifier failures. It is not a general second implementation pass.

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
  accepted_findings:
    - finding_id: <review-or-verifier-finding-id>
      source_lane_id: <lane-id>
      severity: critical | high | medium | low
      remediation_required: true
      scope_boundary: <short-scope>
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

Rules:

- Repair requires explicit authorization before `fix` work starts.
- The repair worker must not be the verifier or reviewer for the same repaired target lineage unless a later approved isolation rule explicitly permits it with distinct runtime identity. Default is separation.
- Repair scope must map to accepted findings or failed verification evidence.
- Any artifact mutation creates a repaired target lineage.
- All verifier evidence for the pre-repair target is stale for the repaired target unless an evidence applicability record proves it remains current for an unchanged aggregate member.
- Critical accepted findings require repair, revision, or stop; they cannot be ignored by score alone.

## Re-Verification Contract

Re-verification proves the repaired target, not the original target.

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

- `FIX_RESULT_ACCEPTED` leads to `re-verify/queued`, never directly back to `review`, `score`, or `close`.
- `REVERIFICATION_ACCEPTED` requires current accepted PASS evidence for every required re-verifier lane.
- Stale pre-fix evidence cannot satisfy re-verification.
- If the repair changes review-relevant content, the section must return to review after re-verification.
- If the repair is purely evidence/environment repair with no target artifact change, a later implementation may allow a reduced review path only if the approved contract and validators can prove the review target did not change.

## Review Progression And Stale Target Contract

Review progression is the bridge between verifier evidence and repair/score decisions.

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
- `REVIEW_ACCEPTED_NO_REMEDIATION` requires `outcome: no-remediation`.
- `REVIEW_ACCEPTED_FOR_REMEDIATION` requires `outcome: remediation-required` and a repair authorization path.
- Review findings are not verifier evidence, but they may become repair inputs and scoring inputs.

## Close Gate Contract

The close gate packages all final preconditions before requesting human judgment.

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

Rules:

- `BeforeClose` must produce a passing close gate before `CLOSE_JUDGMENT_REQUESTED`.
- `CLOSE_JUDGMENT_REQUESTED` requires `close_gate_record.outcome: pass`.
- A close gate passes only when verification, review, repair, re-verification, score, and blocker rules are satisfied for the current target lineage.
- Any non-waivable blocker blocks close.
- Waivable blockers require explicit waiver records and must be visible in the final judgment package.
- The close gate recommends, but does not approve, final close.

## Final Human Judgment Contract

Final human judgment is explicit and terminal only when it approves close after a passing close gate.

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

- `CLOSE_APPROVED` is legal only with `decision: approve-close`.
- `request-revision` keeps the section from completing and routes through the lifecycle revision path.
- `stop` records explicit user stop and must not be conflated with failure.
- A human may approve a close recommendation, request revision, or stop. A human may not turn invalid evidence into valid verifier PASS evidence.

## Lifecycle Event Integration

The missing capability records strengthen the foundation transitions:

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

State-only blocked events should include `OnBlocked` guard results and recovery requirements in the lifecycle event's `guard_results` or `evidence_refs`.

## Verifier Evidence Integration

Verifier evidence remains the only formal verification authority.

- Worker self-checks may inform scoring but cannot satisfy verification.
- Reviewer findings may inform repair and score dimensions but cannot satisfy verification.
- Score records reference verifier evidence but do not validate it.
- Close gates depend on current accepted verifier PASS evidence and evidence applicability records.
- Repair invalidates target-bound verifier evidence unless the orchestrator records current applicability for unchanged target members.
- Re-verification requires verifier evidence for the repaired target lineage.

## Recovery And Checkpointing

`OnBlocked` and `OnCompactRisk` produce recovery-oriented records.

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
- Recovery requirements should be concise enough to guide a later resume without replaying completed artifact writes.

## Future Validator Implications

Later validator rounds should reject:

- active hook, score, repair, close, or final judgment records under `Lifecycle Protocol: legacy`
- phase transition records that lack required hook or gate inputs once `task-runtime-v1` is active
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

These validators should be implemented only after this dormant design is copied into active contract/templates in a later implementation foundation round.

## Future Implementation Sequence

Recommended sequence after this design is approved:

1. Implementation foundation: add dormant contract references/templates/docs for hooks, quality gates, scoring, repair, close gates, final judgment, recovery, and checkpoints.
2. Validator expansion: protect the dormant surfaces and legacy non-authority boundaries.
3. Contract dogfood: create minimal sample records without activation.
4. Packet assembly and verifier binding design: define how real worker, verifier, and reviewer packets get distinct identities for one target lineage.
5. Runtime implementation: implement lifecycle controller behavior behind an explicit activation boundary.
6. Runtime pilot: run one no-repair path and one repair/re-verify path before any migration.

## Acceptance Criteria

- Internal hooks are defined as invocation-scoped WorkWork guards, not daemons.
- Quality gates and scoring have record shapes and hard-blocker rules.
- Repair authorization and re-verification have target-lineage and stale-evidence rules.
- Close gates and final human judgment are distinct and recorded.
- Lifecycle event integration is explicit.
- Verifier evidence remains the only formal verification authority.
- The design remains dormant and does not implement activation, validators, runtime behavior, personas, bindings, command execution, routing, or packet assembly.

## Conclusion

This design fills the contract gap identified by the activation readiness audit. It gives WorkWork a dormant specification for the guard, scoring, repair, close, and judgment records that must exist before `task-runtime-v1` can be implemented or validated safely.

The next round should be an implementation foundation round that copies these approved dormant contracts into the active WorkWork references, templates, and user-facing guidance without activating runtime behavior.
