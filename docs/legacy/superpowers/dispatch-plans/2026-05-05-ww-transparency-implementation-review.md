# Dispatch Plan: WW Transparency Implementation Review

- Date: 2026-05-05
- Plan Revision: 2
- Working Brief Version: 2
- Plan State: completed
- Last Approved Revision: 1
- Rollback Baseline Revision: 1
- Task Routing: code/programming
- Main Orchestrator: staff engineer orchestrator

## Preconditions

- Estimation Complete: true
- Working Brief Status: ready

> Do not launch any real subagent until the preconditions are satisfied and `Plan State: approved`.

## Source Context

- User Request: First use `$ww review` on the `ww` project itself before any further action.
- Working Brief Reference: `docs/legacy/superpowers/working-briefs/2026-05-05-ww-transparency-implementation-review.md`

## Dispatch Summary

- Goal: Revise the transparency-implementation rollout plan so the validated contract gaps are fixed in a controlled follow-up before commit.
- Relevant Context:
  - The completed design round already produced `docs/maintainers/specs/2026-05-04-ww-user-transparency-design.md`.
  - The completed planning round already produced `docs/maintainers/plans/2026-05-04-ww-user-transparency-implementation.md`.
  - The live diff touches three contract artifacts: `SKILL.md`, `assets/dispatch-plan-template.md`, and `references/subagent-packet-contract.md`.
  - Contract-level grep checks pass, and `quick_validate.py` now reports `Skill is valid!`.
  - Review pass `review-1` already evaluated the current diff and found four gaps worth fixing before commit: missing persisted critical-path marker, packet-field drift between `SKILL.md` and the packet contract, under-specified `Display Status` vocabulary, and a non-conforming packet example.
- Constraints:
  - Keep the remediation inside the same three contract artifacts.
  - Do not rewrite the approved design or expand into new product scope.
  - Re-enter approval before any remediation edits are executed.
- Risks:
  - One artifact may still declare stronger guarantees than the others can persist or render.
  - Fixing only the template or only `SKILL.md` would leave packet composition rules inconsistent.
  - Starting edits before the revised plan is re-approved would violate the skill's rollback rules.
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Transparency Contract Remediation

- Section ID: transparency-contract-remediation
- Section State: accepted
- Draft Author Role: staff engineer orchestrator
- Planned Reviewer Persona: review-only code reviewer
- Planned Specialist Personas: none
- Planned Scope:
  - Add a persisted critical-path marker to the dispatch-plan template so the reply contract can render from saved state only.
  - Sync the top-level packet-field list in `SKILL.md` with the stricter packet contract.
  - Define the persisted `Display Status` vocabulary and selection rules strongly enough to make cross-turn rendering deterministic.
  - Make the packet example conform to the required-field contract.
- Planning Rationale: The previous review round already isolated the real gaps, so the next slice should be a tight remediation pass against the same three files before any new review.
- Planned Workflow Bindings:
  - `superpowers:receiving-code-review`
  - `superpowers:test-driven-development`
  - `superpowers:verification-before-completion`
- Packet Created: false

## Section Review Record

### Section: Transparency Contract Remediation

- Section ID: transparency-contract-remediation
- Review Status: completed
- Reviewer Findings:
  - no material findings
- Orchestrator Synthesis:
  - Revision 2 closes the previously validated sync gaps without introducing a new material contract mismatch in the three touched artifacts. Local contract checks pass, `quick_validate.py` reports `Skill is valid!`, and the re-review found no material findings.
- Human Decision: Approve
- Revision Notes:
  - Revision 2 was created after the user chose `Revise` on the review result.
  - The prior review findings are being converted into a bounded remediation plan rather than being implemented blindly.
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped` and plan state becomes `stopped`

## Ordering And Parallelism

- Blocking work first: approve the remediation round before any contract edits are made.
- Parallel sections: none
- Review loop per section: draft -> reviewer findings -> orchestrator synthesis -> human judgment

## Progress Board

> The `Progress Board` is the canonical store for rendered-progress inputs. The reply must not invent values that are absent from this section.

### Workstream: Transparency Contract Remediation

- Workstream ID: transparency-contract-remediation
- Source Section ID: transparency-contract-remediation
- Source Plan Revision: 2
- Workstream Type: implementation
- Scope: revise three ww contract artifacts to fix the validated transparency-sync gaps before re-review
- Owner: staff engineer orchestrator
- Internal State Reference: plan-state completed; section-state accepted; review-status completed; human-decision approved; remediation-verification complete
- Display Status: completed
- Last Update: user approved revision 2 after re-review returned no material findings
- Blocker: none
- Next Handoff: user chooses next integration step
- Review Pass ID: review-2

## Approval Block

- Required Human Choice: `Approve` | `Revise` | `Stop`
- Current Choice: Approve
- Approved By: user
- Approval Time: 2026-05-05
- Notes:
  - Revision 1 was approved and completed through a reviewer pass.
  - User approved revision 2 with `approve`.
  - Execute the bounded remediation in the same three contract artifacts, then re-run contract validation.
  - User approved the post-remediation result after `review-2` returned no material findings.
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial `$ww review` round for the transparency implementation diff
- Supersedes Revision: none
- Revision 2 Created From Brief Version: 2
- Revision Reason: user chose `Revise` after review findings; convert validated findings into a bounded remediation plan
- Supersedes Revision: Revision 1

## Dispatch Log

- Agents Launched: review-only code reviewer
- Launch Time: 2026-05-05
- Completion Time: 2026-05-05
- Revisions Since Approval: 1
- Stop State Preserves Files: true
- No Launch Before Approval: true
