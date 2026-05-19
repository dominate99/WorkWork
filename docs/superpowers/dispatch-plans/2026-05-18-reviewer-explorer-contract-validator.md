# Dispatch Plan: Reviewer And Explorer Contract Validator

- Date: 2026-05-18
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Plan State: completed
- Last Approved Revision: none
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

## Source Context

- User Request: `把 reviewer / explorer contract validator 变成一个 $ww workflow`
- Working Brief Reference: `docs/superpowers/working-briefs/2026-05-18-reviewer-explorer-contract-validator-v1.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: add a repo-local validator for reviewer and explorer role contracts and integrate it into the existing WW repository validation flow
- Relevant Context: the repository already validates packaged skill frontmatter and worker `work_mode` contracts, but reviewer and explorer remain unprotected by dedicated automated contract checks
- Constraints:
  - reviewer and explorer must be treated as role contracts, not `work_mode` contracts
  - first version stays bounded to `SKILL.md`, `subagent-packet-contract.md`, `reviewer-prompt.md`, `explorer-prompt.md`, and repo-level validation integration
  - first version should not expand into persona quality or registry validation
- Risks:
  - role prompts and packet defaults could drift apart without a shared validator
  - reviewer or explorer could accidentally gain worker-only semantics
  - explorer has less example coverage than reviewer, which can tempt overfitting or underchecking
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Reviewer And Explorer Role Contract Validator

- Section ID: section-role-contract-validator
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: senior-backend-engineer
- Planned Reviewer Persona: secure-software-engineer
- Planned Specialist Personas: senior-backend-engineer
- Planned Scope:
  - `tools/validate_ww_role_contracts.py`
  - `tools/validate_ww_repo.py`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: one bounded validator plus one repo-level integration point is simpler and safer than parallel edits because rule shape and entrypoint behavior must agree
- Planned Workflow Bindings:
  - `superpowers:test-driven-development`
  - `superpowers:subagent-driven-development`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: validate-first
- Worker Mode Rationale: this section extends an existing validation system and should confirm the role-contract boundary before implementation details are locked
- Goal Tuning: validation-biased
- Constraint Interaction Rule: preserve reviewer/explorer role boundaries and avoid adding worker-style `mode` logic or persona-quality scoring
- Planned Review Lanes:
  - Lane ID: lane-role-validator-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: secure-software-engineer
  - Required: true
  - Lane ID: lane-role-validator-code-review
  - Lane Type: code-quality-review
  - Reviewer Persona: secure-software-engineer
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/superpowers/specs/2026-05-18-reviewer-explorer-contract-validator-design.md`
    - `path_glob`: `docs/superpowers/plans/2026-05-18-reviewer-explorer-contract-validator.md`
    - `path_glob`: `docs/superpowers/working-briefs/2026-05-18-reviewer-explorer-contract-validator-v1.md`
    - `path_glob`: `docs/superpowers/dispatch-plans/2026-05-18-reviewer-explorer-contract-validator.md`
    - `path_glob`: `tools/validate_ww_role_contracts.py`
    - `path_glob`: `tools/validate_ww_repo.py`
  - `shared_read_scope`:
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/agents/reviewer-prompt.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/agents/explorer-prompt.md`
    - `path_glob`: `tools/quick_validate.py`
    - `path_glob`: `tools/validate_ww_worker_work_mode.py`
    - `path_glob`: `docs/superpowers/specs/2026-05-18-reviewer-explorer-contract-validator-design.md`
    - `path_glob`: `docs/superpowers/plans/2026-05-18-reviewer-explorer-contract-validator.md`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: `role_contract_design_spec`
    - `artifact_kind`: `doc`
    - `artifact_path`: `docs/superpowers/specs/2026-05-18-reviewer-explorer-contract-validator-design.md`
    - `section_anchors`: `Reviewer Contract Rules`, `Explorer Contract Rules`, `Alignment Rules`
    - `artifact_id`: `role_contract_impl_plan`
    - `artifact_kind`: `doc`
    - `artifact_path`: `docs/superpowers/plans/2026-05-18-reviewer-explorer-contract-validator.md`
    - `section_anchors`: none
    - `artifact_id`: `repo_validator_entrypoint`
    - `artifact_kind`: `code`
    - `artifact_path`: `tools/validate_ww_repo.py`
    - `section_anchors`: none
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Invalid state note: `Planned Scope` includes a writable file not mirrored in `exclusive_write_scope`.
- Packet Created: false

## Section Runtime Ledger

### Section: Reviewer And Explorer Role Contract Validator

- Section ID: section-role-contract-validator
- Runtime State: complete
- Active Execution ID:
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
  - Execution ID:
  - Role:
  - Status:
  - Owned Scope:
  - Started At:
  - Finished At:
- Packet Records:
  - Packet ID:
  - Execution ID:
  - Stage:
  - Template Path:
  - Review Target Ref:
  - Supersedes Attempt ID:
  - Accepts Late Results:
- Attempt Records:
  - Attempt ID:
  - Packet ID:
  - Agent ID:
  - Return Status:
  - Runtime State After Return:
  - Launched At:
  - Closed At:
  - Result Summary:
  - Result Artifact Location:
- Attempt Count: 0
- Last Update At: 2026-05-18 America/Los_Angeles
- Next Action: none
- Active Write Scope:
- Result Summary: reviewer and explorer role-contract validator implemented and integrated into the unified WW repository validation entrypoint
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns:
  - explorer role coverage is contract-light compared with reviewer because there is no explorer packet example yet
- Blocker Reason:
- Close State: open
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Reviewer And Explorer Role Contract Validator

- Section ID: section-role-contract-validator
- Review Target Strategy:
  - validate reviewer findings-only boundaries first
  - validate explorer read-only boundaries second
  - validate packet and prompt role-binding alignment third
- Review Lane Records:
  - Lane ID: lane-role-validator-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: secure-software-engineer
  - Execution ID:
  - Packet ID:
  - Attempt ID:
  - Review Target Ref:
    - Artifact Path:
    - Artifact Kind:
    - Artifact Revision:
    - Schema Version:
    - Section Anchor:
    - Content Hash:
  - Reviewer Findings:
    - no material findings; the validator stays bounded to reviewer and explorer role contracts and does not invent worker-style mode semantics
  - Orchestrator Synthesis:
    - the spec-review lane confirms the implemented rule set matches the approved contract scope and current repository surfaces
  - Strict Review Outcome: none
  - Persistence rule: pre-approval plans must preserve this review-lane structure and outcome field pattern; `Review Status` must not reappear here, and durable review-lane data must retain `Reviewer Findings`, `Orchestrator Synthesis`, and the `Strict Review Outcome` field pattern.
  - Applicability rule: `Strict Review Outcome` is required when a strict-review target or durable strict-review result applies; otherwise keep the same field pattern without creating a second schema for valid non-strict lanes.
  - Invalid state note: `Review Status` reappears or durable strict-review outcome data is dropped when applicable.
  - Lane ID: lane-role-validator-code-review
  - Lane Type: code-quality-review
  - Reviewer Persona: secure-software-engineer
  - Execution ID:
  - Packet ID:
  - Attempt ID:
  - Review Target Ref:
    - Artifact Path:
    - Artifact Kind:
    - Artifact Revision:
    - Schema Version:
    - Section Anchor:
    - Content Hash:
  - Reviewer Findings:
    - no material findings; direct role-validator runs, JSON output, unified repo validation, and compile checks all pass
  - Orchestrator Synthesis:
    - the code-quality-review lane confirms the repo validator now runs all three layers without regressing existing checks
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

- Blocking work first: `section-role-contract-validator`
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
- Approval Time: 2026-05-18 America/Los_Angeles
- Notes: user approved the role-contract validator workflow in chat; implementation and verification completed in the same round
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial round for reviewer and explorer role-contract validation
- Supersedes Revision:

## Dispatch Log

- Agents Launched: none
- Retry Events:
- Close Events:
- Review Lane Transitions:
  - role-contract validator design drafted from prior discussion
  - design spec persisted
  - implementation plan persisted
  - working brief persisted
  - dispatch plan drafted
  - repo-local reviewer and explorer role-contract validator implemented under `tools/`
  - unified repo validator extended to call the role-contract validator
  - role validator passed in default and `--json` modes
  - unified repo validator passed with frontmatter, worker, and role-contract checks
  - bounded review found no material findings
- Launch Time: 2026-05-18 America/Los_Angeles
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
