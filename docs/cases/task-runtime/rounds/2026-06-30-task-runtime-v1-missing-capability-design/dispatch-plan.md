# Dispatch Plan: Task Runtime V1 Missing Capability Design

- Date: 2026-06-30
- Schema Version: 2
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: task-runtime
- Round Slug: 2026-06-30-task-runtime-v1-missing-capability-design
- Case Root: `docs/cases/task-runtime/`
- Round Root: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/`
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

- User Request: `$ww round: task-runtime-v1 missing capability design. Based on the activation readiness audit, design the dormant contracts still required before task-runtime-v1 activation: internal hooks, quality gates/scoring, repair authorization/re-verification, close gates, final human judgment, and their relationship to lifecycle events and verifier evidence. Only produce design spec; do not implement activation, modify validators, add personas, add runtime binding, implement command execution, routing, or packet assembly.`
- Working Brief Reference: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/working-brief.md`
- Activation Readiness Audit: `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/design-spec.md`
- Lifecycle Reference: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
- Verification Reference: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`

## Dispatch Summary

- Goal: design the missing dormant `task-runtime-v1` capability contracts required before activation work can proceed
- Relevant Context: the approved activation readiness audit identified missing hook, score, repair/re-verification, close-gate, and final-judgment contracts as blockers before implementation foundation or dogfood
- Constraints:
  - produce only a persisted design spec
  - do not implement activation, validators, runtime behavior, templates, packet assembly, command execution, routing, personas, verifier bindings, or project registry changes
  - do not modify active contract files, README, SKILL, packet contract, or validator code
  - keep this round on `Lifecycle Protocol: legacy`
- Risks:
  - hook design may imply background daemon behavior instead of invocation-scoped WorkWork guards
  - quality scoring may be too subjective or may hide hard blockers
  - repair design may allow stale evidence or self-approval
  - close gates may blur automated checks with final human judgment
  - record shapes may be too vague for later validators
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Missing Capability Design

- Section ID: section-missing-capability-design
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: senior-backend-engineer
- Planned Reviewer Persona: spec-reviewer, code-quality-reviewer, documentation-clarity-reviewer
- Planned Reviewer Persona Source: built-in
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: the design must satisfy the requested missing surfaces, preserve runtime authority boundaries, and remain clear enough for future implementation and validator rounds
- Planned Specialist Personas:
  - Persona ID: senior-backend-engineer
    - Source: project
    - Runtime Role: worker
    - Selection Rationale: project registry provides an eligible senior backend specialist for controller/state-machine contract design with correctness and integration risk
- Planned Scope:
  - `docs/cases/task-runtime/case.md`
  - `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/working-brief.md`
  - `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/dispatch-plan.md`
  - `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/design-spec.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is read-only.
- Planning Rationale: define dormant hooks, quality gates/scoring, repair/re-verification, close gates, and final judgment before implementation foundation or validator expansion
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: research-first
- Worker Mode Rationale: derive the missing contract design from approved lifecycle, verifier, and readiness artifacts before proposing new record shapes.
- Goal Tuning: validation-biased
- Constraint Interaction Rule: implementation, validator, binding, persona, routing, command execution, or packet assembly details may be mentioned only as future work.
- Planned Review Lanes:
  - Lane ID: lane-missing-capability-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify that every requested missing dormant contract surface is covered and exclusions are preserved
  - Required: true
  - Lane ID: lane-missing-capability-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: inspect controller feasibility, lifecycle/verifier authority compatibility, future validator-readiness, and state ownership consistency
  - Required: true
  - Lane ID: lane-missing-capability-doc-clarity-review
  - Lane Type: other
  - Reviewer Persona: documentation-clarity-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify that the design spec is actionable for a later implementation foundation round
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/task-runtime/case.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/working-brief.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/dispatch-plan.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/design-spec.md`
  - `shared_read_scope`:
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/design-spec.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `path_glob`: `tools/validate_ww_round_lifecycle.py`
    - `path_glob`: `tools/validate_ww_repo.py`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: missing_capability_design_spec
      - `artifact_kind`: design_spec
      - `artifact_path`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/design-spec.md`
      - `section_anchors`: internal hooks, quality gates, scoring, repair authorization, re-verification, close gates, final judgment, lifecycle event integration, verifier evidence integration, future validator implications
    - `artifact_id`: activation_readiness_audit
      - `artifact_kind`: design_spec
      - `artifact_path`: `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/design-spec.md`
      - `section_anchors`: blocking activation gaps and next-round recommendation
- Scope declaration rule: every writable file in `Planned Scope` appears in `exclusive_write_scope`; contract, template, README, SKILL, packet, persona, routing, and validator files are read-only targets.
- Packet Created: false

## Section Runtime Ledger

### Section: Missing Capability Design

- Section ID: section-missing-capability-design
- Runtime State: complete
- Active Execution ID: exec-missing-capability-design-01
- Active Packet ID: not created; local orchestrator execution
- Active Agent ID: senior-backend-engineer
- Active Attempt ID: attempt-missing-capability-design-01
- Active Worker Mode: research-first
- Active Persona IDs: senior-backend-engineer, spec-reviewer, code-quality-reviewer, documentation-clarity-reviewer
- Active Persona Sources: project, built-in, built-in, built-in
- Active Persona Role Bindings: worker, reviewer, reviewer, reviewer
- Mode Change History: none
- Execution Records:
  - Execution ID: exec-missing-capability-design-01
  - Attempt ID: attempt-missing-capability-design-01
  - Worker Persona: senior-backend-engineer
  - Persona Source: project
  - Runtime Role: worker
  - Return Status: DONE
  - Summary: produced `design-spec.md` defining dormant task-runtime-v1 missing capability contracts for internal hooks, quality gates/scoring, repair authorization/re-verification, close gates, final human judgment, lifecycle event integration, verifier evidence integration, recovery, checkpoints, and future validator implications.
  - Changed Files:
    - `docs/cases/task-runtime/case.md`
    - `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/working-brief.md`
    - `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/dispatch-plan.md`
    - `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/design-spec.md`
  - Verification Evidence:
    - `C:\Users\domin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe tools\validate_ww_round_lifecycle.py` -> PASS, 106 rules
    - `C:\Users\domin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe tools\validate_ww_repo.py` -> PASS, repository validation passed
    - `git diff --check` -> PASS, with CRLF warning for `docs/cases/task-runtime/case.md`
- Packet Records:
  - Packet Created: false
  - Rationale: this design round used local persisted round records and did not create worker, reviewer, or verifier packets.
- Review Records:
  - Lane ID: lane-missing-capability-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: requested capability coverage and exclusions are primary success criteria
  - Execution ID: review-missing-capability-spec-01
  - Packet ID: not created; local review record
  - Attempt ID: attempt-review-missing-capability-spec-01
  - Review Target Ref: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/design-spec.md`
  - Reviewer Findings: PASS; no material findings. The design covers internal hooks, quality gates/scoring, repair authorization/re-verification, close gates, final human judgment, lifecycle event integration, verifier evidence integration, and preserves all exclusions.
  - Orchestrator Synthesis: spec coverage is complete for this design-only round; implementation, validators, runtime bindings, command execution, routing, and packet assembly are deferred.
  - Strict Review Outcome: none
  - Lane ID: lane-missing-capability-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: controller feasibility and authority-boundary consistency must be checked before future implementation foundation
  - Execution ID: review-missing-capability-code-quality-01
  - Packet ID: not created; local review record
  - Attempt ID: attempt-review-missing-capability-code-quality-01
  - Review Target Ref: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/design-spec.md`
  - Reviewer Findings: PASS; no material findings. The design keeps lifecycle_phase and runtime_state ownership intact, treats hooks/gates as guard records rather than state owners, preserves verifier evidence authority, and gives future validators concrete rejection classes.
  - Orchestrator Synthesis: controller feasibility and authority boundaries are consistent with lifecycle and verification references.
  - Strict Review Outcome: none
  - Lane ID: lane-missing-capability-doc-clarity-review
  - Lane Type: other
  - Reviewer Persona: documentation-clarity-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: the design must be actionable for future contract implementation and validators
  - Execution ID: review-missing-capability-doc-clarity-01
  - Packet ID: not created; local review record
  - Attempt ID: attempt-review-missing-capability-doc-clarity-01
  - Review Target Ref: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/design-spec.md`
  - Reviewer Findings: PASS; no material findings. The design separates goals, non-goals, authority, record families, lifecycle integration, verifier evidence integration, validator implications, and future implementation sequence.
  - Orchestrator Synthesis: the design is actionable for a later implementation foundation round.
  - Strict Review Outcome: none
- Human Decision: Approve
- Human Decision By: user
- Human Decision Time: 2026-06-30
- Revision Notes: final approval accepted the missing capability design spec and its recommendation to follow with an implementation foundation round that copies the approved dormant contracts into active WorkWork references, templates, and user-facing guidance without activating runtime behavior.
- Rollup Rule:
  - Approve -> section state becomes `accepted` and missing-capability design execution may begin
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level plan state follows required-section aggregation

## Ordering And Parallelism

- Blocking work first: section-missing-capability-design
- Parallel sections: none
- Review loop: design spec draft -> spec, code-quality, and documentation-clarity review -> orchestrator synthesis -> human judgment

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
- Approval Time: 2026-06-30
- Notes: approval authorizes design spec creation only; no activation, validator edits, personas, runtime bindings, command execution, routing, packet assembly, template, README, SKILL, packet contract, or project registry changes
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial task-runtime-v1 missing capability design round
- Supersedes Revision:

## Dispatch Log

- Agents Launched: exec-missing-capability-design-01
- Retry Events:
- Close Events:
  - section-missing-capability-design -> complete after final human approval
- Review Lane Transitions:
  - lane-missing-capability-spec-review -> PASS
  - lane-missing-capability-code-quality-review -> PASS
  - lane-missing-capability-doc-clarity-review -> PASS
- Launch Time: 2026-06-30
- Revisions Since Approval: 0
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
