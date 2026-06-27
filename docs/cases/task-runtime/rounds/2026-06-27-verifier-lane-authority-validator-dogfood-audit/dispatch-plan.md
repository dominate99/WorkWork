# Dispatch Plan: Verifier Lane Authority Validator Dogfood Audit

- Date: 2026-06-27
- Schema Version: 2
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: task-runtime
- Round Slug: 2026-06-27-verifier-lane-authority-validator-dogfood-audit
- Case Root: `docs/cases/task-runtime/`
- Round Root: `docs/cases/task-runtime/rounds/2026-06-27-verifier-lane-authority-validator-dogfood-audit/`
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

- User Request: `$ww round: verifier lane authority validator dogfood audit. Based on the completed and pushed verifier lane authority validator expansion, audit whether the new validator truly covers task-runtime-verification reference linkage, legacy non-authority guard, dispatch template verifier lane block, packet dormant verifier gate, working brief verification preparation, negative fixtures, repo-suite integration, and whether checks are too broad or too narrow. Audit and classify only; do not modify the validator, add verifier personas, add runtime binding, implement command execution, repair/scoring/hooks, or activate task-runtime-v1. Decide whether a later validator hardening round is needed.`
- Working Brief Reference: `docs/cases/task-runtime/rounds/2026-06-27-verifier-lane-authority-validator-dogfood-audit/working-brief.md`
- Verifier Validator Expansion Commit: `6b6eaf2 Add verifier authority contract validation`
- Validator Under Audit: `tools/validate_ww_verifier_authority_contracts.py`
- Validator Tests Under Audit: `tools/test_validate_ww_verifier_authority_contracts.py`
- Dormant Verifier Reference: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`

## Dispatch Summary

- Goal: audit whether the newly pushed verifier/lane authority validator has sufficient real coverage and whether a future hardening round is warranted
- Relevant Context: the validator is already implemented and pushed; this round dogfoods coverage and classification only
- Constraints:
  - do not edit validator code, tests, contract templates, README, SKILL, packet contract, project registry, or runtime bindings
  - do not add verifier personas or verifier runtime binding
  - do not implement command execution, repair, scoring, hooks, routing expansion, secondary tags, or `task-runtime-v1` activation
  - produce only a persisted dogfood gap report/design spec and round-local controller records
  - classify over-broad and under-broad checks separately
- Risks:
  - audit may mistake string-presence checks for semantic coverage
  - audit may overlook false positives against legacy historical prose
  - audit may recommend hardening without enough evidence
  - audit may drift into implementation instead of classification
  - review lanes may conflate current sufficiency with future ideal coverage
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Verifier Lane Authority Validator Dogfood Audit

- Section ID: section-verifier-validator-dogfood-audit
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: senior-backend-engineer
- Planned Reviewer Persona: spec-reviewer, code-quality-reviewer, documentation-clarity-reviewer
- Planned Reviewer Persona Source: built-in
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: requirement coverage, validator/test reasoning, and persisted report clarity are each independently material; built-in fallback is used because no project reviewer covers this WorkWork validator dogfood surface more strongly
- Planned Specialist Personas:
  - Persona ID: senior-backend-engineer
    - Source: built-in
    - Runtime Role: worker
    - Selection Rationale: validator rule semantics, negative fixture quality, and repo-suite integration need tooling judgment; built-in fallback is used because no eligible project worker persona covers this WorkWork validator audit more strongly
- Planned Scope:
  - `docs/cases/task-runtime/case.md`
  - `docs/cases/task-runtime/rounds/2026-06-27-verifier-lane-authority-validator-dogfood-audit/working-brief.md`
  - `docs/cases/task-runtime/rounds/2026-06-27-verifier-lane-authority-validator-dogfood-audit/dispatch-plan.md`
  - `docs/cases/task-runtime/rounds/2026-06-27-verifier-lane-authority-validator-dogfood-audit/design-spec.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is read-only.
- Planning Rationale: produce one persisted dogfood report that audits validator coverage against requested surfaces and decides whether hardening should be scheduled
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: research-first
- Worker Mode Rationale: inspect validator, tests, contract references, and repo-suite integration before classifying gaps; do not edit implementation surfaces
- Goal Tuning: validation-biased
- Constraint Interaction Rule: if the audit discovers a validator defect or hardening need, record it as a finding and defer fixes to a later approved round
- Planned Review Lanes:
  - Lane ID: lane-verifier-validator-dogfood-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify that every user-requested dogfood surface is addressed and all exclusions remain honored
  - Required: true
  - Lane ID: lane-verifier-validator-dogfood-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: inspect the report's reasoning about validator implementation, fixture isolation, false positives, false negatives, and repo-suite integration
  - Required: true
  - Lane ID: lane-verifier-validator-dogfood-doc-clarity-review
  - Lane Type: other
  - Reviewer Persona: documentation-clarity-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify the dogfood report is concise, actionable, and clear enough to justify or reject a later hardening round
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/task-runtime/case.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-27-verifier-lane-authority-validator-dogfood-audit/working-brief.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-27-verifier-lane-authority-validator-dogfood-audit/dispatch-plan.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-27-verifier-lane-authority-validator-dogfood-audit/design-spec.md`
  - `shared_read_scope`:
    - `path_glob`: `tools/validate_ww_verifier_authority_contracts.py`
    - `path_glob`: `tools/test_validate_ww_verifier_authority_contracts.py`
    - `path_glob`: `tools/validate_ww_repo.py`
    - `path_glob`: `README.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-25-verifier-lane-authority-validator-expansion/**/*`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: verifier_authority_validator
      - `artifact_kind`: python_validator
      - `artifact_path`: `tools/validate_ww_verifier_authority_contracts.py`
      - `section_anchors`: WWVA001 through WWVA007 rule coverage
    - `artifact_id`: verifier_authority_validator_tests
      - `artifact_kind`: python_test
      - `artifact_path`: `tools/test_validate_ww_verifier_authority_contracts.py`
      - `section_anchors`: negative fixtures and CLI JSON failure schema
    - `artifact_id`: verifier_authority_dogfood_report
      - `artifact_kind`: design_spec
      - `artifact_path`: `docs/cases/task-runtime/rounds/2026-06-27-verifier-lane-authority-validator-dogfood-audit/design-spec.md`
      - `section_anchors`: coverage classification, false-positive risk, false-negative risk, hardening recommendation
- Scope declaration rule: every writable file in `Planned Scope` appears in `exclusive_write_scope`; validator and contract files are read-only targets.
- Packet Created: false

## Section Runtime Ledger

### Section: Verifier Lane Authority Validator Dogfood Audit

- Section ID: section-verifier-validator-dogfood-audit
- Runtime State: complete
- Active Execution ID: exec-verifier-validator-dogfood-audit-01
- Active Packet ID: not created; local orchestrator execution
- Active Agent ID: senior-backend-engineer
- Active Attempt ID: attempt-verifier-validator-dogfood-audit-01
- Active Worker Mode: research-first
- Active Persona IDs: senior-backend-engineer, spec-reviewer, code-quality-reviewer, documentation-clarity-reviewer
- Active Persona Sources: built-in
- Active Persona Role Bindings: worker, reviewer, reviewer, reviewer
- Mode Change History: none
- Execution Records:
  - Execution ID: exec-verifier-validator-dogfood-audit-01
  - Attempt ID: attempt-verifier-validator-dogfood-audit-01
  - Worker Persona: senior-backend-engineer
  - Persona Source: built-in
  - Runtime Role: worker
  - Return Status: DONE
  - Summary: audited verifier/lane authority validator coverage and produced `design-spec.md` as a dogfood gap report. The report classifies current coverage as sufficient for the dormant stage and recommends deferring hardening until `task-runtime-v1` activation becomes concrete or the verifier lane schema changes.
  - Changed Files:
    - `docs/cases/task-runtime/case.md`
    - `docs/cases/task-runtime/rounds/2026-06-27-verifier-lane-authority-validator-dogfood-audit/working-brief.md`
    - `docs/cases/task-runtime/rounds/2026-06-27-verifier-lane-authority-validator-dogfood-audit/dispatch-plan.md`
    - `docs/cases/task-runtime/rounds/2026-06-27-verifier-lane-authority-validator-dogfood-audit/design-spec.md`
  - Verification Evidence:
    - `python tools/validate_ww_verifier_authority_contracts.py --json` -> PASS, 7 rules
    - `python -m unittest tools.test_validate_ww_verifier_authority_contracts -v` -> PASS, 9 tests
    - `python tools/validate_ww_round_lifecycle.py` -> PASS, 100 rules
- Packet Records:
  - Packet Created: false
  - Rationale: this audit used local persisted round records and did not create verifier, worker, or reviewer packets.
- Review Records:
  - Lane ID: lane-verifier-validator-dogfood-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: requested coverage surfaces and exclusions are the primary success criteria
  - Execution ID: review-verifier-validator-dogfood-spec-01
  - Packet ID: not created; local review record
  - Attempt ID: attempt-review-verifier-validator-dogfood-spec-01
  - Review Target Ref: `docs/cases/task-runtime/rounds/2026-06-27-verifier-lane-authority-validator-dogfood-audit/design-spec.md`
  - Reviewer Findings: PASS; no material findings. The report addresses reference linkage, legacy non-authority, dispatch template block coverage, packet dormant gate, working brief preparation, negative fixtures, repo-suite integration, and over/under-broad behavior while preserving all exclusions.
  - Orchestrator Synthesis: spec coverage is complete for an audit-only round; any hardening is deferred to a later approved round.
  - Strict Review Outcome: none
  - Lane ID: lane-verifier-validator-dogfood-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: validator/test quality reasoning is needed before recommending hardening
  - Execution ID: review-verifier-validator-dogfood-code-quality-01
  - Packet ID: not created; local review record
  - Attempt ID: attempt-review-verifier-validator-dogfood-code-quality-01
  - Review Target Ref: `tools/validate_ww_verifier_authority_contracts.py`, `tools/test_validate_ww_verifier_authority_contracts.py`, `tools/validate_ww_repo.py`, and the dogfood report
  - Reviewer Findings: PASS; no material findings. The report correctly distinguishes presence-based sentinel coverage from structural schema validation and identifies representative-fixture limits without overstating current risk.
  - Orchestrator Synthesis: validator/test reasoning is sound for the dormant stage; recommended hardening is appropriately conditional.
  - Strict Review Outcome: none
  - Lane ID: lane-verifier-validator-dogfood-doc-clarity-review
  - Lane Type: other
  - Reviewer Persona: documentation-clarity-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: dogfood classification must be actionable for a later round decision
  - Execution ID: review-verifier-validator-dogfood-doc-clarity-01
  - Packet ID: not created; local review record
  - Attempt ID: attempt-review-verifier-validator-dogfood-doc-clarity-01
  - Review Target Ref: `docs/cases/task-runtime/rounds/2026-06-27-verifier-lane-authority-validator-dogfood-audit/design-spec.md`
  - Reviewer Findings: PASS; no material findings. The report clearly separates current sufficiency, false-positive risk, false-negative risk, and hardening trigger conditions.
  - Orchestrator Synthesis: report is actionable for deciding whether to open a hardening round now or defer.
  - Strict Review Outcome: none
- Human Decision: Approve
- Human Decision By: user
- Human Decision Time: 2026-06-27
- Revision Notes: final approval accepted the dogfood audit report and its recommendation to defer validator hardening until task-runtime-v1 activation becomes concrete or verifier lane schema changes.
- Rollup Rule:
  - Approve -> section state becomes `approved` and audit execution may begin
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level plan state follows required-section aggregation

## Ordering And Parallelism

- Blocking work first: section-verifier-validator-dogfood-audit
- Parallel sections: none
- Review loop: audit report draft -> spec, code-quality, and documentation-clarity review -> orchestrator synthesis -> human judgment

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
- Notes: approval authorizes audit/report creation only; no validator edits, verifier personas, runtime bindings, command execution, repair/scoring/hooks, routing expansion, secondary tags, or `task-runtime-v1` activation
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial verifier lane authority validator dogfood audit round
- Supersedes Revision:

## Dispatch Log

- Agents Launched: exec-verifier-validator-dogfood-audit-01
- Retry Events:
- Close Events:
  - 2026-06-27: user approved final review-pending state; required audit section moved to `complete` and plan moved to `completed`.
- Review Lane Transitions:
  - lane-verifier-validator-dogfood-spec-review -> PASS
  - lane-verifier-validator-dogfood-code-quality-review -> PASS
  - lane-verifier-validator-dogfood-doc-clarity-review -> PASS
- Launch Time: 2026-06-27
- Revisions Since Approval: 0
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
