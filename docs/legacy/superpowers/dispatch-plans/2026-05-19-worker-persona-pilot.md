# Dispatch Plan: Worker Persona Pilot

- Date: 2026-05-19
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Plan State: completed
- Last Approved Revision: none
- Rollback Baseline Revision: none
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

- User Request: `$ww round 做 worker persona pilot`
- Working Brief Reference: `docs/legacy/superpowers/working-briefs/2026-05-19-worker-persona-pilot-v1.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: enrich `senior-backend-engineer` and `java-pro-engineer` so the worker layer becomes more differentiated in implementation judgment before any runtime adoption work
- Relevant Context: orchestrator and reviewer enrichment are complete, and the implementation plan calls for worker persona enrichment next while preserving the current `implementation_principles` and `work_mode` model
- Constraints:
  - only edit the `senior-backend-engineer` and `java-pro-engineer` persona records
  - do not change `SKILL.md`, worker prompts, packet contracts, or validators in this round
  - do not alter existing `implementation_principles` unless a contradiction makes the current wording incompatible with the new fields
- Risks:
  - the pilot can fail by restating existing `implementation_principles` in longer form
  - language specialization alone is too weak if both workers still make the same tradeoffs
  - worker-specific enrichment can accidentally bleed into `work_mode` semantics or prompt behavior
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Built-In Worker Persona Pilot

- Section ID: section-worker-pilot
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: senior-backend-engineer
- Planned Reviewer Persona: staff-engineer-orchestrator
- Planned Specialist Personas: java-pro-engineer
- Planned Scope:
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: the worker pilot should refine the judgment posture of the existing worker personas without altering worker runtime-role surfaces
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: plan-first
- Worker Mode Rationale: the pilot should design the two worker personas as one contrasted pair that would choose differently under the same execution posture
- Goal Tuning: safety-biased
- Constraint Interaction Rule: preserve the phase 1 compatibility boundary and reject enrichment that merely paraphrases existing `implementation_principles` or leaks into `work_mode`
- Planned Review Lanes:
  - Lane ID: lane-worker-pilot-review
  - Lane Type: scope-review
  - Reviewer Persona: staff-engineer-orchestrator
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/legacy/superpowers/working-briefs/2026-05-19-worker-persona-pilot-v1.md`
    - `path_glob`: `docs/legacy/superpowers/dispatch-plans/2026-05-19-worker-persona-pilot.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `shared_read_scope`:
    - `path_glob`: `docs/legacy/superpowers/specs/2026-05-19-persona-enrichment-strategy-design.md`
    - `path_glob`: `docs/legacy/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/agents/worker-prompt.md`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: `built_in_personas`
    - `artifact_kind`: `data`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `section_anchors`: none
    - `artifact_id`: `persona_registry_rules`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - `section_anchors`: `Optional Persona Enrichment Fields`, `Phase 1 Compatibility Boundary`, `Migration Rules`, `Selection Rules`
    - `artifact_id`: `worker_contract_surfaces`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `section_anchors`: `Worker packets additionally require`, `Worker Packet Example`
    - `artifact_id`: `persona_strategy_plan`
    - `artifact_kind`: `doc`
    - `artifact_path`: `docs/legacy/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
    - `section_anchors`: `Enrich selected worker personas third`
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Built-In Worker Persona Pilot

- Section ID: section-worker-pilot
- Runtime State: complete
- Active Execution ID:
- Active Packet ID:
- Active Agent ID:
- Active Attempt ID:
- Active Worker Mode: plan-first
- Mode Change History:
  - Previous Mode:
  - New Mode:
  - Trigger Evidence:
  - Approved By:
  - Changed At:
- Execution Records:
  - Execution ID:
  - Role:
  - Status:
  - Owned Scope:
  - Started At:
  - Finished At:
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
- Last Update At: 2026-05-19 America/Los_Angeles
- Next Action: none
- Active Write Scope:
- Result Summary: the built-in worker persona pair was enriched with contrasted implementation-judgment fields so system-integrity and Java/framework correctness now read as different execution postures without changing worker runtime contracts
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns:
  - the pair may still feel too similar if the Java specialist does not produce different implementation tradeoffs
  - the broader backend persona may become too generic if system-integrity posture is not made explicit
- Blocker Reason:
- Close State: open
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Built-In Worker Persona Pilot

- Section ID: section-worker-pilot
- Review Target Strategy:
  - validate that the worker pair gains clearer implementation-choice contrast
  - validate that the new fields complement rather than duplicate `implementation_principles`
  - validate that the pilot stays inside the phase 1 compatibility boundary
- Review Lane Records:
  - Lane ID: lane-worker-pilot-review
  - Lane Type: scope-review
  - Reviewer Persona: staff-engineer-orchestrator
  - Execution ID:
  - Packet ID:
  - Attempt ID:
  - Review Target Ref:
    - Artifact Path:
    - Artifact Kind:
    - Artifact Revision:
    - Schema Version:
    - Section Anchor:
    - Content Hash:
  - Reviewer Findings:
    - no material findings; the pilot sharpens worker judgment contrast without duplicating worker-prompt behavior or replacing existing `implementation_principles`
  - Orchestrator Synthesis:
    - the worker pilot now makes `senior-backend-engineer` and `java-pro-engineer` feel like meaningfully different implementers under the same `work_mode`
  - Strict Review Outcome: none
  - Persistence rule: pre-approval plans must preserve this review-lane structure and outcome field pattern; `Review Status` must not reappear here, and durable review-lane data must retain `Reviewer Findings`, `Orchestrator Synthesis`, and the `Strict Review Outcome` field pattern.
  - Applicability rule: `Strict Review Outcome` is required when a strict-review target or durable strict-review result applies; otherwise keep the same field pattern without creating a second schema for valid non-strict lanes.
  - Invalid state note: `Review Status` reappears or durable strict-review outcome data is dropped when applicable.

- Human Decision: Approve
- Revision Notes:
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level `plan_state` is derived from `required_for_goal`

## Ordering And Parallelism

- Blocking work first: `section-worker-pilot`
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
- Approval Time: 2026-05-19 America/Los_Angeles
- Notes: this pilot round is scoped to built-in worker persona enrichment only
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial pilot round for built-in worker persona enrichment
- Supersedes Revision:

## Dispatch Log

- Agents Launched: none
- Retry Events:
- Close Events:
- Review Lane Transitions:
  - phase 1 contract reviewed
  - orchestrator and reviewer pilots completed
  - worker pilot scope framed from the approved implementation plan
  - working brief persisted
  - dispatch plan drafted
  - `senior-backend-engineer` and `java-pro-engineer` enriched with contrasted worker judgment fields
  - repo-level validation and worker persona YAML checks passed
  - bounded review found no material findings
- Launch Time: 2026-05-19 America/Los_Angeles
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
