# Working Brief: WW Transparency Implementation Review

Use this brief after estimation and before any persona dispatch.

## Gate State

- `estimation_complete: true`
- `brief_status: ready`
- `brief_version: 2`

## Routing

- `task_routing`: `code/programming`
- `orchestrator_choice`: `staff engineer orchestrator`

## Core Intent

- `goal`: Review the current `ww-subagent-orchestrator` implementation changes for the transparency rollout so the skill contract, dispatch-plan template, and packet contract stay synchronized before commit.
- `artifact_type`: implementation review of Markdown-based skill contracts
- `relevant_context`:
  - The prior `ww-transparency-review` design round is completed and has both a design spec and an implementation plan.
  - The current worktree has uncommitted changes in three files: `skills/ww-subagent-orchestrator/SKILL.md`, `skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`, and `skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`.
  - `SKILL.md` already carries the new four-section reply contract and maintainers-path document references.
  - The template and packet contract were updated afterward to add the canonical `Progress Board` schema and workstream identity linkage fields.
  - Contract checks and `quick_validate.py` pass after installing `PyYAML`.
  - Review pass `review-1` found four validated sync gaps: no persisted critical-path marker, packet-field drift between `SKILL.md` and the packet contract, under-specified `Display Status` vocabulary, and a non-conforming packet example.
- `constraints`:
  - Stay within the current transparency-implementation changes.
  - Revise only the affected contract artifacts and preserve the approved design direction.
  - Do not widen scope into new features, runtime code generation, or unrelated skill refactors.
  - The revised plan must return to approval before any remediation edits are executed.

## Risk And Structure

- `risk_lenses`:
  - Cross-artifact drift risk if one file defines behavior the others cannot support.
  - Rendering-contract risk if the skill requires reply content that the persisted dispatch plan cannot represent.
  - Review-loop risk if packet identity fields are insufficient for repeated reviewer passes.
  - Documentation-path risk if the new maintainer-document references conflict with existing repo conventions.
  - Revision-discipline risk if remediation begins before the revised dispatch plan is re-approved.
- `parallelism_assessment`: low; the review is narrow and centered on one small change set.
- `blocking_dependencies`:
  - User approval of the revised remediation plan before any contract edits are made.
  - Remediation should stay anchored to the validated review findings from `review-1`.
- `section_or_workstream_map`:
  - Section A: Revise the transparency-contract implementation plan to close the four validated sync gaps before commit.

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff engineer orchestrator`
  - `review-only code reviewer`
- `persona_selection_notes`:
  - `staff engineer orchestrator` remains the correct top-level owner because the current step is a contract-remediation revision driven by validated implementation-review findings.
  - The local persona registry still does not define a dedicated review-only contract reviewer for this Markdown skill rollout, so any later re-review continues to fall back to the built-in `review-only code reviewer`.
- `workflow_bindings_by_stage`:
  - Framing and dispatch control: `superpowers:brainstorming`
  - Feedback triage: `superpowers:receiving-code-review`
  - Later review execution: `superpowers:requesting-code-review`
  - Closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`: Approve a bounded remediation section that fixes the validated contract gaps first, then returns to review before commit.

## Rules

- Recommended personas are provisional until dispatch approval.
- Persona selection must cite the working brief, not just task keywords.
- The working brief is an analysis artifact, not the runtime approval record.
- No packet creation until the referenced dispatch plan is in `approved` state.
- If the user requests `Revise`, update the working brief only if the analysis changed, then issue a new brief version for the next dispatch plan revision.
