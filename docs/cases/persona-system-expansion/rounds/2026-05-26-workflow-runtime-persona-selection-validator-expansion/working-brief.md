# Working Brief: Persona Runtime Selection Validator Expansion

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: workflow-runtime-persona-selection-validator-expansion
- `case_slug`: persona-system-expansion
- `round_slug`: 2026-05-26-workflow-runtime-persona-selection-validator-expansion
- `case_root`: `docs/cases/persona-system-expansion/`
- `round_root`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-validator-expansion/`
- `created_at`: 2026-05-26
- `updated_at`: 2026-05-26
- `derived_from_user_request`: `new $ww round: persona runtime selection validator expansion. Based on persona runtime selection adoption design and implementation, expand repo validation to check the runtime persona selection recording contract. Update validate_ww_persona_selection_contracts.py and validate_ww_repo.py, with README/SKILL guidance only if necessary. Check that working brief records candidate_persona_sources and recommended persona source/runtime role/rationale; dispatch plan records planned reviewer/source/runtime role/rationale, specialist source/runtime role/rationale, and review lane source/runtime role; subagent packet contract includes persona_source; and reviewer-only/worker-capability gate contract text still exists. Do not add personas, do not change the project registry, do not expand routing, and do not add secondary tags.`

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

- `goal`: expand WorkWork repo validation so runtime persona selection recording rules are machine-checkable
- `artifact_type`: validator implementation update
- `relevant_context`:
  - The approved runtime selection adoption design defined persona source/rationale persistence for working briefs, dispatch plans, review lanes, and packets.
  - The implementation round updated `SKILL.md`, `working-brief-template.md`, `dispatch-plan-template.md`, `subagent-packet-contract.md`, and README guidance with those recording requirements.
  - `validate_ww_persona_selection_contracts.py` currently checks only the older `SKILL.md` and `persona-registry.md` runtime-selection contract fragments.
  - `validate_ww_repo.py` already invokes the persona selection validator, so this round likely updates that existing check indirectly unless label or README guidance changes are needed.
- `constraints`:
  - Update `tools/validate_ww_persona_selection_contracts.py`.
  - Update `tools/validate_ww_repo.py` only if the aggregate validation contract or label needs to change.
  - Add README or SKILL guidance only if necessary to explain the validator expansion.
  - Do not add, remove, or edit persona records.
  - Do not modify `docs/superpowers/personas/registry.yaml`.
  - Do not expand `task_routing`.
  - Do not add secondary tags.
  - Do not change the runtime selection contract itself except for minimal validator-related guidance if needed.

## Risk And Structure

- `risk_lenses`:
  - validator checks becoming too brittle against harmless wording changes
  - validator checking only one surface and missing template/packet drift
  - accidentally enforcing future packet/runtime behavior before the contract actually says it
  - modifying the persona registry, built-in persona records, routing, or secondary tags while writing validator code
  - missing JSON output compatibility in the validator
- `parallelism_assessment`:
  - Single-section implementation is preferred because the validator must check a coherent cross-file contract and remain integrated with repo validation.
- `blocking_dependencies`:
  - Completed runtime persona selection adoption design spec.
  - Completed runtime persona selection adoption implementation round.
  - Current `validate_ww_persona_selection_contracts.py` parser and JSON/human output behavior.
  - Current `validate_ww_repo.py` aggregate runner.
- `section_or_workstream_map`:
  - section-persona-runtime-selection-validator-expansion: extend validator coverage and run repo validation

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: persona_selection_validator
    - `artifact_kind`: python_validator
    - `artifact_path`: `tools/validate_ww_persona_selection_contracts.py`
    - `section_anchors`: build_results
  - `artifact_id`: repo_validator
    - `artifact_kind`: python_validator
    - `artifact_path`: `tools/validate_ww_repo.py`
    - `section_anchors`: checks
  - `artifact_id`: maintainer_guidance
    - `artifact_kind`: maintainer_doc
    - `artifact_path`: `README.md`
    - `section_anchors`: For Maintainers
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/persona-system-expansion/case.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-validator-expansion/working-brief.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-validator-expansion/dispatch-plan.md`
  - `path_glob`: `tools/validate_ww_persona_selection_contracts.py`
  - `path_glob`: `tools/validate_ww_repo.py`
  - `path_glob`: `README.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- `shared_read_scope`:
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-design/design-spec.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-implementation/working-brief.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-implementation/dispatch-plan.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `path_glob`: `docs/superpowers/personas/registry.yaml`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `candidate_persona_sources`:
  - project registry checked: true
  - built-in fallback checked: true
  - source notes: use built-in validator/code-review personas; do not edit persona registries
- `recommended_personas`:
  - `test-quality-engineer`
    - runtime role: worker
    - source: built-in
    - owned scope: validator implementation and verification commands
    - baseline fit rationale: the task is test/validation infrastructure for a cross-file contract
    - project-priority or built-in-fallback rationale: built-in fallback is used because the current project registry has no stronger validator/test specialist
    - role binding: `worker` via `agents/worker-prompt.md`
    - workflow bindings: `superpowers:test-driven-development`, `superpowers:verification-before-completion`
  - `code-quality-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: review validator implementation for correctness, maintainability, scope discipline, and false-positive risk
    - baseline fit rationale: validator changes are code-quality and regression-risk sensitive
    - project-priority or built-in-fallback rationale: built-in fallback is used because the current project registry has no stronger code-quality reviewer
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`
- `persona_selection_notes`:
  - `test-quality-engineer` fits the implementation because the round is centered on machine-checkable validation behavior.
  - `code-quality-reviewer` fits review because the main risks are validator correctness, maintainability, and over-brittle checks.
- `recommended_worker_mode_by_section`:
  - section-persona-runtime-selection-validator-expansion: validate-first
- `worker_mode_reasoning_by_section`:
  - section-persona-runtime-selection-validator-expansion: existing validators already pass; changes should add failing coverage conceptually, implement checks, then confirm full repo validation stays green.
- `goal_tuning_by_section`:
  - section-persona-runtime-selection-validator-expansion: validation-biased
- `constraint_override_notes_by_section`:
  - section-persona-runtime-selection-validator-expansion: if a useful validator check requires persona records, project registry changes, routing, or secondary tags, record it as follow-up instead of editing those surfaces.
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - implementation execution: `superpowers:test-driven-development`
  - debugging: `superpowers:systematic-debugging`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval to expand the persona selection validator and run targeted plus aggregate validation

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-persona-runtime-selection-validator-expansion: true
- `review_target_strategy`:
  - Review validator code and any README/SKILL guidance for contract coverage, JSON output compatibility, aggregate repo validation integration, and forbidden scope discipline.
- `controller_semantics_notes`:
  - Standard `$ww` round. No strict-review target is active.
  - No validator implementation begins until the dispatch plan is approved.

## Rules

- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
