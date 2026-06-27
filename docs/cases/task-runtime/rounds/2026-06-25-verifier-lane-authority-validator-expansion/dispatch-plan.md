# Dispatch Plan: Verifier Lane Authority Validator Expansion

- Date: 2026-06-25
- Schema Version: 2
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: task-runtime
- Round Slug: 2026-06-25-verifier-lane-authority-validator-expansion
- Case Root: `docs/cases/task-runtime/`
- Round Root: `docs/cases/task-runtime/rounds/2026-06-25-verifier-lane-authority-validator-expansion/`
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

- User Request: `$ww round: verifier lane authority validator expansion. Based on the completed and committed verifier and lane authority implementation foundation, expand WorkWork repo validation to check dormant verifier/lane authority contract surfaces. Update related validator and necessary test fixtures, covering task-runtime-verification reference existence and references from SKILL/README/templates/packet contract; legacy rounds must not use verifier/lane fields as lifecycle authority; dispatch-plan template task-runtime-v1 verifier lane block must contain verifier_lanes, verification_target_ref, evidence_requirements, freshness_policy, model_capability_profile, minimum_capability_floor, model_resolutions; subagent packet contract must preserve active legacy runtime_role gate and clearly dormant verifier packet fields; working brief template must record verification_lane_preparation and legacy non-authority note. Only validator/test/docs guidance; do not add verifier personas, verifier runtime binding, command execution, repair/scoring/hooks, or task-runtime-v1 activation.`
- Working Brief Reference: `docs/cases/task-runtime/rounds/2026-06-25-verifier-lane-authority-validator-expansion/working-brief.md`
- Implementation Foundation Commit: `08378f4 Add task runtime verifier authority foundation`
- Dormant Verifier Reference: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
- Repo Validation Entrypoint: `tools/validate_ww_repo.py`

## Dispatch Summary

- Goal: expand repository validation to check dormant verifier/lane authority contract surfaces and prevent future contract drift
- Relevant Context: verifier/lane authority foundation is committed, but its dormant contract surfaces are not yet directly machine-checked by a dedicated validator
- Constraints:
  - update only validator code, tests/fixtures, repo-suite integration, README guidance, and round-local records
  - do not add verifier personas, verifier runtime binding, verifier packets, command execution, repair, scoring, hooks, routing expansion, project registry records, secondary tags, or `task-runtime-v1` activation
  - do not make legacy rounds consume verifier/lane fields as lifecycle authority
  - preserve active legacy packet `runtime_role` gates
  - keep validator checks deterministic and text/structure based
- Risks:
  - validator checks becoming too broad and blocking valid legacy rounds
  - validator missing one of the required dormant fields in the dispatch template
  - packet contract checks accidentally allowing active verifier role binding
  - negative fixtures proving only missing text rather than the intended drift class
  - repo-suite integration not running the new validator
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Verifier Lane Authority Validator Expansion

- Section ID: section-verifier-lane-authority-validator-expansion
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: senior-backend-engineer
- Planned Reviewer Persona: spec-reviewer, code-quality-reviewer, documentation-clarity-reviewer
- Planned Reviewer Persona Source: built-in
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: requirement fidelity, validator correctness, and maintainer-facing validation guidance are separately material; built-in fallback is used because no project reviewer covers portable WorkWork validator contracts more strongly
- Planned Specialist Personas:
  - Persona ID: senior-backend-engineer
    - Source: built-in
    - Runtime Role: worker
    - Selection Rationale: validator code, regression tests, and repo-suite integration are durable implementation surfaces; built-in fallback is used because no eligible project worker persona covers WorkWork validator architecture more strongly
- Planned Scope:
  - `tools/validate_ww_verifier_authority_contracts.py`
  - `tools/test_validate_ww_verifier_authority_contracts.py`
  - `tools/validate_ww_repo.py`
  - `README.md`
  - `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/packets/lifecycle-foundation-code-quality-review-r2.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is read-only.
- Planning Rationale: add one focused validator that checks dormant verifier contract linkage and required field surfaces, then wire it into the existing repo-level suite with targeted negative fixtures
- Planned Workflow Bindings:
  - `superpowers:test-driven-development`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: validate-first
- Worker Mode Rationale: start from validator failure modes and negative drift fixtures so the implementation proves the exact contract checks requested
- Goal Tuning: validation-biased
- Constraint Interaction Rule: if a change would add verifier personas, verifier runtime binding, command execution, repair, scoring, hooks, routing expansion, project registry records, secondary tags, or `task-runtime-v1` activation, stop and defer it to a later approved round
- Planned Review Lanes:
  - Lane ID: lane-verifier-validator-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify that every requested validator coverage point is represented and dormant-only exclusions are preserved
  - Required: true
  - Lane ID: lane-verifier-validator-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: inspect validator implementation, fixture isolation, failure messages, and repo-suite integration
  - Required: true
  - Lane ID: lane-verifier-validator-doc-clarity-review
  - Lane Type: other
  - Reviewer Persona: documentation-clarity-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: documentation clarity is independently material because maintainers need to discover and interpret the new validator without assuming runtime activation
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/task-runtime/case.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-25-verifier-lane-authority-validator-expansion/working-brief.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-25-verifier-lane-authority-validator-expansion/dispatch-plan.md`
    - `path_glob`: `tools/validate_ww_verifier_authority_contracts.py`
    - `path_glob`: `tools/test_validate_ww_verifier_authority_contracts.py`
    - `path_glob`: `tools/validate_ww_repo.py`
    - `path_glob`: `README.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/packets/lifecycle-foundation-code-quality-review-r2.md`
  - `shared_read_scope`:
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-24-verifier-lane-authority-implementation-foundation/**/*`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: verifier_lane_authority_validator
      - `artifact_kind`: validator_code
      - `artifact_path`: `tools/validate_ww_verifier_authority_contracts.py`
      - `section_anchors`: reference linkage, legacy non-authority, template field coverage, packet dormant verifier gate, working brief verification preparation
    - `artifact_id`: verifier_lane_authority_validator_tests
      - `artifact_kind`: test_code
      - `artifact_path`: `tools/test_validate_ww_verifier_authority_contracts.py`
      - `section_anchors`: negative drift fixtures and repo-suite behavior
- Scope declaration rule: every writable file in `Planned Scope` appears in `exclusive_write_scope`; round-local controller files are separately owned by the orchestrator.
- Packet Created: false

## Section Runtime Ledger

### Section: Verifier Lane Authority Validator Expansion

- Section ID: section-verifier-lane-authority-validator-expansion
- Runtime State: complete
- Active Execution ID: exec-verifier-validator-expansion-01
- Active Packet ID: not created; local orchestrator execution
- Active Agent ID: senior-backend-engineer
- Active Attempt ID: attempt-verifier-validator-expansion-01
- Active Worker Mode: validate-first
- Active Persona IDs: senior-backend-engineer, spec-reviewer, code-quality-reviewer, documentation-clarity-reviewer
- Active Persona Sources: built-in
- Active Persona Role Bindings: worker, reviewer, reviewer, reviewer
- Mode Change History: none
- Execution Records:
  - Execution ID: exec-verifier-validator-expansion-01
  - Attempt ID: attempt-verifier-validator-expansion-01
  - Worker Persona: senior-backend-engineer
  - Persona Source: built-in
  - Runtime Role: worker
  - Return Status: DONE
  - Summary: added `tools/validate_ww_verifier_authority_contracts.py`, regression tests, repo-suite wiring, README validation guidance, and refreshed the stale full-file packet hash for the modified `tools/validate_ww_repo.py` target.
  - Changed Files:
    - `tools/validate_ww_verifier_authority_contracts.py`
    - `tools/test_validate_ww_verifier_authority_contracts.py`
    - `tools/validate_ww_repo.py`
    - `README.md`
    - `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/packets/lifecycle-foundation-code-quality-review-r2.md`
    - `docs/cases/task-runtime/case.md`
    - `docs/cases/task-runtime/rounds/2026-06-25-verifier-lane-authority-validator-expansion/working-brief.md`
    - `docs/cases/task-runtime/rounds/2026-06-25-verifier-lane-authority-validator-expansion/dispatch-plan.md`
  - Verification Evidence:
    - `python -m unittest tools.test_validate_ww_verifier_authority_contracts -v` -> PASS, 9 tests
    - `python tools/validate_ww_verifier_authority_contracts.py --json` -> PASS, 7 rules
    - `python -m py_compile tools/validate_ww_verifier_authority_contracts.py tools/test_validate_ww_verifier_authority_contracts.py` -> PASS
    - `python tools/validate_ww_repo.py` -> PASS
    - `git diff --check` -> PASS with line-ending warnings only
- Packet Records:
  - Packet Created: false
  - Rationale: this round implements repo validator/test/docs surfaces directly in the local workspace and does not create verifier packets or activate `task-runtime-v1`.
- Review Records:
  - Lane ID: lane-verifier-validator-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: requested coverage and dormant-only boundaries are independent required gates
  - Execution ID: review-verifier-validator-spec-01
  - Packet ID: not created; local review record
  - Attempt ID: attempt-review-verifier-validator-spec-01
  - Review Target Ref: validator coverage points in user request, dispatch plan scope, `tools/validate_ww_verifier_authority_contracts.py`, `tools/test_validate_ww_verifier_authority_contracts.py`, `tools/validate_ww_repo.py`, and `README.md`
  - Reviewer Findings: PASS; no material findings. Required coverage points are represented: reference existence/linkage, legacy non-authority, dispatch template verifier-lane fields, packet dormant verifier gate, working brief preparation, and repo-suite integration.
  - Orchestrator Synthesis: spec scope is satisfied without adding verifier personas, bindings, command execution, repair/scoring/hooks, routing expansion, or `task-runtime-v1` activation.
  - Strict Review Outcome: none
  - Lane ID: lane-verifier-validator-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: validator/test correctness and repo-suite integration are independent required gates
  - Execution ID: review-verifier-validator-code-quality-01
  - Packet ID: not created; local review record
  - Attempt ID: attempt-review-verifier-validator-code-quality-01
  - Review Target Ref: `tools/validate_ww_verifier_authority_contracts.py`, `tools/test_validate_ww_verifier_authority_contracts.py`, and repo-suite output
  - Reviewer Findings: PASS; no material findings. Negative fixtures isolate the intended drift classes, CLI JSON schema is exercised, and repo-suite integration runs the new validator.
  - Orchestrator Synthesis: targeted tests, py_compile, and full repo validation pass. The stale packet hash refresh is documented as current artifact snapshot maintenance caused by the repo validation entrypoint change.
  - Strict Review Outcome: none
  - Lane ID: lane-verifier-validator-doc-clarity-review
  - Lane Type: other
  - Reviewer Persona: documentation-clarity-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: maintainer guidance must be discoverable without implying runtime activation
  - Execution ID: review-verifier-validator-doc-clarity-01
  - Packet ID: not created; local review record
  - Attempt ID: attempt-review-verifier-validator-doc-clarity-01
  - Review Target Ref: `README.md` validation guidance and validator output text
  - Reviewer Findings: PASS; no material findings. README lists the new validator and tests and describes dormant verifier/lane authority checks without implying runtime activation.
  - Orchestrator Synthesis: maintainer guidance is discoverable through README and repo-level validation output.
  - Strict Review Outcome: none
- Human Decision: Approve
- Human Decision By: user
- Human Decision Time: 2026-06-26
- Revision Notes: final approval accepted validator expansion, regression tests, repo-suite integration, README guidance, and documented packet hash refresh as complete.
- Rollup Rule:
  - Approve -> section state becomes `approved` and validator implementation may begin
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level plan state follows required-section aggregation

## Ordering And Parallelism

- Blocking work first: section-verifier-lane-authority-validator-expansion
- Parallel sections: none
- Review loop: validator/tests/docs diff -> targeted tests and repo validation -> spec, code-quality, and documentation-clarity reviews -> orchestrator synthesis -> human judgment

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
- Approval Time: 2026-06-26
- Notes: approval authorizes validator/test/docs-guidance implementation only; no verifier persona, runtime binding, command execution, repair, scoring, hooks, routing expansion, or `task-runtime-v1` activation
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial verifier lane authority validator expansion round
- Supersedes Revision:

## Dispatch Log

- Agents Launched: exec-verifier-validator-expansion-01
- Retry Events:
- Close Events:
  - 2026-06-26: user approved final review-pending state; required section moved to `complete` and plan moved to `completed`.
- Review Lane Transitions:
  - lane-verifier-validator-spec-review -> PASS
  - lane-verifier-validator-code-quality-review -> PASS
  - lane-verifier-validator-doc-clarity-review -> PASS
- Launch Time: 2026-06-26
- Revisions Since Approval: 0
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
