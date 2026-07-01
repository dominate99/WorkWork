# Dispatch Plan: Task Runtime Lifecycle Reference Validator Foundation

- Date: 2026-07-01
- Schema Version: 2
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: task-runtime
- Round Slug: 2026-07-01-task-runtime-v1-lifecycle-reference-validator-foundation
- Case Root: `docs/cases/task-runtime/`
- Round Root: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-lifecycle-reference-validator-foundation/`
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

- User Request: `$ww round: task-runtime lifecycle reference validator foundation. Based on activation gate validator design, fill the lifecycle reference linkage validator foundation: add or extend validation to check task-runtime-lifecycle reference exists and is correctly referenced by SKILL, README, working-brief-template, dispatch-plan-template, or related packet/runtime guidance; confirm legacy rounds must not treat lifecycle snapshot, event history, or lifecycle_phase as active authority. Only do validator/test/docs guidance; do not activate task-runtime-v1, add runtime binding, implement command execution/routing/packet assembly/repair/scoring/hooks, or change personas.`
- Working Brief Reference: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-lifecycle-reference-validator-foundation/working-brief.md`
- Activation Gate Design Reference: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/design-spec.md`
- Lifecycle Reference: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
- Existing Round Lifecycle Validator: `tools/validate_ww_round_lifecycle.py`
- Existing Validator Patterns: `tools/validate_ww_verifier_authority_contracts.py`, `tools/validate_ww_missing_capability_contracts.py`

## Dispatch Summary

- Goal: add the lifecycle reference linkage validator foundation that activation gate design identified as a prerequisite
- Relevant Context:
  - `validate_ww_round_lifecycle.py` checks case/round ownership, but not lifecycle reference linkage across active contract surfaces
  - verifier and missing-capability validators already implement the reference-linkage pattern this round should mirror
  - this round may update validator code, tests, repo-suite integration, and necessary docs guidance only
- Constraints:
  - do not activate `task-runtime-v1`
  - do not add runtime binding, command execution, routing, packet assembly, repair/scoring/hooks, or personas
  - do not turn lifecycle future fields into active authority in legacy rounds
  - preserve `Lifecycle Protocol: legacy`
- Risks:
  - overly broad legacy guard that rejects harmless prose
  - underbroad legacy guard that misses future lifecycle authority rendered in legacy dispatch plans
  - validator implementation that duplicates round lifecycle validation instead of checking reference linkage
  - docs guidance that implies activation rather than dormant validation
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Lifecycle Reference Validator Foundation

- Section ID: section-lifecycle-reference-validator-foundation
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: test-quality-engineer
- Planned Reviewer Persona: spec-reviewer, code-quality-reviewer, documentation-clarity-reviewer
- Planned Reviewer Persona Source: built-in
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: validator foundation must stay scoped, technically precise, and clear about dormant lifecycle authority
- Planned Specialist Personas:
  - Persona ID: test-quality-engineer
    - Source: built-in
    - Runtime Role: worker
    - Selection Rationale: lifecycle reference validation is dominated by fixture quality, linkage coverage, JSON output, and false-positive/false-negative control
- Planned Scope:
  - `docs/cases/task-runtime/case.md`
  - `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-lifecycle-reference-validator-foundation/working-brief.md`
  - `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-lifecycle-reference-validator-foundation/dispatch-plan.md`
  - `tools/validate_ww_lifecycle_reference_contracts.py`
  - `tools/test_validate_ww_lifecycle_reference_contracts.py`
  - `tools/validate_ww_repo.py`
  - `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `README.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/packets/lifecycle-foundation-code-quality-review-r2.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is read-only.
- Planning Rationale: implement the lifecycle reference validator gap identified by activation gate design without enabling runtime behavior
- Planned Workflow Bindings:
  - `superpowers:test-driven-development`
  - `superpowers:verification-before-completion`
  - `superpowers:requesting-code-review`
- Planned Worker Mode: test-first
- Worker Mode Rationale: write failing fixtures for missing lifecycle reference linkage and legacy lifecycle authority drift before validator implementation
- Goal Tuning: validation-biased
- Constraint Interaction Rule: if runtime behavior gaps appear, record them as future activation evidence work and do not implement them in this round
- Planned Review Lanes:
  - Lane ID: lane-lifecycle-reference-validator-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify the implementation covers lifecycle reference linkage and all non-activation constraints
  - Required: true
  - Lane ID: lane-lifecycle-reference-validator-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify validator logic, fixture isolation, JSON output, and repo-suite integration
  - Required: true
  - Lane ID: lane-lifecycle-reference-validator-doc-clarity-review
  - Lane Type: other
  - Reviewer Persona: documentation-clarity-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify docs guidance is precise and does not imply activation
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/task-runtime/case.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-lifecycle-reference-validator-foundation/working-brief.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-lifecycle-reference-validator-foundation/dispatch-plan.md`
    - `path_glob`: `tools/validate_ww_lifecycle_reference_contracts.py`
    - `path_glob`: `tools/test_validate_ww_lifecycle_reference_contracts.py`
    - `path_glob`: `tools/validate_ww_repo.py`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `README.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/packets/lifecycle-foundation-code-quality-review-r2.md`
  - `shared_read_scope`:
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
    - `path_glob`: `tools/validate_ww_round_lifecycle.py`
    - `path_glob`: `tools/validate_ww_verifier_authority_contracts.py`
    - `path_glob`: `tools/validate_ww_missing_capability_contracts.py`
    - `path_glob`: `tools/test_validate_ww_verifier_authority_contracts.py`
    - `path_glob`: `tools/test_validate_ww_missing_capability_contracts.py`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/design-spec.md`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: lifecycle_reference_validator
      - `artifact_kind`: validator
      - `artifact_path`: `tools/validate_ww_lifecycle_reference_contracts.py`
      - `section_anchors`: lifecycle reference linkage and legacy non-authority guard
    - `artifact_id`: lifecycle_reference_validator_tests
      - `artifact_kind`: test_module
      - `artifact_path`: `tools/test_validate_ww_lifecycle_reference_contracts.py`
      - `section_anchors`: positive fixture, negative linkage fixtures, legacy authority drift fixtures, JSON output
- Scope declaration rule: every writable file in `Planned Scope` appears in `exclusive_write_scope`; runtime binding, command execution, routing, packet assembly, repair/scoring/hook behavior, activation behavior, and personas are excluded.
- Packet Created: false

## Section Runtime Ledger

### Section: Lifecycle Reference Validator Foundation

- Section ID: section-lifecycle-reference-validator-foundation
- Runtime State: complete
- Active Execution ID: exec-lifecycle-reference-validator-foundation-01
- Active Packet ID:
- Active Agent ID: test-quality-engineer
- Active Attempt ID: attempt-lifecycle-reference-validator-foundation-01
- Active Worker Mode: test-first
- Active Persona IDs: test-quality-engineer
- Active Persona Sources: built-in
- Active Persona Role Bindings: worker
- Mode Change History: none
- Execution Records:
- Execution ID: exec-lifecycle-reference-validator-foundation-01
  - Attempt ID: attempt-lifecycle-reference-validator-foundation-01
  - Agent ID: test-quality-engineer
  - Runtime Role: worker
  - Result: implemented lifecycle reference validator foundation
  - Evidence:
    - `tools/validate_ww_lifecycle_reference_contracts.py` added with WWLC001-WWLC007 checks for reference linkage, template surfaces, packet source context, working brief recommendation, and legacy non-authority drift
    - `tools/test_validate_ww_lifecycle_reference_contracts.py` added with positive fixture, linkage failures, JSON output, heading-only drift, single/multi YAML-like lifecycle assignments, and prose false-positive coverage
    - `tools/validate_ww_repo.py` now runs lifecycle reference contract validation after round lifecycle validation
    - `README.md` documents the lifecycle reference validator command, unittest, repo-suite coverage, and maintenance guidance
    - `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/packets/lifecycle-foundation-code-quality-review-r2.md` review_target_ref hash synchronized because repo-suite integration changed `tools/validate_ww_repo.py`
- Packet Records:
- Attempt Records:
- Attempt ID: attempt-lifecycle-reference-validator-foundation-01
  - Return Status: DONE_WITH_CONCERNS
  - Summary: implementation complete; concern recorded for out-of-round historical packet hash metadata update required by runtime persona packet artifact validation after repo-suite entrypoint changed
- Attempt Count: 1
- Last Update At: 2026-07-01
- Next Action: none; round accepted by human judgment
- Active Write Scope:
  - `tools/validate_ww_lifecycle_reference_contracts.py`
  - `tools/test_validate_ww_lifecycle_reference_contracts.py`
  - `tools/validate_ww_repo.py`
  - `README.md`
  - `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/packets/lifecycle-foundation-code-quality-review-r2.md`
  - round planning artifacts
- Result Summary: lifecycle reference linkage validator foundation implemented and integrated into the repo suite; no task-runtime-v1 activation, runtime binding, command execution, routing, packet assembly, repair/scoring/hooks, or persona changes were made
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns: repo-suite integration changed `tools/validate_ww_repo.py`, requiring the existing full-file packet hash fallback metadata for a historical reviewer packet targeting that file to be synchronized
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy: stale attempt returns may be recorded as history only and must not advance canonical runtime state
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Lifecycle Reference Validator Foundation

- Section ID: section-lifecycle-reference-validator-foundation
- Review Target Strategy:
  - review the final validator/test/docs/repo-suite diff against activation gate design and user constraints
- Review Lane Records:
  - Lane ID: lane-lifecycle-reference-validator-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: requested validator foundation and non-activation constraints are primary acceptance criteria
  - Execution ID: review-lifecycle-reference-validator-spec-01
  - Packet ID:
  - Attempt ID: review-attempt-lifecycle-reference-validator-spec-01
  - Review Target Ref: lifecycle reference validator/test/docs/repo-suite diff
  - Reviewer Findings: PASS - implementation matches requested validator/test/docs guidance scope and keeps task-runtime-v1 dormant
  - Orchestrator Synthesis: no material spec findings; packet hash metadata synchronization is recorded as necessary validation maintenance, not runtime activation
  - Strict Review Outcome: PASS
  - Lane ID: lane-lifecycle-reference-validator-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: validator and fixture quality must avoid broad prose false positives and active-authority false negatives
  - Execution ID: review-lifecycle-reference-validator-code-quality-01
  - Packet ID:
  - Attempt ID: review-attempt-lifecycle-reference-validator-code-quality-01
  - Review Target Ref: `tools/validate_ww_lifecycle_reference_contracts.py`, `tools/test_validate_ww_lifecycle_reference_contracts.py`, `tools/validate_ww_repo.py`
  - Reviewer Findings: PASS - tests cover positive and negative linkage, JSON schema, heading-only drift, YAML-like lifecycle assignments, and prose false-positive allowance
  - Orchestrator Synthesis: no material code-quality findings; regex checks only line-start YAML-like authority fields and reserved lifecycle record headings in legacy dispatch plans
  - Strict Review Outcome: PASS
  - Lane ID: lane-lifecycle-reference-validator-doc-clarity-review
  - Lane Type: other
  - Reviewer Persona: documentation-clarity-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: lifecycle guidance must remain dormant and source-of-truth clear
  - Execution ID: review-lifecycle-reference-validator-doc-clarity-01
  - Packet ID:
  - Attempt ID: review-attempt-lifecycle-reference-validator-doc-clarity-01
  - Review Target Ref: `README.md` and lifecycle reference linkage guidance
  - Reviewer Findings: PASS - README now lists the validator command, unittest, repo-suite coverage, and maintenance guidance without implying activation
  - Orchestrator Synthesis: no material documentation findings; active contract remains dormant and points to existing lifecycle reference surfaces
  - Strict Review Outcome: PASS
- Human Decision: Approve
- Revision Notes:
- Rollup Rule:
  - Approve -> section state becomes `accepted` and lifecycle reference validator foundation execution may begin
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level plan state follows required-section aggregation

## Ordering And Parallelism

- Blocking work first: section-lifecycle-reference-validator-foundation
- Parallel sections: none
- Review loop: test-first validator/docs foundation -> focused verification -> spec, code-quality, and documentation-clarity review -> orchestrator synthesis -> human judgment

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
- Notes: approval authorizes only lifecycle reference validator/test/docs guidance foundation; no runtime activation or runtime behavior implementation
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial lifecycle reference validator foundation round
- Supersedes Revision:

## Dispatch Log

- Agents Launched:
  - test-quality-engineer: exec-lifecycle-reference-validator-foundation-01
- Retry Events:
- Close Events:
  - 2026-07-01: human approved lifecycle reference validator foundation; plan_state completed, section_state accepted, close_state closed
- Review Lane Transitions:
  - lane-lifecycle-reference-validator-spec-review: PASS
  - lane-lifecycle-reference-validator-code-quality-review: PASS
  - lane-lifecycle-reference-validator-doc-clarity-review: PASS
- Launch Time: 2026-07-01
- Revisions Since Approval: 0
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
