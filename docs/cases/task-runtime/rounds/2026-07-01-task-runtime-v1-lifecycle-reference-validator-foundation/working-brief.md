# Working Brief: Task Runtime Lifecycle Reference Validator Foundation

## Artifact Metadata

- `schema_version`: 2
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: task-runtime-v1-lifecycle-reference-validator-foundation
- `case_slug`: task-runtime
- `round_slug`: 2026-07-01-task-runtime-v1-lifecycle-reference-validator-foundation
- `case_root`: `docs/cases/task-runtime/`
- `round_root`: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-lifecycle-reference-validator-foundation/`
- `created_at`: 2026-07-01
- `updated_at`: 2026-07-01
- `derived_from_user_request`: `$ww round: task-runtime lifecycle reference validator foundation. Based on activation gate validator design, fill the lifecycle reference linkage validator foundation: add or extend validation to check task-runtime-lifecycle reference exists and is correctly referenced by SKILL, README, working-brief-template, dispatch-plan-template, or related packet/runtime guidance; confirm legacy rounds must not treat lifecycle snapshot, event history, or lifecycle_phase as active authority. Only do validator/test/docs guidance; do not activate task-runtime-v1, add runtime binding, implement command execution/routing/packet assembly/repair/scoring/hooks, or change personas.`

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

- `goal`: implement the lifecycle-reference linkage validator foundation required before the activation gate validator can be implemented
- `artifact_type`: validator_and_docs_foundation
- `relevant_context`:
  - The activation gate validator design identified a pre-activation gap: WorkWork has verifier and missing-capability reference validators, but lifecycle reference linkage is not yet covered by a dedicated validator.
  - Existing `validate_ww_round_lifecycle.py` checks case/round ownership and dispatch lifecycle state surfaces; it does not check `task-runtime-lifecycle.md` linkage across SKILL, README, templates, or packet guidance.
  - Existing verifier and missing-capability validators provide a local pattern for reference existence, linkage fragments, legacy non-authority guards, JSON output, repo-root fixtures, and repo-suite integration.
  - This round should add lifecycle reference validator coverage without activating `task-runtime-v1`.
- `constraints`:
  - Add or extend validator/test/docs guidance only.
  - Do not activate `task-runtime-v1`.
  - Do not add runtime binding, command execution, routing, packet assembly, repair/scoring/hooks, or personas.
  - Preserve `Lifecycle Protocol: legacy`.
  - Keep active lifecycle authority out of legacy dispatch plans.
  - Preserve current activation gate design artifacts as already completed, uncommitted context.

## Risk And Structure

- `risk_lenses`:
  - false positives from prose that mentions future lifecycle fields without rendering active authority
  - false negatives for active lifecycle snapshot, event history, or writable phase authority in legacy dispatch plans
  - duplicating `validate_ww_round_lifecycle.py` instead of complementing it
  - updating docs so broadly that the round becomes a contract change rather than validator/test/docs guidance
  - failing to integrate the new validator into `validate_ww_repo.py`
- `parallelism_assessment`:
  - Use one serial implementation section because validator rules, fixtures, and repo-suite integration must evolve together.
- `blocking_dependencies`:
  - approved activation gate validator design at `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/design-spec.md`
  - lifecycle reference at `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
  - existing validator patterns in `tools/validate_ww_verifier_authority_contracts.py` and `tools/validate_ww_missing_capability_contracts.py`
- `section_or_workstream_map`:
  - section-lifecycle-reference-validator-foundation: add lifecycle reference validator, tests, repo-suite integration, and necessary docs guidance

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: lifecycle_reference
    - `artifact_kind`: reference_doc
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
    - `section_anchors`: lifecycle protocol, activation boundary, canonical phases, snapshot/event persistence, legacy migration, invalid states
  - `artifact_id`: lifecycle_reference_validator
    - `artifact_kind`: validator
    - `artifact_path`: `tools/validate_ww_lifecycle_reference_contracts.py`
    - `section_anchors`: lifecycle reference linkage and legacy non-authority guard
  - `artifact_id`: lifecycle_reference_validator_tests
    - `artifact_kind`: test_module
    - `artifact_path`: `tools/test_validate_ww_lifecycle_reference_contracts.py`
    - `section_anchors`: positive fixture, linkage negative fixtures, legacy authority negative fixtures, JSON output
  - `artifact_id`: repo_validation_suite
    - `artifact_kind`: validator
    - `artifact_path`: `tools/validate_ww_repo.py`
    - `section_anchors`: lifecycle reference contract validation suite entry
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/task-runtime/case.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-lifecycle-reference-validator-foundation/working-brief.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-lifecycle-reference-validator-foundation/dispatch-plan.md`
  - `path_glob`: `tools/validate_ww_lifecycle_reference_contracts.py`
  - `path_glob`: `tools/test_validate_ww_lifecycle_reference_contracts.py`
  - `path_glob`: `tools/validate_ww_repo.py`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `README.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
- `shared_read_scope`:
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
  - `path_glob`: `tools/validate_ww_round_lifecycle.py`
  - `path_glob`: `tools/validate_ww_verifier_authority_contracts.py`
  - `path_glob`: `tools/validate_ww_missing_capability_contracts.py`
  - `path_glob`: `tools/test_validate_ww_verifier_authority_contracts.py`
  - `path_glob`: `tools/test_validate_ww_missing_capability_contracts.py`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/design-spec.md`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `candidate_persona_sources`:
  - project registry checked: true
  - built-in fallback checked: true
  - project registry outcome: project `senior-backend-engineer` is eligible for Python validator work, but built-in `test-quality-engineer` is stronger for fixture and validator semantics
  - built-in fallback outcome: use built-in `test-quality-engineer` for implementation, with spec/code-quality/documentation review lanes
  - fallback rationale when a built-in persona is recommended: the main risk is validator coverage, negative fixture quality, and false-positive/false-negative behavior
- `recommended_personas`:
  - `test-quality-engineer`
    - runtime role: worker
    - source: built-in
    - owned scope: implement lifecycle reference validator, tests, repo-suite integration, and necessary docs guidance
    - baseline fit rationale: this round is dominated by validation surfaces and fixture design
    - project-priority or built-in-fallback rationale: built-in fallback is stronger than the available project specialist for validator regression confidence
    - enrichment fit rationale: evidence-first decision style fits reference validator foundation work
    - role binding: `worker` via `agents/worker-prompt.md`
    - workflow bindings: `superpowers:test-driven-development`, `superpowers:verification-before-completion`
  - `spec-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: verify the implementation matches the user constraints and activation gate design
    - baseline fit rationale: scope boundaries and non-activation constraints are primary acceptance criteria
    - project-priority or built-in-fallback rationale: no project reviewer is stronger for contract completeness
    - enrichment fit rationale: contract-first review fits lifecycle authority boundaries
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`
  - `code-quality-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: verify validator implementation, fixture isolation, JSON output, and repo-suite integration
    - baseline fit rationale: validator correctness and maintainability are the code-quality risk
    - project-priority or built-in-fallback rationale: built-in reviewer-only persona best matches this review lane
    - enrichment fit rationale: maintainability and false-positive/false-negative focus fit the task
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`
  - `documentation-clarity-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: verify any docs guidance is precise and does not imply runtime activation
    - baseline fit rationale: the round permits docs guidance only when necessary
    - project-priority or built-in-fallback rationale: built-in documentation clarity reviewer is the strongest fit for source-of-truth wording
    - enrichment fit rationale: reader-action-first review prevents activation ambiguity
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`
- `recommended_worker_mode_by_section`:
  - section-lifecycle-reference-validator-foundation: test-first
- `worker_mode_reasoning_by_section`:
  - section-lifecycle-reference-validator-foundation: add failing fixtures for lifecycle reference linkage and legacy authority drift before implementing validator behavior
- `goal_tuning_by_section`:
  - section-lifecycle-reference-validator-foundation: validation-biased
- `constraint_override_notes_by_section`:
  - section-lifecycle-reference-validator-foundation: do not activate task-runtime-v1 or introduce runtime behavior while adding validator coverage
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - implementation: `superpowers:test-driven-development`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval for one serial validator foundation section

## Grill-Me Decision Log

No `grill-me` trigger is active for this round.

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-lifecycle-reference-validator-foundation: true
- `review_target_strategy`:
  - Review the final validator, tests, repo-suite integration, and docs guidance against the activation gate design and user constraints.
- `controller_semantics_notes`:
  - This round remains `lifecycle_protocol: legacy`.
  - Test fixtures may include future lifecycle authority examples inside temporary fixture repositories; those examples are test data only and not active WorkWork authority.
  - No packet creation is required before dispatch plan approval.

## Rules

- Persist the working brief before dispatch-plan approval.
- Every writable file in `Planned Scope` must appear in `exclusive_write_scope`.
- No packet creation until the dispatch plan is approved.
- Keep work limited to lifecycle reference validator/test/docs guidance foundation.
