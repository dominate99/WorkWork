# Working Brief: Case Path Identity Validator

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: case-path-identity-validator
- `case_slug`: case-based-artifact-layout
- `round_slug`: 2026-05-22-case-path-identity-validator
- `case_root`: `docs/superpowers/cases/case-based-artifact-layout/`
- `round_root`: `docs/superpowers/cases/case-based-artifact-layout/rounds/2026-05-22-case-path-identity-validator/`
- `created_at`: 2026-05-22
- `updated_at`: 2026-05-22
- `derived_from_user_request`: `当前最大的残余风险不是这次 diff 本身，而是 validator 还没有检查 case-based path identity`

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

- `goal`: add repo-local validator coverage for case-based path identity so new `$ww` and `$www` rounds are automatically checked for `case_slug`, `round_slug`, `case_root`, `round_root`, canonical case-based default paths, and protection against drift back to type-based canonical write paths
- `artifact_type`: validator implementation round plus approval-ready dispatch plan
- `relevant_context`:
  - the workflow contract now states that new rounds write canonically under `docs/superpowers/cases/<case-slug>/rounds/<round-slug>/`
  - `working-brief-template.md` and `dispatch-plan-template.md` now require explicit case and round identity fields
  - current repo-level validators do not yet check these new path identity semantics
  - the live contract changes for case-based layout are currently present in the working tree and should be treated as the reference contract for this validator round
- `constraints`:
  - default to validator-surface changes rather than broader workflow redesign
  - keep persona, packet, reviewer, and worker-mode semantics out of scope
  - only touch contract text if validator implementation reveals a concrete ambiguity that prevents stable checks
  - preserve the migration rule that legacy type-based paths may remain readable but are not active canonical write targets for new rounds

## Risk And Structure

- `risk_lenses`:
  - a weak validator could allow silent drift back to type-based canonical paths
  - a brittle validator could freeze exact prose instead of checking the path-identity contract
  - if case-based identity rules are checked inconsistently across surfaces, the repo can end up with a false sense of migration safety
  - if repo-level aggregation is not updated cleanly, CI could stay green while skipping the new validator
- `parallelism_assessment`:
  - this round is tightly coupled across the new validator, repo-level aggregation, and maintainer guidance
  - one implementation lane is better because path identity semantics and validator output shape need to stay coherent
- `blocking_dependencies`:
  - the case-based layout contract changes in `SKILL.md`, `working-brief-template.md`, `dispatch-plan-template.md`, and `README.md`
  - the existing validator style in `tools/quick_validate.py`, `tools/validate_ww_worker_work_mode.py`, `tools/validate_ww_role_contracts.py`, and `tools/validate_ww_persona_selection_contracts.py`
- `section_or_workstream_map`:
  - section 1: define validator rule boundaries for case path identity
  - section 2: implement the validator and wire it into repo-level validation

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: `ww_skill_contract`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `section_anchors`: `Working Brief`, `Dispatch Plan File`, `Document Summary Contract`
  - `artifact_id`: `working_brief_template`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `section_anchors`: `Artifact Metadata`, `Scope Preparation`
  - `artifact_id`: `dispatch_plan_template`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `section_anchors`: `Path identity rules`
  - `artifact_id`: `repo_validator`
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
  - `artifact_id`: `persona_selection_validator_reference`
  - `artifact_kind`: `code`
  - `artifact_path`: `tools/validate_ww_persona_selection_contracts.py`
  - `section_anchors`: none
- `exclusive_write_scope`:
  - `path_glob`: `docs/superpowers/cases/case-based-artifact-layout/rounds/2026-05-22-case-path-identity-validator/working-brief.md`
  - `path_glob`: `docs/superpowers/cases/case-based-artifact-layout/rounds/2026-05-22-case-path-identity-validator/dispatch-plan.md`
  - `path_glob`: `tools/validate_ww_case_path_identity.py`
  - `path_glob`: `tools/validate_ww_repo.py`
  - `path_glob`: `README.md`
- `shared_read_scope`:
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `path_glob`: `tools/*.py`
  - `path_glob`: `docs/superpowers/cases/case-based-artifact-layout/**/*`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff-engineer-orchestrator`
  - `pm-orchestrator`
- `persona_selection_notes`:
  - `staff-engineer-orchestrator` fits because this is contract-validation and migration-safety work with authority and compatibility risk
  - `pm-orchestrator` is a useful reviewer lens because the validator should protect user-visible workflow clarity rather than only internal neatness
- `recommended_worker_mode_by_section`:
  - section 1: `validate-first`
  - section 2: `conservative-first`
- `worker_mode_reasoning_by_section`:
  - section 1 should validate the exact path-identity contract now present in the working tree before encoding checks
  - section 2 should add the smallest stable validator surface that protects the migration rules without widening scope
- `goal_tuning_by_section`:
  - section 1: `validation-biased`
  - section 2: `safety-biased`
- `constraint_override_notes_by_section`:
  - section 1: do not freeze incidental wording if the contract semantics can be checked structurally
  - section 2: do not widen into repo-wide migration mechanics or generated artifact rewrites
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - approve one bounded validator lane for case-based path identity semantics
  - require section-aware checks for canonical paths and case/round metadata
  - integrate the new validator into repo-level validation and maintainer guidance

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-case-path-identity-validator: true
- `review_target_strategy`:
  - validate that new rounds require `case_slug`, `round_slug`, `case_root`, and `round_root`
  - validate that canonical default paths point to `docs/superpowers/cases/...`
  - validate that legacy type-based paths are not described as active canonical write targets for new rounds
- `controller_semantics_notes`:
  - this round adds validator coverage only
  - no packet creation until the referenced dispatch plan is in `approved` state
  - contract-path migration behavior should remain unchanged by this round except through validation coverage

## Rules

- Recommended personas are provisional until dispatch approval.
- Validator rules must cite the active contract text, not invent new path semantics.
- The working brief is an analysis artifact, not the runtime approval record.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
- If the user requests `Revise`, update the working brief only if the analysis changed, then issue a new brief version for the next dispatch plan revision.
