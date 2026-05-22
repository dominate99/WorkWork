# Dispatch Plan: Case Path Identity Validator

- Date: 2026-05-22
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: case-based-artifact-layout
- Round Slug: 2026-05-22-case-path-identity-validator
- Case Root: `docs/superpowers/cases/case-based-artifact-layout/`
- Round Root: `docs/superpowers/cases/case-based-artifact-layout/rounds/2026-05-22-case-path-identity-validator/`
- Plan State: completed
- Last Approved Revision: 1
- Rollback Baseline Revision: none
- Task Routing: code/programming
- Main Orchestrator: staff-engineer-orchestrator

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

Path identity rules:

- `Case Root` must resolve to `docs/superpowers/cases/<case_slug>/`
- `Round Root` must resolve to `docs/superpowers/cases/<case_slug>/rounds/<round_slug>/`
- new dispatch-round artifacts are canonically written under `Round Root`
- legacy type-based paths may remain readable during migration, but they are not parallel write targets

## Source Context

- User Request: `当前最大的残余风险不是这次 diff 本身，而是 validator 还没有检查 case-based path identity`
- Working Brief Reference: `docs/superpowers/cases/case-based-artifact-layout/rounds/2026-05-22-case-path-identity-validator/working-brief.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: add repo-local validator coverage for case-based path identity semantics and integrate it into the repo-level validator entrypoint
- Relevant Context: the active contract now requires case and round identity plus case-based canonical paths, but the validator suite does not yet check those semantics
- Constraints:
  - validator-surface changes only by default
  - keep packet, persona, reviewer, and worker-mode semantics out of scope
  - only touch contract text if implementation reveals a concrete ambiguity that blocks stable checks
- Risks:
  - weak checks could allow silent drift back to type-based canonical paths
  - overfit checks could freeze exact wording instead of protecting the contract meaning
  - repo-level aggregation could stay green while skipping the new validator if integration is incomplete
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Case Path Identity Validator

- Section ID: section-case-path-identity-validator
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: staff-engineer-orchestrator
- Planned Reviewer Persona: pm-orchestrator
- Planned Specialist Personas: none
- Planned Scope:
  - `tools/validate_ww_case_path_identity.py`
  - `tools/validate_ww_repo.py`
  - `README.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: validator coverage is the next highest-leverage step now that the case-based path contract exists and needs automated drift protection
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: validate-first
- Worker Mode Rationale: this round should first validate the exact case-path identity semantics now present in the contract, then encode only the smallest stable checks that protect them
- Goal Tuning: validation-biased
- Constraint Interaction Rule: keep the validator semantic enough to catch path drift, but do not widen into broader storage migration behavior
- Planned Review Lanes:
  - Lane ID: lane-case-path-identity-validator-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/superpowers/cases/case-based-artifact-layout/rounds/2026-05-22-case-path-identity-validator/working-brief.md`
    - `path_glob`: `docs/superpowers/cases/case-based-artifact-layout/rounds/2026-05-22-case-path-identity-validator/dispatch-plan.md`
    - `path_glob`: `tools/validate_ww_case_path_identity.py`
    - `path_glob`: `tools/validate_ww_repo.py`
    - `path_glob`: `README.md`
  - `shared_read_scope`:
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `path_glob`: `tools/*.py`
    - `path_glob`: `docs/superpowers/cases/case-based-artifact-layout/**/*`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: `ww_skill_contract`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `section_anchors`: `Working Brief`, `Dispatch Plan File`, `Document Summary Contract`
    - `artifact_id`: `working_brief_template`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `section_anchors`: `Artifact Metadata`, `Scope Preparation`
    - `artifact_id`: `dispatch_plan_template`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `section_anchors`: `Path identity rules`
    - `artifact_id`: `repo_validator`
    - `artifact_kind`: `code`
    - `artifact_path`: `tools/validate_ww_repo.py`
    - `section_anchors`: none
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Case Path Identity Validator

- Section ID: section-case-path-identity-validator
- Runtime State: complete
- Active Execution ID: execution-case-path-identity-validator
- Active Packet ID:
- Active Agent ID:
- Active Attempt ID:
- Active Worker Mode: validate-first
- Mode Change History:
  - Previous Mode:
  - New Mode:
  - Trigger Evidence:
  - Approved By:
  - Changed At:
- Execution Records:
  - Execution ID: execution-case-path-identity-validator
  - Role: orchestrator-implementation
  - Status: DONE
  - Owned Scope: `tools/validate_ww_case_path_identity.py`, `tools/validate_ww_repo.py`, `README.md`, round documents
  - Started At: 2026-05-22 America/Los_Angeles
  - Finished At: 2026-05-22 America/Los_Angeles
- Packet Records:
  - Packet ID:
  - Execution ID:
  - Stage:
  - Template Path:
  - Review Target Ref:
  - Supersedes Attempt ID:
  - Accepts Late Results:
- Attempt Records:
  - Attempt ID: attempt-case-path-identity-validator-1
  - Packet ID:
  - Agent ID:
  - Return Status: DONE
  - Runtime State After Return: complete
  - Launched At: 2026-05-22 America/Los_Angeles
  - Closed At: 2026-05-22 America/Los_Angeles
  - Result Summary: added a section-aware validator for case-based path identity and integrated it into repo-level validation
  - Result Artifact Location: `tools/validate_ww_case_path_identity.py`, `tools/validate_ww_repo.py`, `README.md`
- Attempt Count: 1
- Last Update At: 2026-05-22 America/Los_Angeles
- Next Action: none
- Active Write Scope:
- Result Summary: added repo-local validator coverage for case-based path identity semantics and integrated it into repo-level validation and maintainer guidance
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns:
  - validator semantics could become too brittle if they rely on exact wording instead of path contract structure
  - the current case-based contract changes are still in the working tree and should be stabilized before broader migration work continues
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Case Path Identity Validator

- Section ID: section-case-path-identity-validator
- Review Target Strategy:
  - validate that new rounds require `case_slug`, `round_slug`, `case_root`, and `round_root`
  - validate that canonical default paths point to `docs/superpowers/cases/...`
  - validate that legacy type-based paths are not described as active canonical write targets for new rounds
  - validate that repo-level aggregation includes the new validator explicitly
- Review Lane Records:
  - Lane ID: lane-case-path-identity-validator-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Execution ID: execution-case-path-identity-validator
  - Packet ID:
  - Attempt ID: attempt-case-path-identity-validator-1
  - Review Target Ref:
    - Artifact Path: `tools/validate_ww_case_path_identity.py`
    - Artifact Kind: code
    - Artifact Revision: working-tree
    - Schema Version:
    - Section Anchor:
    - Content Hash:
  - Reviewer Findings: no material findings
  - Orchestrator Synthesis: the validator now checks case and round identity fields, canonical case-based default paths, and the guardrail that legacy type-based paths are not active write targets for new rounds
  - Strict Review Outcome: none
  - Persistence rule: pre-approval plans must preserve this review-lane structure and outcome field pattern; `Review Status` must not reappear here, and durable review-lane data must retain `Reviewer Findings`, `Orchestrator Synthesis`, and the `Strict Review Outcome` field pattern.
  - Applicability rule: `Strict Review Outcome` is required when a strict-review target or durable strict-review result applies; otherwise keep the same field pattern without creating a second schema for valid non-strict lanes.
  - Invalid state note: `Review Status` reappears or durable strict-review outcome data is dropped when applicable.
- Human Decision: Approve
- Revision Notes:
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level `plan_state` is derived from `required_for_goal`

## Ordering And Parallelism

- Blocking work first: `section-case-path-identity-validator`
- Parallel sections: none
- Review loop per section: draft -> reviewer findings -> orchestrator synthesis -> human judgment

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
- Approval Time: 2026-05-22 America/Los_Angeles
- Notes: this pilot round is scoped to validator coverage for case-based path identity semantics only
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial validator round for case-based path identity coverage
- Supersedes Revision:

## Dispatch Log

- Agents Launched: none
- Retry Events:
- Close Events:
- Review Lane Transitions:
  - case-based layout contract changes identified as active dependency
  - validator gap confirmed against the current repo-level validation entrypoint
  - working brief persisted
  - dispatch plan drafted
  - validator implementation completed
  - repo-level validation passed with the new validator included
  - precommit review completed with no material findings
  - human approval received
- Launch Time: 2026-05-22 America/Los_Angeles
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
