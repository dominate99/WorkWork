# Dispatch Plan: Persona Runtime-Selection Validator Pilot

- Date: 2026-05-22
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
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

## Source Context

- User Request: `先做当前这轮的 precommit review，然后 commit；接着起新的 $ww validator round`
- Working Brief Reference: `docs/legacy/superpowers/working-briefs/2026-05-22-persona-runtime-selection-validator-pilot-v1.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: add repo-local validator coverage for persona runtime-selection semantics and integrate it into the repo-level validator entrypoint
- Relevant Context: the runtime-selection guidance pilot is complete, but current repo-local validators still do not check the new baseline-eligibility versus enrichment-ranking contract
- Constraints:
  - validator-surface changes only by default
  - keep packet contracts, prompts, and persona records out of scope
  - only touch contract text if validator implementation reveals a concrete ambiguity that blocks stable checks
- Risks:
  - naive keyword-only checks could miss real semantic drift
  - overfitting to exact prose could create brittle validator noise
  - repo-level aggregation could stay green while silently skipping the new validator if integration is incomplete
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Persona Runtime-Selection Validator

- Section ID: section-persona-runtime-selection-validator
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: staff-engineer-orchestrator
- Planned Reviewer Persona: pm-orchestrator
- Planned Specialist Personas: creative-director-orchestrator
- Planned Scope:
  - `tools/validate_ww_persona_selection_contracts.py`
  - `tools/validate_ww_repo.py`
  - `README.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: validator coverage is the next highest-leverage step now that persona runtime-selection guidance is defined and stable enough to check automatically
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: validate-first
- Worker Mode Rationale: this round should first validate the approved contract semantics, then encode only the smallest stable checks that protect them
- Goal Tuning: validation-biased
- Constraint Interaction Rule: keep the validator semantic enough to catch drift, but do not widen into packet, prompt, or persona-record adoption
- Planned Review Lanes:
  - Lane ID: lane-persona-runtime-selection-validator-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/legacy/superpowers/working-briefs/2026-05-22-persona-runtime-selection-validator-pilot-v1.md`
    - `path_glob`: `docs/legacy/superpowers/dispatch-plans/2026-05-22-persona-runtime-selection-validator-pilot.md`
    - `path_glob`: `tools/validate_ww_persona_selection_contracts.py`
    - `path_glob`: `tools/validate_ww_repo.py`
    - `path_glob`: `README.md`
  - `shared_read_scope`:
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `tools/quick_validate.py`
    - `path_glob`: `tools/validate_ww_worker_work_mode.py`
    - `path_glob`: `tools/validate_ww_role_contracts.py`
    - `path_glob`: `docs/legacy/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: `persona_runtime_selection_rules`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - `section_anchors`: `Selection Rules`, `Runtime Selection Guidance`
    - `artifact_id`: `ww_skill_persona_guidance`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `section_anchors`: `Persona Planning`
    - `artifact_id`: `ww_repo_validator`
    - `artifact_kind`: `code`
    - `artifact_path`: `tools/validate_ww_repo.py`
    - `section_anchors`: none
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Persona Runtime-Selection Validator

- Section ID: section-persona-runtime-selection-validator
- Runtime State: complete
- Active Execution ID: execution-persona-runtime-selection-validator
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
  - Execution ID: execution-persona-runtime-selection-validator
  - Role: orchestrator-implementation
  - Status: DONE
  - Owned Scope: `tools/validate_ww_persona_selection_contracts.py`, `tools/validate_ww_repo.py`, `README.md`, round documents
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
  - Attempt ID: attempt-persona-runtime-selection-validator-1
  - Packet ID:
  - Agent ID:
  - Return Status: DONE
  - Runtime State After Return: complete
  - Launched At: 2026-05-22 America/Los_Angeles
  - Closed At: 2026-05-22 America/Los_Angeles
  - Result Summary: added a section-aware validator for persona runtime-selection guidance and integrated it into repo-level validation
  - Result Artifact Location: `tools/validate_ww_persona_selection_contracts.py`, `tools/validate_ww_repo.py`, `README.md`
- Attempt Count: 1
- Last Update At: 2026-05-22 America/Los_Angeles
- Next Action: none
- Active Write Scope:
- Result Summary: added repo-local validator coverage for persona runtime-selection semantics and integrated it into the repo-level validator entrypoint and maintainer guidance
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns:
  - the validator may accidentally encode wording instead of semantics
  - the repo-level aggregator may not clearly surface the new validator result if integration is too implicit
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Persona Runtime-Selection Validator

- Section ID: section-persona-runtime-selection-validator
- Review Target Strategy:
  - validate that required fields remain the baseline eligibility gate
  - validate that enrichment fields are checked only as ranking, tie-break, and rationale semantics
  - validate that guardrails for role boundary, worker gate, and project-registry preference are preserved
  - validate that repo-level aggregation includes the new validator explicitly
- Review Lane Records:
  - Lane ID: lane-persona-runtime-selection-validator-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Execution ID: execution-persona-runtime-selection-validator
  - Packet ID:
  - Attempt ID: attempt-persona-runtime-selection-validator-1
  - Review Target Ref:
    - Artifact Path: `tools/validate_ww_persona_selection_contracts.py`
    - Artifact Kind: code
    - Artifact Revision: working-tree
    - Schema Version:
    - Section Anchor:
    - Content Hash:
  - Reviewer Findings: no material findings
  - Orchestrator Synthesis: the validator now checks baseline eligibility, enrichment-driven ranking semantics, and runtime-selection guardrails without widening into packet, prompt, or persona-record changes
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

- Blocking work first: `section-persona-runtime-selection-validator`
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
- Notes: this pilot round is scoped to validator coverage for persona runtime-selection semantics only
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial pilot round for persona runtime-selection validator coverage
- Supersedes Revision:

## Dispatch Log

- Agents Launched: none
- Retry Events:
- Close Events:
- Review Lane Transitions:
  - runtime-selection guidance pilot completed and committed
  - validator gap confirmed against current repo-level validation entrypoint
  - working brief persisted
  - dispatch plan drafted
  - validator implementation completed
  - repo-level validation passed with the new validator included
  - scope review completed with no material findings
  - human approval received
- Launch Time: 2026-05-22 America/Los_Angeles
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
