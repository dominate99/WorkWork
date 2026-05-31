# Dispatch Plan: Persona Runtime Selection Dogfood Audit

- Date: 2026-05-28
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: persona-system-expansion
- Round Slug: 2026-05-28-workflow-runtime-persona-selection-dogfood-audit
- Case Root: `docs/cases/persona-system-expansion/`
- Round Root: `docs/cases/persona-system-expansion/rounds/2026-05-28-workflow-runtime-persona-selection-dogfood-audit/`
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

- User Request: `new $ww round: persona runtime selection dogfood audit. Based on the completed and pushed persona runtime selection adoption design, implementation, and validator expansion, audit whether WorkWork's active contract, templates, and recent persona-system-expansion rounds actually record persona source/runtime role/rationale under the new contract. Only audit and classify; produce a persona runtime selection dogfood gap report or design spec; do not implement, add personas, change validators, expand routing, or add secondary tags. Focus on working brief, dispatch plan, review lane records, planned specialist/reviewer personas, subagent packet contract dogfood consistency, and judge whether enough evidence exists to open a routing/secondary tags design round.`
- Working Brief Reference: `docs/cases/persona-system-expansion/rounds/2026-05-28-workflow-runtime-persona-selection-dogfood-audit/working-brief.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: produce a dogfood gap report that audits runtime persona selection recording consistency across active contract surfaces, templates, and recent persona-system-expansion rounds
- Relevant Context: commit `343099a` completed the runtime selection design, implementation, and validator expansion; the validator checks required contract fragments but does not classify whether recent round artifacts are consistently using the new records
- Constraints:
  - produce only `docs/cases/persona-system-expansion/rounds/2026-05-28-workflow-runtime-persona-selection-dogfood-audit/design-spec.md`
  - do not implement contract or template changes
  - do not add, remove, or edit persona records
  - do not change `docs/superpowers/personas/registry.yaml`
  - do not edit validators
  - do not expand routing
  - do not add secondary tags
- Risks:
  - confusing pre-adoption history with active-contract noncompliance
  - under-checking recent rounds that should now dogfood source/runtime role/rationale fields
  - recommending routing or secondary tags without enough evidence
  - turning audit observations into unapproved implementation edits
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Persona Runtime Selection Dogfood Audit

- Section ID: section-persona-runtime-selection-dogfood-audit
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: technical-writer
- Planned Reviewer Persona: spec-reviewer
- Planned Reviewer Persona Source: built-in
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: the review target is a contract/audit artifact whose value depends on complete, coherent, evidence-backed findings
- Planned Specialist Personas:
  - Persona ID: technical-writer
    - Source: built-in
    - Runtime Role: worker
    - Selection Rationale: the section produces maintainer-facing audit documentation and classifies source-of-truth consistency gaps
- Planned Scope:
  - `docs/cases/persona-system-expansion/rounds/2026-05-28-workflow-runtime-persona-selection-dogfood-audit/design-spec.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: the next useful step after contract and validator adoption is to audit whether recent WorkWork artifacts actually use the new persona source/runtime role/rationale records before designing routing or secondary tags
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: conservative-first
- Worker Mode Rationale: the work is an evidence-bound audit over active contracts and recent artifacts, with explicit prohibitions on implementation or routing changes
- Goal Tuning: audit-biased
- Constraint Interaction Rule: if an observation implies implementation, validator, persona, registry, routing, or secondary-tag work, record it as a follow-up recommendation instead of editing those surfaces
- Planned Review Lanes:
  - Lane ID: lane-persona-runtime-selection-dogfood-audit-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: the report must be reviewed for contract completeness, evidence quality, and clean separation between audit findings and follow-up design
  - Required: true
- Review lane mapping rule: default built-in reviewer mapping is `spec-review` -> `spec-reviewer`, `code-quality-review` -> `code-quality-reviewer`, `scope-review` -> `product-scope-reviewer`, `editorial-review` -> `editorial-reviewer`, and `other` -> explicit rationale only.
- Cross-cutting reviewer rule: add `secure-software-engineer`, `accessibility-ux-reviewer`, or `documentation-clarity-reviewer` as a second review lane when that risk surface is independently material, or use one for `other` only with explicit rationale that no durable lane type fits.
- Worker specialist mapping rule: select worker specialists by owned scope and dominant implementation risk, not top-level `task_routing` alone.
- Persona source rule: project personas win only after role-gate and required-field eligibility, and only when stronger or project-specific; otherwise record built-in fallback rationale.
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/persona-system-expansion/case.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-28-workflow-runtime-persona-selection-dogfood-audit/working-brief.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-28-workflow-runtime-persona-selection-dogfood-audit/dispatch-plan.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-28-workflow-runtime-persona-selection-dogfood-audit/design-spec.md`
  - `shared_read_scope`:
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `path_glob`: `docs/superpowers/personas/registry.yaml`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-design/**`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-implementation/**`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-validator-expansion/**`
    - `path_glob`: `tools/validate_ww_persona_selection_contracts.py`
    - `path_glob`: `tools/validate_ww_repo.py`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: persona_runtime_selection_dogfood_gap_report
      - `artifact_kind`: dogfood_gap_report
      - `artifact_path`: `docs/cases/persona-system-expansion/rounds/2026-05-28-workflow-runtime-persona-selection-dogfood-audit/design-spec.md`
      - `section_anchors`: dogfood audit findings
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Persona Runtime Selection Dogfood Audit

- Section ID: section-persona-runtime-selection-dogfood-audit
- Runtime State: complete
- Active Execution ID: execution-persona-runtime-selection-dogfood-audit
- Active Packet ID:
- Active Agent ID:
- Active Attempt ID:
- Active Worker Mode: conservative-first
- Active Persona IDs: technical-writer, spec-reviewer
- Active Persona Sources: technical-writer=built-in, spec-reviewer=built-in
- Active Persona Role Bindings: technical-writer=worker via `agents/worker-prompt.md`; spec-reviewer=reviewer via `agents/reviewer-prompt.md`
- Mode Change History:
  - Previous Mode:
  - New Mode:
  - Trigger Evidence:
  - Approved By:
  - Changed At:
- Execution Records:
  - Execution ID: execution-persona-runtime-selection-dogfood-audit
  - Role: technical-writer
  - Status: complete
  - Owned Scope: `docs/cases/persona-system-expansion/rounds/2026-05-28-workflow-runtime-persona-selection-dogfood-audit/design-spec.md`
  - Started At: 2026-05-28
  - Finished At: 2026-05-28
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
- Last Update At: 2026-05-28
- Next Action: round complete
- Active Write Scope: `docs/cases/persona-system-expansion/rounds/2026-05-28-workflow-runtime-persona-selection-dogfood-audit/design-spec.md`
- Result Summary: produced persona runtime selection dogfood gap report; active contract and templates mostly pass, durable review-lane rationale persistence remains the main cleanup gap, packet-level dogfood needs a future real packet artifact, and routing/secondary tags should remain deferred
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns:
  - keep the round audit-only; no contract, validator, persona, registry, routing, or secondary-tag edits
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Persona Runtime Selection Dogfood Audit

- Section ID: section-persona-runtime-selection-dogfood-audit
- Review Target Strategy:
  - Review the dogfood gap report for faithful evidence classification, correct treatment of pre-adoption history, source/runtime role/rationale coverage, and justified routing/secondary-tags recommendation.
- Review Lane Records:
  - Lane ID: lane-persona-runtime-selection-dogfood-audit-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Execution ID: execution-persona-runtime-selection-dogfood-audit-review
  - Packet ID:
  - Attempt ID: local-spec-review-2026-05-28
  - Review Target Ref:
    - Artifact Path: `docs/cases/persona-system-expansion/rounds/2026-05-28-workflow-runtime-persona-selection-dogfood-audit/design-spec.md`
    - Artifact Kind: dogfood_gap_report
    - Artifact Revision:
    - Schema Version: 1
    - Section Anchor: dogfood audit findings
    - Content Hash:
  - Reviewer Findings: no material findings; residual non-blocking risk is that the audit relies on recent round artifacts rather than live packet artifacts because no recent round created a packet
  - Orchestrator Synthesis: the report accurately separates historical pre-adoption drift from current dogfood gaps, identifies durable review-lane rationale persistence as the main cleanup candidate, treats packet dogfood as an evidence gap rather than a contract failure, and defers routing or secondary tags until more runtime evidence exists
  - Strict Review Outcome: none
- Human Decision: Approve
- Revision Notes: user approved completed dogfood audit on 2026-05-30; report status approved, section state accepted, runtime state complete, and plan state completed
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level `plan_state` is derived from `required_for_goal`

## Ordering And Parallelism

- Blocking work first: section-persona-runtime-selection-dogfood-audit
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
- Approval Time: 2026-05-28
- Notes: approval authorizes audit artifact creation only; implementation, persona records, project registry, validators, routing, and secondary tags remain out of scope
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial persona runtime selection dogfood audit round
- Supersedes Revision:

## Dispatch Log

- Agents Launched:
- Retry Events:
- Close Events:
  - 2026-05-30: user approved the reviewed persona runtime selection dogfood gap report; section closed complete
- Review Lane Transitions:
- Launch Time:
- 2026-05-28: approved dogfood audit section began; plan rollup moved from `approved` to `dispatched`
- Revisions Since Approval: 0
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
