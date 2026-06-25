# Dispatch Plan: Verifier Lane Authority Implementation Foundation

- Date: 2026-06-24
- Schema Version: 2
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: task-runtime
- Round Slug: 2026-06-24-verifier-lane-authority-implementation-foundation
- Case Root: `docs/cases/task-runtime/`
- Round Root: `docs/cases/task-runtime/rounds/2026-06-24-verifier-lane-authority-implementation-foundation/`
- Plan State: completed
- Last Approved Revision: 1
- Rollback Baseline Revision: 1
- Task Routing: code/programming
- Main Orchestrator: staff-engineer-orchestrator
- Lifecycle Protocol: legacy

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

- User Request: `$ww round: verifier and lane authority implementation foundation. Based on the approved verifier and lane authority design, implement the dormant contract for verifier authority, lane schema, evidence records, baseline/risk-triggered lane selection, and model capability profile/floor/resolution across WorkWork active contract, templates, and docs. Only contract/template/docs implementation; do not add verifier personas, verifier runtime binding, command execution, repair/scoring/hooks, or activate task-runtime-v1. Sync SKILL.md, README, dispatch/working brief/packet contract or related references.`
- Working Brief Reference: `docs/cases/task-runtime/rounds/2026-06-24-verifier-lane-authority-implementation-foundation/working-brief.md`
- Approved Verifier Design: `docs/cases/task-runtime/rounds/2026-06-21-verifier-and-lane-authority-design/design-spec.md`
- Lifecycle Foundation Reference: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
- Packet Contract Reference: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`

## Dispatch Summary

- Goal: implement dormant verifier authority, verification lane schema, evidence records, lane selection, and model capability profile/floor/resolution contract surfaces in WorkWork active docs and templates
- Relevant Context: verifier/lane authority design revision 15 is approved; this round converts it into maintainable contract text and template fields while keeping runtime activation disabled
- Constraints:
  - update only active contract, templates, references, README guidance, and round-local records
  - do not add verifier personas, verifier runtime binding, verifier packets, command execution, repair, scoring, hooks, routing expansion, project registry entries, secondary tags, validator behavior, or `task-runtime-v1` activation
  - preserve worker/reviewer/persona selection contracts and existing lifecycle ownership
  - keep verifier contract dormant and explicitly non-authoritative for legacy rounds
  - keep model capability profile/floor/resolution separate from persona identity and provider/model-name bindings
- Risks:
  - dormant verifier fields accidentally read as active close or lifecycle gates
  - implementation text drifting from approved design revision 15
  - packet/template fields allowing worker self-verification or reviewer self-approval
  - model capability floor text implying silent below-floor fallback is acceptable
  - adding validator/runtime promises that this round cannot implement
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Verifier Lane Authority Contract Foundation

- Section ID: section-verifier-lane-authority-contract-foundation
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: senior-backend-engineer
- Planned Reviewer Persona: spec-reviewer, code-quality-reviewer, documentation-clarity-reviewer
- Planned Reviewer Persona Source: built-in
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: approved-design fidelity, template/repo consistency, and reader-facing contract clarity are separately material for a dormant active-contract foundation; built-in fallback is used because no project reviewer covers portable WorkWork verifier contract implementation more strongly
- Planned Specialist Personas:
  - Persona ID: senior-backend-engineer
    - Source: built-in
    - Runtime Role: worker
    - Selection Rationale: this work updates durable runtime contract interfaces and schema-like template surfaces; built-in fallback is used because no eligible project worker persona covers portable WorkWork runtime contract implementation more strongly
- Planned Scope:
  - `README.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is read-only.
- Planning Rationale: centralize verifier/lane authority in a dedicated dormant reference, then add concise pointers and template fields in the active surfaces that need to persist or assemble those records later
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: contract-first
- Worker Mode Rationale: the approved design already fixed semantics, so implementation should first preserve the contract structure and only then tune wording
- Goal Tuning: validation-biased
- Constraint Interaction Rule: if a change would add verifier personas, runtime verifier binding, command execution, repair, scoring, hooks, routing expansion, project registry records, secondary tags, validator enforcement, or `task-runtime-v1` activation, stop and defer it to a later approved round
- Planned Review Lanes:
  - Lane ID: lane-verifier-contract-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: verify that active contract surfaces faithfully implement approved design revision 15 and keep exclusions intact; built-in fallback is used because no stronger eligible project reviewer covers portable WorkWork specification fidelity
  - Required: true
  - Lane ID: lane-verifier-contract-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: inspect template consistency, schema naming, repo validation risk, and unintended behavior changes without expanding validator behavior; built-in fallback is used because no stronger eligible project reviewer covers WorkWork template consistency
  - Required: true
  - Lane ID: lane-verifier-contract-doc-clarity-review
  - Lane Type: other
  - Reviewer Persona: documentation-clarity-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: documentation clarity is independently material because README, SKILL, and references must make dormant verifier authority understandable without implying activation; current durable lane types do not specifically cover procedural-doc clarity
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/task-runtime/case.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-24-verifier-lane-authority-implementation-foundation/working-brief.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-24-verifier-lane-authority-implementation-foundation/dispatch-plan.md`
    - `path_glob`: `README.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
  - `shared_read_scope`:
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-21-verifier-and-lane-authority-design/design-spec.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-19-task-runtime-lifecycle-foundation-design/**/*`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/**/*`
    - `path_glob`: `docs/superpowers/specs/2026-06-19-workwork-task-runtime-design.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `path_glob`: `docs/superpowers/personas/registry.yaml`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: verifier_lane_authority_contract_foundation
      - `artifact_kind`: contract_docs
      - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
      - `section_anchors`: verifier authority, lane schema, evidence records, lane selection, model capability profiles
- Scope declaration rule: every writable file in `Planned Scope` appears in `exclusive_write_scope`; round-local controller files are separately owned by the orchestrator.
- Packet Created: false

## Section Runtime Ledger

### Section: Verifier Lane Authority Contract Foundation

- Section ID: section-verifier-lane-authority-contract-foundation
- Runtime State: complete
- Active Execution ID: exec-verifier-lane-contract-foundation-01
- Active Packet ID:
- Active Agent ID:
- Active Attempt ID: attempt-verifier-lane-contract-foundation-01
- Active Worker Mode: contract-first
- Active Persona IDs: senior-backend-engineer, spec-reviewer, code-quality-reviewer, documentation-clarity-reviewer
- Active Persona Sources: senior-backend-engineer=built-in, spec-reviewer=built-in, code-quality-reviewer=built-in, documentation-clarity-reviewer=built-in
- Active Persona Role Bindings: senior-backend-engineer=worker via `agents/worker-prompt.md`; spec-reviewer=reviewer via `agents/reviewer-prompt.md`; code-quality-reviewer=reviewer via `agents/reviewer-prompt.md`; documentation-clarity-reviewer=reviewer via `agents/reviewer-prompt.md`
- Mode Change History:
- Execution Records:
  - Execution ID: exec-verifier-lane-contract-foundation-01
  - Role: senior-backend-engineer
  - Status: complete
  - Owned Scope: active WorkWork verifier/lane authority contract, template, packet, and README surfaces
  - Started At: 2026-06-25
  - Finished At: 2026-06-25
- Packet Records:
- Review Records:
  - Lane ID: lane-verifier-contract-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: approved-design fidelity is an independent required gate
  - Execution ID: exec-verifier-lane-spec-review-01
  - Packet ID:
  - Attempt ID: attempt-verifier-lane-spec-review-01
  - Review Target Ref: active contract diff for `README.md`, `SKILL.md`, `assets/dispatch-plan-template.md`, `references/working-brief-template.md`, `references/subagent-packet-contract.md`, and `references/task-runtime-verification.md`
  - Reviewer Findings: PASS; no material findings
  - Orchestrator Synthesis: implemented surfaces cover verifier authority, identity isolation, verifier lane schema, evidence requirements, evidence applicability, lane selection, and model capability profile/floor/resolution while preserving explicit non-activation boundaries
  - Strict Review Outcome: none
  - Lane ID: lane-verifier-contract-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: template and repo consistency are independent required gates
  - Execution ID: exec-verifier-lane-code-quality-review-01
  - Packet ID:
  - Attempt ID: attempt-verifier-lane-code-quality-review-01
  - Review Target Ref: active contract diff after repository validation
  - Reviewer Findings: PASS; no material findings
  - Orchestrator Synthesis: repo validation passes after preserving existing packet hash targets; `task-runtime-lifecycle.md` was intentionally left unchanged because modifying it would stale a prior packet full-file target hash
  - Strict Review Outcome: none
  - Lane ID: lane-verifier-contract-doc-clarity-review
  - Lane Type: other
  - Reviewer Persona: documentation-clarity-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: dormant verifier docs need explicit non-activation boundaries and reader actionability
  - Execution ID: exec-verifier-lane-doc-clarity-review-01
  - Packet ID:
  - Attempt ID: attempt-verifier-lane-doc-clarity-review-01
  - Review Target Ref: README, SKILL, and task runtime verification reference text
  - Reviewer Findings: PASS; no material findings
  - Orchestrator Synthesis: documentation clearly separates dormant contract records from active legacy authority and names the later activation prerequisites
  - Strict Review Outcome: none
- Human Decision: Approve
- Human Decision By: user
- Human Decision Time: 2026-06-25
- Revision Notes:
- Rollup Rule:
  - Approve -> section state becomes `approved` and implementation may begin
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level plan state follows required-section aggregation

## Ordering And Parallelism

- Blocking work first: section-verifier-lane-authority-contract-foundation
- Parallel sections: none
- Review loop: implementation diff -> spec, code-quality, and documentation-clarity reviews -> orchestrator synthesis -> human judgment

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
- Approval Time: 2026-06-25
- Notes: approval authorizes contract/template/docs implementation only; no verifier persona, runtime binding, command execution, validator expansion, hooks, repair, scoring, routing expansion, or `task-runtime-v1` activation
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial verifier lane authority implementation foundation round
- Supersedes Revision:

## Dispatch Log

- Agents Launched:
  - exec-verifier-lane-contract-foundation-01
- Retry Events:
- Close Events:
  - 2026-06-25: user approved implementation foundation; required section moved to `complete` and plan state moved to `completed`
- Review Lane Transitions:
  - 2026-06-25: lane-verifier-contract-spec-review returned PASS for active contract diff
  - 2026-06-25: lane-verifier-contract-code-quality-review returned PASS after `validate_ww_repo.py`
  - 2026-06-25: lane-verifier-contract-doc-clarity-review returned PASS for README/SKILL/reference clarity
- Launch Time: 2026-06-25
- Revisions Since Approval: 0
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
