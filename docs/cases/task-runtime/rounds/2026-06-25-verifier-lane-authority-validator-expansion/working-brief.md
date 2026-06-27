# Working Brief: Verifier Lane Authority Validator Expansion

## Artifact Metadata

- `schema_version`: 2
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: verifier-lane-authority-validator-expansion
- `case_slug`: task-runtime
- `round_slug`: 2026-06-25-verifier-lane-authority-validator-expansion
- `case_root`: `docs/cases/task-runtime/`
- `round_root`: `docs/cases/task-runtime/rounds/2026-06-25-verifier-lane-authority-validator-expansion/`
- `created_at`: 2026-06-25
- `updated_at`: 2026-06-25
- `derived_from_user_request`: `$ww round: verifier lane authority validator expansion. Based on the completed and committed verifier and lane authority implementation foundation, expand WorkWork repo validation to check dormant verifier/lane authority contract surfaces. Update related validator and necessary test fixtures, covering task-runtime-verification reference existence and references from SKILL/README/templates/packet contract; legacy rounds must not use verifier/lane fields as lifecycle authority; dispatch-plan template task-runtime-v1 verifier lane block must contain verifier_lanes, verification_target_ref, evidence_requirements, freshness_policy, model_capability_profile, minimum_capability_floor, model_resolutions; subagent packet contract must preserve active legacy runtime_role gate and clearly dormant verifier packet fields; working brief template must record verification_lane_preparation and legacy non-authority note. Only validator/test/docs guidance; do not add verifier personas, verifier runtime binding, command execution, repair/scoring/hooks, or task-runtime-v1 activation.`

## Round Intent

- `quality_mode`: standard
- `lifecycle_protocol_recommendation`: legacy

## Gate State

- `estimation_complete`: true
- `brief_status`: ready
- `brief_version`: 1

## Routing

- `task_routing`: `code/programming`
- `orchestrator_choice`: `staff-engineer-orchestrator`

## Core Intent

- `goal`: add repository validation coverage for the dormant verifier/lane authority contract surfaces introduced by the approved implementation foundation
- `artifact_type`: validator code, regression tests, and maintainer guidance
- `relevant_context`:
  - The implementation foundation was committed as `08378f4 Add task runtime verifier authority foundation`.
  - The normative dormant verifier authority contract is `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`.
  - Existing repo validation is orchestrated by `tools/validate_ww_repo.py`.
  - Current validator suites already cover worker modes, role contracts, grill-me planning, persona selection, packet artifacts, case path identity, case contracts, round lifecycle, and scaffold regressions.
  - `docs/cases/grill-me-inline-planning/` is an unrelated untracked local directory and is outside this round.
- `constraints`:
  - Add validator and test coverage only for dormant verifier/lane authority contract surfaces.
  - Do not add verifier personas.
  - Do not add verifier runtime binding or prompt binding.
  - Do not implement command execution, repair, scoring, hooks, routing expansion, project registry changes, or `task-runtime-v1` activation.
  - Do not make legacy rounds consume verifier/lane fields as lifecycle authority.
  - Preserve active legacy `runtime_role` gates in packet contract validation.
  - Keep docs guidance limited to validator-suite discoverability and maintainer instructions.

## Risk And Structure

- `risk_lenses`:
  - validator silently missing required dormant verifier contract surfaces
  - validator overreaching and enforcing active verifier runtime behavior
  - false positives against legacy rounds that merely contain dormant reference text
  - packet contract validator losing the active legacy role gate while adding future verifier checks
  - tests failing to exercise negative drift fixtures for missing references or missing required fields
  - README/SKILL guidance drifting from repo validator entrypoint behavior
- `parallelism_assessment`:
  - Use one serial validator section because the validator, fixtures, repo-suite integration, and docs guidance share one set of rule names and expected failure messages.
- `blocking_dependencies`:
  - completed implementation foundation commit `08378f4`
  - current `task-runtime-verification.md` dormant contract
  - current `validate_ww_repo.py` suite orchestration
  - current dispatch/working brief/packet contract templates
- `section_or_workstream_map`:
  - section-verifier-lane-authority-validator-expansion: implement validator, negative fixtures/tests, repo-suite integration, and docs guidance

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: verifier_lane_authority_validator
    - `artifact_kind`: validator_code
    - `artifact_path`: `tools/validate_ww_verifier_authority_contracts.py`
    - `section_anchors`: reference linkage, legacy non-authority, template block fields, packet dormant verifier fields, working brief verification preparation
  - `artifact_id`: verifier_lane_authority_validator_tests
    - `artifact_kind`: test_code
    - `artifact_path`: `tools/test_validate_ww_verifier_authority_contracts.py`
    - `section_anchors`: negative drift fixtures and repo-suite behavior
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/task-runtime/case.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-25-verifier-lane-authority-validator-expansion/working-brief.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-25-verifier-lane-authority-validator-expansion/dispatch-plan.md`
  - `path_glob`: `tools/validate_ww_verifier_authority_contracts.py`
  - `path_glob`: `tools/test_validate_ww_verifier_authority_contracts.py`
  - `path_glob`: `tools/validate_ww_repo.py`
  - `path_glob`: `README.md`
- `shared_read_scope`:
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-24-verifier-lane-authority-implementation-foundation/**/*`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `candidate_persona_sources`:
  - project registry checked: true
  - built-in fallback checked: true
  - project registry outcome: no eligible project worker or reviewer persona covers portable WorkWork validator-contract implementation more strongly than the built-in specialists
  - built-in fallback outcome: use `senior-backend-engineer` for validator implementation, `spec-reviewer` for requirement fidelity, `code-quality-reviewer` for validator/test correctness, and `documentation-clarity-reviewer` for maintainer guidance clarity
  - fallback rationale when a built-in persona is recommended: this is portable WorkWork validation and contract-maintenance work rather than project-specific product behavior
- `recommended_personas`:
  - `senior-backend-engineer`
    - runtime role: worker
    - source: built-in
    - owned scope: implement the verifier/lane authority validator, tests, repo-suite integration, and README guidance
    - baseline fit rationale: the work touches validation code, fixtures, repository suite integration, and durable contract invariants
    - project-priority or built-in-fallback rationale: no stronger eligible project worker persona covers WorkWork repo validation architecture
    - role binding: `worker` via `agents/worker-prompt.md`
    - workflow bindings: `superpowers:test-driven-development`, `superpowers:verification-before-completion`
  - `spec-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: check that validator rules match the user-requested coverage and stay dormant-only
    - baseline fit rationale: the validator encodes contract requirements and exclusions
    - project-priority or built-in-fallback rationale: no stronger eligible project reviewer covers portable WorkWork specification fidelity
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
  - `code-quality-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: review validator implementation, negative fixture coverage, and repo-suite integration
    - baseline fit rationale: validator code and tests can create brittle or false-positive checks
    - project-priority or built-in-fallback rationale: no stronger eligible project reviewer covers WorkWork validator quality
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
  - `documentation-clarity-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: review README/SKILL guidance for discoverability without implying runtime activation
    - baseline fit rationale: validator coverage must be understandable to maintainers
    - project-priority or built-in-fallback rationale: no stronger eligible project reviewer covers WorkWork procedural documentation clarity
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
- `recommended_worker_mode_by_section`:
  - section-verifier-lane-authority-validator-expansion: validate-first
- `worker_mode_reasoning_by_section`:
  - section-verifier-lane-authority-validator-expansion: start from failing drift cases and existing suite behavior, then add the validator with minimal contract-specific checks.
- `goal_tuning_by_section`:
  - section-verifier-lane-authority-validator-expansion: validation-biased
- `constraint_override_notes_by_section`:
  - section-verifier-lane-authority-validator-expansion: any implementation of verifier personas, runtime binding, command execution, repair, scoring, hooks, routing, or `task-runtime-v1` activation is out of scope.
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - implementation: `superpowers:test-driven-development`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval for one serial validator implementation section, then add validator/tests and run targeted plus full repo validation

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-verifier-lane-authority-validator-expansion: true
- `review_target_strategy`:
  - Freeze the validator diff and targeted test output before code-quality and spec review.
- `controller_semantics_notes`:
  - This round remains `lifecycle_protocol: legacy`.
  - Validator checks must verify dormant contract surfaces without activating formal verifier runtime behavior.
  - No verifier packet, role binding, command runner, repair/scoring/hook logic, or `task-runtime-v1` activation may be added.

## Rules

- Persist the working brief before dispatch-plan creation.
- Every writable file in `Planned Scope` must appear in `exclusive_write_scope`.
- No packet creation until the dispatch plan is approved.
- Repo validation changes must include targeted tests plus integration into `validate_ww_repo.py`.
