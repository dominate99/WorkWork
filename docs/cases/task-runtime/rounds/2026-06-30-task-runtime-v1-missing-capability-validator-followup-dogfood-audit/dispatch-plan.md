# Dispatch Plan: Task Runtime V1 Missing Capability Validator Dogfood Audit

- Date: 2026-06-30
- Schema Version: 2
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: task-runtime
- Round Slug: 2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit
- Case Root: `docs/cases/task-runtime/`
- Round Root: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/`
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

- User Request: `$ww round: task-runtime-v1 missing capability validator dogfood audit. Based on the completed and committed missing capability validator expansion, audit whether the new validator truly covers task-runtime-missing-capabilities reference linkage, SKILL/README guidance, dispatch template record families, working brief missing_capability_preparation, packet source-context dormant fields, legacy non-authority guard, negative fixtures, JSON output, repo-suite integration, and whether checks are too broad or too narrow. Audit and classify only; do not modify validators, add personas, add runtime binding, implement command execution/routing/packet assembly/repair/scoring/hooks, or activate task-runtime-v1. Decide whether a later validator hardening round is needed.`
- Working Brief Reference: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/working-brief.md`
- Validator Source: `tools/validate_ww_missing_capability_contracts.py`
- Validator Tests: `tools/test_validate_ww_missing_capability_contracts.py`
- Repo Suite Source: `tools/validate_ww_repo.py`

## Dispatch Summary

- Goal: dogfood-audit the missing-capability validator for real coverage, fixture hardness, JSON output, repo-suite integration, and overbroad/underbroad checks
- Relevant Context:
  - missing-capability validator expansion was committed as `55eeba6`
  - the validator currently contains seven rule families and isolated unittest fixtures
  - this round should produce an audit/gap report, not code changes
- Constraints:
  - audit and classification only
  - do not modify validators, fixtures, contract docs, personas, runtime binding, runtime behavior, command execution, routing, packet assembly, repair/scoring/hooks, or project registry
  - do not activate `task-runtime-v1`
  - preserve `Lifecycle Protocol: legacy`
- Risks:
  - missing realistic negative fixture drift
  - overbroad guard rejecting valid dormant docs
  - underbroad guard missing active authority drift
  - repo-suite integration not proven in all relevant modes
  - audit accidentally turning into hardening implementation
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Missing Capability Validator Dogfood Audit

- Section ID: section-missing-capability-validator-followup-dogfood-audit
- Section State: accepted
- Runtime State: completed
- Required For Goal: true
- Draft Author Role: test-quality-engineer
- Planned Reviewer Persona: spec-reviewer, code-quality-reviewer, documentation-clarity-reviewer
- Planned Reviewer Persona Source: built-in
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: audit report must cover the requested dogfood dimensions, assess validator and fixture quality, and communicate whether hardening is needed
- Planned Specialist Personas:
  - Persona ID: test-quality-engineer
    - Source: built-in
    - Runtime Role: worker
    - Selection Rationale: validator dogfood audit is dominated by regression fixture quality, evidence strength, false-positive/false-negative analysis, and deterministic test behavior
- Planned Scope:
  - `docs/cases/task-runtime/case.md`
  - `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/working-brief.md`
  - `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/dispatch-plan.md`
  - `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/design-spec.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is read-only.
- Planning Rationale: produce a bounded validator dogfood gap report and hardening recommendation
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:verification-before-completion`
  - `superpowers:requesting-code-review`
- Planned Worker Mode: research-first
- Worker Mode Rationale: inspect and classify existing validator/test behavior before making any hardening recommendation; do not patch implementation
- Goal Tuning: validation-biased
- Constraint Interaction Rule: any validator/test/docs/code change beyond the report itself must be deferred to a later approved hardening round
- Planned Review Lanes:
  - Lane ID: lane-missing-capability-validator-dogfood-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify the report covers all requested audit surfaces and exclusions
  - Required: true
  - Lane ID: lane-missing-capability-validator-dogfood-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify validator/fixture coverage analysis is technically sound and not too broad or too narrow
  - Required: true
  - Lane ID: lane-missing-capability-validator-dogfood-doc-clarity-review
  - Lane Type: other
  - Reviewer Persona: documentation-clarity-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify the gap report is clear and gives an actionable hardening recommendation without implying implementation
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/task-runtime/case.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/working-brief.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/dispatch-plan.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/design-spec.md`
  - `shared_read_scope`:
    - `path_glob`: `tools/validate_ww_missing_capability_contracts.py`
    - `path_glob`: `tools/test_validate_ww_missing_capability_contracts.py`
    - `path_glob`: `tools/validate_ww_repo.py`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `README.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-expansion/dispatch-plan.md`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: missing_capability_validator
      - `artifact_kind`: validator
      - `artifact_path`: `tools/validate_ww_missing_capability_contracts.py`
      - `section_anchors`: WWMC001-WWMC007 and legacy dispatch guard
    - `artifact_id`: dogfood_audit_report
      - `artifact_kind`: design_spec
      - `artifact_path`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/design-spec.md`
      - `section_anchors`: coverage matrix, fixture audit, overbroad/underbroad analysis, hardening recommendation
- Scope declaration rule: every writable file in `Planned Scope` appears in `exclusive_write_scope`; validator code, fixtures, runtime behavior, personas, routing, packet assembly, command execution, repair/scoring/hook behavior, and project registry are excluded.
- Packet Created: false

## Section Runtime Ledger

### Section: Missing Capability Validator Dogfood Audit

- Section ID: section-missing-capability-validator-followup-dogfood-audit
- Runtime State: completed
- Active Execution ID: exec-missing-capability-validator-dogfood-audit-01
- Active Packet ID:
- Active Agent ID: test-quality-engineer
- Active Attempt ID: attempt-missing-capability-validator-dogfood-audit-01
- Active Worker Mode: research-first
- Active Persona IDs: test-quality-engineer, spec-reviewer, code-quality-reviewer, documentation-clarity-reviewer
- Active Persona Sources: built-in
- Active Persona Role Bindings: test-quality-engineer=worker; spec-reviewer=reviewer; code-quality-reviewer=reviewer; documentation-clarity-reviewer=reviewer
- Mode Change History: none
- Execution Records:
  - Execution ID: exec-missing-capability-validator-dogfood-audit-01
    - Attempt ID: attempt-missing-capability-validator-dogfood-audit-01
    - Agent ID: test-quality-engineer
    - Worker Mode: research-first
    - Result Artifact Location: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/design-spec.md`
    - Summary: audited missing-capability validator coverage, negative fixture strength, JSON output, repo-suite integration, and overbroad/underbroad risks
    - Findings:
      - P2: WWMC007 likely misses single missing-capability record-family assignments in legacy dispatch plans when the canonical heading is absent.
      - P2: the existing legacy negative fixture does not isolate record-family fallback because the heading alone can trigger failure.
      - P3: raw record-family name prose can become a false positive if two field names appear outside an authority block.
- Packet Records:
- Attempt Records:
  - Attempt ID: attempt-missing-capability-validator-dogfood-audit-01
    - Started At: 2026-06-30
    - Completed At: 2026-06-30
    - Result Artifact Location: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/design-spec.md`
    - Status: completed
- Attempt Count: 1
- Last Update At: 2026-06-30
- Next Action: round complete; ready for follow-up hardening round if requested
- Active Write Scope:
  - `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/design-spec.md`
  - round planning artifacts
- Result Summary: missing-capability validator covers the requested dormant contract scaffold and repo-suite integration, but WWMC007 needs focused hardening before activation-grade reliance
- Canonical Result Artifact Location: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/design-spec.md`
- Concerns:
  - single record-family legacy authority drift may pass
  - current legacy fixture does not isolate record-family fallback behavior
  - raw field-name prose may be overflagged by the fallback heuristic
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy: stale attempt returns may be recorded as history only and must not advance canonical runtime state
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Missing Capability Validator Dogfood Audit

- Section ID: section-missing-capability-validator-followup-dogfood-audit
- Review Target Strategy:
  - review the produced `design-spec.md` gap report against the validator source, tests, repo-suite integration, and user-requested dogfood dimensions
- Review Lane Records:
  - Lane ID: lane-missing-capability-validator-dogfood-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: requested audit coverage and exclusions are primary acceptance criteria
  - Execution ID: review-missing-capability-validator-dogfood-spec-01
  - Packet ID:
  - Attempt ID: review-attempt-missing-capability-validator-dogfood-spec-01
  - Review Target Ref: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/design-spec.md`
  - Reviewer Findings: no blocking findings; the report covers every requested audit surface and preserves the no-implementation, no-activation exclusions
  - Orchestrator Synthesis: accepted; the report directly answers whether a hardening round is needed and scopes it narrowly
  - Strict Review Outcome: pass
  - Lane ID: lane-missing-capability-validator-dogfood-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: validator and fixture coverage analysis must be technically credible
  - Execution ID: review-missing-capability-validator-dogfood-code-quality-01
  - Packet ID:
  - Attempt ID: review-attempt-missing-capability-validator-dogfood-code-quality-01
  - Review Target Ref: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/design-spec.md`
  - Reviewer Findings: no blocking findings; the P2 single-family underbreadth and fixture-isolation gap are technically credible and trace to the validator heuristic
  - Orchestrator Synthesis: accepted; the hardening recommendation is limited to validator/tests and does not alter runtime behavior
  - Strict Review Outcome: pass
  - Lane ID: lane-missing-capability-validator-dogfood-doc-clarity-review
  - Lane Type: other
  - Reviewer Persona: documentation-clarity-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: the gap report must be clear and actionable as future-work guidance
  - Execution ID: review-missing-capability-validator-dogfood-doc-clarity-01
  - Packet ID:
  - Attempt ID: review-attempt-missing-capability-validator-dogfood-doc-clarity-01
  - Review Target Ref: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/design-spec.md`
  - Reviewer Findings: no blocking findings; the coverage matrix, findings, and recommendation are readable as future-work guidance
  - Orchestrator Synthesis: accepted; the report avoids implying validator changes were made in this round
  - Strict Review Outcome: pass
- Human Decision: Approve
- Revision Notes: dogfood audit approved; no validator, fixture, runtime, persona, routing, packet, command execution, repair/scoring/hook, activation, or project registry changes were made
- Rollup Rule:
  - Approve -> section state becomes `accepted` and plan state becomes `completed`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level plan state follows required-section aggregation

## Ordering And Parallelism

- Blocking work first: section-missing-capability-validator-followup-dogfood-audit
- Parallel sections: none
- Review loop: dogfood gap report -> spec, code-quality, and documentation-clarity review -> orchestrator synthesis -> human judgment

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
- Notes: approval authorizes audit/report work only; no validator, fixture, runtime, persona, routing, packet, command execution, repair/scoring/hook, activation, or project registry changes
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial missing-capability validator dogfood audit round
- Supersedes Revision:

## Dispatch Log

- Agents Launched:
  - test-quality-engineer (simulated inline worker per approved legacy plan)
- Retry Events:
- Close Events:
  - 2026-06-30: user approved dogfood audit report; round closed with recommendation to run a focused WWMC007 validator hardening round before activation-grade reliance
- Review Lane Transitions:
  - lane-missing-capability-validator-dogfood-spec-review: pass
  - lane-missing-capability-validator-dogfood-code-quality-review: pass
  - lane-missing-capability-validator-dogfood-doc-clarity-review: pass
- Launch Time: 2026-06-30
- Revisions Since Approval: 0
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
