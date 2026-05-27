# Dispatch Plan: Persona Runtime Selection Validator Expansion

- Date: 2026-05-26
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: persona-system-expansion
- Round Slug: 2026-05-26-workflow-runtime-persona-selection-validator-expansion
- Case Root: `docs/cases/persona-system-expansion/`
- Round Root: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-validator-expansion/`
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

- User Request: `new $ww round: persona runtime selection validator expansion. Based on persona runtime selection adoption design and implementation, expand repo validation to check the runtime persona selection recording contract. Update validate_ww_persona_selection_contracts.py and validate_ww_repo.py, with README/SKILL guidance only if necessary. Check that working brief records candidate_persona_sources and recommended persona source/runtime role/rationale; dispatch plan records planned reviewer/source/runtime role/rationale, specialist source/runtime role/rationale, and review lane source/runtime role; subagent packet contract includes persona_source; and reviewer-only/worker-capability gate contract text still exists. Do not add personas, do not change the project registry, do not expand routing, and do not add secondary tags.`
- Working Brief Reference: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-validator-expansion/working-brief.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: expand WorkWork repo validation so runtime persona selection recording rules are machine-checkable
- Relevant Context: the adoption design and implementation rounds added runtime persona source/rationale fields across skill, templates, and packet contract; the persona selection validator now needs to inspect those surfaces, not only the older skill and registry rules
- Constraints:
  - update `tools/validate_ww_persona_selection_contracts.py`
  - update `tools/validate_ww_repo.py` only if aggregate validation label or wiring needs a change
  - update README or `SKILL.md` only if validator guidance needs to name the new checks
  - do not add, remove, or edit persona records
  - do not change `docs/superpowers/personas/registry.yaml`
  - do not expand routing
  - do not add secondary tags
- Risks:
  - overly brittle validator string checks
  - missing one of the newly updated contract/template surfaces
  - breaking `--json` output compatibility
  - scope creep into persona data, project registry, routing, or secondary tags
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Persona Runtime Selection Validator Expansion

- Section ID: section-persona-runtime-selection-validator-expansion
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: test-quality-engineer
- Planned Reviewer Persona: code-quality-reviewer
- Planned Reviewer Persona Source: built-in
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: the review target is validator correctness, maintainability, and false-positive risk
- Planned Specialist Personas:
  - Persona ID: test-quality-engineer
    - Source: built-in
    - Runtime Role: worker
    - Selection Rationale: the section updates repo validation behavior and requires deterministic coverage checks
- Planned Scope:
  - `tools/validate_ww_persona_selection_contracts.py`
  - `tools/validate_ww_repo.py`
  - `README.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: validator expansion is the next step after contract/template adoption, and the highest risk is under-checking or over-brittle checking of the new runtime selection recording contract
- Planned Workflow Bindings:
  - `superpowers:test-driven-development`
  - `superpowers:systematic-debugging`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: validate-first
- Worker Mode Rationale: begin from existing passing validators, add coverage for the new contract surfaces, then verify targeted and aggregate validation
- Goal Tuning: validation-biased
- Constraint Interaction Rule: if a check would require persona records, project registry changes, routing expansion, or secondary tags, record it as follow-up instead of editing those surfaces
- Planned Review Lanes:
  - Lane ID: lane-persona-runtime-selection-validator-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: validator implementation should be reviewed for correctness, maintainability, and false-positive/false-negative risk
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/persona-system-expansion/case.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-validator-expansion/working-brief.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-validator-expansion/dispatch-plan.md`
    - `path_glob`: `tools/validate_ww_persona_selection_contracts.py`
    - `path_glob`: `tools/validate_ww_repo.py`
    - `path_glob`: `README.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `shared_read_scope`:
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-design/design-spec.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-implementation/working-brief.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-implementation/dispatch-plan.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `path_glob`: `docs/superpowers/personas/registry.yaml`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: persona_selection_validator
      - `artifact_kind`: python_validator
      - `artifact_path`: `tools/validate_ww_persona_selection_contracts.py`
      - `section_anchors`: build_results
    - `artifact_id`: repo_validator
      - `artifact_kind`: python_validator
      - `artifact_path`: `tools/validate_ww_repo.py`
      - `section_anchors`: checks
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Persona Runtime Selection Validator Expansion

- Section ID: section-persona-runtime-selection-validator-expansion
- Runtime State: complete
- Active Execution ID: execution-persona-runtime-selection-validator-expansion
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
  - Execution ID: execution-persona-runtime-selection-validator-expansion
  - Role: test-quality-engineer
  - Status: complete
  - Owned Scope: `tools/validate_ww_persona_selection_contracts.py`, `tools/validate_ww_repo.py`, `README.md`
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
- Last Update At: 2026-05-27
- Next Action: round complete
- Active Write Scope: `tools/validate_ww_persona_selection_contracts.py`, `tools/validate_ww_repo.py`, `README.md`, `SKILL.md`
- Result Summary: expanded persona selection validator from 13 to 28 rules, added checks for working brief template, dispatch plan template, packet contract persona_source, and aggregate repo label
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns:
  - keep validator expansion separate from persona records, project registry, routing, and secondary tags
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Persona Runtime Selection Validator Expansion

- Section ID: section-persona-runtime-selection-validator-expansion
- Review Target Strategy:
  - Review validator changes for coverage of the runtime persona selection recording contract, JSON/human output compatibility, repo validator integration, false-positive risk, and forbidden scope discipline.
- Review Lane Records:
  - Lane ID: lane-persona-runtime-selection-validator-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Execution ID: execution-persona-runtime-selection-validator-review
  - Packet ID:
  - Attempt ID: 019e6832-f678-7411-ac70-f17a1a9fcd9a
  - Review Target Ref:
    - Artifact Path: `tools/validate_ww_persona_selection_contracts.py`
    - Artifact Kind: python_validator
    - Artifact Revision:
    - Schema Version: 1
    - Section Anchor: build_results
    - Content Hash:
  - Reviewer Findings: no material findings; residual non-blocking risk notes that `Source: project | built-in` remains an exact fragment check, so future wording-only template edits may need validator updates
  - Orchestrator Synthesis: the validator now checks runtime persona selection recording across SKILL, working brief template, dispatch plan template, and packet contract; targeted human and JSON runs pass, aggregate repo validation passes, py_compile passes, and no persona records, project registry, routing, or secondary tags were changed
  - Strict Review Outcome: none
- Human Decision: Approve
- Revision Notes: user approved completed validator expansion on 2026-05-27; section state accepted, runtime state complete, and plan state completed
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level `plan_state` is derived from `required_for_goal`

## Ordering And Parallelism

- Blocking work first: section-persona-runtime-selection-validator-expansion
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
- Notes: approval authorizes validator expansion and necessary guidance only; persona records, project registry, routing, and secondary tags remain out of scope
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial persona runtime selection validator expansion round
- Supersedes Revision:

## Dispatch Log

- Agents Launched:
  - 019e6832-f678-7411-ac70-f17a1a9fcd9a: code-quality-reviewer re-review returned no material findings
- Retry Events:
- Close Events:
  - 2026-05-27: user approved review-pending validator expansion result; plan completed
- Review Lane Transitions:
  - 2026-05-26: code-quality review found one material false-negative risk
  - 2026-05-26: orchestrator patched WWPS022 to assert specialist source
  - 2026-05-26: re-review returned no material findings
- Launch Time:
  - 2026-05-26: approved validator expansion section began; plan rollup moved from `approved` to `dispatched`
- Revisions Since Approval: 0
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
