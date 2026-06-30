# Dispatch Plan: Task Runtime V1 Activation Readiness Audit

- Date: 2026-06-27
- Schema Version: 2
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: task-runtime
- Round Slug: 2026-06-27-workwork-task-runtime-v1-activation-readiness-audit
- Case Root: `docs/cases/task-runtime/`
- Round Root: `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/`
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

- User Request: `$ww round: task-runtime-v1 activation readiness audit. Based on completed lifecycle foundation, verifier/lane authority foundation, validator expansion, and dogfood audit, audit what WorkWork still lacks before real task-runtime-v1 activation across contract, validator, runtime behavior, and dogfood evidence. Audit and classify only; do not implement activation, modify validators, add personas, or implement hooks/repair/scoring/command execution. Focus on lifecycle_phase authority, verifier lane authority, internal hooks, quality gates, worker/reviewer/verifier isolation, packet assembly, evidence freshness, close gates, what dormant contract is sufficient, and what must get design first. Produce an activation readiness gap report and decide whether the next round should be design, implementation foundation, or dogfood.`
- Working Brief Reference: `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/working-brief.md`
- Lifecycle Reference: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
- Verification Reference: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
- Prior Dogfood Audit: `docs/cases/task-runtime/rounds/2026-06-27-verifier-lane-authority-validator-dogfood-audit/design-spec.md`

## Dispatch Summary

- Goal: classify activation readiness gaps before any real `task-runtime-v1` activation work
- Relevant Context: lifecycle and verifier authority contracts are dormant, validator coverage exists for dormant verifier surfaces, and prior dogfood says validator hardening can wait until activation becomes concrete
- Constraints:
  - do not implement activation, validators, runtime behavior, hooks, repair, scoring, close gates, command execution, personas, routing, or packet assembly changes
  - do not modify active contract, templates, packet contract, README, SKILL, or validator files
  - produce only a persisted activation readiness gap report and round-local controller records
  - keep this round on `Lifecycle Protocol: legacy`
- Risks:
  - dormant contract may be mistaken for runtime readiness
  - missing repair/scoring/hooks/close-gate design may be hidden by lifecycle vocabulary
  - verifier lane authority may look complete while runtime binding and packet assembly remain absent
  - dogfood evidence may be insufficient to justify implementation foundation
  - next-round recommendation may skip required design
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Task Runtime V1 Activation Readiness Audit

- Section ID: section-task-runtime-v1-readiness-audit
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: senior-backend-engineer
- Planned Reviewer Persona: spec-reviewer, code-quality-reviewer, documentation-clarity-reviewer
- Planned Reviewer Persona Source: built-in
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: activation readiness must be checked for requirement coverage, runtime feasibility, and report clarity; built-in fallback is used because no project reviewer covers WorkWork runtime activation more strongly
- Planned Specialist Personas:
  - Persona ID: senior-backend-engineer
    - Source: built-in
    - Runtime Role: worker
    - Selection Rationale: activation readiness crosses controller semantics, validators, packet assembly, and runtime behavior; built-in fallback is used because no eligible project worker persona covers this WorkWork runtime audit more strongly
- Planned Scope:
  - `docs/cases/task-runtime/case.md`
  - `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/working-brief.md`
  - `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/dispatch-plan.md`
  - `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/design-spec.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is read-only.
- Planning Rationale: create a persisted readiness report before choosing design, implementation foundation, or dogfood as the next step
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: research-first
- Worker Mode Rationale: inspect existing dormant contracts and evidence before classifying gaps; do not edit implementation surfaces
- Goal Tuning: validation-biased
- Constraint Interaction Rule: any missing capability discovered by the audit must be recorded as a gap and deferred to a later approved round
- Planned Review Lanes:
  - Lane ID: lane-task-runtime-readiness-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify that every requested activation readiness surface is classified and all exclusions are preserved
  - Required: true
  - Lane ID: lane-task-runtime-readiness-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: inspect runtime/validator feasibility reasoning and whether the next-round recommendation follows from existing evidence
  - Required: true
  - Lane ID: lane-task-runtime-readiness-doc-clarity-review
  - Lane Type: other
  - Reviewer Persona: documentation-clarity-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify the readiness report is actionable and clearly separates contract, validator, runtime, and dogfood gaps
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/task-runtime/case.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/working-brief.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/dispatch-plan.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/design-spec.md`
  - `shared_read_scope`:
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `path_glob`: `tools/validate_ww_repo.py`
    - `path_glob`: `tools/validate_ww_round_lifecycle.py`
    - `path_glob`: `tools/validate_ww_verifier_authority_contracts.py`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-19-task-runtime-lifecycle-foundation-design/**/*`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/**/*`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-21-verifier-and-lane-authority-design/**/*`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-24-verifier-lane-authority-implementation-foundation/**/*`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-25-verifier-lane-authority-validator-expansion/**/*`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-27-verifier-lane-authority-validator-dogfood-audit/**/*`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: activation_readiness_report
      - `artifact_kind`: design_spec
      - `artifact_path`: `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/design-spec.md`
      - `section_anchors`: readiness matrix, activation blockers, sufficient dormant surfaces, missing design, missing validator/runtime/dogfood evidence, next-round recommendation
    - `artifact_id`: task_runtime_lifecycle_reference
      - `artifact_kind`: reference_doc
      - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
      - `section_anchors`: activation boundary and lifecycle_phase authority
    - `artifact_id`: task_runtime_verification_reference
      - `artifact_kind`: reference_doc
      - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
      - `section_anchors`: verifier authority, evidence freshness, isolation, and missing repair/scoring/hooks/close gates
- Scope declaration rule: every writable file in `Planned Scope` appears in `exclusive_write_scope`; contract and validator files are read-only targets.
- Packet Created: false

## Section Runtime Ledger

### Section: Task Runtime V1 Activation Readiness Audit

- Section ID: section-task-runtime-v1-readiness-audit
- Runtime State: complete
- Active Execution ID: exec-task-runtime-v1-readiness-audit-01
- Active Packet ID: not created; local orchestrator execution
- Active Agent ID: senior-backend-engineer
- Active Attempt ID: attempt-task-runtime-v1-readiness-audit-01
- Active Worker Mode: research-first
- Active Persona IDs: senior-backend-engineer, spec-reviewer, code-quality-reviewer, documentation-clarity-reviewer
- Active Persona Sources: built-in
- Active Persona Role Bindings: worker, reviewer, reviewer, reviewer
- Mode Change History: none
- Execution Records:
  - Execution ID: exec-task-runtime-v1-readiness-audit-01
  - Attempt ID: attempt-task-runtime-v1-readiness-audit-01
  - Worker Persona: senior-backend-engineer
  - Persona Source: built-in
  - Runtime Role: worker
  - Return Status: DONE
  - Summary: audited WorkWork activation readiness for `task-runtime-v1` and produced `design-spec.md` as an activation readiness gap report. The report concludes that lifecycle and verifier authority dormant contracts are sufficient for the current stage, but activation is blocked by missing hook, quality gate, repair/re-verification, close-gate, runtime binding, validator, and dogfood capabilities. It recommends a design round next.
  - Changed Files:
    - `docs/cases/task-runtime/case.md`
    - `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/working-brief.md`
    - `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/dispatch-plan.md`
    - `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/design-spec.md`
  - Verification Evidence:
    - `C:\Users\domin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe tools\validate_ww_round_lifecycle.py` -> PASS, 103 rules
    - `C:\Users\domin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe tools\validate_ww_repo.py` -> PASS, repository validation passed
    - `git diff --check` -> PASS, with CRLF warning for `docs/cases/task-runtime/case.md`
- Packet Records:
  - Packet Created: false
  - Rationale: this readiness audit used local persisted round records and did not create worker, reviewer, or verifier packets.
- Review Records:
  - Lane ID: lane-task-runtime-readiness-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: activation boundary coverage and scope exclusions are primary success criteria
  - Execution ID: review-task-runtime-v1-readiness-spec-01
  - Packet ID: not created; local review record
  - Attempt ID: attempt-review-task-runtime-v1-readiness-spec-01
  - Review Target Ref: `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/design-spec.md`
  - Reviewer Findings: PASS; no material findings. The report classifies each requested readiness surface, preserves the audit-only exclusions, and distinguishes dormant contract sufficiency from real activation readiness.
  - Orchestrator Synthesis: spec coverage is complete for this audit round; activation work is deferred.
  - Strict Review Outcome: none
  - Lane ID: lane-task-runtime-readiness-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: runtime and validator feasibility reasoning must be grounded before recommending a next round
  - Execution ID: review-task-runtime-v1-readiness-code-quality-01
  - Packet ID: not created; local review record
  - Attempt ID: attempt-review-task-runtime-v1-readiness-code-quality-01
  - Review Target Ref: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`, `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`, `tools/validate_ww_verifier_authority_contracts.py`, and the readiness report
  - Reviewer Findings: PASS; no material findings. The report correctly treats existing validators as dormant-contract sentinels and does not claim runtime, command execution, evidence freshness, scoring, repair, or close-gate behavior exists.
  - Orchestrator Synthesis: runtime and validator readiness reasoning is sound; implementation foundation should wait until missing contract design exists.
  - Strict Review Outcome: none
  - Lane ID: lane-task-runtime-readiness-doc-clarity-review
  - Lane Type: other
  - Reviewer Persona: documentation-clarity-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: readiness report must clearly separate design, implementation, validator, and dogfood gaps
  - Execution ID: review-task-runtime-v1-readiness-doc-clarity-01
  - Packet ID: not created; local review record
  - Attempt ID: attempt-review-task-runtime-v1-readiness-doc-clarity-01
  - Review Target Ref: `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/design-spec.md`
  - Reviewer Findings: PASS; no material findings. The report clearly separates sufficient dormant surfaces, blocking gaps, validator/runtime/dogfood gaps, and the recommended next round.
  - Orchestrator Synthesis: report is actionable for deciding the next WorkWork round type.
  - Strict Review Outcome: none
- Human Decision: Approve
- Human Decision By: user
- Human Decision Time: 2026-06-28
- Revision Notes: final approval accepted the activation readiness gap report and its recommendation to open a missing-capability design round before any task-runtime-v1 implementation foundation, validator expansion, dogfood pilot, or activation attempt.
- Rollup Rule:
  - Approve -> section state becomes `approved` and readiness audit execution may begin
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level plan state follows required-section aggregation

## Ordering And Parallelism

- Blocking work first: section-task-runtime-v1-readiness-audit
- Parallel sections: none
- Review loop: readiness report draft -> spec, code-quality, and documentation-clarity review -> orchestrator synthesis -> human judgment

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
- Approval Time: 2026-06-27
- Notes: approval authorizes readiness audit/report creation only; no activation, validator edits, personas, runtime bindings, hooks, repair, scoring, close gates, command execution, routing, or packet assembly changes
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial task-runtime-v1 activation readiness audit round
- Supersedes Revision:

## Dispatch Log

- Agents Launched: exec-task-runtime-v1-readiness-audit-01
- Retry Events:
- Close Events:
  - section-task-runtime-v1-readiness-audit -> complete after final human approval
- Review Lane Transitions:
  - lane-task-runtime-readiness-spec-review -> PASS
  - lane-task-runtime-readiness-code-quality-review -> PASS
  - lane-task-runtime-readiness-doc-clarity-review -> PASS
- Launch Time: 2026-06-27
- Revisions Since Approval: 0
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
