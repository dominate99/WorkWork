# Working Brief: Built-In Worker Persona Expansion

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: worker-persona-expansion
- `case_slug`: persona-system-expansion
- `round_slug`: 2026-05-26-worker-persona-expansion
- `case_root`: `docs/cases/persona-system-expansion/`
- `round_root`: `docs/cases/persona-system-expansion/rounds/2026-05-26-worker-persona-expansion/`
- `created_at`: 2026-05-26
- `updated_at`: 2026-05-26
- `derived_from_user_request`: `new $ww round: built-in worker persona expansion. Based on the persona taxonomy contract, add worker-capable specialist personas to built-in-personas.yaml covering frontend/product UI implementation, test and quality engineering, DevOps/release/infrastructure operations, data/analytics/ML workflows, and technical writing/documentation production. Sync necessary contract/docs and project guidance. Only add built-in worker personas; do not add reviewer personas, do not change validators, and do not expand routing.`

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

- `goal`: add built-in worker-capable specialist personas for the five minimum execution families defined by the persona taxonomy contract
- `artifact_type`: built-in persona data-record update
- `relevant_context`:
  - The persona coverage audit identified missing worker-capable families.
  - The taxonomy contract now defines the minimum worker-capable built-in execution families.
  - Current built-in worker-capable specialists cover backend/service work and Java-specific work only.
  - This round should fill the built-in worker floor without adding reviewer personas, routing values, validators, or project-specific records.
- `constraints`:
  - Add built-in worker-capable specialist persona records only.
  - Every new worker persona must satisfy the worker-capability gate: `review_only: false`, `role_type` not equal to `orchestrator`, and exactly two `implementation_principles`.
  - Do not add reviewer-only personas.
  - Do not modify `docs/superpowers/personas/registry.yaml`.
  - Do not modify validator scripts.
  - Do not expand `task_routing` values.
  - Documentation sync may only clarify built-in worker persona availability and must not introduce new workflow behavior outside this round.

## Risk And Structure

- `risk_lenses`:
  - accidentally adding reviewer personas instead of worker-capable specialists
  - failing the worker gate by omitting or overfilling `implementation_principles`
  - adding language/framework variants instead of family-level worker coverage
  - creating duplicate or overlapping personas with weak contrast
  - expanding routing or validator behavior prematurely
- `parallelism_assessment`:
  - Single-section implementation is preferred because all new records live in one YAML file and must be reviewed for contrast as a set.
- `blocking_dependencies`:
  - Completed persona taxonomy contract in `persona-registry.md`.
  - Current built-in persona schema and existing worker records.
  - Current persona runtime-selection validator wording.
- `section_or_workstream_map`:
  - section-built-in-worker-persona-expansion: add the five built-in worker specialist records and minimal docs guidance

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: built_in_persona_records
    - `artifact_kind`: yaml_persona_registry
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `section_anchors`: personas
  - `artifact_id`: worker_persona_guidance
    - `artifact_kind`: maintainer_doc
    - `artifact_path`: `README.md`
    - `section_anchors`: Customization, For Maintainers
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/persona-system-expansion/case.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-worker-persona-expansion/working-brief.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-worker-persona-expansion/dispatch-plan.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `path_glob`: `README.md`
- `shared_read_scope`:
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/design-spec.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-persona-taxonomy-contract/working-brief.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-persona-taxonomy-contract/dispatch-plan.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `path_glob`: `docs/superpowers/personas/registry.yaml`
  - `path_glob`: `tools/validate_ww_persona_selection_contracts.py`
  - `path_glob`: `tools/validate_ww_repo.py`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff-engineer-orchestrator`
    - owned scope: implement built-in worker persona records and minimal maintainer guidance
    - workflow bindings: `superpowers:subagent-driven-development`, `superpowers:test-driven-development`, `superpowers:verification-before-completion`
    - role binding: `orchestrator` via `agents/orchestrator-prompt.md`
  - `pm-orchestrator`
    - owned scope: review whether the new worker persona set covers the taxonomy families without drifting into reviewer/routing/validator scope
    - workflow bindings: `superpowers:requesting-code-review`
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
- `persona_selection_notes`:
  - `staff-engineer-orchestrator` fits because the primary work changes runtime-facing packaged persona data and must preserve schema compatibility.
  - `pm-orchestrator` fits review because the set must remain understandable as a portfolio, not just technically valid YAML.
- `recommended_worker_mode_by_section`:
  - section-built-in-worker-persona-expansion: standard
- `worker_mode_reasoning_by_section`:
  - section-built-in-worker-persona-expansion: bounded data-record edits with explicit schema and scope constraints.
- `goal_tuning_by_section`:
  - section-built-in-worker-persona-expansion: emphasize distinct persona contrast, worker-gate compliance, and minimal docs sync.
- `constraint_override_notes_by_section`:
  - section-built-in-worker-persona-expansion: do not satisfy reviewer, validator, routing, or project-registry gaps in this round; record them as later work if they appear.
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - implementation execution: `superpowers:subagent-driven-development`
  - code/data changes: `superpowers:test-driven-development`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval to add five built-in worker-capable specialist personas and minimal README guidance, then validate schema/contract behavior and run a narrow reviewer pass

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-built-in-worker-persona-expansion: true
- `review_target_strategy`:
  - review `built-in-personas.yaml` and README changes against the taxonomy contract, worker gate, user constraints, and absence of validator/routing/project-registry changes
- `controller_semantics_notes`:
  - Standard `$ww` round. No strict-review target is active.

## Rules

- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
