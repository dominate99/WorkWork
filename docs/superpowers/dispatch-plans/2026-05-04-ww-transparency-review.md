# Dispatch Plan: WW Transparency Review

- Date: 2026-05-04
- Plan Revision: 1
- Working Brief Version: 1
- Plan State: approved
- Last Approved Revision: 1
- Rollback Baseline Revision: none
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

- Goal: Produce a written PM design spec that upgrades the `ww` skill from artifact-heavy orchestration to status-visible orchestration.
- Relevant Context: The current skill exposes gates and document summaries, but it does not clearly show current stage, waiting state, blocker state, or per-subagent progress in the chat reply itself.
- Constraints: Keep the existing approval lifecycle, reviewer convergence rules, and document summary contract. Improve transparency without turning replies into raw execution logs.
- Risks: Adding status detail can create noisy replies, duplicate document content, or confuse users if internal states are shown without translation.
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: PM Transparency Redesign Spec

- Section ID: section-pm-transparency-redesign
- Section State: drafted
- Draft Author Role: PM orchestrator
- Planned Reviewer Persona: PM reviewer (findings only; not launched in this round)
- Planned Specialist Personas: none
- Planned Scope: Define the user-facing response contract, subagent progress visibility model, decision prompt model, and state-language translation for the `ww` skill.
- Planning Rationale: This round is a single PM design artifact with low implementation ambiguity, so a single-orchestrator pass is the highest-signal path.
- Planned Workflow Bindings: `superpowers:brainstorming`
- Packet Created: false

## Section Review Record

### Section: PM Transparency Redesign Spec

- Section ID: section-pm-transparency-redesign
- Review Status: not-started
- Reviewer Findings:
- Orchestrator Synthesis:
- Human Decision: none
- Revision Notes:
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped` and plan state becomes `stopped`

## Ordering And Parallelism

- Blocking work first: write the design spec, self-review it, then pause for user review before any implementation planning
- Parallel sections: none
- Review loop per section: draft -> reviewer findings -> orchestrator synthesis -> human judgment

## Progress Board

### Workstream: PM Transparency Redesign Spec

- Owner: PM orchestrator
- Status: awaiting user review
- Last Update: written spec completed and self-reviewed; waiting for user review before implementation planning
- Blocker: none
- Next Handoff: user reviews the written spec

## Approval Block

- Required Human Choice: `Approve` | `Revise` | `Stop`
- Current Choice: Approve
- Approved By: user
- Approval Time: 2026-05-04
- Notes: Approval covers the PM direction for the redesign proposal. It does not yet approve implementation.
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial PM transparency redesign dispatch
- Supersedes Revision:

## Dispatch Log

- Agents Launched: none
- Launch Time:
- Revisions Since Approval: 0
- Stop State Preserves Files: true
- No Launch Before Approval: true
