# Dispatch Plan: Reviewer Persona Pilot

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

- User Request: `2` after the orchestrator pilot commit, meaning open a reviewer persona pilot round
- Working Brief Reference: `docs/legacy/superpowers/working-briefs/2026-05-19-reviewer-persona-pilot-v1.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: enrich `secure-software-engineer` so the reviewer layer becomes more precise about materiality, risk focus, and escalation posture before any runtime adoption work
- Relevant Context: orchestrator enrichment is complete, and the implementation plan calls for reviewer persona enrichment next while keeping findings-only behavior in role prompts and packet contracts
- Constraints:
  - only edit the `secure-software-engineer` persona record
  - do not change `reviewer-prompt.md`, packet contracts, `SKILL.md`, or validators in this round
  - do not add new personas or expand into worker or runtime-adoption work
- Risks:
  - the pilot can fail by repeating reviewer-role rules instead of sharpening judgment
  - generic security language can sound stronger without improving routing or review focus
  - weak escalation wording can leave the reviewer sounding more confident than the contract should allow
  - a merely careful-sounding reviewer can still fail if it does not make bad release decisions easier to stop
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Built-In Reviewer Persona Pilot

- Section ID: section-reviewer-pilot
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: senior-backend-engineer
- Planned Reviewer Persona: creative-director-orchestrator
- Planned Specialist Personas: secure-software-engineer
- Planned Scope:
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: the reviewer pilot should refine the judgment posture of the existing reviewer persona without altering the findings-only runtime role
  The revision bar is Jobs-like: reject weak blocking criteria, remove average overlap, and make the reviewer more decisive about what should not ship.
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: plan-first
- Worker Mode Rationale: the pilot should design one coherent reviewer viewpoint around materiality and risk focus instead of filling optional fields independently
- Goal Tuning: safety-biased
- Constraint Interaction Rule: preserve the phase 1 compatibility boundary and reject any enrichment that merely restates reviewer prompt behavior
  Reject filler threat-model language, balanced checklist phrasing, and any enrichment that sounds more serious without changing what the reviewer would actually block or escalate.
- Planned Review Lanes:
  - Lane ID: lane-reviewer-pilot-review
  - Lane Type: scope-review
  - Reviewer Persona: creative-director-orchestrator
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/legacy/superpowers/working-briefs/2026-05-19-reviewer-persona-pilot-v1.md`
    - `path_glob`: `docs/legacy/superpowers/dispatch-plans/2026-05-19-reviewer-persona-pilot.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `shared_read_scope`:
    - `path_glob`: `docs/legacy/superpowers/specs/2026-05-19-persona-enrichment-strategy-design.md`
    - `path_glob`: `docs/legacy/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/agents/reviewer-prompt.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
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
    - `artifact_id`: `reviewer_role_contract`
    - `artifact_kind`: `prompt`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/agents/reviewer-prompt.md`
    - `section_anchors`: `Responsibilities`, `Operating rules`
    - `artifact_id`: `persona_strategy_plan`
    - `artifact_kind`: `doc`
    - `artifact_path`: `docs/legacy/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
    - `section_anchors`: `Enrich reviewer personas second`
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Built-In Reviewer Persona Pilot

- Section ID: section-reviewer-pilot
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
- Result Summary: the built-in reviewer persona was enriched with sharper materiality, exploitability, and escalation posture while keeping the findings-only runtime role unchanged
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns:
  - the persona may still read like a generic security reviewer unless materiality is made explicit
  - escalation posture can easily become vague unless it is tied to concrete uncertainty or release risk
  - the pilot will miss if the reviewer still sounds like it is cataloging risks instead of killing unacceptable outcomes
- Blocker Reason:
- Close State: open
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Built-In Reviewer Persona Pilot

- Section ID: section-reviewer-pilot
- Review Target Strategy:
  - validate that the reviewer persona gains a clearer materiality bar
  - validate that risk focus becomes more specific instead of more verbose
  - validate that the pilot stays inside the phase 1 compatibility boundary
  - validate that weak blocking criteria are removed instead of hidden behind richer wording
- Review Lane Records:
  - Lane ID: lane-reviewer-pilot-review
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
    - no material findings; the pilot sharpens what the reviewer should block or escalate without collapsing persona fields into reviewer-prompt behavior
  - Orchestrator Synthesis:
    - the reviewer pilot now makes `secure-software-engineer` feel more decisive about trust-boundary risk and release-stop conditions instead of merely more verbose
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

- Blocking work first: `section-reviewer-pilot`
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
- Notes: this pilot round is scoped to built-in reviewer persona enrichment only, with a stricter taste-and-decision bar than the original draft
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial pilot round for built-in reviewer persona enrichment
- Supersedes Revision:

## Dispatch Log

- Agents Launched: none
- Retry Events:
- Close Events:
- Review Lane Transitions:
  - phase 1 contract reviewed
  - orchestrator pilot completed
  - reviewer pilot scope framed from the approved implementation plan
  - user requested a Jobs-style revision to make reviewer judgment more decisive and less checklist-driven
  - working brief persisted
  - dispatch plan drafted
  - `secure-software-engineer` enriched with judgment-oriented reviewer fields
  - repo-level validation and reviewer persona YAML checks passed
  - bounded review found no material findings
- Launch Time: 2026-05-19 America/Los_Angeles
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
