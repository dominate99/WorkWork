# Working Brief: Persona Taxonomy Contract

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: persona-taxonomy-contract
- `case_slug`: persona-system-expansion
- `round_slug`: 2026-05-26-persona-taxonomy-contract
- `case_root`: `docs/cases/persona-system-expansion/`
- `round_root`: `docs/cases/persona-system-expansion/rounds/2026-05-26-persona-taxonomy-contract/`
- `created_at`: 2026-05-26
- `updated_at`: 2026-05-26
- `derived_from_user_request`: `new $ww round: persona taxonomy contract. Based on the persona coverage audit design spec, update the ww-subagent-orchestrator persona system taxonomy contract. Define minimum persona portfolio coverage, orchestrator/worker/reviewer/explorer role families, when to add a persona rather than only adding enrichment fields, and the division of responsibility between project registry and built-in personas. Only update contract/docs; do not add concrete persona records and do not change validators.`

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

- `goal`: update the persona-system contract documentation so future persona expansion is governed by explicit taxonomy, minimum coverage, and source-of-truth boundaries
- `artifact_type`: contract documentation update
- `relevant_context`:
  - The completed persona coverage audit found narrow worker-capable specialist coverage, reviewer lane mismatch, compressed routing, limited project-registry differentiation, and no coverage validator yet.
  - This round should translate those audit findings into normative contract language.
  - The round must not add actual persona records or validator behavior; those belong to later rounds.
- `constraints`:
  - Update contract/docs only.
  - Do not edit `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`.
  - Do not edit `docs/superpowers/personas/registry.yaml`.
  - Do not edit validator scripts.
  - Do not change routing values yet.
  - Keep the contract compatible with current validators.

## Risk And Structure

- `risk_lenses`:
  - taxonomy becoming too abstract to guide later implementation
  - accidentally authorizing persona additions in this round
  - weakening role-boundary and worker-capability gates
  - creating contract language that current validators reject
  - over-prescribing future persona names before the expansion round
- `parallelism_assessment`:
  - Single-section contract update is preferred because `SKILL.md`, `persona-registry.md`, and maintainer docs must stay semantically aligned.
- `blocking_dependencies`:
  - Completed audit design spec: `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/design-spec.md`
  - Current contract files: `SKILL.md`, `persona-registry.md`, and `README.md`
- `section_or_workstream_map`:
  - section-persona-taxonomy-contract: update taxonomy guidance and documentation only

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: taxonomy_contract_skill
    - `artifact_kind`: markdown_contract
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `section_anchors`: Persona Planning
  - `artifact_id`: taxonomy_contract_registry
    - `artifact_kind`: markdown_contract
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - `section_anchors`: Required Persona Fields, Selection Rules, Migration Rules
  - `artifact_id`: taxonomy_contract_readme
    - `artifact_kind`: maintainer_doc
    - `artifact_path`: `README.md`
    - `section_anchors`: Development and validation guidance
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/persona-system-expansion/case.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-persona-taxonomy-contract/working-brief.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-26-persona-taxonomy-contract/dispatch-plan.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `path_glob`: `README.md`
- `shared_read_scope`:
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/design-spec.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `path_glob`: `docs/superpowers/personas/registry.yaml`
  - `path_glob`: `tools/validate_ww_persona_selection_contracts.py`
  - `path_glob`: `tools/validate_ww_repo.py`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff-engineer-orchestrator`
    - owned scope: update the persona taxonomy contract language across docs without changing persona records or validators
    - workflow bindings: `superpowers:writing-plans`, `superpowers:verification-before-completion`
    - role binding: `orchestrator` via `agents/orchestrator-prompt.md`
  - `pm-orchestrator`
    - owned scope: review whether the taxonomy is understandable, actionable, and properly staged for later expansion rounds
    - workflow bindings: `superpowers:requesting-code-review`
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
- `persona_selection_notes`:
  - `staff-engineer-orchestrator` fits because the round changes workflow contract text and must preserve validator-compatible semantics.
  - `pm-orchestrator` fits review because the taxonomy must be useful for staged product/process evolution, not only technically precise.
- `recommended_worker_mode_by_section`:
  - section-persona-taxonomy-contract: standard
- `worker_mode_reasoning_by_section`:
  - section-persona-taxonomy-contract: targeted contract edits with explicit constraints; no broad autonomous rewrite is needed.
- `goal_tuning_by_section`:
  - section-persona-taxonomy-contract: emphasize crisp definitions, minimum coverage floors, and future-round boundaries.
- `constraint_override_notes_by_section`:
  - section-persona-taxonomy-contract: if a needed concept implies future implementation, describe it as a later-round requirement instead of modifying records or validators.
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval to update contract/docs in one section, then run validator and reviewer checks before human judgment

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-persona-taxonomy-contract: true
- `review_target_strategy`:
  - review changed contract docs against the audit design spec, user constraints, existing validators, and role-boundary rules
- `controller_semantics_notes`:
  - Standard `$ww` round. No strict-review target is active.

## Rules

- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
