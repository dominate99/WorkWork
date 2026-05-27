# Working Brief: Persona Runtime Selection Adoption Implementation

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: workflow-runtime-persona-selection-adoption-implementation
- `case_slug`: persona-system-expansion
- `round_slug`: 2026-05-26-workflow-runtime-persona-selection-adoption-implementation
- `case_root`: `docs/cases/persona-system-expansion/`
- `round_root`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-implementation/`
- `created_at`: 2026-05-26
- `updated_at`: 2026-05-26
- `derived_from_user_request`: `new $ww round: persona runtime selection adoption implementation. Based on the persona runtime selection adoption design spec, implement runtime persona selection recording rules in the WorkWork active contract and templates. Update SKILL.md, working-brief-template.md, dispatch-plan-template.md, subagent-packet-contract.md, and necessary README guidance. Only implement the persona-selection recording and contract layer: project registry priority, built-in fallback, worker-capability gate, reviewer-only gate, review lane reviewer mapping, worker specialist mapping, and persona source/rationale persistence. Do not add personas, do not change the project registry, do not expand routing, do not add secondary tags, and do not change validators.`

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

- `goal`: implement the approved runtime persona selection adoption design at the WorkWork contract and template layer
- `artifact_type`: contract and template update
- `relevant_context`:
  - The approved runtime selection adoption design spec defines how project registry priority, built-in fallback, role gates, reviewer lane mapping, worker specialist mapping, and persona source/rationale persistence should appear in WorkWork artifacts.
  - The active skill already contains persona planning language, but it does not yet fully require source/rationale persistence across working briefs, dispatch plans, review lanes, and packets.
  - The working brief template, dispatch plan template, and subagent packet contract need explicit fields so future rounds can record runtime persona selection consistently before validator enforcement.
  - README maintainer guidance should mention the active contract/template surfaces that must stay synchronized when runtime persona selection rules change.
- `constraints`:
  - Update only the contract/template/documentation surfaces authorized by the user.
  - Do not add, remove, or edit persona records.
  - Do not modify `docs/superpowers/personas/registry.yaml`.
  - Do not modify validator scripts.
  - Do not expand `task_routing`.
  - Do not add secondary route tags.
  - Do not implement runtime code outside the contract/template layer.
  - Preserve existing round lifecycle ownership and keep approval/runtime state in this round's `dispatch-plan.md`.

## Risk And Structure

- `risk_lenses`:
  - changing templates without matching the canonical skill contract
  - documenting project registry priority in a way that lets project records bypass role gates
  - making built-in fallback silent instead of rationale-backed
  - allowing reviewer-only personas into worker packets or worker-capable personas into reviewer lanes
  - drifting into validator, routing, project registry, or persona record changes
  - failing to keep packet contract fields aligned with template fields
- `parallelism_assessment`:
  - Single-section implementation is preferred because the edited contract and template files must agree on the same field names and selection semantics.
- `blocking_dependencies`:
  - Completed and approved runtime persona selection adoption design spec.
  - Existing persona taxonomy contract in `persona-registry.md`.
  - Existing built-in worker and reviewer persona records.
  - Current validators, which must continue passing without modification.
- `section_or_workstream_map`:
  - section-runtime-selection-contract-adoption: update active contract/template/docs surfaces to persist persona source, rationale, role gates, reviewer mapping, and worker mapping

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: active_skill_contract
    - `artifact_kind`: markdown_contract
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `section_anchors`: persona planning
  - `artifact_id`: working_brief_template
    - `artifact_kind`: markdown_template
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `section_anchors`: persona and workflow guidance
  - `artifact_id`: dispatch_plan_template
    - `artifact_kind`: markdown_template
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `section_anchors`: planned sections
  - `artifact_id`: subagent_packet_contract
    - `artifact_kind`: markdown_contract
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `section_anchors`: persona selection fields
  - `artifact_id`: maintainer_guidance
    - `artifact_kind`: maintainer_doc
    - `artifact_path`: `README.md`
    - `section_anchors`: For Maintainers
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/persona-system-expansion/case.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-implementation/working-brief.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-implementation/dispatch-plan.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `path_glob`: `README.md`
- `shared_read_scope`:
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-design/design-spec.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `path_glob`: `docs/superpowers/personas/registry.yaml`
  - `path_glob`: `tools/validate_ww_persona_selection_contracts.py`
  - `path_glob`: `tools/validate_ww_repo.py`
  - `path_glob`: `tools/validate_ww_round_lifecycle.py`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `candidate_persona_sources`:
  - project registry checked: true
  - built-in fallback checked: true
  - source notes: use the active project-first and built-in fallback contract as the subject of this implementation round, but do not edit either persona registry
- `recommended_personas`:
  - `technical-writer`
    - runtime role: worker
    - source: built-in
    - owned scope: contract/template documentation updates in `SKILL.md`, working brief template, dispatch plan template, packet contract, and README
    - baseline fit rationale: the working brief's artifact type is documentation/contract production across maintainer-facing markdown surfaces
    - enrichment fit rationale: reader-task-first and source-of-truth clarity fit the risk of duplicated or ambiguous contract guidance
    - role binding: `worker` via `agents/worker-prompt.md`
    - workflow bindings: `superpowers:writing-plans`, `superpowers:verification-before-completion`
  - `spec-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: review the contract/template updates for fidelity to the approved design spec and scope constraints
    - baseline fit rationale: this round implements an approved design contract and needs acceptance-criteria review
    - enrichment fit rationale: contract-first review protects against ambiguous runtime adoption language
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`
- `persona_selection_notes`:
  - The implementation worker is `technical-writer` because the authorized work is contract/template documentation, not runtime code.
  - The reviewer is `spec-reviewer` because the primary risk is whether the implementation faithfully reflects the approved design spec.
  - Built-in fallback is used because the current project registry does not provide a stronger documentation-contract worker or spec-review specialist for this task.
- `recommended_worker_mode_by_section`:
  - section-runtime-selection-contract-adoption: conservative-first
- `worker_mode_reasoning_by_section`:
  - section-runtime-selection-contract-adoption: the work updates canonical workflow contracts, so edits should be narrow, source-grounded, and compatibility-preserving.
- `goal_tuning_by_section`:
  - section-runtime-selection-contract-adoption: validation-biased
- `constraint_override_notes_by_section`:
  - section-runtime-selection-contract-adoption: if implementation would require validator, routing, secondary-tag, persona-record, project-registry, or runtime-code changes, record it as follow-up instead of editing those surfaces.
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - implementation execution: `superpowers:subagent-driven-development`
  - contract updates: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval to update the authorized contract/template/docs files, then run validation and a narrow spec-review pass

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-runtime-selection-contract-adoption: true
- `review_target_strategy`:
  - Review the edited contract/template/docs surfaces against the approved design spec, checking field consistency, source/rationale persistence, role gates, reviewer and worker mappings, and absence of forbidden scope changes.
- `controller_semantics_notes`:
  - Standard `$ww` round. No strict-review target is active.
  - No subagent packet or implementation work should start until this dispatch plan is approved.

## Rules

- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
