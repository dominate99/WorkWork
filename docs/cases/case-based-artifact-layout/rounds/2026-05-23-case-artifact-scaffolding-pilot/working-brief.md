# Working Brief: Case Artifact Scaffolding Pilot

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: case-artifact-scaffolding-pilot
- `case_slug`: case-based-artifact-layout
- `round_slug`: 2026-05-23-case-artifact-scaffolding-pilot
- `case_root`: `docs/cases/case-based-artifact-layout/`
- `round_root`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-case-artifact-scaffolding-pilot/`
- `created_at`: 2026-05-23
- `updated_at`: 2026-05-23
- `derived_from_user_request`: `case artifact scaffolding pilot`

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

- `goal`: add a repo-local helper that scaffolds case-based WW round artifacts under `docs/cases/...` without introducing new workflow decision logic
- `artifact_type`: tooling and documentation round
- `relevant_context`:
  - the active workflow root is already `docs/cases/<case-slug>/rounds/<round-slug>/`
  - active and legacy surfaces are now split cleanly
  - maintainers still have to hand-create `case.md`, `working-brief.md`, and `dispatch-plan.md` for every new round
  - the repo already has stable templates for working briefs and dispatch plans, but no helper to create a case/round directory shape
- `constraints`:
  - keep the helper limited to structure generation
  - do not add runtime dispatch decisions to the helper
  - do not change the legacy surface
  - only create minimal default files by default; optional artifacts should stay opt-in

## Risk And Structure

- `risk_lenses`:
  - a helper that tries to infer too much would silently become a workflow controller
  - over-eager file creation could make `design-spec.md` and `implementation-plan.md` look mandatory when they are still conditional artifacts
  - updating `case.md` must preserve existing case metadata rather than rewriting the whole file every time
- `parallelism_assessment`:
  - helper behavior, documentation, and verification are tightly coupled
  - one bounded implementation lane is better than parallel lanes here
- `blocking_dependencies`:
  - the completed case-based artifact generation pilot
  - the completed legacy archival and normalization rounds
  - the existing working brief and dispatch plan templates
- `section_or_workstream_map`:
  - section 1: define scaffold contract and helper behavior
  - section 2: implement the helper and document usage

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: `ww_skill_contract`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `section_anchors`: `Working Brief persistence rules`, `Default document references`
  - `artifact_id`: `ww_readme`
  - `artifact_kind`: `doc`
  - `artifact_path`: `README.md`
  - `section_anchors`: `What It Does`, `For Maintainers`
  - `artifact_id`: `brief_template`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `section_anchors`: `Artifact Metadata`, `Artifact-layout rules`
  - `artifact_id`: `dispatch_template`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `section_anchors`: `Path identity rules`, `Approval Block`
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/case-based-artifact-layout/case.md`
  - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-case-artifact-scaffolding-pilot/**/*`
  - `path_glob`: `README.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `tools/scaffold_ww_case_artifacts.py`
- `shared_read_scope`:
  - `path_glob`: `docs/cases/**/*`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/**/*`
  - `path_glob`: `tools/*.py`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff-engineer-orchestrator`
  - `pm-orchestrator`
- `persona_selection_notes`:
  - `staff-engineer-orchestrator` fits because the helper must preserve existing contract boundaries and avoid accidental workflow inflation
  - `pm-orchestrator` is a useful reviewer lens because the helper should feel simple and predictable to maintainers
- `recommended_worker_mode_by_section`:
  - section 1: `validate-first`
  - section 2: `conservative-first`
- `worker_mode_reasoning_by_section`:
  - section 1 should lock the smallest acceptable helper behavior before code is written
  - section 2 should add only the minimal script and docs needed to scaffold a new round
- `goal_tuning_by_section`:
  - section 1: `validation-biased`
  - section 2: `safety-biased`
- `constraint_override_notes_by_section`:
  - section 1: helper behavior must remain scaffolding-only
  - section 2: optional round artifacts stay opt-in rather than becoming default requirements
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - approve one bounded helper implementation lane
  - create `working-brief.md` and `dispatch-plan.md` by default
  - create `design-spec.md` and `implementation-plan.md` only when explicitly requested

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-case-artifact-scaffolding-pilot: true
- `review_target_strategy`:
  - validate that the helper only creates structure and placeholder content
  - validate that `case.md` updates preserve existing case metadata and only advance `Current Round` and `Round Index`
  - validate that helper usage and generated paths stay aligned with `docs/cases/...`
- `controller_semantics_notes`:
  - this round should not change runtime packet semantics
  - the helper may scaffold placeholders, but it must not claim a round is approval-ready by itself
  - a generated round remains a draft until humans fill the planning content

## Rules

- Recommended personas are provisional until dispatch approval.
- The helper must stay structure-only and must not become a workflow controller.
- `working-brief.md` and `dispatch-plan.md` are the only default round artifacts created automatically.
- `design-spec.md` and `implementation-plan.md` remain opt-in artifacts.
- The working brief is an analysis artifact, not the runtime approval record.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
