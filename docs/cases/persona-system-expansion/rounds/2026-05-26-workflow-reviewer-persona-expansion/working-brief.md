# Working Brief: Reviewer Persona Expansion

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: workflow-reviewer-persona-expansion
- `case_slug`: persona-system-expansion
- `round_slug`: 2026-05-26-workflow-reviewer-persona-expansion
- `case_root`: `docs/cases/persona-system-expansion/`
- `round_root`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-reviewer-persona-expansion/`
- `created_at`: 2026-05-26
- `updated_at`: 2026-05-26
- `derived_from_user_request`: `new $ww round: reviewer persona expansion. Based on the persona taxonomy contract and worker persona expansion, add built-in reviewer-only personas to cover existing review lanes: spec-review, code-quality-review, scope-review, editorial-review, plus accessibility/UX and documentation clarity reviewer. Only add built-in reviewer personas; do not add worker personas, do not change validators, do not expand routing, and do not change the project registry.`

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

- `goal`: add built-in reviewer-only personas for the review lane and quality surfaces identified by the persona taxonomy contract and coverage audit
- `artifact_type`: built-in persona data-record update
- `relevant_context`:
  - The coverage audit found reviewer persona coverage does not match review lane semantics.
  - The taxonomy contract says durable review lane types should have viable reviewer persona families.
  - The worker persona expansion already filled worker-capable coverage and must not be widened in this round.
  - Current built-in reviewer-only coverage is primarily security-specific.
- `constraints`:
  - Add built-in reviewer-only persona records only.
  - Every new reviewer persona must use `role_type: reviewer`, `review_only: true`, and no `implementation_principles`.
  - Do not add worker personas.
  - Do not modify `docs/superpowers/personas/registry.yaml`.
  - Do not modify validator scripts.
  - Do not expand `task_routing` values.
  - Documentation sync may only clarify built-in reviewer persona availability and must not introduce new workflow behavior outside this round.

## Risk And Structure

- `risk_lenses`:
  - accidentally creating worker-capable reviewers by including `implementation_principles`
  - adding reviewer personas that rewrite or implement instead of returning findings only
  - weak mapping between reviewer personas and durable lane types
  - scope creep into validator, routing, project registry, or worker persona changes
  - duplicate reviewer personas with unclear contrast
- `parallelism_assessment`:
  - Single-section implementation is preferred because all new reviewer records live in one YAML file and must be reviewed as a coherent reviewer portfolio.
- `blocking_dependencies`:
  - Completed persona taxonomy contract in `persona-registry.md`.
  - Completed worker persona expansion in `built-in-personas.yaml`.
  - Current review lane definitions in `SKILL.md` and dispatch-plan template.
- `section_or_workstream_map`:
  - section-reviewer-persona-expansion: add the built-in reviewer-only persona records and minimal docs guidance

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: built_in_reviewer_persona_records
    - `artifact_kind`: yaml_persona_registry
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `section_anchors`: personas
  - `artifact_id`: reviewer_persona_guidance
    - `artifact_kind`: maintainer_doc
    - `artifact_path`: `README.md`
    - `section_anchors`: Customization, For Maintainers
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/persona-system-expansion/case.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-reviewer-persona-expansion/working-brief.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-reviewer-persona-expansion/dispatch-plan.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `path_glob`: `README.md`
- `shared_read_scope`:
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/design-spec.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-persona-taxonomy-contract/working-brief.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-persona-taxonomy-contract/dispatch-plan.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-worker-persona-expansion/working-brief.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-worker-persona-expansion/dispatch-plan.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `path_glob`: `docs/superpowers/personas/registry.yaml`
  - `path_glob`: `tools/validate_ww_persona_selection_contracts.py`
  - `path_glob`: `tools/validate_ww_repo.py`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff-engineer-orchestrator`
    - owned scope: implement built-in reviewer persona records and minimal maintainer guidance
    - workflow bindings: `superpowers:subagent-driven-development`, `superpowers:test-driven-development`, `superpowers:verification-before-completion`
    - role binding: `orchestrator` via `agents/orchestrator-prompt.md`
  - `pm-orchestrator`
    - owned scope: review whether the new reviewer persona set maps clearly to lanes and stays reviewer-only
    - workflow bindings: `superpowers:requesting-code-review`
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
- `persona_selection_notes`:
  - `staff-engineer-orchestrator` fits because the primary work changes packaged persona data while preserving role boundaries and validator compatibility.
  - `pm-orchestrator` fits review because reviewer personas must be understandable as a portfolio and useful for workflow staffing.
- `recommended_worker_mode_by_section`:
  - section-reviewer-persona-expansion: standard
- `worker_mode_reasoning_by_section`:
  - section-reviewer-persona-expansion: bounded YAML/data-record and docs edits with explicit schema constraints.
- `goal_tuning_by_section`:
  - section-reviewer-persona-expansion: emphasize reviewer-only boundaries, lane mapping, and concise persona contrast.
- `constraint_override_notes_by_section`:
  - section-reviewer-persona-expansion: do not satisfy worker, validator, routing, or project-registry gaps in this round; record them as later work if they appear.
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - implementation execution: `superpowers:subagent-driven-development`
  - code/data changes: `superpowers:test-driven-development`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval to add built-in reviewer-only personas and minimal README guidance, then validate schema/role boundaries and run a narrow reviewer pass

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-reviewer-persona-expansion: true
- `review_target_strategy`:
  - review `built-in-personas.yaml` and README changes against the taxonomy contract, reviewer-only constraints, lane coverage, and absence of validator/routing/project-registry changes
- `controller_semantics_notes`:
  - Standard `$ww` round. No strict-review target is active.

## Rules

- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
