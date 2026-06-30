# Dispatch Plan: Task Runtime V1 Missing Capability Validator Expansion

- Date: 2026-06-30
- Schema Version: 2
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: task-runtime
- Round Slug: 2026-06-30-task-runtime-v1-missing-capability-validator-expansion
- Case Root: `docs/cases/task-runtime/`
- Round Root: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-expansion/`
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

- User Request: `$ww round: task-runtime-v1 missing capability validator expansion. Based on the committed missing capability implementation foundation, extend WorkWork repo validation for dormant missing capability contract surfaces. Update relevant validator and necessary test fixtures, covering reference linkage, legacy non-authority, dispatch template record families and omission rule, working brief preparation guidance, packet source-context fields, and dormant wording. Validator/test/docs guidance only; do not activate task-runtime-v1, add personas, add runtime binding, or implement command execution, routing, packet assembly, repair, scoring, or hooks.`
- Working Brief Reference: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-expansion/working-brief.md`
- Implementation Foundation Source: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-implementation-foundation/dispatch-plan.md`
- Missing Capability Reference: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`
- Verifier Validator Pattern: `tools/validate_ww_verifier_authority_contracts.py`

## Dispatch Summary

- Goal: add repository validation for dormant task-runtime missing-capability contract surfaces
- Relevant Context:
  - the missing capability implementation foundation is committed as `315b577`
  - the active contract now includes a new missing-capability reference plus SKILL, README, dispatch template, working brief template, and packet contract linkages
  - the existing verifier authority validator provides the closest structural pattern for a dormant task-runtime contract validator
- Constraints:
  - validator/test/docs guidance only
  - do not activate `task-runtime-v1`
  - do not add personas
  - do not add runtime binding
  - do not implement command execution, routing, packet assembly, repair, scoring, hooks, or runtime lifecycle behavior
  - preserve `Lifecycle Protocol: legacy` for this round
- Risks:
  - validator could overmatch design/reference examples and reject legitimate dormant documentation
  - validator could undermatch legacy dispatch plans and miss active authority drift
  - new repo-suite integration could break JSON aggregation if the child validator does not follow established payload shape
  - docs guidance could imply runtime activation instead of dormant validation
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Missing Capability Validator Expansion

- Section ID: section-missing-capability-validator-expansion
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: senior-backend-engineer
- Planned Reviewer Persona: spec-reviewer, code-quality-reviewer, documentation-clarity-reviewer
- Planned Reviewer Persona Source: built-in
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: validator coverage must match the requested dormant contract surfaces, preserve runtime exclusions, and keep guidance clear for maintainers
- Planned Specialist Personas:
  - Persona ID: senior-backend-engineer
    - Source: project
    - Runtime Role: worker
    - Selection Rationale: project registry provides an eligible worker-capable specialist for Python validation logic, test harness integration, and controller contract correctness
- Planned Scope:
  - `docs/cases/task-runtime/case.md`
  - `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-expansion/working-brief.md`
  - `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-expansion/dispatch-plan.md`
  - `tools/validate_ww_missing_capability_contracts.py`
  - `tools/test_validate_ww_missing_capability_contracts.py`
  - `tools/validate_ww_repo.py`
  - `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/packets/lifecycle-foundation-code-quality-review-r2.md`
  - `README.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is read-only.
- Planning Rationale: implement a sibling validator for dormant missing-capability surfaces using the verifier authority validator as the local pattern
- Planned Workflow Bindings:
  - `superpowers:test-driven-development`
  - `superpowers:systematic-debugging`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: test-driven
- Worker Mode Rationale: validator behavior needs isolated negative fixtures and repo-suite verification to avoid shallow or brittle checks
- Goal Tuning: validation-biased
- Constraint Interaction Rule: any runtime activation, persona, binding, command execution, routing, packet assembly, repair, scoring, or hook implementation must be deferred to a later approved round
- Planned Review Lanes:
  - Lane ID: lane-missing-capability-validator-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify exact coverage of the user-requested validator surfaces and exclusions
  - Required: true
  - Lane ID: lane-missing-capability-validator-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: inspect validator implementation, fixture isolation, JSON output shape, and repo-suite integration
  - Required: true
  - Lane ID: lane-missing-capability-validator-doc-clarity-review
  - Lane Type: other
  - Reviewer Persona: documentation-clarity-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify README/SKILL guidance says dormant validation only and does not imply runtime activation
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/task-runtime/case.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-expansion/working-brief.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-expansion/dispatch-plan.md`
    - `path_glob`: `tools/validate_ww_missing_capability_contracts.py`
    - `path_glob`: `tools/test_validate_ww_missing_capability_contracts.py`
    - `path_glob`: `tools/validate_ww_repo.py`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/packets/lifecycle-foundation-code-quality-review-r2.md`
    - `path_glob`: `README.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `shared_read_scope`:
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `path_glob`: `tools/validate_ww_verifier_authority_contracts.py`
    - `path_glob`: `tools/test_validate_ww_verifier_authority_contracts.py`
    - `path_glob`: `tools/validate_ww_round_lifecycle.py`
    - `path_glob`: `tools/validate_ww_case_contracts.py`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: missing_capability_reference
      - `artifact_kind`: reference_doc
      - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`
      - `section_anchors`: dormant record families and legacy non-authority rules
    - `artifact_id`: verifier_validator_pattern
      - `artifact_kind`: validator
      - `artifact_path`: `tools/validate_ww_verifier_authority_contracts.py`
      - `section_anchors`: RuleResult, contains_all, read_required_texts, legacy dispatch guard, JSON output
- Scope declaration rule: every writable file in `Planned Scope` appears in `exclusive_write_scope`; runtime code, personas, routing, packet assembly, command execution, repair/scoring/hook behavior, and project registry are excluded. The listed historical reviewer packet may only receive target hash maintenance caused by the approved `tools/validate_ww_repo.py` integration.
- Packet Created: false

## Section Runtime Ledger

### Section: Missing Capability Validator Expansion

- Section ID: section-missing-capability-validator-expansion
- Runtime State: complete
- Active Execution ID: exec-missing-capability-validator-expansion-01
- Active Packet ID: not created; local orchestrator execution
- Active Agent ID: senior-backend-engineer
- Active Attempt ID: attempt-missing-capability-validator-expansion-01
- Active Worker Mode: test-driven
- Active Persona IDs: senior-backend-engineer, spec-reviewer, code-quality-reviewer, documentation-clarity-reviewer
- Active Persona Sources: project, built-in, built-in, built-in
- Active Persona Role Bindings: worker, reviewer, reviewer, reviewer
- Mode Change History: none
- Execution Records:
- Execution ID: exec-missing-capability-validator-expansion-01
- Attempt ID: attempt-missing-capability-validator-expansion-01
- Worker Persona: senior-backend-engineer
- Persona Source: project
- Runtime Role: worker
- Return Status: DONE
- Summary: implemented a new dormant missing-capability contract validator, isolated regression tests, repo-suite integration, scoped README/SKILL guidance, and the required reviewer packet target hash maintenance caused by `tools/validate_ww_repo.py` changing.
- Changed Files:
  - `docs/cases/task-runtime/case.md`
  - `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-expansion/working-brief.md`
  - `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-expansion/dispatch-plan.md`
  - `tools/validate_ww_missing_capability_contracts.py`
  - `tools/test_validate_ww_missing_capability_contracts.py`
  - `tools/validate_ww_repo.py`
  - `README.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/packets/lifecycle-foundation-code-quality-review-r2.md`
- Verification Evidence:
  - `C:\Users\domin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe -m py_compile tools\validate_ww_missing_capability_contracts.py tools\test_validate_ww_missing_capability_contracts.py` -> PASS
  - `C:\Users\domin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe tools\validate_ww_missing_capability_contracts.py --json` -> PASS, 7 rules
  - `C:\Users\domin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe -m unittest tools.test_validate_ww_missing_capability_contracts -v` -> PASS, 9 tests
  - `C:\Users\domin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe tools\validate_ww_persona_packets.py` -> PASS, 288 rules
  - `C:\Users\domin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe tools\validate_ww_repo.py` -> PASS, repository validation passed
  - `git diff --check` -> PASS, with LF/CRLF warnings for README, packet, SKILL, and validate_ww_repo.py
- Packet Records:
- Packet Created: false
- Rationale: this implementation used local persisted round records and did not create worker, reviewer, or verifier packets.
- Attempt Records:
- Attempt Count: 1
- Last Update At: 2026-06-30
- Next Action: await final human approval
- Active Write Scope:
  - `tools/validate_ww_missing_capability_contracts.py`
  - `tools/test_validate_ww_missing_capability_contracts.py`
  - `tools/validate_ww_repo.py`
  - `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/packets/lifecycle-foundation-code-quality-review-r2.md`
  - `README.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - round planning artifacts
- Result Summary: missing-capability contract validation is implemented and integrated into the repo suite; all verification commands pass.
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns:
- Blocker Reason:
- Close State: open
- Superseded Attempt IDs:
- Stale Result Policy: stale attempt returns may be recorded as history only and must not advance canonical runtime state
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Missing Capability Validator Expansion

- Section ID: section-missing-capability-validator-expansion
- Review Target Strategy:
  - review the final validator/test/docs diff against the user-requested dormant missing-capability coverage and scope exclusions
- Review Lane Records:
  - Lane ID: lane-missing-capability-validator-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: requested validator surface coverage and exclusions are primary acceptance criteria
  - Execution ID: review-missing-capability-validator-spec-01
  - Packet ID: not created; local review record
  - Attempt ID: attempt-review-missing-capability-validator-spec-01
  - Review Target Ref: validator/test/docs diff for missing-capability contract coverage
  - Reviewer Findings: PASS; no material findings. The validator covers reference linkage, SKILL/README guidance, dispatch template record families and legacy omission, working brief preparation, packet source-context fields, and legacy non-authority drift without activating task-runtime-v1.
  - Orchestrator Synthesis: requested validator surfaces and exclusions are covered; runtime activation, persona, binding, command execution, routing, packet assembly, repair/scoring/hook behavior, runtime code, and project registry changes were not introduced.
  - Strict Review Outcome: none
  - Lane ID: lane-missing-capability-validator-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: validator implementation and fixtures must avoid false positives/negatives and fit repo-suite conventions
  - Execution ID: review-missing-capability-validator-code-quality-01
  - Packet ID: not created; local review record
  - Attempt ID: attempt-review-missing-capability-validator-code-quality-01
  - Review Target Ref: `tools/validate_ww_missing_capability_contracts.py`, `tools/test_validate_ww_missing_capability_contracts.py`, `tools/validate_ww_repo.py`, and packet hash maintenance
  - Reviewer Findings: PASS; no material findings. The validator follows existing RuleResult/JSON/repo-root conventions, tests isolate temporary repositories and negative fixtures, repo-suite integration uses the standard child-validator path, and packet hash maintenance restores existing packet validation after the repo-suite target changed.
  - Orchestrator Synthesis: implementation is consistent with existing validator patterns and avoids broad runtime semantics.
  - Strict Review Outcome: none
  - Lane ID: lane-missing-capability-validator-doc-clarity-review
  - Lane Type: other
  - Reviewer Persona: documentation-clarity-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: docs guidance must clearly frame dormant validation without implying runtime activation
  - Execution ID: review-missing-capability-validator-doc-clarity-01
  - Packet ID: not created; local review record
  - Attempt ID: attempt-review-missing-capability-validator-doc-clarity-01
  - Review Target Ref: `README.md`, `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`, and new validator rule names
  - Reviewer Findings: PASS; no material findings. The guidance frames the validator as dormant contract alignment and does not imply active missing-capability runtime behavior.
  - Orchestrator Synthesis: maintainer guidance is clear and bounded.
  - Strict Review Outcome: none
- Human Decision: Approve
- Human Decision By: user
- Human Decision Time: 2026-06-30
- Revision Notes: final approval accepted the missing-capability validator expansion; next round should dogfood-audit the new validator coverage and fixture hardness before any activation attempt.
- Rollup Rule:
  - Approve -> section state becomes `accepted` and validator/test/docs implementation may begin
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level plan state follows required-section aggregation

## Ordering And Parallelism

- Blocking work first: section-missing-capability-validator-expansion
- Parallel sections: none
- Review loop: validator/test/docs changes -> spec, code-quality, and documentation-clarity review -> orchestrator synthesis -> human judgment

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
- Notes: approval authorizes validator, test fixture, repo-suite integration, and necessary docs guidance only; no task-runtime-v1 activation, personas, runtime binding, command execution, routing, packet assembly, repair/scoring/hooks, runtime code, or project registry changes
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial task-runtime-v1 missing capability validator expansion round
- Supersedes Revision:

## Dispatch Log

- Agents Launched: exec-missing-capability-validator-expansion-01
- Retry Events:
- Close Events:
- section-missing-capability-validator-expansion -> complete after final human approval
- Review Lane Transitions:
- lane-missing-capability-validator-spec-review -> PASS
- lane-missing-capability-validator-code-quality-review -> PASS
- lane-missing-capability-validator-doc-clarity-review -> PASS
- Launch Time: 2026-06-30
- Revisions Since Approval: 0
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
