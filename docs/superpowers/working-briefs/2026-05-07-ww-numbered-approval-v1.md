# Working Brief: WW Numbered Approval Prompt

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: ww-numbered-approval
- `created_at`: 2026-05-07
- `updated_at`: 2026-05-07
- `derived_from_user_request`: `$ww make a plan to change the workwork human interact like a check box and accept 1 approve, 2,revise, 3 stop some thing similar use number as same as the words`

## Gate State

- `estimation_complete`: true
- `brief_status`: ready
- `brief_version`: 1

## Routing

- `task_routing`: `code/programming`
- `orchestrator_choice`: `staff engineer orchestrator`

## Core Intent

- `goal`: plan a consistency-only contract update so the `ww-subagent-orchestrator` approval prompt prefers numbered choices while still accepting the words `Approve`, `Revise`, and `Stop` as aliases
- `artifact_type`: skill contract and documentation consistency update
- `relevant_context`:
  - active contract surface: `skills/ww-subagent-orchestrator/SKILL.md`
  - active template surface: `skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - active user-facing doc surface: `README.md`
  - no runtime parser or external UI layer is in scope for this round
  - the user wants the numbered interaction reflected in contract wording and examples only
- `constraints`:
  - preserve the existing approval semantics and lifecycle
  - do not introduce a new parser, app layer, or clickable GUI control
  - keep historical maintainer artifacts unchanged unless they are promoted to active examples later
  - keep the new preferred prompt format consistent across the skill, template, and README

## Risk And Structure

- `risk_lenses`:
  - wording drift between the canonical skill contract and the dispatch plan template
  - user-facing README examples lagging behind the canonical prompt contract
  - accidental semantic drift where numbered choices are treated as replacing the existing word commands instead of supplementing them
  - over-scoping into parser or UI implementation that the user explicitly excluded
- `parallelism_assessment`:
  - this is a small serial documentation and contract-planning round
  - no real parallel work is needed because the affected files are tightly coupled and low-volume
- `blocking_dependencies`:
  - the design spec must be approved before the implementation plan is written
  - the implementation plan should stay bounded to the three active contract surfaces only
- `section_or_workstream_map`:
  - section 1: define the approval prompt contract and alias rules
  - section 2: map the contract to the active repo surfaces
  - section 3: define implementation and verification boundaries for the later plan

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff engineer orchestrator`
  - `codex skill contract implementer`
  - `runtime policy reviewer`
- `persona_selection_notes`:
  - `staff engineer orchestrator` fits because the primary output is a bounded programming-oriented contract change in the skill artifacts
  - `codex skill contract implementer` should own the later wording edits across the skill, template, and README
  - `runtime policy reviewer` should check that numbering changes the prompt surface only and does not change approval semantics
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - implementation execution: `superpowers:subagent-driven-development`
  - code/document changes: `superpowers:test-driven-development`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - approve a single bounded implementation-planning round after spec review
  - keep the later plan limited to `SKILL.md`, the dispatch plan template, and the README
  - verify that numbered prompts and word aliases are described consistently everywhere they appear

## Rules

- Recommended personas are provisional until dispatch approval.
- Persona selection must cite the working brief, not just task keywords.
- The working brief is an analysis artifact, not the runtime approval record.
- No packet creation until the referenced dispatch plan is in `approved` state.
- If the user requests `Revise`, update the working brief only if the analysis changed, then issue a new brief version for the next dispatch plan revision.
