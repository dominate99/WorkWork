# Dispatch Plan: Task Runtime V1 Activation Gate Validator Design

- Date: 2026-07-01
- Schema Version: 2
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: task-runtime
- Round Slug: 2026-07-01-task-runtime-v1-activation-gate-validator-design
- Case Root: `docs/cases/task-runtime/`
- Round Root: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/`
- Plan State: completed
- Last Approved Revision: 1
- Rollback Baseline Revision: 1
- Task Routing: code/programming
- Main Orchestrator: staff-engineer-orchestrator
- Lifecycle Protocol: legacy

## Strict Review Runtime State

```yaml
strict_review:
  mode: standard
  target: none
  state: idle
  cycle_count: 0
```

## Preconditions

- Estimation Complete: true
- Working Brief Status: ready

> Do not launch any real subagent until the preconditions are satisfied and `Plan State: approved`.

## Source Context

- User Request: `$ww round: task-runtime-v1 activation gate validator design. Based on lifecycle foundation, verifier/lane authority foundation, missing capability foundation, and the completed WWMC007 hardening, design a unified pre-activation gate validator for task-runtime-v1. Produce only a design spec; do not implement the validator, change contracts, add personas, add runtime binding, implement command execution/routing/packet assembly/repair/scoring/hooks. Focus on which dormant contract surfaces must be satisfied together, which legacy non-authority guards must remain, which validator suites must exist before activation, and which evidence can prove verifier evidence, missing-capability close gates, worker/reviewer/verifier isolation, and lifecycle_phase authority are sufficient to enter an activation round.`
- Working Brief Reference: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/working-brief.md`
- Lifecycle Reference: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
- Verification Reference: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
- Missing Capability Reference: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`
- WWMC007 Hardening Reference: `docs/cases/task-runtime/rounds/2026-07-01-missing-capability-legacy-guard-validator-hardening/dispatch-plan.md`

## Dispatch Summary

- Goal: design the unified activation gate validator that must pass before WorkWork may enter a real `task-runtime-v1` activation round
- Relevant Context:
  - lifecycle, verifier/lane authority, and missing-capability contracts are currently dormant
  - existing validators prove individual contract surfaces, but no single gate yet defines activation-entry evidence
  - WWMC007 hardening improved legacy non-authority protection for missing-capability fields
  - this round is design-only and should not implement the validator
- Constraints:
  - produce only `design-spec.md`
  - do not implement validator code or tests
  - do not change contracts, templates, README, SKILL, personas, project registry, routing, packet assembly, runtime binding, command execution, repair/scoring/hooks, or activation behavior
  - preserve `Lifecycle Protocol: legacy`
- Risks:
  - confusing dormant contract completeness with runtime activation readiness
  - designing a validator that duplicates existing suites instead of composing them
  - missing cross-suite evidence for verifier evidence, close gates, isolation, or lifecycle phase authority
  - weakening legacy non-authority guards by treating future surfaces as active too early
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Activation Gate Validator Design

- Section ID: section-activation-gate-validator-design
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: test-quality-engineer
- Planned Reviewer Persona: spec-reviewer, code-quality-reviewer, documentation-clarity-reviewer
- Planned Reviewer Persona Source: built-in
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: design must satisfy the exact activation-gate scope, be implementable later, and stay clear about dormant versus active authority
- Planned Specialist Personas:
  - Persona ID: test-quality-engineer
    - Source: built-in
    - Runtime Role: worker
    - Selection Rationale: activation gate validator design is dominated by validator suite composition, evidence sufficiency, and false-positive/false-negative boundaries
- Planned Scope:
  - `docs/cases/task-runtime/case.md`
  - `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/working-brief.md`
  - `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/dispatch-plan.md`
  - `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/design-spec.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is read-only.
- Planning Rationale: produce an activation gate design that can guide a later validator implementation round without activating runtime behavior
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:verification-before-completion`
  - `superpowers:requesting-code-review`
- Planned Worker Mode: research-first
- Worker Mode Rationale: synthesize existing dormant contracts, validators, and dogfood evidence before defining gate rules
- Goal Tuning: validation-biased
- Constraint Interaction Rule: if the design reveals missing implementation behavior, record it as an activation prerequisite rather than implementing it in this round
- Planned Review Lanes:
  - Lane ID: lane-activation-gate-validator-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify the design covers all requested gate surfaces and exclusions
  - Required: true
  - Lane ID: lane-activation-gate-validator-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify the future validator architecture is implementable and not overbroad or underbroad
  - Required: true
  - Lane ID: lane-activation-gate-validator-doc-clarity-review
  - Lane Type: other
  - Reviewer Persona: documentation-clarity-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify the design is clear as a future implementation source and does not imply activation
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/task-runtime/case.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/working-brief.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/dispatch-plan.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/design-spec.md`
  - `shared_read_scope`:
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `README.md`
    - `path_glob`: `tools/validate_ww_round_lifecycle.py`
    - `path_glob`: `tools/validate_ww_verifier_authority_contracts.py`
    - `path_glob`: `tools/validate_ww_missing_capability_contracts.py`
    - `path_glob`: `tools/validate_ww_repo.py`
    - `path_glob`: `docs/cases/task-runtime/rounds/**`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: activation_gate_design_spec
      - `artifact_kind`: design_spec
      - `artifact_path`: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/design-spec.md`
      - `section_anchors`: activation gate purpose, suite composition, evidence thresholds, non-authority guard preservation, activation-entry criteria
- Scope declaration rule: every writable file in `Planned Scope` appears in `exclusive_write_scope`; validator implementation, contract changes, personas, routing, packet assembly, runtime command execution, repair/scoring/hook behavior, and project registry are excluded.
- Packet Created: false

## Section Runtime Ledger

### Section: Activation Gate Validator Design

- Section ID: section-activation-gate-validator-design
- Runtime State: complete
- Active Execution ID: exec-activation-gate-validator-design-01
- Active Packet ID:
- Active Agent ID: test-quality-engineer
- Active Attempt ID: attempt-activation-gate-validator-design-01
- Active Worker Mode: research-first
- Active Persona IDs: test-quality-engineer, spec-reviewer, code-quality-reviewer, documentation-clarity-reviewer
- Active Persona Sources: built-in
- Active Persona Role Bindings: test-quality-engineer=worker; spec-reviewer=reviewer; code-quality-reviewer=reviewer; documentation-clarity-reviewer=reviewer
- Mode Change History: none
- Execution Records:
  - Execution ID: exec-activation-gate-validator-design-01
    - Attempt ID: attempt-activation-gate-validator-design-01
    - Agent ID: test-quality-engineer
    - Worker Mode: research-first
    - Result Artifact Location: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/design-spec.md`
    - Summary: designed a future activation gate validator with prerequisite suite inventory, dormant contract completeness, runtime behavior evidence, cross-suite consistency, legacy non-authority preservation, and activation-entry criteria
    - Notable Design Decision: lifecycle reference linkage should become a dedicated activation prerequisite because current repo validation covers round lifecycle ownership but not a full lifecycle-reference linkage suite
- Packet Records:
- Attempt Records:
  - Attempt ID: attempt-activation-gate-validator-design-01
    - Started At: 2026-07-01
    - Completed At: 2026-07-01
    - Result Artifact Location: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/design-spec.md`
    - Status: completed
- Attempt Count: 1
- Last Update At: 2026-07-01
- Next Action: round complete; ready for follow-up lifecycle-reference linkage validator foundation round
- Active Write Scope:
  - `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/design-spec.md`
  - round planning artifacts
- Result Summary: activation gate validator design complete; it defines WWAG001-WWAG009, activation evidence manifest expectations, prerequisite suites, cross-suite evidence, and the boundary that passing the gate permits only a separate activation round
- Canonical Result Artifact Location: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/design-spec.md`
- Concerns:
  - lifecycle reference linkage needs its own validator foundation before activation gate implementation
  - runtime behavior evidence is still missing for verifier authority, stale-target handling, repair/re-verification, scoring, close gates, and lifecycle event pilots
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy: stale attempt returns may be recorded as history only and must not advance canonical runtime state
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Activation Gate Validator Design

- Section ID: section-activation-gate-validator-design
- Review Target Strategy:
  - review the produced `design-spec.md` against dormant contracts, existing validator suites, WWMC007 hardening evidence, and the requested activation-gate evidence surfaces
- Review Lane Records:
  - Lane ID: lane-activation-gate-validator-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: requested activation-gate coverage and exclusions are primary acceptance criteria
  - Execution ID: review-activation-gate-validator-spec-01
  - Packet ID:
  - Attempt ID: review-attempt-activation-gate-validator-spec-01
  - Review Target Ref: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/design-spec.md`
  - Reviewer Findings: no material findings; the design covers dormant surfaces, legacy non-authority guards, prerequisite suites, verifier evidence, close gates, role isolation, lifecycle_phase authority, and activation-entry boundaries
  - Orchestrator Synthesis: accepted; the spec preserves the design-only scope and explicitly avoids runtime activation
  - Strict Review Outcome: pass
  - Lane ID: lane-activation-gate-validator-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: future validator design must be implementable without duplicating or weakening existing suites
  - Execution ID: review-activation-gate-validator-code-quality-01
  - Packet ID:
  - Attempt ID: review-attempt-activation-gate-validator-code-quality-01
  - Review Target Ref: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/design-spec.md`
  - Reviewer Findings: no material findings; the future validator architecture composes existing suites, identifies missing lifecycle-reference linkage validation, and separates manifest evidence checks from command execution
  - Orchestrator Synthesis: accepted; implementation is deferred and rule families are scoped enough for a later validator round
  - Strict Review Outcome: pass
  - Lane ID: lane-activation-gate-validator-doc-clarity-review
  - Lane Type: other
  - Reviewer Persona: documentation-clarity-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: the design must be clear future-work guidance and must not imply activation
  - Execution ID: review-activation-gate-validator-doc-clarity-01
  - Packet ID:
  - Attempt ID: review-attempt-activation-gate-validator-doc-clarity-01
  - Review Target Ref: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/design-spec.md`
  - Reviewer Findings: no material findings; the design is readable as future implementation guidance and repeatedly states the gate does not activate task-runtime-v1
  - Orchestrator Synthesis: accepted; recommended next rounds are explicit and ordered
  - Strict Review Outcome: pass
- Human Decision: Approve
- Revision Notes: design spec approved; no validator implementation, contract change, persona change, runtime binding, command execution, routing, packet assembly, repair/scoring/hook implementation, or activation was performed
- Rollup Rule:
  - Approve -> section state becomes `accepted` and plan state becomes `completed`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level plan state follows required-section aggregation

## Ordering And Parallelism

- Blocking work first: section-activation-gate-validator-design
- Parallel sections: none
- Review loop: design spec -> spec, code-quality, and documentation-clarity review -> orchestrator synthesis -> human judgment

## Approval Block

- Required Human Choice (rendered labels):
  - `1. Approve`
  - `2. Revise`
  - `3. Stop`
- Numeric Reply Mapping:
  - `1` -> `Approve`
  - `2` -> `Revise`
  - `3` -> `Stop`
- Canonical Decision Values: `Approve` | `Revise` | `Stop`
- Accepted Word Replies: `Approve` | `Revise` | `Stop`
- Current Choice: Approve
- Approved By: user
- Approval Time: 2026-07-01
- Notes: approval authorizes only the design spec; no validator implementation, contract change, persona change, runtime binding, command execution, routing, packet assembly, repair/scoring/hook implementation, or activation
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial activation gate validator design round
- Supersedes Revision:

## Dispatch Log

- Agents Launched:
  - test-quality-engineer (inline worker per approved legacy plan)
- Retry Events:
- Close Events:
  - 2026-07-01: user approved activation gate validator design; round closed
- Review Lane Transitions:
  - lane-activation-gate-validator-spec-review: pass
  - lane-activation-gate-validator-code-quality-review: pass
  - lane-activation-gate-validator-doc-clarity-review: pass
- Launch Time: 2026-07-01
- Revisions Since Approval: 0
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
