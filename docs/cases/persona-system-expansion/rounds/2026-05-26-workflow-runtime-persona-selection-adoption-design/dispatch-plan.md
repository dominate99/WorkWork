# Dispatch Plan: Persona Runtime Selection Adoption Design

- Date: 2026-05-26
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: persona-system-expansion
- Round Slug: 2026-05-26-workflow-runtime-persona-selection-adoption-design
- Case Root: `docs/cases/persona-system-expansion/`
- Round Root: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-design/`
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

- User Request: `new $ww round: persona runtime selection adoption design. Based on persona taxonomy contract, worker persona expansion, and reviewer persona expansion, design how WorkWork selects and records built-in/project personas in actual working brief, dispatch plan, reviewer lane, and worker packet artifacts. Only produce a design spec; do not implement, add personas, change validators, or expand routing. Focus on project registry priority, built-in fallback, worker-capability gate, reviewer-only gate, review lane to reviewer persona mapping, worker section to specialist persona mapping, and whether a later routing/secondary tag round is needed.`
- Working Brief Reference: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-design/working-brief.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: produce a design spec for adopting the expanded persona taxonomy and built-in/project persona records in runtime selection and persisted WorkWork artifacts
- Relevant Context: taxonomy, worker persona, and reviewer persona records now exist, but WorkWork still needs a design for how actual working briefs, dispatch plans, reviewer lanes, and worker packets select and record those personas without bypassing project-registry priority or role gates
- Constraints:
  - produce only `design-spec.md` in this round
  - do not implement runtime selection changes
  - do not add, remove, or edit persona records
  - do not modify validators
  - do not expand routing values or add secondary tags
  - do not change the project registry
  - record follow-up routing or secondary-tag needs without implementing them
- Risks:
  - designing around built-ins in a way that weakens project registry priority
  - allowing reviewer-only personas into worker packets or worker-capable personas into review lanes without role gates
  - producing prose that does not specify persisted artifact placement
  - accidentally widening this design round into implementation, validator, routing, or registry edits
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Runtime Selection Adoption Design

- Section ID: section-runtime-selection-adoption-design
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: staff-engineer-orchestrator
- Planned Reviewer Persona: spec-reviewer
- Planned Specialist Personas: none
- Planned Scope:
  - `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-design/design-spec.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: the next gap is not persona data but runtime adoption design, so the section should produce one contract-style design spec before any implementation or validator round
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: standard
- Worker Mode Rationale: bounded design-spec authoring with no implementation, validator, routing, or persona registry changes
- Goal Tuning: specify selection order, gate checks, mapping rules, persisted artifact fields, and follow-up boundaries in implementation-ready language
- Constraint Interaction Rule: if a change requires implementation, validator updates, routing expansion, secondary tags, or registry edits, record it as follow-up instead of changing that surface
- Planned Review Lanes:
  - Lane ID: lane-runtime-selection-design-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/persona-system-expansion/case.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-design/working-brief.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-design/dispatch-plan.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-design/design-spec.md`
  - `shared_read_scope`:
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/design-spec.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-persona-taxonomy-contract/working-brief.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-persona-taxonomy-contract/dispatch-plan.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-worker-persona-expansion/working-brief.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-worker-persona-expansion/dispatch-plan.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-reviewer-persona-expansion/working-brief.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-reviewer-persona-expansion/dispatch-plan.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `path_glob`: `docs/superpowers/personas/registry.yaml`
    - `path_glob`: `tools/validate_ww_persona_selection_contracts.py`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: persona_runtime_selection_adoption_design_spec
    - `artifact_kind`: design_spec
    - `artifact_path`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-design/design-spec.md`
    - `section_anchors`: runtime selection adoption design
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Runtime Selection Adoption Design

- Section ID: section-runtime-selection-adoption-design
- Runtime State: complete
- Active Execution ID: execution-runtime-selection-adoption-design
- Active Packet ID:
- Active Agent ID:
- Active Attempt ID:
- Active Worker Mode:
- Mode Change History:
  - Previous Mode:
  - New Mode:
  - Trigger Evidence:
  - Approved By:
  - Changed At:
- Execution Records:
  - Execution ID: execution-runtime-selection-adoption-design
  - Role: orchestrator-design-author
  - Status: complete
  - Owned Scope: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-design/design-spec.md`
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
- Active Write Scope: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-design/design-spec.md`
- Result Summary: drafted runtime persona selection adoption design spec
- Canonical Result Artifact Location: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-design/design-spec.md`
- Concerns:
  - keep this round design-only and separate from implementation, validator, routing, secondary-tag, and registry changes
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Runtime Selection Adoption Design

- Section ID: section-runtime-selection-adoption-design
- Review Target Strategy:
  - Review the produced design spec for contract completeness, selection-order clarity, role-gate preservation, artifact-placement specificity, and follow-up boundary discipline.
- Review Lane Records:
  - Lane ID: lane-runtime-selection-design-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Execution ID: execution-runtime-selection-adoption-design-review
  - Packet ID:
  - Attempt ID: 019e6319-e826-7f02-b9b9-1f234342db70
  - Review Target Ref:
    - Artifact Path: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-design/design-spec.md`
    - Artifact Kind: design_spec
    - Artifact Revision:
    - Schema Version: 1
    - Section Anchor: runtime selection adoption design
    - Content Hash:
  - Reviewer Findings: no material findings; residual non-blocking risk notes that the approval-to-dispatched lifecycle is documented in prose rather than normalized state-history fields
  - Orchestrator Synthesis: the design spec now resolves the project-priority versus built-in-fallback ambiguity, preserves reviewer and worker role gates, maps durable review lanes and worker surfaces to built-in personas, and keeps implementation, validator, routing, secondary-tag, persona-record, and project-registry changes out of scope
  - Strict Review Outcome: none
- Human Decision: Approve
- Revision Notes:
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level `plan_state` is derived from `required_for_goal`

## Ordering And Parallelism

- Blocking work first: section-runtime-selection-adoption-design
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
- Notes: approval authorizes only creation of `design-spec.md`; implementation, persona records, validators, routing, secondary tags, and project registry changes remain out of scope
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`
- Post-Approval Transition Note: revision 1 reached `Plan State: approved` on 2026-05-26, then moved to `Plan State: dispatched` when the approved design section began.

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial runtime persona selection adoption design round
- Supersedes Revision:

## Dispatch Log

- Agents Launched:
  - 019e6319-e826-7f02-b9b9-1f234342db70: spec-reviewer re-review returned no material findings
- Retry Events:
- Close Events:
  - 2026-05-26: user approved the reviewed runtime persona selection adoption design spec; section closed complete
- Review Lane Transitions:
  - 2026-05-26: spec review found two material issues
  - 2026-05-26: orchestrator patched project priority wording and approval-to-dispatched transition note
  - 2026-05-26: re-review returned no material findings
- Launch Time:
- 2026-05-26: approved design section began; plan rollup moved from `approved` to `dispatched`
- Revisions Since Approval: 0
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
