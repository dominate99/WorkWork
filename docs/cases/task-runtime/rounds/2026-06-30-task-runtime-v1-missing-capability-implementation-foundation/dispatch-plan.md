# Dispatch Plan: Task Runtime V1 Missing Capability Implementation Foundation

- Date: 2026-06-30
- Schema Version: 2
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: task-runtime
- Round Slug: 2026-06-30-task-runtime-v1-missing-capability-implementation-foundation
- Case Root: `docs/cases/task-runtime/`
- Round Root: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-implementation-foundation/`
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

- User Request: `$ww round: task-runtime-v1 missing capability implementation foundation. Based on the approved missing capability design, land dormant contracts for internal hooks, quality gates/scoring, repair authorization/re-verification, close gates, final human judgment, recovery/checkpoint records into WorkWork active references, templates, and docs guidance. Sync SKILL.md, README, dispatch-plan-template, working-brief-template, subagent-packet-contract, or related references. Contract/template/docs implementation only; do not activate task-runtime-v1, modify validators, add personas, add runtime binding, implement command execution, routing, or packet assembly.`
- Working Brief Reference: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-implementation-foundation/working-brief.md`
- Approved Design Source: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/design-spec.md`
- Lifecycle Reference: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
- Verification Reference: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`

## Dispatch Summary

- Goal: land the approved missing capability dormant contracts into active WorkWork references, templates, and docs guidance
- Relevant Context: approved design defines dormant records for hooks, quality gates/scoring, repair, re-verification, close gates, final judgment, recovery, and checkpoints; current active contract does not yet expose those surfaces
- Constraints:
  - contract/template/docs implementation only
  - do not activate `task-runtime-v1`
  - do not modify validators/tests/runtime code
  - do not add personas, verifier runtime binding, command execution, routing, packet assembly, or project registry changes
  - preserve `Lifecycle Protocol: legacy` for this round
- Risks:
  - dormant template blocks could look active in legacy rounds
  - new reference could contradict lifecycle/verifier authority
  - SKILL/README guidance could overpromise activation readiness
  - packet contract text could imply verifier packet launchability before bindings exist
  - no validator changes means existing tests only catch current sentinel surfaces
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Missing Capability Implementation Foundation

- Section ID: section-missing-capability-implementation-foundation
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: senior-backend-engineer
- Planned Reviewer Persona: spec-reviewer, code-quality-reviewer, documentation-clarity-reviewer
- Planned Reviewer Persona Source: built-in
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: implementation must match the approved design, preserve authority boundaries, and provide clear dormant guidance for future implementation/validator rounds
- Planned Specialist Personas:
  - Persona ID: senior-backend-engineer
    - Source: project
    - Runtime Role: worker
    - Selection Rationale: project registry provides an eligible senior backend specialist for controller contract/template implementation with correctness and integration risk
- Planned Scope:
  - `docs/cases/task-runtime/case.md`
  - `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-implementation-foundation/working-brief.md`
  - `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-implementation-foundation/dispatch-plan.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `README.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is read-only.
- Planning Rationale: copy approved dormant missing capability contract into active WorkWork references/templates/docs without activation
- Planned Workflow Bindings:
  - `superpowers:test-driven-development`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: test-driven
- Worker Mode Rationale: perform scoped contract/template/docs edits and verify with existing repo validation; do not add validator tests in this round.
- Goal Tuning: validation-biased
- Constraint Interaction Rule: any validator, runtime, persona, binding, command execution, routing, or packet assembly work must be deferred to later approved rounds.
- Planned Review Lanes:
  - Lane ID: lane-missing-capability-implementation-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify that implementation covers the approved design surfaces and preserves all exclusions
  - Required: true
  - Lane ID: lane-missing-capability-implementation-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: inspect contract/template consistency, lifecycle/verifier authority compatibility, and future validator-readiness
  - Required: true
  - Lane ID: lane-missing-capability-implementation-doc-clarity-review
  - Lane Type: other
  - Reviewer Persona: documentation-clarity-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify dormant guidance is clear and does not imply runtime activation
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/task-runtime/case.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-implementation-foundation/working-brief.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-implementation-foundation/dispatch-plan.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `README.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`
  - `shared_read_scope`:
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/design-spec.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/dispatch-plan.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/design-spec.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
    - `path_glob`: `tools/validate_ww_round_lifecycle.py`
    - `path_glob`: `tools/validate_ww_repo.py`
    - `path_glob`: `tools/validate_ww_verifier_authority_contracts.py`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: missing_capability_reference
      - `artifact_kind`: reference_doc
      - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`
      - `section_anchors`: dormant hooks, quality gates, scoring, repair, re-verification, close gates, final judgment, recovery, checkpointing, lifecycle integration, verifier evidence integration
    - `artifact_id`: approved_missing_capability_design
      - `artifact_kind`: design_spec
      - `artifact_path`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/design-spec.md`
      - `section_anchors`: record shapes and implementation sequence
- Scope declaration rule: every writable file in `Planned Scope` appears in `exclusive_write_scope`; validators, tests, runtime code, personas, routing, and project registry are read-only targets.
- Packet Created: false

## Section Runtime Ledger

### Section: Missing Capability Implementation Foundation

- Section ID: section-missing-capability-implementation-foundation
- Runtime State: complete
- Active Execution ID: exec-missing-capability-implementation-foundation-01
- Active Packet ID: not created; local orchestrator execution
- Active Agent ID: senior-backend-engineer
- Active Attempt ID: attempt-missing-capability-implementation-foundation-01
- Active Worker Mode: test-driven
- Active Persona IDs: senior-backend-engineer, spec-reviewer, code-quality-reviewer, documentation-clarity-reviewer
- Active Persona Sources: project, built-in, built-in, built-in
- Active Persona Role Bindings: worker, reviewer, reviewer, reviewer
- Mode Change History: none
- Execution Records:
  - Execution ID: exec-missing-capability-implementation-foundation-01
  - Attempt ID: attempt-missing-capability-implementation-foundation-01
  - Worker Persona: senior-backend-engineer
  - Persona Source: project
  - Runtime Role: worker
  - Return Status: DONE
  - Summary: implemented the approved dormant missing capability contract across active WorkWork references, templates, packet contract, SKILL, and README guidance without activating `task-runtime-v1` or changing validators/runtime/personas/routing/packet assembly.
  - Changed Files:
    - `docs/cases/task-runtime/case.md`
    - `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-implementation-foundation/working-brief.md`
    - `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-implementation-foundation/dispatch-plan.md`
    - `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `README.md`
    - `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`
  - Verification Evidence:
    - `C:\Users\domin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe tools\validate_ww_round_lifecycle.py` -> PASS, 109 rules
    - `C:\Users\domin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe tools\validate_ww_repo.py` -> PASS, repository validation passed
    - `git diff --check` -> PASS, with CRLF warnings for README, case.md, SKILL, dispatch-plan-template, subagent-packet-contract, and working-brief-template
- Packet Records:
  - Packet Created: false
  - Rationale: this implementation foundation used local persisted round records and did not create worker, reviewer, or verifier packets.
- Review Records:
  - Lane ID: lane-missing-capability-implementation-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: approved design coverage and exclusions are primary success criteria
  - Execution ID: review-missing-capability-implementation-spec-01
  - Packet ID: not created; local review record
  - Attempt ID: attempt-review-missing-capability-implementation-spec-01
  - Review Target Ref: active WorkWork contract/template/docs changes in this round
  - Reviewer Findings: PASS; no material findings. The implementation covers internal hooks, quality gates/scoring, repair/re-verification, close gates, final human judgment, recovery requirements, checkpoints, lifecycle integration, verifier evidence integration, and preserves all user-requested exclusions.
  - Orchestrator Synthesis: scope fidelity is complete; no validator, runtime, persona, binding, command execution, routing, packet assembly, or activation changes were made.
  - Strict Review Outcome: none
  - Lane ID: lane-missing-capability-implementation-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: contract/template consistency and lifecycle/verifier authority boundaries must be checked
  - Execution ID: review-missing-capability-implementation-code-quality-01
  - Packet ID: not created; local review record
  - Attempt ID: attempt-review-missing-capability-implementation-code-quality-01
  - Review Target Ref: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`, `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`, `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`, `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - Reviewer Findings: PASS; no material findings. The new reference keeps missing capability records as guard/gate/decision records rather than state owners, dispatch template blocks are `task-runtime-v1` only, packet contract fields are dormant source context, and verifier sentinel anchors still pass.
  - Orchestrator Synthesis: contract/template consistency and lifecycle/verifier authority boundaries are preserved.
  - Strict Review Outcome: none
  - Lane ID: lane-missing-capability-implementation-doc-clarity-review
  - Lane Type: other
  - Reviewer Persona: documentation-clarity-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: dormant guidance must be clear enough for future implementation and validator rounds
  - Execution ID: review-missing-capability-implementation-doc-clarity-01
  - Packet ID: not created; local review record
  - Attempt ID: attempt-review-missing-capability-implementation-doc-clarity-01
  - Review Target Ref: `README.md`, `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`, templates, and new reference
  - Reviewer Findings: PASS; no material findings. README and SKILL now identify the missing capability reference alongside lifecycle and verifier references, and guidance clearly says dormant verifier and missing-capability fields are not active lifecycle authority under `Lifecycle Protocol: legacy`.
  - Orchestrator Synthesis: dormant guidance is clear enough for a later validator expansion round.
  - Strict Review Outcome: none
- Human Decision: Approve
- Human Decision By: user
- Human Decision Time: 2026-06-30
- Revision Notes: final approval accepted the missing capability implementation foundation and its dormant contract/template/docs guidance; next round should expand validation for these dormant surfaces.
- Rollup Rule:
  - Approve -> section state becomes `accepted` and contract/template/docs implementation may begin
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level plan state follows required-section aggregation

## Ordering And Parallelism

- Blocking work first: section-missing-capability-implementation-foundation
- Parallel sections: none
- Review loop: contract/template/docs changes -> spec, code-quality, and documentation-clarity review -> orchestrator synthesis -> human judgment

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
- Notes: approval authorizes contract/template/docs implementation only; no activation, validator/test edits, personas, runtime bindings, command execution, routing, packet assembly, runtime code, or project registry changes
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial task-runtime-v1 missing capability implementation foundation round
- Supersedes Revision:

## Dispatch Log

- Agents Launched: exec-missing-capability-implementation-foundation-01
- Retry Events:
- Close Events:
  - section-missing-capability-implementation-foundation -> complete after final human approval
- Review Lane Transitions:
  - lane-missing-capability-implementation-spec-review -> PASS
  - lane-missing-capability-implementation-code-quality-review -> PASS
  - lane-missing-capability-implementation-doc-clarity-review -> PASS
- Launch Time: 2026-06-30
- Revisions Since Approval: 0
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
