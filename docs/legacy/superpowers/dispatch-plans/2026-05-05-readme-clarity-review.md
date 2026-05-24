# Dispatch Plan: README Clarity Review

- Date: 2026-05-05
- Plan Revision: 2
- Working Brief Version: 2
- Plan State: completed
- Last Approved Revision: 1
- Rollback Baseline Revision: 1
- Task Routing: design/ads/product
- Main Orchestrator: PM orchestrator

## Preconditions

- Estimation Complete: true
- Working Brief Status: ready

> Do not launch any real subagent until the preconditions are satisfied and `Plan State: approved`.

## Source Context

- User Request: `$ww check readme file is clean and easy to understand and the format is read friendly`
- Working Brief Reference: `docs/legacy/superpowers/working-briefs/2026-05-05-readme-clarity-review.md`

## Dispatch Summary

- Goal: Revise the README improvement plan so the validated clarity findings can be fixed in one bounded edit round.
- Relevant Context:
  - The README introduces the `ww-subagent-orchestrator` skill and repository layout.
  - It also includes installation instructions, GitHub install guidance, maintainer-doc references, persona-registry notes, and validation notes.
  - Review pass `review-1` found three issues worth fixing before this README can be called clean and easy to scan: a maintainer-doc path contradiction, weak audience separation, and front-loaded inventory that slows practical onboarding.
  - The user chose `Revise`, so this round converts those findings into a bounded rewrite plan rather than editing immediately.
- Constraints:
  - Keep the remediation inside `README.md` only.
  - Do not widen scope into repo-wide docs cleanup or other files.
  - Re-enter approval before any README edits are executed.
- Risks:
  - A rewrite that fixes only wording but not section order will leave the scanability problem intact.
  - A rewrite that fixes structure but leaves the path contradiction will still undermine trust.
  - Starting edits before this revised plan is re-approved would violate the rollback rules.
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Root README Remediation Plan

- Section ID: root-readme-remediation-plan
- Section State: accepted
- Draft Author Role: PM orchestrator
- Planned Reviewer Persona: review-only code reviewer
- Planned Specialist Personas: none
- Planned Scope:
  - Rewrite the README plan so the path contradiction is removed.
  - Separate the README into clearer reader modes: what the skill is, how to install it, and where maintainer docs live.
  - Reorder sections so a new reader hits practical orientation and install guidance before detailed repository inventory.
  - Keep the rewrite small enough to re-review in one pass.
- Planning Rationale: The previous review already isolated the reader-facing problems, so the next slice should be a bounded rewrite plan aimed only at those issues.
- Planned Workflow Bindings:
  - `superpowers:receiving-code-review`
  - `superpowers:verification-before-completion`
- Packet Created: true

## Section Review Record

### Section: Root README Remediation Plan

- Section ID: root-readme-remediation-plan
- Review Status: completed
- Reviewer Findings:
  - no material findings
- Orchestrator Synthesis:
  - The README rewrite resolves the validated contradiction, separates reader modes more clearly, and improves skim order without introducing a new material readability issue. The re-review found no material findings.
- Human Decision: Approve
- Revision Notes:
  - Revision 2 was created after the user chose `Revise` on the README review result.
  - The prior review findings are being converted into a bounded rewrite plan rather than being implemented blindly.
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped` and plan state becomes `stopped`

## Ordering And Parallelism

- Blocking work first: approve the README remediation plan before any README edits begin.
- Parallel sections: none
- Review loop per section: draft -> reviewer findings -> orchestrator synthesis -> human judgment

## Progress Board

> The `Progress Board` is the canonical store for rendered-progress inputs. The reply must not invent values that are absent from this section.
>
> Allowed `Display Status` values: `not started`, `queued`, `running`, `waiting on orchestrator`, `waiting on user`, `blocked`, `completed`, `failed`.
>
> `Display Status` precedence, highest to lowest: `failed`, `completed`, `blocked`, `waiting on user`, `waiting on orchestrator`, `running`, `queued`, `not started`.
>
> Mark the single workstream used for `Status Summary` with `Critical Path: yes`. All other workstreams must use `Critical Path: no`.

### Workstream: Root README Remediation Plan

- Workstream ID: root-readme-remediation-plan
- Source Section ID: root-readme-remediation-plan
- Source Plan Revision: 2
- Workstream Type: implementation
- Critical Path: yes
- Scope: revise the root README plan to fix the validated readability and consistency findings before editing
- Owner: PM orchestrator
- Internal State Reference: plan-state completed; section-state accepted; review-status completed; human-decision approved; remediation-edit complete
- Display Status: completed
- Last Update: user approved the rewritten README after re-review returned no material findings
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
  - User approved revision 2.
  - Execute the bounded README rewrite, then run a re-review before closing the round.
  - User approved the post-remediation result after `review-2` returned no material findings.
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial `$ww` review round for root README clarity and readability
- Supersedes Revision: none
- Revision 2 Created From Brief Version: 2
- Revision Reason: user chose `Revise` after review findings; convert validated README findings into a bounded rewrite plan
- Supersedes Revision: Revision 1

## Dispatch Log

- Agents Launched: review-only code reviewer
- Launch Time: 2026-05-05
- Completion Time: 2026-05-05
- Revisions Since Approval: 1
- Stop State Preserves Files: true
- No Launch Before Approval: true
