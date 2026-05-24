# Working Brief: Persona Runtime-Selection Validator Pilot

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: persona-runtime-selection-validator-pilot
- `created_at`: 2026-05-22
- `updated_at`: 2026-05-22
- `derived_from_user_request`: `先做当前这轮的 precommit review，然后 commit；接着起新的 $ww validator round`

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

- `goal`: add repo-local validator coverage for persona runtime-selection guidance so the new selection contract stops being documentation-only and becomes automatically checkable
- `artifact_type`: validator implementation round plus approval-ready dispatch plan
- `relevant_context`:
  - the runtime-selection guidance pilot is complete and committed
  - current repo validators cover packaged skill frontmatter, worker `work_mode`, and reviewer/explorer role contracts
  - no validator currently checks that persona runtime-selection guidance keeps required fields as eligibility gates and enrichment fields as ranking and rationale inputs only
- `constraints`:
  - default to validator-surface changes, not new workflow behavior
  - keep packet contracts, prompts, and persona records out of scope
  - only touch contract files if validator implementation reveals a concrete ambiguity that blocks stable checks
  - preserve the distinction between required-field eligibility and enrichment-driven ranking

## Risk And Structure

- `risk_lenses`:
  - a weak validator will only grep for words and miss contract drift
  - an over-strong validator can accidentally freeze wording instead of checking semantics
  - if the validator blurs ranking with eligibility, it will encode the wrong selection model
  - if repo-level aggregation is not updated cleanly, CI could stay green while skipping the new checks
- `parallelism_assessment`:
  - this round is tightly coupled across the new validator, repo-level aggregator, and maintainer documentation
  - one implementation lane is better than parallel slices because the schema and aggregation shape need one coherent design
- `blocking_dependencies`:
  - the approved runtime-selection guidance in `persona-registry.md` and `SKILL.md`
  - the existing validator style in `tools/validate_ww_worker_work_mode.py`, `tools/validate_ww_role_contracts.py`, and `tools/validate_ww_repo.py`
- `section_or_workstream_map`:
  - section 1: define validator scope and rule boundaries
  - section 2: implement the persona runtime-selection validator and integrate it into repo-level validation

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: `persona_runtime_selection_rules`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `section_anchors`: `Selection Rules`, `Runtime Selection Guidance`
  - `artifact_id`: `ww_skill_persona_guidance`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `section_anchors`: `Persona Planning`
  - `artifact_id`: `ww_repo_validator`
  - `artifact_kind`: `code`
  - `artifact_path`: `tools/validate_ww_repo.py`
  - `section_anchors`: none
  - `artifact_id`: `worker_mode_validator_reference`
  - `artifact_kind`: `code`
  - `artifact_path`: `tools/validate_ww_worker_work_mode.py`
  - `section_anchors`: none
  - `artifact_id`: `role_contract_validator_reference`
  - `artifact_kind`: `code`
  - `artifact_path`: `tools/validate_ww_role_contracts.py`
  - `section_anchors`: none
- `exclusive_write_scope`:
  - `path_glob`: `docs/legacy/superpowers/working-briefs/2026-05-22-persona-runtime-selection-validator-pilot-v1.md`
  - `path_glob`: `docs/legacy/superpowers/dispatch-plans/2026-05-22-persona-runtime-selection-validator-pilot.md`
  - `path_glob`: `tools/validate_ww_persona_selection_contracts.py`
  - `path_glob`: `tools/validate_ww_repo.py`
  - `path_glob`: `README.md`
- `shared_read_scope`:
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `tools/quick_validate.py`
  - `path_glob`: `tools/validate_ww_worker_work_mode.py`
  - `path_glob`: `tools/validate_ww_role_contracts.py`
  - `path_glob`: `docs/legacy/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff-engineer-orchestrator`
  - `pm-orchestrator`
  - `creative-director-orchestrator`
- `persona_selection_notes`:
  - `staff-engineer-orchestrator` fits because this is validator and contract integration work inside the orchestration system
  - `pm-orchestrator` is a strong reviewer lens because the validator must stay outcome-focused and check the user-visible intent of persona selection
  - `creative-director-orchestrator` is a useful counterweight because a good validator should preserve semantic contrast without freezing incidental wording
- `recommended_worker_mode_by_section`:
  - section 1: `validate-first`
  - section 2: `conservative-first`
- `worker_mode_reasoning_by_section`:
  - section 1 should validate the exact runtime-selection semantics that now exist before encoding them
  - section 2 should add the smallest stable validator surface that catches contract drift without widening runtime behavior
- `goal_tuning_by_section`:
  - section 1: `validation-biased`
  - section 2: `safety-biased`
- `constraint_override_notes_by_section`:
  - section 1: do not turn ranking semantics into hard-required-field semantics
  - section 2: do not widen into packet, prompt, or persona-record changes unless a real ambiguity blocks validation
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - approve one bounded validator lane for persona runtime-selection semantics
  - require section-aware checks instead of whole-file keyword checks
  - integrate the new validator into repo-level validation and maintainer guidance

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-persona-runtime-selection-validator: true
- `review_target_strategy`:
  - review whether the validator enforces baseline eligibility before enrichment-driven ranking
  - review whether the validator preserves role-boundary, worker-gate, and project-registry guardrails
  - treat wording-freezing or hidden scope growth as blocking
- `controller_semantics_notes`:
  - this round adds validator coverage only
  - no packet, prompt, or persona-record adoption is in scope
  - repo-level aggregation must stay green and keep human-readable output by default

## Rules

- Recommended personas are provisional until dispatch approval.
- Persona-validation rules must cite the approved contract text, not invent new semantics.
- The working brief is an analysis artifact, not the runtime approval record.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
- If the user requests `Revise`, update the working brief only if the analysis changed, then issue a new brief version for the next dispatch plan revision.
