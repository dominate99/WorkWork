# Working Brief: README Clarity Review

Use this brief after estimation and before any persona dispatch.

## Gate State

- `estimation_complete: true`
- `brief_status: ready`
- `brief_version: 2`

## Routing

- `task_routing`: `design/ads/product`
- `orchestrator_choice`: `PM orchestrator`

## Core Intent

- `goal`: Improve the repository root `README.md` so it reads cleanly, is easy to understand, and feels reader-friendly without widening into a repo-wide docs rewrite.
- `artifact_type`: user-facing documentation remediation plan
- `relevant_context`:
  - The target artifact is the repository root `README.md`.
  - The README currently explains the `ww-subagent-orchestrator` skill, repository layout, installation paths, maintainer docs, and validation notes.
  - Review pass `review-1` validated three reader-facing issues: one real path contradiction, weak audience separation across user/install/maintainer modes, and section ordering that slows skimming.
  - The user asked for cleanliness, ease of understanding, and reader-friendly formatting, so the next step is a bounded rewrite plan for `README.md`, not a repo-wide docs cleanup.
- `constraints`:
  - Stay within `README.md` only.
  - Revise only the structure and wording needed to resolve the validated readability findings.
  - Do not widen scope into other docs or unrelated repository cleanup.
  - The revised plan must return to approval before any README edits are made.

## Risk And Structure

- `risk_lenses`:
  - Reader-confusion risk if the README mixes user-install instructions with maintainer-only context without clear boundaries.
  - Trust risk if paths or repository-structure notes contradict each other.
  - Readability risk if sections are technically correct but not easy to scan.
  - Audience-fit risk if first-time users cannot tell which steps apply to them.
  - Revision-discipline risk if rewriting begins before the revised plan is explicitly re-approved.
- `parallelism_assessment`: low; this is one document and should stay in one bounded review stream.
- `blocking_dependencies`:
  - User approval of the revised README remediation plan before any README edits are made.
  - The remediation should stay anchored to the validated findings from `review-1`.
- `section_or_workstream_map`:
  - Section A: Revise the root README structure and wording plan to fix the validated clarity and formatting issues.

## Persona And Workflow Guidance

- `recommended_personas`:
  - `PM orchestrator`
  - `review-only code reviewer`
- `persona_selection_notes`:
  - `PM orchestrator` remains the right top-level owner because the current step is a user-facing documentation remediation plan rather than a code-delivery task.
  - The project persona registry still does not include a dedicated documentation reviewer, so any later re-review continues to fall back to the built-in `review-only code reviewer` with a narrow README-only scope.
- `workflow_bindings_by_stage`:
  - Framing and dispatch control: `superpowers:brainstorming`
  - Feedback triage: `superpowers:receiving-code-review`
  - Later review execution: `superpowers:requesting-code-review`
  - Closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`: Approve a bounded README rewrite plan that fixes the validated contradiction, separates audiences more clearly, and improves skim order before any edit is made.

## Rules

- Recommended personas are provisional until dispatch approval.
- Persona selection must cite the working brief, not just task keywords.
- The working brief is an analysis artifact, not the runtime approval record.
- No packet creation until the referenced dispatch plan is in `approved` state.
- If the user requests `Revise`, update the working brief only if the analysis changed, then issue a new brief version for the next dispatch plan revision.
