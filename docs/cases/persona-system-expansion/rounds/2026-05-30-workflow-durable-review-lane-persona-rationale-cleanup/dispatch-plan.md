# Dispatch Plan: Durable Review Lane Persona Rationale Cleanup

- Date: 2026-05-30
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: persona-system-expansion
- Round Slug: 2026-05-30-workflow-durable-review-lane-persona-rationale-cleanup
- Case Root: `docs/cases/persona-system-expansion/`
- Round Root: `docs/cases/persona-system-expansion/rounds/2026-05-30-workflow-durable-review-lane-persona-rationale-cleanup/`
- Plan State: completed
- Last Approved Revision: 1
- Rollback Baseline Revision: 1
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

- User Request: `new $ww round: durable review lane persona rationale cleanup. Based on the persona runtime selection dogfood audit, add durable Section Review Record Reviewer Selection Rationale persistence to the active contract and dispatch plan template. Synchronize validate_ww_persona_selection_contracts.py and necessary README/SKILL guidance. Only fix review lane rationale persistence; do not backfill historical rounds, add personas, change the project registry, expand routing, add secondary tags, or change the packet contract.`
- Working Brief Reference: `docs/cases/persona-system-expansion/rounds/2026-05-30-workflow-durable-review-lane-persona-rationale-cleanup/working-brief.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: close DG-001 by persisting reviewer selection rationale in durable Section Review Record lane records and enforcing the field in validation
- Relevant Context: planned review lanes already persist reviewer source/runtime role/rationale, while durable review records preserve source/runtime role but omit rationale
- Constraints:
  - update `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - update `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - update `tools/validate_ww_persona_selection_contracts.py`
  - update README only if necessary
  - do not backfill historical rounds
  - do not add personas, modify project registry, expand routing, add secondary tags, or edit packet contract
- Risks:
  - template and validator drift
  - vague durable snapshot semantics
  - scope creep into historical records or packet contract
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Durable Review Lane Persona Rationale Cleanup

- Section ID: section-durable-review-lane-persona-rationale-cleanup
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: technical-writer
- Planned Reviewer Persona: code-quality-reviewer
- Planned Reviewer Persona Source: built-in
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: validator synchronization and false-negative risk make the built-in code-quality reviewer the strongest eligible reviewer-only match
- Planned Specialist Personas:
  - Persona ID: technical-writer
    - Source: built-in
    - Runtime Role: worker
    - Selection Rationale: the primary edit is a durable workflow-contract and template persistence rule
- Planned Scope:
  - `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `tools/validate_ww_persona_selection_contracts.py`
  - `README.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: close the single medium DG-001 dogfood gap before starting packet-level dogfood work
- Planned Workflow Bindings:
  - `superpowers:test-driven-development`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: validate-first
- Worker Mode Rationale: tighten the existing durable review-record validator check alongside the contract/template update, then run targeted and aggregate validation
- Goal Tuning: validation-biased
- Constraint Interaction Rule: any historical backfill, persona, project-registry, routing, secondary-tag, or packet-contract change is out of scope and must remain a follow-up
- Planned Review Lanes:
  - Lane ID: lane-durable-review-lane-persona-rationale-cleanup-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: review synchronized contract, template, and validator edits for DG-001 closure and false-negative risk
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/persona-system-expansion/case.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-30-workflow-durable-review-lane-persona-rationale-cleanup/working-brief.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-30-workflow-durable-review-lane-persona-rationale-cleanup/dispatch-plan.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `path_glob`: `tools/validate_ww_persona_selection_contracts.py`
    - `path_glob`: `README.md`
  - `shared_read_scope`:
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-28-workflow-runtime-persona-selection-dogfood-audit/design-spec.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `path_glob`: `docs/superpowers/personas/registry.yaml`
    - `path_glob`: `tools/validate_ww_repo.py`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: active_skill_contract
      - `artifact_kind`: markdown_contract
      - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
      - `section_anchors`: persona planning
    - `artifact_id`: dispatch_plan_template
      - `artifact_kind`: markdown_template
      - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
      - `section_anchors`: section review record
    - `artifact_id`: persona_selection_validator
      - `artifact_kind`: python_validator
      - `artifact_path`: `tools/validate_ww_persona_selection_contracts.py`
      - `section_anchors`: WWPS024
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Durable Review Lane Persona Rationale Cleanup

- Section ID: section-durable-review-lane-persona-rationale-cleanup
- Runtime State: complete
- Active Execution ID: execution-durable-review-lane-persona-rationale-cleanup
- Active Packet ID:
- Active Agent ID:
- Active Attempt ID:
- Active Worker Mode: validate-first
- Active Persona IDs: technical-writer, code-quality-reviewer
- Active Persona Sources: technical-writer=built-in, code-quality-reviewer=built-in
- Active Persona Role Bindings: technical-writer=worker via `agents/worker-prompt.md`; code-quality-reviewer=reviewer via `agents/reviewer-prompt.md`
- Mode Change History:
  - Previous Mode:
  - New Mode:
  - Trigger Evidence:
  - Approved By:
  - Changed At:
- Execution Records:
  - Execution ID: execution-durable-review-lane-persona-rationale-cleanup
  - Role: technical-writer
  - Status: complete
  - Owned Scope: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`, `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`, `tools/validate_ww_persona_selection_contracts.py`
  - Started At: 2026-05-31
  - Finished At: 2026-05-31
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
- Last Update At: 2026-05-31
- Next Action: round complete
- Active Write Scope: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`, `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`, `tools/validate_ww_persona_selection_contracts.py`
- Result Summary: closed DG-001 by requiring durable review-lane reviewer selection rationale in SKILL.md and the dispatch plan template, and tightened WWPS024 so validation checks both the active contract rule and template field
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns:
  - keep cleanup limited to DG-001
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Durable Review Lane Persona Rationale Cleanup

- Section ID: section-durable-review-lane-persona-rationale-cleanup
- Review Target Strategy:
  - Review DG-001 closure across active contract, template, and validator surfaces with no historical or packet-contract scope growth.
- Review Lane Records:
  - Lane ID: lane-durable-review-lane-persona-rationale-cleanup-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: review synchronized DG-001 cleanup for contract clarity and validator false-negative risk
  - Execution ID: execution-durable-review-lane-persona-rationale-cleanup-review
  - Packet ID:
  - Attempt ID: local-code-quality-review-2026-05-31
  - Review Target Ref:
    - Artifact Path: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - Artifact Kind: markdown_template
    - Artifact Revision:
    - Schema Version: 1
    - Section Anchor: section review record
    - Content Hash:
  - Reviewer Findings: initial review found one material validator-drift risk because WWPS024 checked only the template field and would not fail if the new SKILL durable snapshot rule disappeared; patched WWPS024 to check both active contract wording and template field; re-review returned no material findings
  - Orchestrator Synthesis: DG-001 is closed with a narrow synchronized change across SKILL.md, dispatch-plan-template.md, and validate_ww_persona_selection_contracts.py; README and packet contract remain unchanged; targeted, aggregate, lifecycle, py_compile, and diff checks pass
  - Strict Review Outcome: none
- Human Decision: Approve
- Revision Notes: user approved completed DG-001 cleanup on 2026-05-31; section state accepted, runtime state complete, and plan state completed
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level `plan_state` is derived from `required_for_goal`

## Ordering And Parallelism

- Blocking work first: section-durable-review-lane-persona-rationale-cleanup
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
- Approval Time: 2026-05-31
- Notes: approval authorizes DG-001 durable review-lane rationale cleanup only; historical rounds, personas, project registry, routing, secondary tags, and packet contract remain out of scope
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial durable review lane persona rationale cleanup round
- Supersedes Revision:

## Dispatch Log

- Agents Launched:
- Retry Events:
- Close Events:
  - 2026-05-31: user approved the reviewed durable review-lane persona rationale cleanup; section closed complete
- Review Lane Transitions:
  - 2026-05-31: code-quality review found one material validator-drift risk
  - 2026-05-31: orchestrator patched WWPS024 to bind active contract wording and template field
  - 2026-05-31: re-review returned no material findings
- Launch Time:
  - 2026-05-31: approved DG-001 cleanup section began; plan rollup moved from `approved` to `dispatched`
- Revisions Since Approval: 0
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
