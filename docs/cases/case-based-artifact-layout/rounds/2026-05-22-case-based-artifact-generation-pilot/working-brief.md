# Working Brief: Case-Based Artifact Generation Pilot

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 2
- `brief_status`: ready
- `topic_slug`: case-based-artifact-generation-pilot
- `case_slug`: case-based-artifact-layout
- `round_slug`: 2026-05-22-case-based-artifact-generation-pilot
- `case_root`: `docs/cases/case-based-artifact-layout/`
- `round_root`: `docs/cases/case-based-artifact-layout/rounds/2026-05-22-case-based-artifact-generation-pilot/`
- `created_at`: 2026-05-22
- `updated_at`: 2026-05-22
- `derived_from_user_request`: `case-based artifact generation pilot`

## Round Intent

- `quality_mode`: standard

## Gate State

- `estimation_complete`: true
- `brief_status`: ready
- `brief_version`: 2

## Routing

- `task_routing`: `code/programming`
- `orchestrator_choice`: `staff-engineer-orchestrator`

## Core Intent

- `goal`: make new `$ww` and `$www` rounds generate their required artifacts only under the case-based layout, while classifying pre-cutover type-based documents as legacy history rather than an active transition bridge
- `artifact_type`: adoption-planning and implementation round plus approval-ready dispatch plan
- `relevant_context`:
  - the workflow contract and validator suite now recognize case-based path identity as canonical
  - the design and implementation docs already define the target case/round model and migration posture
  - this round applies the root cutover so new rounds generate their artifacts into `docs/cases/<case-slug>/rounds/<round-slug>/`
  - legacy type-based directories should be explicitly treated as historical legacy storage, and may be reclassified behind a dedicated legacy surface rather than preserved as an active compatibility layer
- `constraints`:
  - prioritize actual new-round generation behavior over broad historical migration
  - keep required runtime-state artifacts minimal and do not promote optional explanatory artifacts into gates by default
  - do not widen into packet, prompt, persona, or validator redesign unless implementation reveals a concrete blocker
  - cutover should preserve one canonical write-path model with no dual-write bridge
  - historical pre-cutover artifacts remain out of scope for bulk movement in this pilot

## Risk And Structure

- `risk_lenses`:
  - if generation behavior stays partly implicit, operators may continue creating new round artifacts in the old type-based directories even though the contract changed
  - if legacy handling is phrased loosely, the repo can drift back into split operator behavior even without formal dual-write
  - if case-level entrypoints are introduced without a narrow role, they can become another stale log surface instead of a useful index
  - if this round tries to bulk-migrate historical artifacts, the adoption value can get buried under low-signal file churn
- `parallelism_assessment`:
  - this round is tightly coupled across generation behavior, canonical path guidance, and transition rules
  - one bounded implementation lane is better than parallel edits because the authority model must stay coherent across every touched surface
- `blocking_dependencies`:
  - the approved case-based artifact layout design and implementation plan
  - the live contract surfaces in `SKILL.md`, `working-brief-template.md`, `dispatch-plan-template.md`, and `README.md`
  - the case-path identity validator and repo-level validator entrypoint
- `section_or_workstream_map`:
  - section 1: define the default artifact-generation behavior for new rounds
  - section 2: define the hard legacy boundary for historical type-based artifacts

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: `ww_skill_contract`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `section_anchors`: `Working Brief`, `Dispatch Plan File`, `Document Summary Contract`
  - `artifact_id`: `working_brief_template`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `section_anchors`: `Artifact Metadata`, `Rules`
  - `artifact_id`: `dispatch_plan_template`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `section_anchors`: `Path identity rules`, `Preconditions`
  - `artifact_id`: `readme`
  - `artifact_kind`: `doc`
  - `artifact_path`: `README.md`
  - `section_anchors`: none
  - `artifact_id`: `case_layout_design`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/legacy/superpowers/specs/2026-05-22-case-based-artifact-layout-design.md`
  - `section_anchors`: `Target Model`, `Migration Strategy`, `Compatibility Rules`
  - `artifact_id`: `case_layout_plan`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/legacy/superpowers/plans/2026-05-22-case-based-artifact-layout.md`
  - `section_anchors`: `Introduce case-based path templates for new rounds`, `Decide the first compatibility bridge`
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-22-case-based-artifact-generation-pilot/working-brief.md`
  - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-22-case-based-artifact-generation-pilot/dispatch-plan.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `path_glob`: `README.md`
  - `path_glob`: `docs/cases/case-based-artifact-layout/case.md`
- `shared_read_scope`:
  - `path_glob`: `docs/cases/case-based-artifact-layout/**/*`
  - `path_glob`: `docs/legacy/superpowers/specs/2026-05-22-case-based-artifact-layout-design.md`
  - `path_glob`: `docs/legacy/superpowers/plans/2026-05-22-case-based-artifact-layout.md`
  - `path_glob`: `tools/validate_ww_case_path_identity.py`
  - `path_glob`: `tools/validate_ww_repo.py`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff-engineer-orchestrator`
  - `pm-orchestrator`
- `persona_selection_notes`:
  - `staff-engineer-orchestrator` fits because this is a migration-authority and generation-adoption round where canonical path ownership matters more than cosmetic organization
  - `pm-orchestrator` is a useful reviewer lens because generation behavior should stay simple and obvious for humans, and `docs/cases/...` is easier to discover than a deeper workflow-specific tree
- `recommended_worker_mode_by_section`:
  - section 1: `validate-first`
  - section 2: `conservative-first`
- `worker_mode_reasoning_by_section`:
  - section 1 should validate exactly which surfaces still govern new-round generation before changing defaults
  - section 2 should define the narrowest hard-cut boundary that keeps old artifacts historical without implying ongoing compatibility
- `goal_tuning_by_section`:
  - section 1: `validation-biased`
  - section 2: `safety-biased`
- `constraint_override_notes_by_section`:
  - section 1: do not widen into repo-wide historical migration
  - section 2: do not make optional explanatory artifacts into default required outputs just because colocated round folders make them easy to add
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - approve one bounded adoption lane for case-based round generation behavior
  - make new round artifact defaults unambiguously case-based under `docs/cases/...`
  - define a hard legacy classification for pre-cutover type-based artifacts instead of an open-ended transition bridge

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-case-based-artifact-generation-adoption: true
- `review_target_strategy`:
  - validate that new rounds are explicitly generated under `docs/cases/<case-slug>/rounds/<round-slug>/`
  - validate that required artifacts remain minimal and clearly separated from optional explanatory artifacts
  - validate that legacy type-based locations are described as legacy history only, not as active defaults or ongoing compatibility surfaces
- `controller_semantics_notes`:
  - this round should change generation behavior and guidance only after approval
  - no packet creation until the referenced dispatch plan is in `approved` state
  - if implementation reveals a missing stable case entrypoint, a bounded `case.md` addition may be allowed, but it must remain informational rather than a dispatch gate

## Rules

- Recommended personas are provisional until dispatch approval.
- New-round generation behavior must preserve one canonical write-path model.
- Pre-cutover type-based artifacts should be classified as legacy history rather than treated as an active bridge for new generation.
- Required artifacts stay minimal unless the user explicitly requests a heavier workflow.
- The working brief is an analysis artifact, not the runtime approval record.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
- If the user requests `Revise`, update the working brief only if the analysis changed, then issue a new brief version for the next dispatch plan revision.
