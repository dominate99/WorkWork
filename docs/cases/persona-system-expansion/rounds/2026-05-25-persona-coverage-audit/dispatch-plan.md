# Dispatch Plan: Persona Coverage Audit

- Date: 2026-05-25
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: persona-system-expansion
- Round Slug: 2026-05-25-persona-coverage-audit
- Case Root: `docs/cases/persona-system-expansion/`
- Round Root: `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/`
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

- User Request: `new $ww round: persona coverage audit; review the current ww-subagent-orchestrator persona system and produce a persona coverage gap design spec. Audit and classify only. Do not add personas and do not change validators. Focus on built-in personas, project registry, routing categories, review lanes, and worker capability gates.`
- Working Brief Reference: `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/working-brief.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: produce a persona coverage gap design spec that audits and classifies current persona-system gaps without changing persona records, validators, routing, templates, or packet contracts
- Relevant Context: current review found the persona system concentrated around a small engineering-heavy catalog and repeated use of `pm-orchestrator` as reviewer in recent rounds
- Constraints:
  - audit and classification only
  - no new persona records
  - no validator changes
  - no routing model changes
  - no dispatch template or packet contract changes
- Risks:
  - accidentally turning the audit into implementation scope
  - missing project-registry overlap because built-in records and project records are similar but not identical
  - treating optional enrichment gaps as the same class of problem as missing role-family coverage
  - recommending expansion without preserving worker/reviewer/orchestrator role boundaries
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Persona Coverage Gap Design

- Section ID: section-persona-coverage-gap-design
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: staff-engineer-orchestrator
- Planned Reviewer Persona: pm-orchestrator
- Planned Specialist Personas: none
- Planned Scope:
  - `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/design-spec.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: the primary artifact is a repo workflow design spec, and the highest risk is misclassifying persona-system contract gaps as immediate implementation work
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: standard
- Worker Mode Rationale: bounded audit synthesis with one markdown output does not require aggressive autonomous implementation
- Goal Tuning: prioritize source-grounded coverage taxonomy, clean gap categories, and explicit out-of-scope boundaries for later rounds
- Constraint Interaction Rule: user constraints prohibit persona additions and validator changes; the section must stop at `design-spec.md`
- Planned Review Lanes:
  - Lane ID: lane-persona-coverage-gap-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/persona-system-expansion/case.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/working-brief.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/dispatch-plan.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/design-spec.md`
  - `shared_read_scope`:
    - `path_glob`: `README.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `path_glob`: `docs/superpowers/personas/registry.yaml`
    - `path_glob`: `tools/validate_ww_persona_selection_contracts.py`
    - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/*/dispatch-plan.md`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: persona_coverage_gap_design_spec
    - `artifact_kind`: markdown_design_spec
    - `artifact_path`: `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/design-spec.md`
    - `section_anchors`: none
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Persona Coverage Gap Design

- Section ID: section-persona-coverage-gap-design
- Runtime State: complete
- Active Execution ID: execution-persona-coverage-gap-design
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
  - Execution ID: execution-persona-coverage-gap-design
  - Role: orchestrator-design
  - Status: complete
  - Owned Scope: `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/design-spec.md`
  - Started At: 2026-05-25
  - Finished At: 2026-05-25
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
- Last Update At: 2026-05-25
- Next Action: none
- Active Write Scope: `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/design-spec.md`
- Result Summary: drafted persona coverage gap design spec and completed planned narrow reviewer pass
- Canonical Result Artifact Location: `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/design-spec.md`
- Concerns:
  - keep audit findings separate from expansion implementation
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Persona Coverage Gap Design

- Section ID: section-persona-coverage-gap-design
- Review Target Strategy:
  - Review the produced design spec for source coverage, classification clarity, out-of-scope discipline, and readiness to feed later taxonomy and expansion rounds.
- Review Lane Records:
  - Lane ID: lane-persona-coverage-gap-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Execution ID:
  - Packet ID:
  - Attempt ID:
  - Review Target Ref:
    - Artifact Path: `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/design-spec.md`
    - Artifact Kind: markdown_design_spec
    - Artifact Revision:
    - Schema Version: 1
    - Section Anchor:
    - Content Hash:
  - Reviewer Findings: no material findings
  - Orchestrator Synthesis: the design spec covers the requested audit surfaces, keeps persona additions and validator changes out of scope, and is ready for human judgment as input to later taxonomy and expansion rounds
  - Strict Review Outcome: none
- Human Decision: Approve
- Revision Notes:
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level `plan_state` is derived from `required_for_goal`

## Ordering And Parallelism

- Blocking work first: section-persona-coverage-gap-design
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
- Approval Time: 2026-05-25
- Notes: approval allows the single audit section to produce `design-spec.md`; no persona or validator changes are approved in this round

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial persona coverage audit round
- Supersedes Revision:

## Dispatch Log

- Agents Launched:
- Retry Events:
- Close Events:
  - 2026-05-25: user approved the reviewed persona coverage gap design spec; section closed complete
- Review Lane Transitions:
- Launch Time:
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
