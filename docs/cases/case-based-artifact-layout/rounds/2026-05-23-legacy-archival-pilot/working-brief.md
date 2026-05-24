# Working Brief: Legacy Archival Pilot

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: legacy-archival-pilot
- `case_slug`: case-based-artifact-layout
- `round_slug`: 2026-05-23-legacy-archival-pilot
- `case_root`: `docs/cases/case-based-artifact-layout/`
- `round_root`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-archival-pilot/`
- `created_at`: 2026-05-23
- `updated_at`: 2026-05-23
- `derived_from_user_request`: `legacy archival pilot`

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

- `goal`: define and implement a bounded legacy archival pilot that moves pre-cutover workflow documents into an explicit legacy directory model without disturbing the new `docs/cases/...` canonical path for active rounds
- `artifact_type`: archival-planning and implementation round plus approval-ready dispatch plan
- `relevant_context`:
  - new `$ww` and `$www` rounds now write canonically under `docs/cases/<case-slug>/rounds/<round-slug>/`
  - older workflow artifacts still exist in type-based locations under `docs/superpowers/...`
  - those historical artifacts are already defined as legacy history, but they have not yet been physically grouped into a dedicated legacy surface
  - the archival move should improve retrieval and reduce ambiguity without changing active workflow contract semantics
- `constraints`:
  - preserve `docs/cases/...` as the only active generation root
  - keep the first archival move narrow and deterministic
  - do not mix archival with fresh workflow redesign
  - do not break explicit references or validator assumptions without updating the matching contract text and docs

## Risk And Structure

- `risk_lenses`:
  - a bulk move without a crisp archival model could create broken references and low-signal churn
  - mixing active and archived artifacts in one directory tree could recreate operator confusion
  - a legacy directory that is too broad or underspecified could become another ambiguous bucket
  - if archival rewrites path assumptions without bounded validation, future retrieval can silently regress
- `parallelism_assessment`:
  - this round is tightly coupled across archival model, path movement, and retrieval guidance
  - one bounded implementation lane is better than parallel edits because path authority and migration notes need to stay coherent
- `blocking_dependencies`:
  - the approved case-based artifact layout design
  - the completed case-based artifact generation pilot
  - the current validator and contract surfaces that define active canonical paths
- `section_or_workstream_map`:
  - section 1: define the dedicated legacy directory model
  - section 2: pilot a bounded archival move for the old type-based workflow artifacts

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: `ww_skill_contract`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `section_anchors`: `Working Brief`, `Dispatch Plan File`, `Document Summary Contract`
  - `artifact_id`: `readme`
  - `artifact_kind`: `doc`
  - `artifact_path`: `README.md`
  - `section_anchors`: none
  - `artifact_id`: `case_layout_design`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/legacy/superpowers/specs/2026-05-22-case-based-artifact-layout-design.md`
  - `section_anchors`: `Migration Strategy`, `Compatibility Rules`
  - `artifact_id`: `case_layout_plan`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/legacy/superpowers/plans/2026-05-22-case-based-artifact-layout.md`
  - `section_anchors`: `Decide the first compatibility bridge`, `Recommended Execution Sequence`
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-archival-pilot/working-brief.md`
  - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-archival-pilot/dispatch-plan.md`
  - `path_glob`: `docs/legacy/**/*`
  - `path_glob`: `README.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- `shared_read_scope`:
  - `path_glob`: `docs/cases/case-based-artifact-layout/**/*`
  - `path_glob`: `docs/legacy/superpowers/**/*`
  - `path_glob`: `tools/*.py`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff-engineer-orchestrator`
  - `pm-orchestrator`
- `persona_selection_notes`:
  - `staff-engineer-orchestrator` fits because this is storage authority and migration safety work
  - `pm-orchestrator` is a useful reviewer lens because archived material still has to stay discoverable and understandable for humans
- `recommended_worker_mode_by_section`:
  - section 1: `validate-first`
  - section 2: `conservative-first`
- `worker_mode_reasoning_by_section`:
  - section 1 should validate the archival boundary before moving any files
  - section 2 should move the smallest coherent legacy set rather than attempting repo-wide cleanup
- `goal_tuning_by_section`:
  - section 1: `validation-biased`
  - section 2: `safety-biased`
- `constraint_override_notes_by_section`:
  - section 1: do not reopen active-path design questions already settled by the cutover
  - section 2: do not archive live `docs/cases/...` artifacts
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - approve one bounded archival lane
  - define a dedicated legacy surface explicitly
  - move only the old type-based workflow artifact families in the pilot

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-legacy-archival-pilot: true
- `review_target_strategy`:
  - validate that the legacy directory is clearly separated from active `docs/cases/...`
  - validate that only pre-cutover type-based artifacts move in this pilot
  - validate that active contract text still points only to `docs/cases/...`
- `controller_semantics_notes`:
  - this round should not launch real subagents before approval
  - archival should preserve active-path authority
  - if implementation reveals widespread reference churn, stop at the smallest safe archival slice and record follow-up work instead of widening in-place

## Rules

- Recommended personas are provisional until dispatch approval.
- Legacy archival must not alter the active canonical write path for new rounds.
- Archived artifacts are historical references, not active workflow surfaces.
- The working brief is an analysis artifact, not the runtime approval record.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
- If the user requests `Revise`, update the working brief only if the analysis changed, then issue a new brief version for the next dispatch plan revision.
