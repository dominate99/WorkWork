# Dispatch Plan: Reviewer Persona Expansion

- Date: 2026-05-26
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: persona-system-expansion
- Round Slug: 2026-05-26-workflow-reviewer-persona-expansion
- Case Root: `docs/cases/persona-system-expansion/`
- Round Root: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-reviewer-persona-expansion/`
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

Path identity rules:

- `Case Root` must resolve to `docs/cases/<case_slug>/`
- `Round Root` must resolve to `docs/cases/<case_slug>/rounds/<round_slug>/`
- new dispatch-round artifacts are canonically written under `Round Root`
- legacy type-based paths are legacy history only; they are not canonical targets or ongoing generation defaults

## Source Context

- User Request: `new $ww round: reviewer persona expansion. Based on the persona taxonomy contract and worker persona expansion, add built-in reviewer-only personas to cover existing review lanes: spec-review, code-quality-review, scope-review, editorial-review, plus accessibility/UX and documentation clarity reviewer. Only add built-in reviewer personas; do not add worker personas, do not change validators, do not expand routing, and do not change the project registry.`
- Working Brief Reference: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-reviewer-persona-expansion/working-brief.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: add built-in reviewer-only personas for existing review lanes plus accessibility/UX and documentation clarity review
- Relevant Context: current built-in reviewer-only coverage is security-specific, while the taxonomy contract requires viable reviewer families for durable review lanes
- Constraints:
  - add built-in reviewer-only personas only
  - do not add worker personas
  - do not edit project persona registry records
  - do not edit validators
  - do not expand routing values
  - keep docs sync minimal and guidance-oriented
- Risks:
  - reviewer records accidentally becoming worker-capable
  - reviewer personas overlapping too much to guide lane staffing
  - scope creep into worker persona expansion, validator coverage, or routing changes
  - project registry drift if records are copied there prematurely
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Reviewer Persona Expansion

- Section ID: section-reviewer-persona-expansion
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: staff-engineer-orchestrator
- Planned Reviewer Persona: pm-orchestrator
- Planned Specialist Personas: none
- Planned Scope:
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `README.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: the reviewer gap is now the largest remaining persona portfolio gap after worker expansion, and this round can fill built-in reviewer-only coverage without changing routing or validators
- Planned Workflow Bindings:
  - `superpowers:subagent-driven-development`
  - `superpowers:test-driven-development`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: standard
- Worker Mode Rationale: bounded YAML/data-record and docs edits with explicit role-boundary constraints
- Goal Tuning: make each new reviewer persona findings-only, lane-oriented, and clearly distinct
- Constraint Interaction Rule: if a change would require worker personas, validator updates, routing expansion, or project registry records, record it as follow-up instead of implementing it
- Planned Review Lanes:
  - Lane ID: lane-reviewer-persona-expansion-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/persona-system-expansion/case.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-reviewer-persona-expansion/working-brief.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-reviewer-persona-expansion/dispatch-plan.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `path_glob`: `README.md`
  - `shared_read_scope`:
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/design-spec.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-persona-taxonomy-contract/working-brief.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-persona-taxonomy-contract/dispatch-plan.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-worker-persona-expansion/working-brief.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-worker-persona-expansion/dispatch-plan.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `path_glob`: `docs/superpowers/personas/registry.yaml`
    - `path_glob`: `tools/validate_ww_persona_selection_contracts.py`
    - `path_glob`: `tools/validate_ww_repo.py`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: built_in_reviewer_persona_records
    - `artifact_kind`: yaml_persona_registry
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `section_anchors`: personas
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Reviewer Persona Expansion

- Section ID: section-reviewer-persona-expansion
- Runtime State: complete
- Active Execution ID: execution-reviewer-persona-expansion
- Active Packet ID:
- Active Agent ID:
- Active Attempt ID:
- Active Worker Mode: standard
- Mode Change History:
  - Previous Mode:
  - New Mode:
  - Trigger Evidence:
  - Approved By:
  - Changed At:
- Execution Records:
  - Execution ID: execution-reviewer-persona-expansion
  - Role: orchestrator-data-update
  - Status: complete
  - Owned Scope: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`, `README.md`
  - Started At: 2026-05-26
  - Finished At: 2026-05-26
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
- Last Update At: 2026-05-26
- Next Action: none
- Active Write Scope: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`, `README.md`
- Result Summary: added six reviewer-only built-in personas for spec, code quality, product scope, editorial, accessibility/UX, and documentation clarity review, plus minimal README maintainer guidance
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns:
  - keep reviewer persona expansion separate from worker, validator, routing, and project-registry expansion
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Reviewer Persona Expansion

- Section ID: section-reviewer-persona-expansion
- Review Target Strategy:
  - Review the new built-in reviewer records and README guidance for lane coverage, reviewer-only compliance, persona contrast, and scope discipline.
- Review Lane Records:
  - Lane ID: lane-reviewer-persona-expansion-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Execution ID:
  - Packet ID:
  - Attempt ID:
  - Review Target Ref:
    - Artifact Path: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - Artifact Kind: yaml_persona_registry
    - Artifact Revision:
    - Schema Version: 1
    - Section Anchor: personas
    - Content Hash:
  - Reviewer Findings: no material findings
  - Orchestrator Synthesis: the built-in catalog now includes reviewer-only coverage for spec, code quality, product scope, editorial, accessibility/UX, and documentation clarity review; each new reviewer record preserves reviewer-only boundaries and no worker, validator, routing, or project-registry scope was changed
  - Strict Review Outcome: none
- Human Decision: Approve
- Revision Notes:
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level `plan_state` is derived from `required_for_goal`

## Ordering And Parallelism

- Blocking work first: section-reviewer-persona-expansion
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
- Approval Time: 2026-05-26
- Notes: approval allows built-in reviewer-only persona records and minimal README guidance only; worker personas, validators, routing, and project registry records remain out of scope

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial reviewer persona expansion round
- Supersedes Revision:

## Dispatch Log

- Agents Launched:
- Retry Events:
- Close Events:
  - 2026-05-26: user approved the reviewed built-in reviewer persona expansion; section closed complete
- Review Lane Transitions:
- Launch Time:
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
