# Dispatch Plan: WW Transparency Review

- Date: 2026-05-04
- Plan Revision: 4
- Working Brief Version: 4
- Plan State: awaiting-approval
- Last Approved Revision: 1
- Rollback Baseline Revision: 1
- Task Routing: design/ads/product
- Main Orchestrator: PM orchestrator

## Preconditions

- Estimation Complete: true
- Working Brief Status: ready

> Do not launch any real subagent until the preconditions are satisfied and `Plan State: approved`.

## Source Context

- User Request: Review and improve the `ww` skill with stronger user-facing transparency and better subagent progress visibility; then produce a PM-oriented revision proposal.
- Working Brief Reference: `docs/superpowers/working-briefs/2026-05-04-ww-transparency-review.md`

## Dispatch Summary

- Goal: Produce a revised written PM design spec that upgrades the `ww` skill from artifact-heavy orchestration to status-visible orchestration and resolves the remaining contract-level engineering review findings.
- Relevant Context: The current skill exposes gates and document summaries, but it does not clearly show current stage, waiting state, blocker state, or per-subagent progress in the chat reply itself. The third spec draft improved determinism, but still left gaps around deriving `waiting on` and `next action`, exact `Progress Board` schema, reviewer-progress identity, and example-rule alignment.
- Constraints: Keep the existing approval lifecycle, reviewer convergence rules, and document summary contract. Improve transparency without turning replies into raw execution logs or creating unsynchronized state sources.
- Risks: Adding status detail can create noisy replies, duplicate document content, confuse users if internal states are shown without translation, drift if rendered reply state is not anchored to a canonical persisted source, or create implementation variance if the schema and derivation contracts remain implicit.
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: PM Transparency Redesign Spec

- Section ID: section-pm-transparency-redesign
- Section State: revision-requested
- Draft Author Role: PM orchestrator
- Planned Reviewer Persona: staff engineer reviewer findings already incorporated; no new reviewer launch in this revision round
- Planned Specialist Personas: none
- Planned Scope: Define the user-facing response contract, subagent progress visibility model, decision prompt model, canonical runtime source, display-state mapping, update semantics, display-status precedence, critical-path stage selection, top-line derivation rules, and exact progress-board schema for the `ww` skill.
- Planning Rationale: This round remains a single PM design artifact, but the spec must now explicitly close the remaining engineering gaps around deterministic rendering and contract shape before implementation planning starts.
- Planned Workflow Bindings: `superpowers:brainstorming`
- Packet Created: false

## Section Review Record

### Section: PM Transparency Redesign Spec

- Section ID: section-pm-transparency-redesign
- Review Status: revision-requested
- Reviewer Findings:
- Resolve the contradiction between a fixed four-section reply shape and a conditional `Decision Block`
- Define the canonical source of runtime truth and how the chat reply derives from it
- Add explicit mapping rules between internal lifecycle states and user-facing display states
- Define when progress fields such as `last update` are refreshed and by whom
- Add precedence rules for overlapping display-status conditions
- Define how `current stage` is selected in parallel work
- Require same-turn rendering from the current persisted state
- Decide whether reviewer progress lives in the dispatch plan, the packet contract, or both
- Derive `user decision needed` and `Decision Block` from the same source
- Define exact derivation rules for `waiting on` and `next action`
- Define the exact `Progress Board` schema in the template contract
- Define reviewer-progress identity across review passes
- Align examples with the stricter rule set
- Orchestrator Synthesis:
- Human Decision: none
- Revision Notes:
- Revision 2 updates the design to make the dispatch plan the canonical runtime store and the chat reply a rendered view, preserves a fixed four-section reply shape, and adds display-state and refresh rules.
- Revision 3 adds deterministic precedence rules, critical-path stage selection, same-turn render rules, and a single persistence location for reviewer progress.
- Revision 4 adds exact top-line derivation rules, `Progress Board` schema requirements, reviewer identity rules, and example alignment.
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped` and plan state becomes `stopped`

## Ordering And Parallelism

- Blocking work first: revise the design spec using the latest staff engineer findings, self-review it, then pause for user review before any implementation planning
- Parallel sections: none
- Review loop per section: draft -> reviewer findings -> orchestrator synthesis -> human judgment

## Progress Board

### Workstream: PM Transparency Redesign Spec

- Owner: PM orchestrator
- Status: awaiting user review
- Last Update: revision 4 completed and self-reviewed after the latest staff engineer review; waiting for user review before implementation planning
- Blocker: none
- Next Handoff: user reviews the written spec

## Approval Block

- Required Human Choice: `Approve` | `Revise` | `Stop`
- Current Choice: none
- Approved By:
- Approval Time:
- Notes: Revision 4 incorporates the latest staff engineer review findings and is ready for renewed user approval. It does not yet approve implementation.
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial PM transparency redesign dispatch
- Supersedes Revision:
- Revision 2 Created From Brief Version: 2
- Revision Reason: revise the spec based on staff engineer review findings
- Supersedes Revision: 1
- Revision 3 Created From Brief Version: 3
- Revision Reason: revise the spec based on the second staff engineer review
- Supersedes Revision: 2
- Revision 4 Created From Brief Version: 4
- Revision Reason: revise the spec based on the third staff engineer review
- Supersedes Revision: 3

## Dispatch Log

- Agents Launched: none
- Launch Time:
- Revisions Since Approval: 3
- Stop State Preserves Files: true
- No Launch Before Approval: true
