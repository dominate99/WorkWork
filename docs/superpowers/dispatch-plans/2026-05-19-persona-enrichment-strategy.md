# Dispatch Plan: Persona Enrichment Strategy

- Date: 2026-05-19
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Plan State: completed
- Last Approved Revision: none
- Rollback Baseline Revision: none
- Task Routing: design/ads/product
- Main Orchestrator: pm-orchestrator

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

- User Request: `$ww 你现在是乔布斯，你觉得persona 如何丰富 让我们的能力更强更好`
- Working Brief Reference: `docs/superpowers/working-briefs/2026-05-19-persona-enrichment-strategy-v1.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: produce a high-leverage strategy for enriching the persona system so it improves decision quality, taste, and execution strength
- Relevant Context: the repo already has clearer worker, reviewer, and explorer role contracts, but the persona layer is still relatively shallow and mostly registry-driven
- Constraints:
  - do not equate richer personas with merely adding more persona records
  - preserve the current separation between `persona`, `runtime_role`, and role prompt behavior
  - keep this round design-first rather than turning it into immediate schema implementation
- Risks:
  - overproducing persona records increases selection noise
  - verbose persona prose without stronger runtime meaning will not improve outcomes
  - a strong visionary answer can stay inspirational unless translated into a concrete model
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Persona System Enrichment Strategy

- Section ID: section-persona-strategy
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: pm-orchestrator
- Planned Reviewer Persona: senior-backend-engineer
- Planned Specialist Personas: creative-director-orchestrator
- Planned Scope:
  - `persona-registry.md`
  - `built-in-personas.yaml`
  - `docs/superpowers/personas/registry.yaml`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: the user is asking for a product/system direction, so the main job is to define a stronger persona model and prioritization sequence before any implementation
- Planned Workflow Bindings:
  - `superpowers:brainstorming`
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
- Planned Worker Mode: plan-first
- Worker Mode Rationale: after validating the current persona surface, the highest-leverage step is to synthesize an opinionated design rather than jumping to isolated edits
- Goal Tuning: speed-biased
- Constraint Interaction Rule: preserve the current role-contract model and avoid collapsing persona enrichment into more verbose registry text
- Planned Review Lanes:
  - Lane ID: lane-persona-strategy-review
  - Lane Type: scope-review
  - Reviewer Persona: senior-backend-engineer
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/superpowers/working-briefs/2026-05-19-persona-enrichment-strategy-v1.md`
    - `path_glob`: `docs/superpowers/dispatch-plans/2026-05-19-persona-enrichment-strategy.md`
  - `shared_read_scope`:
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `path_glob`: `docs/superpowers/personas/registry.yaml`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: `persona_registry_rules`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - `section_anchors`: `Required Persona Fields`, `Selection Rules`, `Prompt Binding Roles`
    - `artifact_id`: `built_in_personas`
    - `artifact_kind`: `data`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `section_anchors`: none
    - `artifact_id`: `project_personas`
    - `artifact_kind`: `data`
    - `artifact_path`: `docs/superpowers/personas/registry.yaml`
    - `section_anchors`: none
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Invalid state note: `Planned Scope` includes a writable file not mirrored in `exclusive_write_scope`.
- Packet Created: false

## Section Runtime Ledger

### Section: Persona System Enrichment Strategy

- Section ID: section-persona-strategy
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
- Result Summary: persona-enrichment strategy synthesized into a persisted design spec and a staged implementation plan for strengthening judgment, taste, tradeoff posture, and escalation behavior
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns:
  - the persona system currently lacks a strong notion of decision style, taste, escalation posture, and collaboration mode
  - the most dangerous failure mode is adding taxonomy rather than increasing decision quality
- Blocker Reason:
- Close State: open
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Persona System Enrichment Strategy

- Section ID: section-persona-strategy
- Review Target Strategy:
  - validate that the proposal enriches capability rather than inflating persona count
  - validate that the proposal stays compatible with the current role and packet model
  - validate that the recommendations are specific enough to drive a later implementation plan
- Review Lane Records:
  - Lane ID: lane-persona-strategy-review
  - Lane Type: scope-review
  - Reviewer Persona: senior-backend-engineer
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
    - no material findings; the strategy stays compatible with the current separation between persona, runtime_role, and role prompt behavior
  - Orchestrator Synthesis:
    - the highest-leverage path is to deepen persona judgment structure before increasing persona count
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

- Blocking work first: `section-persona-strategy`
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
- Notes: user approved the persona-enrichment strategy round; the follow-up request converted that strategy into a persisted implementation plan without starting runtime implementation
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial round for persona enrichment strategy
- Supersedes Revision:

## Dispatch Log

- Agents Launched: none
- Retry Events:
- Close Events:
- Review Lane Transitions:
  - persona-enrichment strategy round framed from current registry and runtime-role contracts
  - working brief persisted
  - dispatch plan drafted
  - strategy synthesized with emphasis on judgment structure over persona count growth
  - design spec persisted
  - implementation plan persisted from the approved strategy
  - bounded review found no material findings
- Launch Time: 2026-05-19 America/Los_Angeles
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
