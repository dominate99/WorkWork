# Dispatch Plan: Worker Work-Mode Validator

- Date: 2026-05-17
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

- User Request: `$ww 帮你把这个验证脚本也设计并加进去`
- Working Brief Reference: `docs/legacy/superpowers/working-briefs/2026-05-17-worker-work-mode-validator-v1.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: add a repo-local Python validator for the worker `work_mode` contract and document how maintainers run it
- Relevant Context: the five worker `work_mode` contract files already exist; the repo does not yet have a local validation tool or a local dependency story for Markdown AST parsing
- Constraints: first version validates only the worker `work_mode` contract, uses a fixed file list, stays section-aware, and fails non-zero on any rule violation
- Risks:
  - a plain-text validator would allow false positives from the wrong section
  - a missing dependency path would leave the tool unusable
  - docs could drift from the actual command or dependency path
  - unstable JSON output would make future CI adoption harder
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Worker Work-Mode Validator

- Section ID: section-worker-work-mode-validator
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: senior-backend-engineer
- Planned Reviewer Persona: secure-software-engineer
- Planned Specialist Personas: senior-backend-engineer
- Planned Scope:
  - `tools/validate_ww_worker_work_mode.py`
  - `README.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: the round adds one bounded tool plus matching maintainer docs, so a single implementation lane is simpler than parallel edits
- Planned Workflow Bindings:
  - `superpowers:test-driven-development`
  - `superpowers:subagent-driven-development`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: validate-first
- Worker Mode Rationale: the worker should confirm the approved contract and dependency path before locking the validator implementation
- Goal Tuning: validation-biased
- Constraint Interaction Rule: keep first-version scope bounded to the fixed five-file worker `work_mode` validator even if broader validator ideas appear during implementation
- Planned Review Lanes:
  - Lane ID: lane-validator-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: secure-software-engineer
  - Required: true
  - Lane ID: lane-validator-code-review
  - Lane Type: code-quality-review
  - Reviewer Persona: secure-software-engineer
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `tools/validate_ww_worker_work_mode.py`
    - `path_glob`: `README.md`
    - `path_glob`: `docs/legacy/superpowers/working-briefs/2026-05-17-worker-work-mode-validator-v1.md`
    - `path_glob`: `docs/legacy/superpowers/dispatch-plans/2026-05-17-worker-work-mode-validator.md`
  - `shared_read_scope`:
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/agents/worker-prompt.md`
    - `path_glob`: `docs/legacy/superpowers/specs/2026-05-17-worker-work-mode-validator-design.md`
    - `path_glob`: `docs/legacy/superpowers/plans/2026-05-17-worker-work-mode-validator.md`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: `validator_design_spec`
    - `artifact_kind`: `doc`
    - `artifact_path`: `docs/legacy/superpowers/specs/2026-05-17-worker-work-mode-validator-design.md`
    - `section_anchors`: `Validation Model`, `First Rule Set`
    - `artifact_id`: `validator_impl_plan`
    - `artifact_kind`: `doc`
    - `artifact_path`: `docs/legacy/superpowers/plans/2026-05-17-worker-work-mode-validator.md`
    - `section_anchors`: none
    - `artifact_id`: `repo_readme`
    - `artifact_kind`: `doc`
    - `artifact_path`: `README.md`
    - `section_anchors`: `For Maintainers`
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Invalid state note: `Planned Scope` includes a writable file not mirrored in `exclusive_write_scope`.
- Packet Created: false

## Section Runtime Ledger

### Section: Worker Work-Mode Validator

- Section ID: section-worker-work-mode-validator
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
- Last Update At: 2026-05-17 America/Los_Angeles
- Next Action: none
- Active Write Scope:
- Result Summary: repo-local worker work-mode validator implemented, documented, and verified in both default and JSON output modes
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns:
- Blocker Reason:
- Close State: open
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Worker Work-Mode Validator

- Section ID: section-worker-work-mode-validator
- Review Target Strategy:
  - validate section-aware parsing instead of whole-file text matching
  - validate stable `--json` output shape
  - validate clear failure behavior when the Markdown AST dependency is missing
- Review Lane Records:
  - Lane ID: lane-validator-spec-review
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
    - no material findings; the validator stays bounded to the approved five-file scope and uses section-aware parsing
  - Orchestrator Synthesis:
    - the spec-review lane confirms the implementation follows the approved design and dependency model
  - Strict Review Outcome: none
  - Persistence rule: pre-approval plans must preserve this review-lane structure and outcome field pattern; `Review Status` must not reappear here, and durable review-lane data must retain `Reviewer Findings`, `Orchestrator Synthesis`, and the `Strict Review Outcome` field pattern.
  - Applicability rule: `Strict Review Outcome` is required when a strict-review target or durable strict-review result applies; otherwise keep the same field pattern without creating a second schema for valid non-strict lanes.
  - Invalid state note: `Review Status` reappears or durable strict-review outcome data is dropped when applicable.
  - Lane ID: lane-validator-code-review
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
    - no material findings; both output modes pass, the JSON schema is stable, and the validator catches the intended contract surfaces
  - Orchestrator Synthesis:
    - the code-quality-review lane confirms the tool behavior, docs, and bounded scope are aligned
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

- Blocking work first: `section-worker-work-mode-validator`
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
- Approval Time: 2026-05-17 America/Los_Angeles
- Notes: user approved the validator design in chat and the implementation completed in the same round
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial round for the repo-local worker work-mode validator
- Supersedes Revision:

## Dispatch Log

- Agents Launched: none
- Retry Events:
- Close Events:
- Review Lane Transitions:
  - validator design approved in chat
  - design spec persisted
  - implementation plan persisted
  - working brief persisted
  - dispatch plan drafted
  - markdown-it-py dependency installed
  - repo-local validator implemented under `tools/`
  - maintainer run instructions added to `README.md`
  - validator passed in default and `--json` modes
  - bounded review found no material findings
- Launch Time: 2026-05-17 America/Los_Angeles
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
