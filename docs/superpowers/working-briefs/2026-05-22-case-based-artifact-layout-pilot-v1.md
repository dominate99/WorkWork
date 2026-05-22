# Working Brief: Case-Based Artifact Layout Pilot

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: case-based-artifact-layout-pilot
- `created_at`: 2026-05-22
- `updated_at`: 2026-05-22
- `derived_from_user_request`: `新的 $ww round 做： case-based artifact layout pilot`

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

- `goal`: define a case-based artifact layout model so each `$ww` or `$www` round can keep its own files together, while preserving a clear migration and compatibility path from the current type-based `docs/superpowers/*` structure
- `artifact_type`: design and planning artifacts for workflow-storage architecture
- `relevant_context`:
  - the current packaged skill contract hardcodes type-based locations such as `docs/superpowers/working-briefs/`, `dispatch-plans/`, `specs/`, and `plans/`
  - the user wants per-case grouping so one case folder contains all files for that case or round instead of scattering them by document type
  - current validators and README guidance still describe the existing type-based structure
  - the repository now has a growing number of `$ww` rounds and artifacts, so retrieval, auditing, and narrative continuity are becoming more important
- `constraints`:
  - this round should first define the case/round directory model and migration approach before changing runtime behavior
  - avoid making existing working brief and dispatch plan files substantially heavier just to carry more references
  - preserve the distinction between mandatory runtime-state artifacts and optional explanatory or log-like artifacts
  - do not assume an immediate repo-wide migration unless compatibility strategy is explicit

## Risk And Structure

- `risk_lenses`:
  - if the new layout is underspecified, the repo can end up with both type-based and case-based storage competing indefinitely
  - if migration is too aggressive, current references in `SKILL.md`, validators, and maintainer guidance could break together
  - if case and round are not clearly separated, one folder could become a dump instead of a coherent unit
  - if optional log-like artifacts are treated as dispatch gates, the workflow will get heavier instead of clearer
  - if authority is not singular during migration, the repo will drift into split-brain path semantics where producers and validators disagree on canonical locations
  - if compatibility rules are hand-wavy, every future artifact-producing round will have to re-decide path behavior locally
- `parallelism_assessment`:
  - this round is architecture-heavy and tightly coupled across contract paths, storage semantics, and migration design
  - one coordinated design lane is better than splitting layout, migration, and compatibility into parallel sub-workstreams
- `blocking_dependencies`:
  - current packaged path rules in `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - current maintainer/user guidance in `README.md`
  - current generated artifact layout under `docs/superpowers/`
- `section_or_workstream_map`:
  - section 1: define the case / round folder model
  - section 2: define default file landing points for `$ww` and `$www`
  - section 3: define migration and compatibility strategy from type-based storage

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: `ww_skill_contract`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `section_anchors`: `Working Brief`, `Dispatch Plan File`, `Document Summary Contract`, `References`
  - `artifact_id`: `readme_guidance`
  - `artifact_kind`: `doc`
  - `artifact_path`: `README.md`
  - `section_anchors`: `How It Works`, `Output Locations`, `For Maintainers`
  - `artifact_id`: `persona_enrichment_plan`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
  - `section_anchors`: none
  - `artifact_id`: `current_superpowers_layout`
  - `artifact_kind`: `dir`
  - `artifact_path`: `docs/superpowers/`
  - `section_anchors`: none
- `exclusive_write_scope`:
  - `path_glob`: `docs/superpowers/working-briefs/2026-05-22-case-based-artifact-layout-pilot-v1.md`
  - `path_glob`: `docs/superpowers/dispatch-plans/2026-05-22-case-based-artifact-layout-pilot.md`
  - `path_glob`: `docs/superpowers/specs/2026-05-22-case-based-artifact-layout-design.md`
  - `path_glob`: `docs/superpowers/plans/2026-05-22-case-based-artifact-layout.md`
- `shared_read_scope`:
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `README.md`
  - `path_glob`: `docs/superpowers/**/*`
  - `path_glob`: `tools/*.py`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff-engineer-orchestrator`
  - `pm-orchestrator`
  - `creative-director-orchestrator`
- `persona_selection_notes`:
  - `staff-engineer-orchestrator` fits because this is a repository architecture and workflow-storage design problem with compatibility risk
  - `pm-orchestrator` is useful as a secondary lens because the new layout should reduce user/operator friction, not just improve internal neatness
  - this round should still be judged primarily by architecture integrity, authority clarity, and migration safety rather than by presentation neatness
- `recommended_worker_mode_by_section`:
  - section 1: `plan-first`
  - section 2: `validate-first`
- `worker_mode_reasoning_by_section`:
  - section 1 should design the target case/round model before discussing migration mechanics
  - section 2 should validate every migration and compatibility step against current contract assumptions
- `goal_tuning_by_section`:
  - section 1: `safety-biased`
  - section 2: `validation-biased`
- `constraint_override_notes_by_section`:
  - section 1: keep the top-level model simple enough to explain to users without an extra taxonomy layer
  - section 2: optional explanatory artifacts should remain optional unless a later approved round promotes them into required runtime state
  - section 2: require a single canonical write path model for every artifact class during each migration phase; avoid dual-authority designs
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - approve a design-first round that produces a case-based layout design spec and migration-oriented implementation plan
  - require explicit answers for canonical authority, migration phases, and fallback behavior before approving runtime contract edits

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-case-layout-design: true
- `review_target_strategy`:
  - validate that the case/round model is clearer than the current type-based split
  - validate that default landing points work for both mandatory and optional artifacts
  - treat migration ambiguity, dual-layout drift, or hidden required-log behavior as blocking
  - treat any design that leaves producers, validators, and human operators with different beliefs about canonical artifact paths as blocking
- `controller_semantics_notes`:
  - this is a design/planning round only
  - no packet creation until the dispatch plan is approved
  - storage-model changes should be designed before implementation, validator, or migration rounds begin

## Rules

- Recommended personas are provisional until dispatch approval.
- Persona selection must cite the working brief, not just task keywords.
- The working brief is an analysis artifact, not the runtime approval record.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
- If the user requests `Revise`, update the working brief only if the analysis changed, then issue a new brief version for the next dispatch plan revision.
