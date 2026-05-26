# Working Brief: Persona Coverage Audit

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: persona-coverage-audit
- `case_slug`: persona-system-expansion
- `round_slug`: 2026-05-25-persona-coverage-audit
- `case_root`: `docs/cases/persona-system-expansion/`
- `round_root`: `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/`
- `created_at`: 2026-05-25
- `updated_at`: 2026-05-25
- `derived_from_user_request`: `new $ww round: persona coverage audit; review the current ww-subagent-orchestrator persona system and produce a persona coverage gap design spec. Audit and classify only. Do not add personas and do not change validators. Focus on built-in personas, project registry, routing categories, review lanes, and worker capability gates.`

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

- `goal`: produce a persona coverage gap design spec that classifies current persona-system coverage gaps without changing persona records, validators, routing, templates, packet contracts, or runtime behavior
- `artifact_type`: design spec
- `relevant_context`:
  - User observed that the current persona set feels too small and too uniform.
  - The current built-in persona catalog is concentrated around three orchestrators, one security reviewer, and two engineering specialists.
  - The project registry mirrors a similarly narrow set and lacks broad worker and reviewer coverage.
  - The active workflow package requires persona selection to stay grounded in the working brief and to preserve role boundaries.
- `constraints`:
  - Audit and classification only.
  - Do not add or modify persona records in `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`.
  - Do not add or modify persona records in `docs/superpowers/personas/registry.yaml`.
  - Do not change validators in this round.
  - Do not update routing, dispatch templates, or packet contracts in this round.
  - The output artifact is `design-spec.md` under this round root.

## Risk And Structure

- `risk_lenses`:
  - worker-capable coverage gaps
  - reviewer lane staffing gaps
  - routing category compression
  - project registry versus built-in fallback overlap
  - worker capability gate side effects
  - optional enrichment versus missing role-family coverage
- `parallelism_assessment`:
  - Single-section audit is preferred because the output is one classification artifact and the source files overlap heavily.
- `blocking_dependencies`:
  - The design spec depends on reading the current persona registry rules, built-in persona records, project registry, dispatch template, working brief template, and persona selection validator.
- `section_or_workstream_map`:
  - section-persona-coverage-gap-design: audit current persona coverage and write the gap classification design spec

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: persona_coverage_gap_design_spec
    - `artifact_kind`: markdown_design_spec
    - `artifact_path`: `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/design-spec.md`
    - `section_anchors`: none
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/persona-system-expansion/case.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/working-brief.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/dispatch-plan.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/design-spec.md`
- `shared_read_scope`:
  - `path_glob`: `README.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `path_glob`: `docs/superpowers/personas/registry.yaml`
  - `path_glob`: `tools/validate_ww_persona_selection_contracts.py`
  - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/*/dispatch-plan.md`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff-engineer-orchestrator`
    - owned scope: create the coverage-gap design spec and synthesize source-file evidence
    - workflow bindings: `superpowers:brainstorming`, `superpowers:writing-plans`, `superpowers:verification-before-completion`
    - role binding: `orchestrator` via `agents/orchestrator-prompt.md`
  - `pm-orchestrator`
    - owned scope: review classification usefulness, routing/product-scope coverage, and whether the audit stays actionable without adding implementation scope
    - workflow bindings: `superpowers:requesting-code-review`
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
- `persona_selection_notes`:
  - `staff-engineer-orchestrator` is selected because the primary artifact is a repo workflow design spec grounded in contract files.
  - `pm-orchestrator` is selected as a narrow reviewer because the output must classify portfolio coverage and scope gaps rather than implement code.
  - No worker-capable implementation specialist is needed before approval; the eventual section writes a design artifact only.
- `recommended_worker_mode_by_section`:
  - section-persona-coverage-gap-design: standard
- `worker_mode_reasoning_by_section`:
  - section-persona-coverage-gap-design: the task is evidence-gathering and synthesis with a bounded markdown output; no aggressive autonomous implementation is appropriate.
- `goal_tuning_by_section`:
  - section-persona-coverage-gap-design: bias toward taxonomy clarity, source-grounded findings, and downstream round readiness.
- `constraint_override_notes_by_section`:
  - section-persona-coverage-gap-design: user constraints explicitly block persona additions and validator changes, so the design spec must stop at audit findings and classification.
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval to produce `design-spec.md` as the single required section output, then review it before human judgment

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-persona-coverage-gap-design: true
- `review_target_strategy`:
  - review `design-spec.md` against the user constraints, current persona sources, role-boundary rules, and whether gaps are classified without introducing changes
- `controller_semantics_notes`:
  - This standard `$ww` round uses the normal review loop. No strict-review target is active.

## Rules

- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
