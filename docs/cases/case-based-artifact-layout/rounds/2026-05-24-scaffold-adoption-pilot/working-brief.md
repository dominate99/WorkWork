# Working Brief: Scaffold Adoption Pilot

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: scaffold-adoption-pilot
- `case_slug`: case-based-artifact-layout
- `round_slug`: 2026-05-24-scaffold-adoption-pilot
- `case_root`: `docs/cases/case-based-artifact-layout/`
- `round_root`: `docs/cases/case-based-artifact-layout/rounds/2026-05-24-scaffold-adoption-pilot/`
- `created_at`: 2026-05-24
- `updated_at`: 2026-05-24
- `derived_from_user_request`: `scaffold adoption pilot`

## Round Intent

- `quality_mode`: standard

## Gate State

- `estimation_complete`: true
- `brief_status`: ready
- `brief_version`: 1

## Routing

- `task_routing`: `code/programming`
- `orchestrator_choice`: `staff-engineer-orchestrator`

## Core Intent

- `goal`: make scaffold generation the default initialization path for new `$ww/$www` rounds without widening the helper into workflow decision logic
- `artifact_type`: workflow adoption and contract-alignment round
- `relevant_context`:
  - `docs/cases/...` is already the active root for new rounds
  - `tools/scaffold_ww_case_artifacts.py` exists and can generate `case.md`, `working-brief.md`, and `dispatch-plan.md`
  - `tools/validate_ww_case_contracts.py` already proves helper output conforms to the structural case contract
- `constraints`:
  - keep scope focused on adoption guidance, not helper redesign
  - do not change legacy handling again
  - do not add new runtime packet or subagent behavior in this round

## Risk And Structure

- `risk_lenses`:
  - documentation drift between helper behavior and canonical skill contract
  - premature automation that implies approval-ready artifacts
  - ambiguous defaulting that lets maintainers bypass the scaffold flow
- `parallelism_assessment`:
  - single bounded documentation/planning section; no parallel execution value
- `blocking_dependencies`:
  - scaffold helper and case contract validator must already be in place
- `section_or_workstream_map`:
  - section 1: define scaffold adoption rules and approval-facing guidance

## Scope Preparation

- `artifact_mappings`:
  - `SKILL.md`: establish scaffold-first startup guidance
  - `README.md`: reflect maintainer-facing initialization path
  - current round artifacts: record the adoption pilot and approval state
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/case-based-artifact-layout/case.md`
  - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-24-scaffold-adoption-pilot/working-brief.md`
  - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-24-scaffold-adoption-pilot/dispatch-plan.md`
  - `path_glob`: `README.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- `shared_read_scope`:
  - `path_glob`: `docs/cases/**/*`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/case-template.md`
  - `path_glob`: `tools/scaffold_ww_case_artifacts.py`
  - `path_glob`: `tools/validate_ww_case_contracts.py`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff-engineer-orchestrator`
  - `pm-orchestrator`
- `persona_selection_notes`:
  - `staff-engineer-orchestrator` should own the contract and migration-safety judgment
  - `pm-orchestrator` should act as the reviewer lens for clarity and adoption friction
- `recommended_worker_mode_by_section`:
  - section 1: `validate-first`
- `worker_mode_reasoning_by_section`:
  - section 1: confirm current helper, validator, and contract surfaces align before tightening default usage language
- `goal_tuning_by_section`:
  - section 1: `validation-biased`
- `constraint_override_notes_by_section`:
  - section 1: user wants adoption, but the round should still avoid broadening into helper feature expansion
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - proceed with one bounded adoption section and require explicit approval before any follow-on implementation beyond contract/docs

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-1: true
- `review_target_strategy`:
  - review whether scaffold-first wording is precise, non-ambiguous, and does not imply helper output is approval-ready
- `controller_semantics_notes`:
  - no packet creation or subagent launch is needed for this round; it is an orchestrator-owned contract/documentation pass

## Rules

- This round starts from scaffolded files, but the planning content above is now the canonical approval draft.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
- This adoption round is complete once active guidance clearly makes scaffold-first initialization the default for new case-based rounds without changing helper scope.
