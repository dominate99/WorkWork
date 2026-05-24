# Working Brief: Legacy Normalization Pilot

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: legacy-normalization-pilot
- `case_slug`: case-based-artifact-layout
- `round_slug`: 2026-05-23-legacy-normalization-pilot
- `case_root`: `docs/cases/case-based-artifact-layout/`
- `round_root`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-normalization-pilot/`
- `created_at`: 2026-05-23
- `updated_at`: 2026-05-23
- `derived_from_user_request`: `legacy normalization pilot`

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

- `goal`: normalize archived legacy workflow documents so the legacy surface is internally more coherent, while preserving `docs/cases/...` as the only active workflow root
- `artifact_type`: cleanup-planning and implementation round plus approval-ready dispatch plan
- `relevant_context`:
  - the old type-based workflow artifact families already live under `docs/legacy/superpowers/`
  - many archived documents still contain internal references to their pre-archive `docs/superpowers/...` paths
  - those stale internal references are acceptable for history, but they make the legacy surface harder to browse and reason about
  - normalization should improve archival consistency without turning legacy docs back into active workflow surfaces
- `constraints`:
  - keep `docs/cases/...` untouched
  - keep normalization bounded to archived workflow docs and any minimal guide/index text needed around them
  - do not reopen active workflow contract design unless a correctness issue forces it
  - prefer mechanical, low-risk normalization over editorial rewrites

## Risk And Structure

- `risk_lenses`:
  - an over-broad normalization pass could rewrite historical meaning instead of just fixing stale internal links and surface semantics
  - touching too many archived files in one round could create low-signal churn that is hard to review
  - mixing active and archived references during normalization could reintroduce path ambiguity
  - if the pilot tries to make legacy docs perfect, it can become an endless cleanup project
- `parallelism_assessment`:
  - this round is tightly coupled across normalization rules, archived document edits, and review strategy
  - one bounded implementation lane is better because the stop condition and rewrite rules need to stay consistent
- `blocking_dependencies`:
  - the completed legacy archival pilot
  - the current active workflow contract under `docs/cases/...`
  - the archived legacy surface under `docs/legacy/superpowers/`
- `section_or_workstream_map`:
  - section 1: define normalization rules for archived documents
  - section 2: apply a bounded normalization pass to the archived workflow artifact families

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: `ww_skill_contract`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `section_anchors`: `Working Brief`, `Dispatch Plan File`, `Document Summary Contract`
  - `artifact_id`: `legacy_index`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/legacy/superpowers/README.md`
  - `section_anchors`: none
  - `artifact_id`: `legacy_archival_design`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-archival-pilot/design-spec.md`
  - `section_anchors`: `Goal`, `Legacy Surface`, `Decisions`
  - `artifact_id`: `legacy_archival_plan`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-archival-pilot/implementation-plan.md`
  - `section_anchors`: `Guardrails`
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/case-based-artifact-layout/case.md`
  - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-normalization-pilot/working-brief.md`
  - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-normalization-pilot/dispatch-plan.md`
  - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-normalization-pilot/design-spec.md`
  - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-normalization-pilot/implementation-plan.md`
  - `path_glob`: `docs/legacy/superpowers/**/*`
- `shared_read_scope`:
  - `path_glob`: `docs/cases/case-based-artifact-layout/**/*`
  - `path_glob`: `README.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/**/*`
  - `path_glob`: `tools/*.py`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff-engineer-orchestrator`
  - `pm-orchestrator`
- `persona_selection_notes`:
  - `staff-engineer-orchestrator` fits because normalization needs a disciplined stop condition and migration-safety lens
  - `pm-orchestrator` is a useful reviewer lens because legacy docs should still be understandable to humans browsing history
- `recommended_worker_mode_by_section`:
  - section 1: `validate-first`
  - section 2: `conservative-first`
- `worker_mode_reasoning_by_section`:
  - section 1 should define exactly what counts as normalization versus historical rewriting
  - section 2 should make the smallest set of mechanical updates that materially improve legacy coherence
- `goal_tuning_by_section`:
  - section 1: `validation-biased`
  - section 2: `safety-biased`
- `constraint_override_notes_by_section`:
  - section 1: keep active-path semantics out of scope
  - section 2: stop at stale link/path normalization and legacy-surface wording rather than rewriting historical reasoning
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - approve one bounded normalization lane
  - define a strict normalization rule before editing archived docs
  - prefer mechanical consistency gains over broad historical cleanup

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-legacy-normalization-pilot: true
- `review_target_strategy`:
  - validate that normalization improves legacy coherence without touching active roots
  - validate that edits stay within archived workflow docs
  - validate that the pilot stops at a bounded mechanical cleanup bar
- `controller_semantics_notes`:
  - this round should not dispatch real subagents before approval
  - normalization should preserve archived status rather than making legacy docs look active
  - if the scope balloons, stop at the first coherent normalization slice and record a follow-up instead of continuing indefinitely

## Rules

- Recommended personas are provisional until dispatch approval.
- Legacy normalization must not change the active `docs/cases/...` workflow root.
- Archived documents remain historical references even after normalization.
- The working brief is an analysis artifact, not the runtime approval record.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
- If the user requests `Revise`, update the working brief only if the analysis changed, then issue a new brief version for the next dispatch plan revision.
