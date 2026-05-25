# Working Brief: Round Lifecycle Pilot

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: round-lifecycle-pilot
- `case_slug`: case-based-artifact-layout
- `round_slug`: 2026-05-24-round-lifecycle-pilot
- `case_root`: `docs/cases/case-based-artifact-layout/`
- `round_root`: `docs/cases/case-based-artifact-layout/rounds/2026-05-24-round-lifecycle-pilot/`
- `created_at`: 2026-05-24
- `updated_at`: 2026-05-24
- `derived_from_user_request`: `round lifecycle pilot`

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

- `goal`: define how `case.md` and round artifacts should stay synchronized as rounds move from drafted to approved to completed or stopped
- `artifact_type`: lifecycle contract and maintenance pilot
- `relevant_context`:
  - `docs/cases/...` is now the only active workflow artifact root
  - `case.md` exists as a navigational entrypoint and is scaffold-updated today
  - current contract validates structure, but not round lifecycle consistency
- `constraints`:
  - keep scope on lifecycle semantics, not on adding more artifact families
  - do not redesign dispatch approval flow
  - do not reopen legacy path policy or helper scope

## Risk And Structure

- `risk_lenses`:
  - stale `Current Round` pointers in `case.md`
  - completed/stopped rounds that leave case state ambiguous
  - dual sources of truth between `case.md` and per-round dispatch state
- `parallelism_assessment`:
  - single bounded contract/planning section; parallelism is unnecessary
- `blocking_dependencies`:
  - scaffold-first initialization and case contract validation must remain intact
- `section_or_workstream_map`:
  - section 1: define lifecycle ownership, transitions, and validation direction

## Scope Preparation

- `artifact_mappings`:
  - `case.md`: lifecycle-facing case index semantics
  - current round docs: lifecycle pilot design and implementation notes
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/case-based-artifact-layout/case.md`
  - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-24-round-lifecycle-pilot/working-brief.md`
  - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-24-round-lifecycle-pilot/dispatch-plan.md`
  - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-24-round-lifecycle-pilot/design-spec.md`
  - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-24-round-lifecycle-pilot/implementation-plan.md`
- `shared_read_scope`:
  - `path_glob`: `docs/cases/**/*`
  - `path_glob`: `README.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/**/*`
  - `path_glob`: `tools/scaffold_ww_case_artifacts.py`
  - `path_glob`: `tools/validate_ww_case_contracts.py`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff-engineer-orchestrator`
  - `pm-orchestrator`
- `persona_selection_notes`:
  - `staff-engineer-orchestrator` should define deterministic lifecycle ownership and single-source-of-truth rules
  - `pm-orchestrator` should review whether lifecycle semantics stay understandable for maintainers
- `recommended_worker_mode_by_section`:
  - section 1: `validate-first`
- `worker_mode_reasoning_by_section`:
  - section 1: confirm existing case and round state surfaces before tightening lifecycle rules
- `goal_tuning_by_section`:
  - section 1: `validation-biased`
- `constraint_override_notes_by_section`:
  - section 1: user wants stronger lifecycle semantics, but this round should avoid turning `case.md` into a runtime state machine
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - proceed with one bounded lifecycle-definition section and keep implementation concerns limited to deterministic metadata ownership

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-1: true
- `review_target_strategy`:
  - review that lifecycle rules preserve `case.md` as a navigational surface while still making stale round state machine drift detectable
- `controller_semantics_notes`:
  - no subagent launch is needed for this round; this is a contract/planning pass focused on lifecycle semantics

## Rules

- This round starts from scaffolded files, but the planning content above is now the canonical approval draft.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
- This pilot completes once lifecycle ownership is deterministic on paper without adding a second runtime state machine to `case.md`.
