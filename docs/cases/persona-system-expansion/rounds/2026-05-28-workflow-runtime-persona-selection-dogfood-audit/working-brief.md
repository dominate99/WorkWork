# Working Brief: Persona Runtime Selection Dogfood Audit

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: workflow-runtime-persona-selection-dogfood-audit
- `case_slug`: persona-system-expansion
- `round_slug`: 2026-05-28-workflow-runtime-persona-selection-dogfood-audit
- `case_root`: `docs/cases/persona-system-expansion/`
- `round_root`: `docs/cases/persona-system-expansion/rounds/2026-05-28-workflow-runtime-persona-selection-dogfood-audit/`
- `created_at`: 2026-05-28
- `updated_at`: 2026-05-28
- `derived_from_user_request`: `new $ww round: persona runtime selection dogfood audit. Based on the completed and pushed persona runtime selection adoption design, implementation, and validator expansion, audit whether WorkWork's active contract, templates, and recent persona-system-expansion rounds actually record persona source/runtime role/rationale under the new contract. Only audit and classify; produce a persona runtime selection dogfood gap report or design spec; do not implement, add personas, change validators, expand routing, or add secondary tags. Focus on working brief, dispatch plan, review lane records, planned specialist/reviewer personas, subagent packet contract dogfood consistency, and judge whether enough evidence exists to open a routing/secondary tags design round.`

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

- `goal`: audit whether the runtime persona selection recording contract is being used consistently by WorkWork's own active contract, templates, and recent persona-system-expansion rounds
- `artifact_type`: dogfood audit gap report
- `relevant_context`:
  - Runtime persona selection adoption design, implementation, and validator expansion were completed and pushed in commit `343099a`.
  - The active contract now requires persona source, runtime role, baseline fit, and project-priority or built-in-fallback rationale in working briefs, dispatch plans, review lanes, and packets.
  - The validator checks that the contract surfaces exist, but it does not judge whether recent rounds consistently dogfood the new recording contract.
  - The next decision is whether evidence supports a routing or secondary tags design round, or whether gaps remain in current dogfood consistency.
- `constraints`:
  - Produce only an audit/classification artifact, expected as `design-spec.md` with a gap-report structure.
  - Do not implement contract or template changes.
  - Do not add, remove, or edit persona records.
  - Do not modify `docs/superpowers/personas/registry.yaml`.
  - Do not change validator scripts.
  - Do not expand `task_routing`.
  - Do not add secondary tags.
  - Do not change project registry priority rules.

## Risk And Structure

- `risk_lenses`:
  - mistaking validator existence for real dogfood consistency
  - over-claiming the need for routing or secondary tags without enough round evidence
  - treating older pre-adoption rounds as failures instead of historical baseline
  - blurring audit recommendations into implementation changes
  - missing drift between templates and actual recent round records
- `parallelism_assessment`:
  - Single-section audit is preferred because the evidence set is shared and the output should be one coherent gap report.
- `blocking_dependencies`:
  - Completed runtime persona selection adoption design.
  - Completed runtime persona selection adoption implementation.
  - Completed runtime persona selection validator expansion.
  - Active contract and template files after commit `343099a`.
  - Recent persona-system-expansion round artifacts.
- `section_or_workstream_map`:
  - section-persona-runtime-selection-dogfood-audit: inspect active contract, templates, and recent rounds; classify dogfood gaps; decide whether routing/secondary tags design has enough evidence

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: persona_runtime_selection_dogfood_gap_report
    - `artifact_kind`: dogfood_gap_report
    - `artifact_path`: `docs/cases/persona-system-expansion/rounds/2026-05-28-workflow-runtime-persona-selection-dogfood-audit/design-spec.md`
    - `section_anchors`: dogfood audit findings
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/persona-system-expansion/case.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-28-workflow-runtime-persona-selection-dogfood-audit/working-brief.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-28-workflow-runtime-persona-selection-dogfood-audit/dispatch-plan.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-28-workflow-runtime-persona-selection-dogfood-audit/design-spec.md`
- `shared_read_scope`:
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `path_glob`: `docs/superpowers/personas/registry.yaml`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-design/**`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-implementation/**`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-validator-expansion/**`
  - `path_glob`: `tools/validate_ww_persona_selection_contracts.py`
  - `path_glob`: `tools/validate_ww_repo.py`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `candidate_persona_sources`:
  - project registry checked: true
  - built-in fallback checked: true
  - project registry outcome: no stronger documentation/audit specialist or spec reviewer exists in `docs/superpowers/personas/registry.yaml` for this contract dogfood audit
  - built-in fallback outcome: use `technical-writer` for the audit artifact and `spec-reviewer` for required review
  - fallback rationale when a built-in persona is recommended: built-in personas carry the strongest required-field fit for documentation/source-of-truth audit production and spec-contract review
- `recommended_personas`:
  - `technical-writer`
    - runtime role: worker
    - source: built-in
    - owned scope: dogfood gap report artifact
    - baseline fit rationale: the work product is a maintainer-facing audit report about source-of-truth clarity and template/document consistency
    - project-priority or built-in-fallback rationale: built-in fallback is used because the project registry has no stronger eligible documentation/audit specialist with worker-capable fields
    - enrichment fit rationale: quality bar and failure modes favor source-of-truth clarity over broad implementation analysis
    - role binding: `worker` via `agents/worker-prompt.md`
    - workflow bindings: `superpowers:writing-plans`, `superpowers:verification-before-completion`
  - `spec-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: review the dogfood gap report for contract completeness, evidence quality, and boundary discipline
    - baseline fit rationale: the target is a contract/audit artifact whose value depends on coherent requirements and testable findings
    - project-priority or built-in-fallback rationale: built-in fallback is used because the project registry has no stronger eligible reviewer-only spec persona
    - enrichment fit rationale: contract-first decision style matches the need to distinguish actual contract gaps from future design ideas
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`, `superpowers:verification-before-completion`
- `persona_selection_notes`:
  - The section should classify dogfood gaps, not patch them.
  - The report should distinguish current active contract/template gaps from historical round artifacts that predate adoption.
  - Routing or secondary tags should be recommended only if repeated ambiguity appears in the evidence.
- `recommended_worker_mode_by_section`:
  - section-persona-runtime-selection-dogfood-audit: conservative-first
- `worker_mode_reasoning_by_section`:
  - section-persona-runtime-selection-dogfood-audit: the round is evidence classification over recently changed workflow contracts, so the worker should avoid speculative redesign.
- `goal_tuning_by_section`:
  - section-persona-runtime-selection-dogfood-audit: audit-biased
- `constraint_override_notes_by_section`:
  - section-persona-runtime-selection-dogfood-audit: any implementation, validator, persona, registry, routing, or secondary-tag change must be recorded as follow-up, not performed in this round.
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - audit execution: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval to produce a dogfood gap report in `design-spec.md`

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-persona-runtime-selection-dogfood-audit: true
- `review_target_strategy`:
  - Review the completed dogfood gap report for accurate evidence classification, faithful scope boundaries, and a justified routing/secondary-tags recommendation.
- `controller_semantics_notes`:
  - Standard `$ww` round. No strict-review target is active.
  - No audit artifact creation begins until the dispatch plan is approved.

## Rules

- Recommended personas are provisional until dispatch approval.
- Persona selection must cite the working brief, not just task keywords.
- Persona selection must record source, runtime role, baseline fit, and project-priority or built-in-fallback rationale.
- The working brief recommends `worker mode` by section, but it does not act as the final execution authority.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
