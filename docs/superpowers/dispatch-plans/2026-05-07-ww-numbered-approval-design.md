# Dispatch Plan: WW Numbered Approval Design

- Date: 2026-05-07
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
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

- User Request: `$ww make a plan to change the workwork human interact like a check box and accept 1 approve, 2,revise, 3 stop some thing similar use number as same as the words`
- Working Brief Reference: `docs/superpowers/working-briefs/2026-05-07-ww-numbered-approval-v1.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: write and approve a bounded design spec for the numbered approval prompt contract before creating the implementation plan
- Relevant Context: the user wants a repo-only wording and contract update across `SKILL.md`, the dispatch plan template, and the README; no parser or GUI layer is in scope
- Constraints: preserve approval semantics, keep word aliases, keep historical docs out of scope, and do not launch any real subagent work before approval
- Risks:
  - the skill and template may diverge on how numbered choices are described
  - the README may continue to imply the old words-only prompt
  - the plan could accidentally drift into parser or UI implementation
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Numbered Approval Prompt Design

- Section ID: section-numbered-approval-design
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: staff engineer orchestrator
- Planned Reviewer Persona: runtime policy reviewer
- Planned Specialist Personas: staff engineer orchestrator
- Planned Scope:
  - `docs/maintainers/specs/2026-05-07-ww-numbered-approval-design.md`
  - `docs/superpowers/working-briefs/2026-05-07-ww-numbered-approval-v1.md`
- Planning Rationale: this round exists to lock the approval prompt contract and scope boundary before an implementation plan is written
- Planned Workflow Bindings:
  - `superpowers:brainstorming`
  - `superpowers:writing-plans`
- Planned Review Lanes:
  - Lane ID: lane-design-scope-review
  - Lane Type: scope-review
  - Reviewer Persona: runtime policy reviewer
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/maintainers/specs/2026-05-07-ww-numbered-approval-design.md`
    - `path_glob`: `docs/superpowers/working-briefs/2026-05-07-ww-numbered-approval-v1.md`
    - `path_glob`: `docs/superpowers/dispatch-plans/2026-05-07-ww-numbered-approval-design.md`
  - `shared_read_scope`:
    - `path_glob`: `skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `path_glob`: `README.md`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: `numbered_approval_design_spec`
    - `artifact_kind`: `spec`
    - `artifact_path`: `docs/maintainers/specs/2026-05-07-ww-numbered-approval-design.md`
    - `section_anchors`: none
- Packet Created: false

## Section Runtime Ledger

### Section: Numbered Approval Prompt Design

- Section ID: section-numbered-approval-design
- Runtime State: review-pending
- Active Execution ID:
- Active Packet ID:
- Active Agent ID:
- Active Attempt ID:
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
  - Result Summary: written design spec is ready for user review
  - Result Artifact Location: `docs/maintainers/specs/2026-05-07-ww-numbered-approval-design.md`
- Attempt Count: 0
- Last Update At: 2026-05-07 America/Los_Angeles
- Next Action: user reviews the written design spec and chooses Approve, Revise, or Stop
- Active Write Scope:
- Result Summary: written design spec is ready for review
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns:
- Blocker Reason:
- Close State: open
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Numbered Approval Prompt Design

- Section ID: section-numbered-approval-design
- Review Status: completed
- Review Target Strategy: user reviews the written spec before implementation planning begins
- Review Lane Records:
  - Lane ID: lane-design-scope-review
  - Lane Type: scope-review
  - Reviewer Persona: runtime policy reviewer
  - Execution ID:
  - Packet ID:
  - Attempt ID:
  - Review Target Ref:
    - Artifact Path: `docs/maintainers/specs/2026-05-07-ww-numbered-approval-design.md`
    - Artifact Kind: `spec`
    - Artifact Revision: 1
    - Schema Version: 1
    - Section Anchor:
    - Content Hash:
  - Review Status: completed
  - Reviewer Findings:
    - no material findings in the bounded design draft; the remaining gate is user review
  - Orchestrator Synthesis:
    - Recommendation: approve the design if the numbered prompt contract and repo-only scope match intent, then proceed to implementation planning.
    - Reason: the design keeps approval semantics unchanged, preserves word aliases, and limits the later edit surface to the three requested active files.
- Human Decision: Approve
- Revision Notes:
- user approved the written design and requested the implementation plan
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level `plan_state` is derived from `required_for_goal`

## Ordering And Parallelism

- Blocking work first: `section-numbered-approval-design`
- Parallel sections: none
- Review loop per section: draft -> reviewer findings -> orchestrator synthesis -> human judgment

## Approval Block

- Required Human Choice: `Approve` | `Revise` | `Stop`
- Current Choice: Approve
- Approved By: user
- Approval Time: 2026-05-07 America/Los_Angeles
- Notes: user approved the design spec, which closes the design round and allows implementation planning
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial design review round for the numbered approval prompt contract
- Supersedes Revision:

## Dispatch Log

- Agents Launched: none
- Retry Events:
- Close Events:
- Review Lane Transitions:
  - design draft written locally
  - spec self-review completed locally
  - user approved the written design spec
  - implementation plan written after design approval; waiting for execution choice
- Launch Time:
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
