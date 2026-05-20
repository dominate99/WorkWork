# Dispatch Plan: Orchestrator Persona Pilot

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

- User Request: `开新的 $ww round 做 orchestrator pilot`
- Working Brief Reference: `docs/superpowers/working-briefs/2026-05-19-orchestrator-persona-pilot-v1.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: enrich the built-in orchestrator pilot set with contrasted judgment-oriented fields so the orchestrator layer becomes more differentiated before any runtime adoption work
- Relevant Context: phase 1 defined optional enrichment fields and migration rules, but the built-in orchestrator records still use only the pre-enrichment baseline
- Constraints:
  - only edit the three built-in orchestrator persona records
  - do not change `SKILL.md`, packet contracts, prompts, or validators in this round
  - do not add new personas or expand into reviewer or worker pilots
- Risks:
  - the pilot can become decorative if the three orchestrators sound richer without becoming more different
  - filling every optional field symmetrically can reduce routing clarity
  - runtime-role behavior could leak into persona records if the wording is not kept viewpoint-oriented
  - a merely "well-rounded" pilot can still fail if it does not make weak overlap easy to remove
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Built-In Orchestrator Persona Pilot

- Section ID: section-orchestrator-pilot
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: senior-backend-engineer
- Planned Reviewer Persona: creative-director-orchestrator
- Planned Specialist Personas: pm-orchestrator
- Planned Scope:
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: the first pilot should enrich the orchestrator layer as a contrasted set because it has the highest leverage on routing, synthesis, and escalation quality
  The revision bar is Jobs-like: remove average overlap, sharpen what each orchestrator defends, and make selection feel more decisive rather than more descriptive.
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: plan-first
- Worker Mode Rationale: this round should design the three orchestrator records as a single contrasted system instead of patching each record independently
- Goal Tuning: safety-biased
- Constraint Interaction Rule: preserve the phase 1 contract boundary and optimize for routing contrast rather than symmetric completeness
  Reject filler fields, balanced committee phrasing, and any enrichment that does not change what the orchestrator would actually notice, reject, or escalate.
- Planned Review Lanes:
  - Lane ID: lane-orchestrator-pilot-review
  - Lane Type: scope-review
  - Reviewer Persona: creative-director-orchestrator
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/superpowers/working-briefs/2026-05-19-orchestrator-persona-pilot-v1.md`
    - `path_glob`: `docs/superpowers/dispatch-plans/2026-05-19-orchestrator-persona-pilot.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `shared_read_scope`:
    - `path_glob`: `docs/superpowers/specs/2026-05-19-persona-enrichment-strategy-design.md`
    - `path_glob`: `docs/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
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
    - `section_anchors`: `Optional Persona Enrichment Fields`, `Phase 1 Compatibility Boundary`, `Migration Rules`
    - `artifact_id`: `persona_strategy_plan`
    - `artifact_kind`: `doc`
    - `artifact_path`: `docs/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
    - `section_anchors`: `Pilot enrichment on orchestrator personas first`
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Built-In Orchestrator Persona Pilot

- Section ID: section-orchestrator-pilot
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
- Result Summary: the three built-in orchestrator personas were enriched with contrasted judgment-oriented fields that sharpen systems, product, and creative decision posture without changing runtime contracts
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns:
  - orchestrator contrast may still be too shallow if enrichment entries overlap heavily
  - taste and escalation language can drift into vague prose if not kept operational
  - the pilot will miss the mark if all three personas still read like variations of the same competent generalist
- Blocker Reason:
- Close State: open
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Built-In Orchestrator Persona Pilot

- Section ID: section-orchestrator-pilot
- Review Target Strategy:
  - validate that each orchestrator gains a distinct decision posture
  - validate that the three enriched records improve routing contrast as a set
  - validate that the pilot stays inside the phase 1 compatibility boundary
  - validate that weak overlap is removed instead of hidden behind richer wording
- Review Lane Records:
  - Lane ID: lane-orchestrator-pilot-review
  - Lane Type: scope-review
  - Reviewer Persona: creative-director-orchestrator
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
    - no material findings; the pilot increases contrast across the three orchestrators and avoids collapsing persona fields into runtime-role behavior
  - Orchestrator Synthesis:
    - the pilot now makes the default engineering, product, and creative orchestrators feel more decisive and easier to choose between
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

- Blocking work first: `section-orchestrator-pilot`
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
- Notes: this pilot round stayed scoped to built-in orchestrator persona enrichment only and used the stricter taste-and-differentiation bar from the Jobs-style revision
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial pilot round for built-in orchestrator persona enrichment
- Supersedes Revision:

## Dispatch Log

- Agents Launched: none
- Retry Events:
- Close Events:
- Review Lane Transitions:
  - phase 1 contract reviewed
  - orchestrator pilot scope framed from the approved implementation plan
  - user requested a Jobs-style revision to strengthen taste, contrast, and anti-overlap review pressure
  - working brief persisted
  - dispatch plan drafted
  - built-in orchestrator persona records enriched with contrasted judgment-oriented fields
  - bounded review found no material findings
- Launch Time: 2026-05-19 America/Los_Angeles
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
