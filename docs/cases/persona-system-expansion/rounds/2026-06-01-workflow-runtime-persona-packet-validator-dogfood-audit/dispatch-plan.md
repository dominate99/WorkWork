# Dispatch Plan: Runtime Persona Packet Validator Dogfood Audit

- Date: 2026-06-01
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: persona-system-expansion
- Round Slug: 2026-06-01-workflow-runtime-persona-packet-validator-dogfood-audit
- Case Root: `docs/cases/persona-system-expansion/`
- Round Root: `docs/cases/persona-system-expansion/rounds/2026-06-01-workflow-runtime-persona-packet-validator-dogfood-audit/`
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

- User Request: `new $ww round: runtime persona packet validator dogfood audit. Based on the completed and pushed packet dogfood pilot and packet validator expansion, audit whether the new validator covers real packet artifacts, negative drift fixtures, full-file hash fallback, explicit-revision excerpt identity, repo-relative path containment, multi-section snapshot, secondary reviewer lane, and repo suite integration. Only audit and classify; do not change validator, packet contract, runtime code, personas, or routing. Judge whether a canonical slice resolver design round is truly needed.`
- Working Brief Reference: `docs/cases/persona-system-expansion/rounds/2026-06-01-workflow-runtime-persona-packet-validator-dogfood-audit/working-brief.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: produce a dogfood gap report that audits the pushed runtime persona packet validator against real packet artifacts, focused drift fixtures, full-file and excerpt identity semantics, path containment, section-aware snapshots, secondary reviewer lanes, and aggregate repo integration
- Relevant Context: commit `b97f1b3` completed the packet dogfood artifacts and validator expansion; the remaining question is whether current proof justifies a canonical slice resolver design round
- Constraints:
  - produce only `docs/cases/persona-system-expansion/rounds/2026-06-01-workflow-runtime-persona-packet-validator-dogfood-audit/design-spec.md`
  - do not edit validators
  - do not edit packet contract surfaces
  - do not implement runtime code
  - do not add, remove, or edit persona records
  - do not change `docs/superpowers/personas/registry.yaml`
  - do not expand routing
  - do not add secondary tags
- Risks:
  - mistaking representative fixture coverage for exhaustive proof
  - overlooking the deliberate semantic boundary between recomputed full-file hashes and explicit-revision excerpt identities
  - proposing canonical slice resolution before stable slice semantics exist
  - turning audit findings into unapproved implementation changes
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Runtime Persona Packet Validator Dogfood Audit

- Section ID: section-runtime-persona-packet-validator-dogfood-audit
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: technical-writer
- Planned Reviewer Persona: spec-reviewer
- Planned Reviewer Persona Source: built-in
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: the review target is a contract-focused validator evidence audit whose value depends on complete classification and a justified follow-up decision
- Planned Specialist Personas:
  - Persona ID: technical-writer
    - Source: built-in
    - Runtime Role: worker
    - Selection Rationale: the section produces a maintainer-facing evidence audit and must distinguish proven validation behavior, representative fixture coverage, and deferred slice-resolution design
- Planned Scope:
  - `docs/cases/persona-system-expansion/rounds/2026-06-01-workflow-runtime-persona-packet-validator-dogfood-audit/design-spec.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: audit the pushed packet validator before creating another design round, so canonical slice resolution is opened only if current evidence establishes a real need
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: conservative-first
- Worker Mode Rationale: the work is an evidence-bound audit over pushed artifacts and tests, with explicit prohibitions on validator, contract, and runtime changes
- Goal Tuning: audit-biased
- Constraint Interaction Rule: if an observation implies validator, contract, runtime, persona, registry, routing, or secondary-tag work, record it as a follow-up recommendation instead of editing those surfaces
- Planned Review Lanes:
  - Lane ID: lane-runtime-persona-packet-validator-dogfood-audit-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: review implementation and fixture evidence classification, explicit-revision excerpt boundaries, and the canonical-slice-resolver recommendation
  - Required: true
- Review lane mapping rule: default built-in reviewer mapping is `spec-review` -> `spec-reviewer`, `code-quality-review` -> `code-quality-reviewer`, `scope-review` -> `product-scope-reviewer`, `editorial-review` -> `editorial-reviewer`, and `other` -> explicit rationale only.
- Cross-cutting reviewer rule: add `secure-software-engineer`, `accessibility-ux-reviewer`, or `documentation-clarity-reviewer` as a second review lane when that risk surface is independently material, or use one for `other` only with explicit rationale that no durable lane type fits.
- Worker specialist mapping rule: select worker specialists by owned scope and dominant implementation risk, not top-level `task_routing` alone.
- Persona source rule: project personas win only after role-gate and required-field eligibility, and only when stronger or project-specific; otherwise record built-in fallback rationale.
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/persona-system-expansion/case.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-06-01-workflow-runtime-persona-packet-validator-dogfood-audit/working-brief.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-06-01-workflow-runtime-persona-packet-validator-dogfood-audit/dispatch-plan.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-06-01-workflow-runtime-persona-packet-validator-dogfood-audit/design-spec.md`
  - `shared_read_scope`:
    - `path_glob`: `README.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `path_glob`: `docs/superpowers/personas/registry.yaml`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/**`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-validator-expansion/**`
    - `path_glob`: `tools/validate_ww_persona_packets.py`
    - `path_glob`: `tools/test_validate_ww_persona_packets.py`
    - `path_glob`: `tools/validate_ww_repo.py`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: runtime_persona_packet_validator_dogfood_gap_report
      - `artifact_kind`: dogfood_gap_report
      - `artifact_path`: `docs/cases/persona-system-expansion/rounds/2026-06-01-workflow-runtime-persona-packet-validator-dogfood-audit/design-spec.md`
      - `section_anchors`: packet validator dogfood findings
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Runtime Persona Packet Validator Dogfood Audit

- Section ID: section-runtime-persona-packet-validator-dogfood-audit
- Runtime State: complete
- Active Execution ID: execution-runtime-persona-packet-validator-dogfood-audit
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
  - Execution ID: execution-runtime-persona-packet-validator-dogfood-audit
  - Role: technical-writer
  - Status: complete
  - Owned Scope: `docs/cases/persona-system-expansion/rounds/2026-06-01-workflow-runtime-persona-packet-validator-dogfood-audit/design-spec.md`
  - Started At: 2026-06-01
  - Finished At: 2026-06-01
- Packet Records:
- Attempt Records:
- Attempt Count: 0
- Last Update At: 2026-06-01
- Next Action: round complete
- Active Write Scope: `docs/cases/persona-system-expansion/rounds/2026-06-01-workflow-runtime-persona-packet-validator-dogfood-audit/design-spec.md`
- Result Summary: audited pushed packet validator evidence; current contract is adequately dogfooded; optional explicit traversal fixtures are a narrow hardening opportunity; canonical slice resolver design should remain deferred until a real excerpt-backed packet and stable slice semantics exist
- Canonical Result Artifact Location: `docs/cases/persona-system-expansion/rounds/2026-06-01-workflow-runtime-persona-packet-validator-dogfood-audit/design-spec.md`
- Concerns:
  - keep the round audit-only; no validator, contract, runtime, persona, registry, routing, or secondary-tag edits
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Runtime Persona Packet Validator Dogfood Audit

- Section ID: section-runtime-persona-packet-validator-dogfood-audit
- Review Target Strategy:
  - Review the dogfood gap report for faithful implementation and fixture classification, explicit-revision excerpt semantics, scope boundaries, and a justified canonical-slice-resolver recommendation.
- Review Lane Records:
  - Lane ID: lane-runtime-persona-packet-validator-dogfood-audit-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: review validator dogfood evidence and the boundary between current proof and future canonical slice resolution
  - Execution ID: execution-runtime-persona-packet-validator-dogfood-audit-review
  - Packet ID:
  - Attempt ID: local-spec-review-2026-06-01
  - Review Target Ref:
    - Artifact Path: `docs/cases/persona-system-expansion/rounds/2026-06-01-workflow-runtime-persona-packet-validator-dogfood-audit/design-spec.md`
    - Artifact Kind: dogfood_gap_report
    - Artifact Revision:
    - Schema Version: 1
    - Section Anchor: packet validator dogfood findings
    - Content Hash:
  - Reviewer Findings: no material findings; the report correctly distinguishes artifact-backed full-file verification from explicit-revision excerpt identity persistence and classifies direct traversal fixtures as optional hardening rather than a current contract failure
  - Orchestrator Synthesis: current validator evidence is sufficient for the active packet contract; defer canonical slice resolver design until a real excerpt-backed packet and stable selector, normalization, ambiguity, and immutable-source semantics exist
  - Strict Review Outcome: none
- Human Decision: Approve
- Revision Notes: user approved the reviewed packet validator dogfood gap report on 2026-06-01; report status approved, section state accepted, runtime state complete, and plan state completed
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level `plan_state` is derived from `required_for_goal`

## Ordering And Parallelism

- Blocking work first: section-runtime-persona-packet-validator-dogfood-audit
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
- Approved By: human
- Approval Time: 2026-06-01
- Notes: approval authorizes audit artifact creation only; validators, packet contracts, runtime code, persona records, project registry, routing, and secondary tags remain read-only
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial runtime persona packet validator dogfood audit round
- Supersedes Revision:

## Dispatch Log

- Agents Launched:
- Retry Events:
- Close Events:
  - 2026-06-01: user approved the reviewed runtime persona packet validator dogfood gap report; section closed complete
- Review Lane Transitions:
- Launch Time:
- 2026-06-01: user approved revision 1; audit artifact production authorized
- 2026-06-01: audit report drafted and locally spec-reviewed; plan moved from `approved` to `dispatched`
- 2026-06-01: user approved reviewed audit report; plan moved from `dispatched` to `completed`
- Revisions Since Approval: 0
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
