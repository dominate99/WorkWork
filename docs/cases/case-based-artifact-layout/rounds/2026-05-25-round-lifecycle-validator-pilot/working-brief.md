# Working Brief: Round Lifecycle Validator Pilot

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: round-lifecycle-validator-pilot
- `case_slug`: case-based-artifact-layout
- `round_slug`: 2026-05-25-round-lifecycle-validator-pilot
- `case_root`: `docs/cases/case-based-artifact-layout/`
- `round_root`: `docs/cases/case-based-artifact-layout/rounds/2026-05-25-round-lifecycle-validator-pilot/`
- `created_at`: 2026-05-25
- `updated_at`: 2026-05-25
- `derived_from_user_request`: `round lifecycle validator pilot`

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

- `goal`: convert the round lifecycle ownership rules into machine-checkable contract validation without creating a second runtime state surface
- `artifact_type`: lifecycle contract validation pilot
- `relevant_context`:
  - the prior round defined that `case.md` remains navigational and `dispatch-plan.md` remains the source of truth for round lifecycle state
  - current validators already check case structure and path identity, but not lifecycle ownership semantics
  - `case.md` now updates `Current Round` on round creation, which creates a clear validation target
- `constraints`:
  - keep the validator structural and deterministic
  - do not redesign helper behavior in this round
  - do not turn lifecycle validation into prose-quality review

## Risk And Structure

- `risk_lenses`:
  - stale `Current Round` values in `case.md`
  - `case.md` drifting into runtime-state language
  - round lifecycle state duplicated outside `dispatch-plan.md`
- `parallelism_assessment`:
  - single bounded validator/design section; no parallel work needed
- `blocking_dependencies`:
  - lifecycle ownership model must stay unchanged from the previous round
- `section_or_workstream_map`:
  - section 1: define and validate lifecycle ownership rules

## Scope Preparation

- `artifact_mappings`:
  - `case.md`: lifecycle pointer semantics
  - current round docs: validator pilot contract and implementation notes
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/case-based-artifact-layout/case.md`
  - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-25-round-lifecycle-validator-pilot/working-brief.md`
  - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-25-round-lifecycle-validator-pilot/dispatch-plan.md`
  - `path_glob`: `README.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `tools/validate_ww_repo.py`
  - `path_glob`: `tools/validate_ww_round_lifecycle.py`
- `shared_read_scope`:
  - `path_glob`: `docs/cases/**/*`
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
  - `staff-engineer-orchestrator` should convert lifecycle ownership into deterministic validator rules
  - `pm-orchestrator` should review whether the lifecycle checks stay understandable and bounded
- `recommended_worker_mode_by_section`:
  - section 1: `validate-first`
- `worker_mode_reasoning_by_section`:
  - section 1: read the established lifecycle contract first, then add only the smallest validator surface needed to enforce it
- `goal_tuning_by_section`:
  - section 1: `validation-biased`
- `constraint_override_notes_by_section`:
  - section 1: user wants stronger determinism, but the validator must not widen into general workflow linting
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - proceed with one bounded validator section focused on lifecycle ownership and stale-pointer detection

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-1: true
- `review_target_strategy`:
  - review that validator rules enforce ownership without mutating the lifecycle model itself
- `controller_semantics_notes`:
  - no packet launch is required; this round is a repo-local validator and contract pass

## Rules

- This round starts from scaffolded files, but the planning content above is now the canonical approval draft.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
- This pilot completes once lifecycle ownership becomes machine-checkable without changing the ownership model itself.
