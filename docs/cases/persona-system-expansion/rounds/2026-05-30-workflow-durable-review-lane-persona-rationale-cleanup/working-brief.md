# Working Brief: Durable Review Lane Persona Rationale Cleanup

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: workflow-durable-review-lane-persona-rationale-cleanup
- `case_slug`: persona-system-expansion
- `round_slug`: 2026-05-30-workflow-durable-review-lane-persona-rationale-cleanup
- `case_root`: `docs/cases/persona-system-expansion/`
- `round_root`: `docs/cases/persona-system-expansion/rounds/2026-05-30-workflow-durable-review-lane-persona-rationale-cleanup/`
- `created_at`: 2026-05-30
- `updated_at`: 2026-05-30
- `derived_from_user_request`: `new $ww round: durable review lane persona rationale cleanup. Based on the persona runtime selection dogfood audit, add durable Section Review Record Reviewer Selection Rationale persistence to the active contract and dispatch plan template. Synchronize validate_ww_persona_selection_contracts.py and necessary README/SKILL guidance. Only fix review lane rationale persistence; do not backfill historical rounds, add personas, change the project registry, expand routing, add secondary tags, or change the packet contract.`

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

- `goal`: close DG-001 from the approved dogfood audit by persisting reviewer selection rationale in durable Section Review Record lane records and enforcing that field in repo validation
- `artifact_type`: active contract, template, and validator cleanup
- `relevant_context`:
  - The approved dogfood audit identified durable review-lane rationale persistence as the strongest remaining runtime persona selection recording gap.
  - Planned review lanes already record reviewer source, runtime role, and selection rationale.
  - Durable `Section Review Record` lane records currently preserve reviewer source and runtime role but omit reviewer selection rationale.
  - `validate_ww_persona_selection_contracts.py` WWPS024 checks durable review record source/runtime role fields and should be tightened to include rationale persistence.
- `constraints`:
  - Update the active contract and `dispatch-plan-template.md` only as needed to require durable reviewer selection rationale.
  - Update `tools/validate_ww_persona_selection_contracts.py` to check the durable field.
  - Update README or SKILL guidance only if needed to state the durable persistence rule.
  - Do not backfill historical rounds.
  - Do not add, remove, or edit persona records.
  - Do not modify `docs/superpowers/personas/registry.yaml`.
  - Do not expand `task_routing`.
  - Do not add secondary tags.
  - Do not edit `subagent-packet-contract.md`.

## Risk And Structure

- `risk_lenses`:
  - adding the field to the template without stating its durable snapshot semantics in the active contract
  - updating guidance without tightening validator coverage
  - widening the round into historical backfill or packet-contract edits
  - making WWPS024 brittle beyond the specific durable field requirement
- `parallelism_assessment`:
  - Single-section cleanup is preferred because contract wording, template field shape, and validator fragment check must land together.
- `blocking_dependencies`:
  - Approved persona runtime selection dogfood audit report.
  - Current `SKILL.md` persona planning contract.
  - Current `dispatch-plan-template.md` Section Review Record shape.
  - Current WWPS024 validator rule.
- `section_or_workstream_map`:
  - section-durable-review-lane-persona-rationale-cleanup: update active contract, dispatch plan template, validator, and necessary guidance; verify repo validation

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: active_skill_contract
    - `artifact_kind`: markdown_contract
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `section_anchors`: persona planning
  - `artifact_id`: dispatch_plan_template
    - `artifact_kind`: markdown_template
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `section_anchors`: section review record
  - `artifact_id`: persona_selection_validator
    - `artifact_kind`: python_validator
    - `artifact_path`: `tools/validate_ww_persona_selection_contracts.py`
    - `section_anchors`: WWPS024
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/persona-system-expansion/case.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-30-workflow-durable-review-lane-persona-rationale-cleanup/working-brief.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-30-workflow-durable-review-lane-persona-rationale-cleanup/dispatch-plan.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `path_glob`: `tools/validate_ww_persona_selection_contracts.py`
  - `path_glob`: `README.md`
- `shared_read_scope`:
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-28-workflow-runtime-persona-selection-dogfood-audit/design-spec.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `path_glob`: `docs/superpowers/personas/registry.yaml`
  - `path_glob`: `tools/validate_ww_repo.py`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `candidate_persona_sources`:
  - project registry checked: true
  - built-in fallback checked: true
  - project registry outcome: no stronger eligible documentation-contract worker or code-quality reviewer exists in `docs/superpowers/personas/registry.yaml` for this narrow cleanup
  - built-in fallback outcome: use `technical-writer` for contract/template cleanup and `code-quality-reviewer` for validator-sensitive review
  - fallback rationale when a built-in persona is recommended: built-in records provide the strongest required-field fit for synchronized contract wording and validator correctness
- `recommended_personas`:
  - `technical-writer`
    - runtime role: worker
    - source: built-in
    - owned scope: active contract and dispatch plan template reviewer rationale persistence edits
    - baseline fit rationale: the main work product is maintainer-facing source-of-truth contract wording and template field shape
    - project-priority or built-in-fallback rationale: built-in fallback is used because the project registry has no stronger eligible documentation-contract worker
    - enrichment fit rationale: reader-task-first and source-of-truth clarity match the narrow cleanup
    - role binding: `worker` via `agents/worker-prompt.md`
    - workflow bindings: `superpowers:writing-plans`, `superpowers:verification-before-completion`
  - `code-quality-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: review active contract, template, and validator synchronization for false-negative and scope-creep risk
    - baseline fit rationale: the cleanup changes a Python validation rule and contract fragments that must remain synchronized
    - project-priority or built-in-fallback rationale: built-in fallback is used because the project registry has no stronger eligible code-quality reviewer
    - enrichment fit rationale: correctness-and-maintainability-first review matches validator drift risk
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`, `superpowers:verification-before-completion`
- `persona_selection_notes`:
  - Keep the change narrow: durable review lane rationale only.
  - Historical round artifacts remain untouched.
  - Packet contract remains untouched because DG-001 is a dispatch review-record gap.
- `recommended_worker_mode_by_section`:
  - section-durable-review-lane-persona-rationale-cleanup: validate-first
- `worker_mode_reasoning_by_section`:
  - section-durable-review-lane-persona-rationale-cleanup: begin from the existing passing WWPS024 check, add the specific durable rationale requirement, and verify targeted plus aggregate validation.
- `goal_tuning_by_section`:
  - section-durable-review-lane-persona-rationale-cleanup: validation-biased
- `constraint_override_notes_by_section`:
  - section-durable-review-lane-persona-rationale-cleanup: any historical backfill, persona, registry, routing, secondary-tag, or packet-contract change must be recorded as follow-up instead of edited.
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - cleanup implementation: `superpowers:test-driven-development`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval to close DG-001 with synchronized active contract, template, and validator edits

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-durable-review-lane-persona-rationale-cleanup: true
- `review_target_strategy`:
  - Review the cleanup for exact DG-001 closure, template/validator synchronization, clear durable snapshot semantics, and absence of historical, packet, persona, registry, routing, or secondary-tag edits.
- `controller_semantics_notes`:
  - Standard `$ww` round. No strict-review target is active.
  - No cleanup implementation begins until the dispatch plan is approved.

## Rules

- Recommended personas are provisional until dispatch approval.
- Persona selection must cite the working brief, not just task keywords.
- Persona selection must record source, runtime role, baseline fit, and project-priority or built-in-fallback rationale.
- The working brief recommends `worker mode` by section, but it does not act as the final execution authority.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
