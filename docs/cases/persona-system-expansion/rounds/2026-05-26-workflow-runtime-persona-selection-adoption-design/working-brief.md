# Working Brief: Persona Runtime Selection Adoption Design

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: workflow-runtime-persona-selection-adoption-design
- `case_slug`: persona-system-expansion
- `round_slug`: 2026-05-26-workflow-runtime-persona-selection-adoption-design
- `case_root`: `docs/cases/persona-system-expansion/`
- `round_root`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-design/`
- `created_at`: 2026-05-26
- `updated_at`: 2026-05-26
- `derived_from_user_request`: `new $ww round: persona runtime selection adoption design. Based on persona taxonomy contract, worker persona expansion, and reviewer persona expansion, design how WorkWork selects and records built-in/project personas in actual working brief, dispatch plan, reviewer lane, and worker packet artifacts. Only produce a design spec; do not implement, add personas, change validators, or expand routing. Focus on project registry priority, built-in fallback, worker-capability gate, reviewer-only gate, review lane to reviewer persona mapping, worker section to specialist persona mapping, and whether a later routing/secondary tag round is needed.`

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

- `goal`: produce a design spec for adopting the expanded persona taxonomy and built-in/project persona records in runtime selection and persisted WorkWork artifacts
- `artifact_type`: runtime-selection adoption design spec
- `relevant_context`:
  - The persona coverage audit identified runtime adoption, reviewer-lane staffing, worker specialist mapping, routing compression, and validator coverage as follow-up areas.
  - The taxonomy contract now defines project-registry priority, built-in fallback boundaries, worker-capability gates, reviewer-only gates, and optional enrichment rules.
  - Built-in worker-capable personas and reviewer-only personas now exist, but the live workflow still needs a concrete design for selecting and recording them in working briefs, dispatch plans, reviewer lanes, and worker packets.
  - This round should define adoption behavior before any implementation, validator, routing, or packet-template changes.
- `constraints`:
  - Produce only `design-spec.md` in this round.
  - Do not implement runtime selection changes.
  - Do not add, remove, or edit persona records.
  - Do not modify validators.
  - Do not expand `task_routing` values or add secondary tags.
  - Do not change the project persona registry.
  - Record whether later routing or secondary-tag work is needed, but leave it as follow-up design or implementation work.

## Risk And Structure

- `risk_lenses`:
  - designing runtime selection in a way that bypasses project registry priority
  - allowing reviewer-only personas into worker packets or worker-capable personas into findings-only review lanes without role gating
  - mapping review lane labels to personas too rigidly before routing/secondary-tag policy is decided
  - hiding adoption behavior in prose without specifying which persisted artifacts carry selection rationale
  - accidentally widening scope into validator, routing, or implementation edits
- `parallelism_assessment`:
  - Single-section design work is preferred because the output is one coherent design spec and the mapping rules must be internally consistent.
- `blocking_dependencies`:
  - Completed persona coverage audit design spec.
  - Completed persona taxonomy contract.
  - Completed built-in worker persona expansion.
  - Completed built-in reviewer persona expansion.
  - Current `SKILL.md`, subagent packet contract, working brief template, dispatch plan template, built-in persona records, and project registry rules.
- `section_or_workstream_map`:
  - section-runtime-selection-adoption-design: write the runtime selection adoption design spec and keep all implementation and validator work out of scope

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: persona_runtime_selection_adoption_design_spec
    - `artifact_kind`: design_spec
    - `artifact_path`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-design/design-spec.md`
    - `section_anchors`: runtime selection adoption design
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/persona-system-expansion/case.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-design/working-brief.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-design/dispatch-plan.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-design/design-spec.md`
- `shared_read_scope`:
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/design-spec.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-persona-taxonomy-contract/working-brief.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-persona-taxonomy-contract/dispatch-plan.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-worker-persona-expansion/working-brief.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-worker-persona-expansion/dispatch-plan.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-reviewer-persona-expansion/working-brief.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-reviewer-persona-expansion/dispatch-plan.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `path_glob`: `docs/superpowers/personas/registry.yaml`
  - `path_glob`: `tools/validate_ww_persona_selection_contracts.py`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff-engineer-orchestrator`
    - owned scope: draft `design-spec.md` and synthesize adoption design from existing contracts and completed persona expansion rounds
    - workflow bindings: `superpowers:writing-plans`, `superpowers:verification-before-completion`
    - role binding: `orchestrator` via `agents/orchestrator-prompt.md`
  - `spec-reviewer`
    - owned scope: review whether the design spec is contract-complete, implementation-ready, and scoped to design-only output
    - workflow bindings: `superpowers:requesting-code-review`
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
- `persona_selection_notes`:
  - `staff-engineer-orchestrator` fits because the round designs runtime artifact behavior and contract adoption, not product messaging or creative direction.
  - `spec-reviewer` fits because the output must be a coherent design contract with testable acceptance criteria for later implementation and validator rounds.
  - This round intentionally dogfoods the new reviewer persona catalog by using a reviewer-only built-in for the `spec-review` lane.
- `recommended_worker_mode_by_section`:
  - section-runtime-selection-adoption-design: standard
- `worker_mode_reasoning_by_section`:
  - section-runtime-selection-adoption-design: bounded design-spec authoring with no implementation, validator, routing, or registry changes.
- `goal_tuning_by_section`:
  - section-runtime-selection-adoption-design: prioritize explicit artifact fields, gate ordering, and follow-up boundaries over broad architecture prose.
- `constraint_override_notes_by_section`:
  - section-runtime-selection-adoption-design: if the design reveals a need for implementation, validator, routing, secondary tags, or registry changes, record that as follow-up rather than editing those surfaces.
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - design drafting: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval to write the design spec, then review it against the taxonomy contract, completed persona records, and design-only scope limits

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-runtime-selection-adoption-design: true
- `review_target_strategy`:
  - Review `design-spec.md` for coverage of project registry priority, built-in fallback, worker-capability gate, reviewer-only gate, reviewer lane mapping, worker specialist mapping, persisted artifact placement, and follow-up routing/secondary-tag decision points.
- `controller_semantics_notes`:
  - Standard `$ww` round. No strict-review target is active.
  - The design spec becomes the only result artifact after approval; no packet, validator, routing, or persona record changes are authorized by this plan.

## Rules

- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
