# Dispatch Plan: Missing Capability Legacy Guard Validator Hardening

- Date: 2026-07-01
- Schema Version: 2
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: task-runtime
- Round Slug: 2026-07-01-missing-capability-legacy-guard-validator-hardening
- Case Root: `docs/cases/task-runtime/`
- Round Root: `docs/cases/task-runtime/rounds/2026-07-01-missing-capability-legacy-guard-validator-hardening/`
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

- User Request: `$ww round: missing capability legacy guard validator hardening. Based on the task-runtime-v1 missing capability validator dogfood audit, fix the WWMC007 legacy non-authority guard coverage gap. Harden validate_ww_missing_capability_contracts.py and tests so any YAML-like active missing-capability record family in a legacy dispatch fails; add heading-only, single-family without heading, multi-family without heading, and dormant/prose-only allowed fixtures; avoid raw field-name prose false positives. Only change validator/tests and necessary test notes; do not change dormant contract, personas, project registry, routing, packet assembly, runtime command execution, repair/scoring/hooks, or activate task-runtime-v1.`
- Working Brief Reference: `docs/cases/task-runtime/rounds/2026-07-01-missing-capability-legacy-guard-validator-hardening/working-brief.md`
- Dogfood Audit Reference: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/design-spec.md`
- Validator Source: `tools/validate_ww_missing_capability_contracts.py`
- Validator Tests: `tools/test_validate_ww_missing_capability_contracts.py`

## Dispatch Summary

- Goal: harden WWMC007 legacy non-authority validation so YAML-like active missing-capability record-family assignments in legacy dispatch plans are rejected while dormant prose is accepted
- Relevant Context:
  - the previous dogfood audit found one underbroad guard, one weak fixture shape, and one possible prose false-positive risk
  - the current validator scans legacy dispatch plans under `docs/cases/**/dispatch-plan.md`
  - this plan itself must avoid rendering multiple active missing-capability assignment examples because it is also a legacy dispatch plan
- Constraints:
  - only change validator/tests and necessary test notes
  - do not change dormant contracts, README, SKILL, templates, personas, project registry, routing, packet assembly, runtime command execution, repair/scoring/hooks, or activation state
  - do not activate `task-runtime-v1`
  - preserve `Lifecycle Protocol: legacy`
- Risks:
  - false positives from raw field-name prose
  - false negatives for one-family assignment drift
  - tests that pass through heading detection rather than assignment detection
  - accidentally broadening the round beyond WWMC007
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Missing Capability Legacy Guard Hardening

- Section ID: section-missing-capability-legacy-guard-hardening
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: test-quality-engineer
- Planned Reviewer Persona: spec-reviewer, code-quality-reviewer, documentation-clarity-reviewer
- Planned Reviewer Persona Source: built-in
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: this validator hardening must stay scoped, technically precise, and clear about test-only fixture authority
- Planned Specialist Personas:
  - Persona ID: test-quality-engineer
    - Source: built-in
    - Runtime Role: worker
    - Selection Rationale: WWMC007 hardening is driven by fixture isolation, false-positive/false-negative control, and deterministic regression tests
- Planned Scope:
  - `docs/cases/task-runtime/case.md`
  - `docs/cases/task-runtime/rounds/2026-07-01-missing-capability-legacy-guard-validator-hardening/working-brief.md`
  - `docs/cases/task-runtime/rounds/2026-07-01-missing-capability-legacy-guard-validator-hardening/dispatch-plan.md`
  - `tools/validate_ww_missing_capability_contracts.py`
  - `tools/test_validate_ww_missing_capability_contracts.py`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is read-only.
- Planning Rationale: implement the focused hardening recommended by the dogfood audit without touching dormant contracts or runtime activation
- Planned Workflow Bindings:
  - `superpowers:test-driven-development`
  - `superpowers:systematic-debugging`
  - `superpowers:verification-before-completion`
  - `superpowers:requesting-code-review`
- Planned Worker Mode: test-first
- Worker Mode Rationale: add failing regression fixtures for the known WWMC007 gaps before changing the validator
- Goal Tuning: validation-biased
- Constraint Interaction Rule: if a broader contract, routing, packet, or activation change appears useful, record it as future work and do not implement it in this round
- Planned Review Lanes:
  - Lane ID: lane-missing-capability-legacy-guard-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify the implementation covers the requested fixture types and preserves all exclusions
  - Required: true
  - Lane ID: lane-missing-capability-legacy-guard-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify guard logic detects active assignments without raw-prose false positives
  - Required: true
  - Lane ID: lane-missing-capability-legacy-guard-doc-clarity-review
  - Lane Type: other
  - Reviewer Persona: documentation-clarity-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify any test notes and final explanation are clear without implying dormant contract changes
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/task-runtime/case.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-07-01-missing-capability-legacy-guard-validator-hardening/working-brief.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-07-01-missing-capability-legacy-guard-validator-hardening/dispatch-plan.md`
    - `path_glob`: `tools/validate_ww_missing_capability_contracts.py`
    - `path_glob`: `tools/test_validate_ww_missing_capability_contracts.py`
  - `shared_read_scope`:
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/design-spec.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`
    - `path_glob`: `tools/validate_ww_repo.py`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: missing_capability_validator
      - `artifact_kind`: validator
      - `artifact_path`: `tools/validate_ww_missing_capability_contracts.py`
      - `section_anchors`: WWMC007 legacy dispatch guard
    - `artifact_id`: missing_capability_validator_tests
      - `artifact_kind`: test_module
      - `artifact_path`: `tools/test_validate_ww_missing_capability_contracts.py`
      - `section_anchors`: isolated legacy guard fixtures
- Scope declaration rule: every writable file in `Planned Scope` appears in `exclusive_write_scope`; dormant contracts, personas, routing, packet assembly, runtime command execution, repair/scoring/hook behavior, and project registry are excluded.
- Packet Created: false

## Section Runtime Ledger

### Section: Missing Capability Legacy Guard Hardening

- Section ID: section-missing-capability-legacy-guard-hardening
- Runtime State: complete
- Active Execution ID: exec-missing-capability-legacy-guard-hardening-01
- Active Packet ID:
- Active Agent ID: test-quality-engineer
- Active Attempt ID: attempt-missing-capability-legacy-guard-hardening-01
- Active Worker Mode: test-first
- Active Persona IDs: test-quality-engineer, spec-reviewer, code-quality-reviewer, documentation-clarity-reviewer
- Active Persona Sources: built-in
- Active Persona Role Bindings: test-quality-engineer=worker; spec-reviewer=reviewer; code-quality-reviewer=reviewer; documentation-clarity-reviewer=reviewer
- Mode Change History: none
- Execution Records:
  - Execution ID: exec-missing-capability-legacy-guard-hardening-01
    - Attempt ID: attempt-missing-capability-legacy-guard-hardening-01
    - Agent ID: test-quality-engineer
    - Worker Mode: test-first
    - Result Artifact Location: `tools/validate_ww_missing_capability_contracts.py`, `tools/test_validate_ww_missing_capability_contracts.py`
    - Summary: hardened WWMC007 to detect YAML-like active record-family assignments at line start while allowing raw field-name prose; added isolated heading-only, single-family, multi-family, and prose fixtures
    - Red Evidence: focused unit tests failed before implementation on single-family assignment drift and raw-prose false-positive cases
    - Green Evidence: focused unit tests now pass with 13 tests
- Packet Records:
- Attempt Records:
  - Attempt ID: attempt-missing-capability-legacy-guard-hardening-01
    - Started At: 2026-07-01
    - Completed At: 2026-07-01
    - Result Artifact Location: `tools/validate_ww_missing_capability_contracts.py`, `tools/test_validate_ww_missing_capability_contracts.py`
    - Status: completed
- Attempt Count: 1
- Last Update At: 2026-07-01
- Next Action: round complete; ready for commit when requested
- Active Write Scope:
  - `tools/validate_ww_missing_capability_contracts.py`
  - `tools/test_validate_ww_missing_capability_contracts.py`
  - round planning artifacts
- Result Summary: WWMC007 now rejects heading-only active blocks and YAML-like active record-family assignments, including single-family drift, while allowing raw field-name prose that does not assign fields
- Canonical Result Artifact Location: `tools/validate_ww_missing_capability_contracts.py`, `tools/test_validate_ww_missing_capability_contracts.py`
- Concerns:
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy: stale attempt returns may be recorded as history only and must not advance canonical runtime state
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Missing Capability Legacy Guard Hardening

- Section ID: section-missing-capability-legacy-guard-hardening
- Review Target Strategy:
  - review the final validator and test diff against the dogfood audit report, user constraints, and focused verification results
- Review Lane Records:
  - Lane ID: lane-missing-capability-legacy-guard-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: requested scope and exclusion boundaries are primary acceptance criteria
  - Execution ID: review-missing-capability-legacy-guard-spec-01
  - Packet ID:
  - Attempt ID: review-attempt-missing-capability-legacy-guard-spec-01
  - Review Target Ref: `git diff -- tools/validate_ww_missing_capability_contracts.py tools/test_validate_ww_missing_capability_contracts.py`
  - Reviewer Findings: no material findings; the implementation covers heading-only, single-family, multi-family, and prose-allowed fixtures without changing dormant contracts or activation state
  - Orchestrator Synthesis: accepted; scope stayed limited to validator/tests and planning artifacts
  - Strict Review Outcome: pass
  - Lane ID: lane-missing-capability-legacy-guard-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: validator matching semantics must be narrow enough to avoid prose false positives and broad enough to catch active assignments
  - Execution ID: review-missing-capability-legacy-guard-code-quality-01
  - Packet ID:
  - Attempt ID: review-attempt-missing-capability-legacy-guard-code-quality-01
  - Review Target Ref: `git diff -- tools/validate_ww_missing_capability_contracts.py tools/test_validate_ww_missing_capability_contracts.py`
  - Reviewer Findings: no material findings; the regex is constrained to line-start YAML-like assignments and avoids the previous normalized-text count false positive
  - Orchestrator Synthesis: accepted; focused tests and repo validation cover the intended regression surface
  - Strict Review Outcome: pass
  - Lane ID: lane-missing-capability-legacy-guard-doc-clarity-review
  - Lane Type: other
  - Reviewer Persona: documentation-clarity-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: any necessary test explanation must be clear and not imply runtime activation
  - Execution ID: review-missing-capability-legacy-guard-doc-clarity-01
  - Packet ID:
  - Attempt ID: review-attempt-missing-capability-legacy-guard-doc-clarity-01
  - Review Target Ref: `git diff -- tools/validate_ww_missing_capability_contracts.py tools/test_validate_ww_missing_capability_contracts.py`
  - Reviewer Findings: no material findings; no contract or runtime docs were changed, and final explanation can describe the fixture behavior without implying activation
  - Orchestrator Synthesis: accepted; no documentation follow-up required
  - Strict Review Outcome: pass
- Human Decision: Approve
- Revision Notes: implementation and review approved; no dormant contract, persona, project registry, routing, packet assembly, runtime command execution, repair/scoring/hook, or activation changes were made
- Rollup Rule:
  - Approve -> section state becomes `accepted` and plan state becomes `completed`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level plan state follows required-section aggregation

## Ordering And Parallelism

- Blocking work first: section-missing-capability-legacy-guard-hardening
- Parallel sections: none
- Review loop: test-first hardening -> focused verification -> spec, code-quality, and documentation-clarity review -> orchestrator synthesis -> human judgment

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
- Notes: approval authorizes only focused WWMC007 validator/test hardening and necessary test notes
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial missing-capability legacy guard validator hardening round
- Supersedes Revision:

## Dispatch Log

- Agents Launched:
  - test-quality-engineer (inline worker per approved legacy plan)
- Retry Events:
- Close Events:
  - 2026-07-01: user approved reviewed validator hardening; round closed
- Review Lane Transitions:
  - lane-missing-capability-legacy-guard-spec-review: pass
  - lane-missing-capability-legacy-guard-code-quality-review: pass
  - lane-missing-capability-legacy-guard-doc-clarity-review: pass
- Launch Time: 2026-07-01
- Revisions Since Approval: 0
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
