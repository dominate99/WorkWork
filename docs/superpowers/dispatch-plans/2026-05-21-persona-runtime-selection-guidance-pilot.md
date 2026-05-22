# Dispatch Plan: Persona Runtime-Selection Guidance Pilot

- Date: 2026-05-21
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Plan State: completed
- Last Approved Revision: 1
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

- User Request: `新的 $ww round：persona runtime-selection guidance pilot`
- Working Brief Reference: `docs/superpowers/working-briefs/2026-05-21-persona-runtime-selection-guidance-pilot-v1.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: make enriched persona fields meaningfully available to runtime selection and rationale writing without yet expanding into packet, prompt, or validator adoption
- Relevant Context: persona pilots are complete across orchestrator, reviewer, and worker layers, but current registry rules still describe enrichment fields as advisory until runtime-adoption guidance is explicitly updated
- Constraints:
  - only update `persona-registry.md` and `SKILL.md`
  - do not change packet contracts, prompts, or validators in this round
  - do not add or modify persona records in this round
- Risks:
  - weak guidance leaves enrichment fields decorative and unused
  - overly strong guidance can turn optional fields into hidden hard gates
  - if selection rules and skill guidance diverge, orchestrators will get conflicting instructions
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Runtime Persona-Selection Guidance

- Section ID: section-runtime-selection-guidance
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: staff-engineer-orchestrator
- Planned Reviewer Persona: pm-orchestrator
- Planned Specialist Personas: creative-director-orchestrator
- Planned Scope:
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: the next highest-leverage adoption step is to teach orchestrators how to use enriched persona fields at selection time before those fields are pushed deeper into runtime surfaces
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: validate-first
- Worker Mode Rationale: this round should first validate how current guidance underuses enriched fields, then codify a deliberate runtime-selection policy
- Goal Tuning: validation-biased
- Constraint Interaction Rule: keep enriched fields usable and meaningful, but do not let them become hidden required fields or packet-time semantics yet
- Planned Review Lanes:
  - Lane ID: lane-runtime-selection-guidance-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/superpowers/working-briefs/2026-05-21-persona-runtime-selection-guidance-pilot-v1.md`
    - `path_glob`: `docs/superpowers/dispatch-plans/2026-05-21-persona-runtime-selection-guidance-pilot.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `shared_read_scope`:
    - `path_glob`: `docs/superpowers/specs/2026-05-19-persona-enrichment-strategy-design.md`
    - `path_glob`: `docs/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: `persona_registry_rules`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - `section_anchors`: `Selection Rules`, `Migration Rules`, `Built-In Routing Defaults`
    - `artifact_id`: `ww_skill_contract`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `section_anchors`: `Core Rules`, `Persona Planning`
    - `artifact_id`: `persona_strategy_plan`
    - `artifact_kind`: `doc`
    - `artifact_path`: `docs/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
    - `section_anchors`: `Update runtime-selection guidance after the pilot set is stable`
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Runtime Persona-Selection Guidance

- Section ID: section-runtime-selection-guidance
- Runtime State: not started
- Active Execution ID: execution-runtime-selection-guidance
- Active Packet ID:
- Active Agent ID:
- Active Attempt ID:
- Active Worker Mode: validate-first
- Mode Change History:
  - Previous Mode:
  - New Mode:
  - Trigger Evidence:
  - Approved By:
  - Changed At:
- Execution Records:
  - Execution ID: execution-runtime-selection-guidance
  - Role: orchestrator-implementation
  - Status: DONE
  - Owned Scope: `persona-registry.md`, `SKILL.md`, round documents
  - Started At: 2026-05-21 America/Los_Angeles
  - Finished At: 2026-05-21 America/Los_Angeles
- Packet Records:
  - Packet ID:
  - Execution ID:
  - Stage:
  - Template Path:
  - Review Target Ref:
  - Supersedes Attempt ID:
  - Accepts Late Results:
- Attempt Records:
  - Attempt ID: attempt-runtime-selection-guidance-1
  - Packet ID:
  - Agent ID:
  - Return Status: DONE
  - Runtime State After Return: complete
  - Launched At: 2026-05-21 America/Los_Angeles
  - Closed At: 2026-05-21 America/Los_Angeles
  - Result Summary: runtime-selection guidance now explicitly uses optional enrichment fields for ranking and rationale after required-field eligibility is established
  - Result Artifact Location: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`, `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- Attempt Count: 1
- Last Update At: 2026-05-21 America/Los_Angeles
- Next Action: none
- Active Write Scope:
- Result Summary: updated registry and skill guidance so required fields establish eligibility first and optional enrichment fields participate in ranking, tie-breaks, and rationale without becoming hidden gates
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns:
  - the guidance may still underuse enrichment fields if it does not specify concrete selection and tie-break points
  - the guidance may overshoot if it turns optional fields into hidden gates
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Runtime Persona-Selection Guidance

- Section ID: section-runtime-selection-guidance
- Review Target Strategy:
  - validate that enriched persona fields become actually usable for selection and rationale writing
  - validate that guidance preserves optionality and compatibility during transition
  - validate that packet, prompt, and validator adoption remain out of scope
- Review Lane Records:
  - Lane ID: lane-runtime-selection-guidance-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Execution ID: execution-runtime-selection-guidance
  - Packet ID:
  - Attempt ID: attempt-runtime-selection-guidance-1
  - Review Target Ref:
    - Artifact Path: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - Artifact Kind: doc
    - Artifact Revision: working-tree
    - Schema Version: 1
    - Section Anchor: `Selection Rules`
    - Content Hash:
  - Reviewer Findings: no material findings
  - Orchestrator Synthesis: selection guidance now makes optional enrichment fields usable after required-field eligibility is established, and the skill contract mirrors the same ranking, tie-break, and rationale posture without widening into packet or prompt semantics
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

- Blocking work first: `section-runtime-selection-guidance`
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
- Approval Time: 2026-05-21 America/Los_Angeles
- Notes: this pilot round is scoped to runtime persona-selection guidance only
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial pilot round for persona runtime-selection guidance
- Supersedes Revision:

## Dispatch Log

- Agents Launched: none
- Retry Events:
- Close Events:
- Review Lane Transitions:
  - phase 1 contract reviewed
  - orchestrator, reviewer, and worker persona pilots completed
  - runtime-selection guidance scope framed from the approved implementation plan
  - working brief persisted
  - dispatch plan drafted
- execution completed
- scope review completed with no material findings
- human approval received
- Launch Time: 2026-05-21 America/Los_Angeles
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
