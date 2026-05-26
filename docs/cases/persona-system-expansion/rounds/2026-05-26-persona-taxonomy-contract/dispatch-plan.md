# Dispatch Plan: Persona Taxonomy Contract

- Date: 2026-05-26
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: persona-system-expansion
- Round Slug: 2026-05-26-persona-taxonomy-contract
- Case Root: `docs/cases/persona-system-expansion/`
- Round Root: `docs/cases/persona-system-expansion/rounds/2026-05-26-persona-taxonomy-contract/`
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

- User Request: `new $ww round: persona taxonomy contract. Based on the persona coverage audit design spec, update the ww-subagent-orchestrator persona system taxonomy contract. Define minimum persona portfolio coverage, orchestrator/worker/reviewer/explorer role families, when to add a persona rather than only adding enrichment fields, and the division of responsibility between project registry and built-in personas. Only update contract/docs; do not add concrete persona records and do not change validators.`
- Working Brief Reference: `docs/cases/persona-system-expansion/rounds/2026-05-26-persona-taxonomy-contract/working-brief.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: update persona taxonomy contract docs so later persona expansion rounds have explicit minimum coverage, role-family, and source-of-truth rules
- Relevant Context: the previous audit round identified coverage gaps but intentionally did not change contracts, persona records, or validators
- Constraints:
  - update contract/docs only
  - do not add concrete persona records
  - do not edit built-in or project persona registries
  - do not change validators
  - do not change routing values yet
  - preserve current role-boundary and worker-capability gates
- Risks:
  - adding implementation behavior instead of contract language
  - overfitting the taxonomy to specific future persona names
  - contradicting existing persona selection validator rules
  - failing to make expansion thresholds concrete enough for later rounds
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Persona Taxonomy Contract

- Section ID: section-persona-taxonomy-contract
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: staff-engineer-orchestrator
- Planned Reviewer Persona: pm-orchestrator
- Planned Specialist Personas: none
- Planned Scope:
  - `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `README.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: the contract needs one coherent taxonomy pass across the skill, registry rules, and maintainer docs before records or validators can safely expand
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: standard
- Worker Mode Rationale: bounded documentation-contract edits with clear constraints
- Goal Tuning: define taxonomy floors and expansion criteria without implementing later rounds
- Constraint Interaction Rule: user constraints prohibit persona-record additions and validator changes, so any such need must be documented as follow-up only
- Planned Review Lanes:
  - Lane ID: lane-persona-taxonomy-contract-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/persona-system-expansion/case.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-persona-taxonomy-contract/working-brief.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-persona-taxonomy-contract/dispatch-plan.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - `path_glob`: `README.md`
  - `shared_read_scope`:
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/design-spec.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `path_glob`: `docs/superpowers/personas/registry.yaml`
    - `path_glob`: `tools/validate_ww_persona_selection_contracts.py`
    - `path_glob`: `tools/validate_ww_repo.py`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: taxonomy_contract_skill
    - `artifact_kind`: markdown_contract
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `section_anchors`: Persona Planning
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Persona Taxonomy Contract

- Section ID: section-persona-taxonomy-contract
- Runtime State: complete
- Active Execution ID: execution-persona-taxonomy-contract
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
  - Execution ID: execution-persona-taxonomy-contract
  - Role: orchestrator-contract-update
  - Status: complete
  - Owned Scope: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`, `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`, `README.md`
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
- Active Write Scope: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`, `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`, `README.md`
- Result Summary: added persona portfolio taxonomy, minimum coverage guidance, expansion decision rules, and source-of-truth split to contract docs without editing persona records or validators
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns:
  - preserve line between contract taxonomy and persona-record implementation
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Persona Taxonomy Contract

- Section ID: section-persona-taxonomy-contract
- Review Target Strategy:
  - Review changed contract docs for audit alignment, actionable taxonomy, out-of-scope discipline, and compatibility with current validators.
- Review Lane Records:
  - Lane ID: lane-persona-taxonomy-contract-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Execution ID:
  - Packet ID:
  - Attempt ID:
  - Review Target Ref:
    - Artifact Path: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - Artifact Kind: markdown_contract
    - Artifact Revision:
    - Schema Version: 1
    - Section Anchor: Persona Taxonomy
    - Content Hash:
  - Reviewer Findings:
    - Initial review found the worker coverage floor needed explicit minimum execution families.
    - Initial review found the `worker` role family needed clarification as a runtime/portfolio family rather than a literal `role_type`.
    - Initial review found the catch-all `other` review lane needed an exception/rationale rule.
    - Re-review result: no material findings.
  - Orchestrator Synthesis: the contract now defines persona portfolio taxonomy, explicit worker coverage families, durable-review-lane expectations, `other` lane rationale requirements, expansion decision rules, and built-in/project source-of-truth boundaries while preserving worker gates and leaving persona records and validators unchanged
  - Strict Review Outcome: none
- Human Decision: Approve
- Revision Notes:
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level `plan_state` is derived from `required_for_goal`

## Ordering And Parallelism

- Blocking work first: section-persona-taxonomy-contract
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
- Notes: approval allows contract/doc updates only; persona records and validators remain out of scope

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial persona taxonomy contract round
- Supersedes Revision:

## Dispatch Log

- Agents Launched:
- Retry Events:
- Close Events:
  - 2026-05-26: user approved the reviewed persona taxonomy contract updates; section closed complete
- Review Lane Transitions:
- Launch Time:
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
