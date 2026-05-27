# Dispatch Plan: Persona Runtime Selection Adoption Implementation

- Date: 2026-05-26
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: persona-system-expansion
- Round Slug: 2026-05-26-workflow-runtime-persona-selection-adoption-implementation
- Case Root: `docs/cases/persona-system-expansion/`
- Round Root: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-implementation/`
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

- User Request: `new $ww round: persona runtime selection adoption implementation. Based on the persona runtime selection adoption design spec, implement runtime persona selection recording rules in the WorkWork active contract and templates. Update SKILL.md, working-brief-template.md, dispatch-plan-template.md, subagent-packet-contract.md, and necessary README guidance. Only implement the persona-selection recording and contract layer: project registry priority, built-in fallback, worker-capability gate, reviewer-only gate, review lane reviewer mapping, worker specialist mapping, and persona source/rationale persistence. Do not add personas, do not change the project registry, do not expand routing, do not add secondary tags, and do not change validators.`
- Working Brief Reference: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-implementation/working-brief.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: implement the approved runtime persona selection adoption design at the WorkWork contract and template layer
- Relevant Context: the approved design spec defines project-first lookup, built-in fallback rationale, role gates, reviewer lane mapping, worker specialist mapping, and persona source/rationale persistence, but active contract and template files do not yet fully encode those recording requirements
- Constraints:
  - update only `SKILL.md`, `working-brief-template.md`, `dispatch-plan-template.md`, `subagent-packet-contract.md`, `README.md`, and this round's case artifacts
  - do not add, remove, or edit persona records
  - do not change `docs/superpowers/personas/registry.yaml`
  - do not change validator scripts
  - do not expand `task_routing`
  - do not add secondary route tags
  - do not implement runtime code outside the contract/template layer
- Risks:
  - field drift between skill contract, working brief template, dispatch plan template, and packet contract
  - project registry priority wording that bypasses role gates
  - silent built-in fallback without rationale
  - reviewer and worker role-boundary leakage
  - accidental validator, routing, registry, or persona data edits
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Runtime Selection Contract Adoption

- Section ID: section-runtime-selection-contract-adoption
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: technical-writer
- Planned Reviewer Persona: spec-reviewer
- Planned Reviewer Persona Source: built-in
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: the review target is contract fidelity to an approved design spec, so the built-in spec reviewer is the strongest eligible reviewer-only persona
- Planned Specialist Personas:
  - Persona ID: technical-writer
    - Source: built-in
    - Runtime Role: worker
    - Selection Rationale: the section writes maintainer-facing contract and template markdown, and the working brief identifies source-of-truth clarity as the dominant risk
- Planned Scope:
  - `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `README.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: the approved design spec is ready for contract/template adoption, and a single section keeps the shared terminology synchronized across all active surfaces
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:subagent-driven-development`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: conservative-first
- Worker Mode Rationale: this section updates canonical workflow contracts and templates, so changes should be narrow, source-grounded, and compatibility-preserving
- Goal Tuning: validation-biased
- Constraint Interaction Rule: if a change requires validators, routing expansion, secondary tags, persona records, project registry edits, or runtime code, record it as follow-up instead of editing that surface
- Planned Review Lanes:
  - Lane ID: lane-runtime-selection-contract-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: the review target is contract fidelity to an approved design spec and scope boundary discipline
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/persona-system-expansion/case.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-implementation/working-brief.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-implementation/dispatch-plan.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `path_glob`: `README.md`
  - `shared_read_scope`:
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-design/design-spec.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `path_glob`: `docs/superpowers/personas/registry.yaml`
    - `path_glob`: `tools/validate_ww_persona_selection_contracts.py`
    - `path_glob`: `tools/validate_ww_repo.py`
    - `path_glob`: `tools/validate_ww_round_lifecycle.py`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: active_skill_contract
      - `artifact_kind`: markdown_contract
      - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
      - `section_anchors`: persona planning
    - `artifact_id`: working_brief_template
      - `artifact_kind`: markdown_template
      - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
      - `section_anchors`: persona and workflow guidance
    - `artifact_id`: dispatch_plan_template
      - `artifact_kind`: markdown_template
      - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
      - `section_anchors`: planned sections
    - `artifact_id`: subagent_packet_contract
      - `artifact_kind`: markdown_contract
      - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
      - `section_anchors`: persona selection fields
    - `artifact_id`: maintainer_guidance
      - `artifact_kind`: maintainer_doc
      - `artifact_path`: `README.md`
      - `section_anchors`: For Maintainers
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Runtime Selection Contract Adoption

- Section ID: section-runtime-selection-contract-adoption
- Runtime State: complete
- Active Execution ID: execution-runtime-selection-contract-adoption
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
  - Execution ID: execution-runtime-selection-contract-adoption
  - Role: technical-writer
  - Status: complete
  - Owned Scope: `SKILL.md`, `working-brief-template.md`, `dispatch-plan-template.md`, `subagent-packet-contract.md`, `README.md`
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
- Active Write Scope: `SKILL.md`, `working-brief-template.md`, `dispatch-plan-template.md`, `subagent-packet-contract.md`, `README.md`
- Result Summary: updated active contract, working brief template, dispatch plan template, packet contract, and README guidance for runtime persona selection recording
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns:
  - keep contract/template adoption separate from validator, routing, secondary-tag, persona-record, project-registry, and runtime-code changes
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Runtime Selection Contract Adoption

- Section ID: section-runtime-selection-contract-adoption
- Review Target Strategy:
  - Review the edited contract/template/docs surfaces against the approved design spec for field consistency, source/rationale persistence, role gate preservation, reviewer/worker mapping clarity, and absence of forbidden scope changes.
- Review Lane Records:
  - Lane ID: lane-runtime-selection-contract-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Execution ID: execution-runtime-selection-contract-review
  - Packet ID:
  - Attempt ID: 019e6824-9652-7641-9058-ca39b4ef5b3b
  - Review Target Ref:
    - Artifact Path: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - Artifact Kind: markdown_contract
    - Artifact Revision:
    - Schema Version: 1
    - Section Anchor: persona planning
    - Content Hash:
  - Reviewer Findings: no material findings; residual non-blocking risk notes that re-review was limited to the patched findings and adjacent changed contract/template text
  - Orchestrator Synthesis: the contract/template updates now preserve durable review-lane mapping, constrain cross-cutting reviewers to added lanes or explicit `other` rationale, persist reviewer source/runtime-role/rationale fields in this round's approval record, and keep persona records, project registry, validators, routing, secondary tags, and runtime code out of scope
  - Strict Review Outcome: none
- Human Decision: Approve
- Revision Notes:
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level `plan_state` is derived from `required_for_goal`

## Ordering And Parallelism

- Blocking work first: section-runtime-selection-contract-adoption
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
- Notes: approval authorizes only the contract/template/docs updates listed in `exclusive_write_scope`; persona records, project registry, validators, routing, secondary tags, and runtime code remain out of scope
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial runtime persona selection adoption implementation round
- Supersedes Revision:

## Dispatch Log

- Agents Launched:
  - 019e6824-9652-7641-9058-ca39b4ef5b3b: spec-reviewer re-review returned no material findings
- Retry Events:
- Close Events:
  - 2026-05-26: user approved the reviewed runtime persona selection adoption implementation; section closed complete
- Review Lane Transitions:
  - 2026-05-26: spec review found two material issues
  - 2026-05-26: orchestrator patched cross-cutting reviewer guardrail and this round's reviewer source/runtime-role/rationale fields
  - 2026-05-26: re-review returned no material findings
- Launch Time:
  - 2026-05-26: approved contract/template section began; plan rollup moved from `approved` to `dispatched`
- Revisions Since Approval: 0
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
