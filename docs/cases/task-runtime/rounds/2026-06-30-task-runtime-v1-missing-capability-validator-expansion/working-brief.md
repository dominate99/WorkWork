# Working Brief: Task Runtime V1 Missing Capability Validator Expansion

## Artifact Metadata

- `schema_version`: 2
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: task-runtime-v1-missing-capability-validator-expansion
- `case_slug`: task-runtime
- `round_slug`: 2026-06-30-task-runtime-v1-missing-capability-validator-expansion
- `case_root`: `docs/cases/task-runtime/`
- `round_root`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-expansion/`
- `created_at`: 2026-06-30
- `updated_at`: 2026-06-30
- `derived_from_user_request`: `$ww round: task-runtime-v1 missing capability validator expansion. Based on the committed missing capability implementation foundation, extend WorkWork repository validation for dormant missing-capability contract surfaces. Update the relevant validator and necessary test fixtures. Cover reference linkage, legacy non-authority, dispatch template record families and omission rule, working brief preparation guidance, packet source-context fields, and dormant wording. Validator/test/docs guidance only; do not activate task-runtime-v1, add personas, add runtime binding, or implement command execution, routing, packet assembly, repair, scoring, or hooks.`

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

- `goal`: add repository validation for the dormant task-runtime missing-capability contract surfaces that were introduced in the previous implementation foundation round
- `artifact_type`: validator_and_fixture_implementation
- `relevant_context`:
  - `task-runtime-missing-capabilities.md` now defines dormant contract surfaces for internal hooks, quality gates/scoring, repair authorization/re-verification, review synthesis, close gates, final human judgment, recovery requirements, and checkpoints.
  - `SKILL.md`, `README.md`, `dispatch-plan-template.md`, `working-brief-template.md`, and `subagent-packet-contract.md` now reference those dormant surfaces.
  - `validate_ww_verifier_authority_contracts.py` is the closest existing pattern for dormant task-runtime reference linkage, template blocks, packet dormant gates, working brief guidance, negative legacy guard checks, JSON output, and repo-suite integration.
  - This round should make the new missing-capability contract machine-checkable without activating runtime behavior.
- `constraints`:
  - Validator, test, and necessary docs guidance only.
  - Do not activate `task-runtime-v1`.
  - Do not add personas.
  - Do not add verifier/runtime binding.
  - Do not implement command execution, routing, packet assembly, repair, scoring, hooks, or runtime lifecycle behavior.
  - Preserve `Lifecycle Protocol: legacy` for this round.
  - Preserve the existing verifier authority validator behavior unless shared helper extraction is clearly necessary and low-risk.

## Risk And Structure

- `risk_lenses`:
  - validator could be too shallow and merely check one token instead of the full record-family contract
  - legacy guard could false-positive on design specs or reference examples that are intentionally dormant
  - legacy guard could false-negative if it only searches one field name
  - adding a repo-suite check without JSON contract compatibility could break `validate_ww_repo.py --json`
  - test fixtures could accidentally depend on the live repository state instead of isolated temporary files
  - docs guidance could imply activation or runtime enforcement rather than validation of dormant surfaces
- `parallelism_assessment`:
  - Use one serial section because the validator, fixtures, repo-suite integration, and docs guidance must agree on rule names and fixture scope.
- `blocking_dependencies`:
  - committed missing capability implementation foundation commit `315b577`
  - active missing capability reference at `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`
  - existing validator suite pattern in `tools/validate_ww_verifier_authority_contracts.py`
- `section_or_workstream_map`:
  - section-missing-capability-validator-expansion: implement validator rules, tests/fixtures, repo-suite integration, and scoped docs guidance for dormant missing-capability contract surfaces

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: missing_capability_reference
    - `artifact_kind`: reference_doc
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`
    - `section_anchors`: dormant record families, authority boundary, internal hooks, quality gates and scoring, repair and re-verification, review synthesis, close gates, final judgment, recovery and checkpoints, invalid states for later validators
  - `artifact_id`: missing_capability_implementation_round
    - `artifact_kind`: dispatch_round
    - `artifact_path`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-implementation-foundation/dispatch-plan.md`
    - `section_anchors`: execution records, verification evidence, review records, final human approval
  - `artifact_id`: verifier_authority_validator
    - `artifact_kind`: validator
    - `artifact_path`: `tools/validate_ww_verifier_authority_contracts.py`
    - `section_anchors`: dormant reference linkage pattern, legacy non-authority guard, JSON output shape, repo-root argument
  - `artifact_id`: verifier_authority_validator_tests
    - `artifact_kind`: test_module
    - `artifact_path`: `tools/test_validate_ww_verifier_authority_contracts.py`
    - `section_anchors`: negative fixture pattern and validator regression tests
  - `artifact_id`: repo_validation_suite
    - `artifact_kind`: validator
    - `artifact_path`: `tools/validate_ww_repo.py`
    - `section_anchors`: build_checks integration
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/task-runtime/case.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-expansion/working-brief.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-expansion/dispatch-plan.md`
  - `path_glob`: `tools/validate_ww_missing_capability_contracts.py`
  - `path_glob`: `tools/test_validate_ww_missing_capability_contracts.py`
  - `path_glob`: `tools/validate_ww_repo.py`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/packets/lifecycle-foundation-code-quality-review-r2.md`
  - `path_glob`: `README.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- `shared_read_scope`:
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `path_glob`: `tools/validate_ww_verifier_authority_contracts.py`
  - `path_glob`: `tools/test_validate_ww_verifier_authority_contracts.py`
  - `path_glob`: `tools/validate_ww_round_lifecycle.py`
  - `path_glob`: `tools/validate_ww_case_contracts.py`
- `scope_adjustment_note`:
  - updating `tools/validate_ww_repo.py` changes the full-file hash referenced by an existing reviewer packet; this round may update only that packet's immutable target hash fields as validation maintenance, without changing packet contract behavior or creating new packets
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `candidate_persona_sources`:
  - project registry checked: true
  - built-in fallback checked: true
  - project registry outcome: use project `senior-backend-engineer` as the worker-capable specialist because the change is Python validator implementation tied to WorkWork controller contracts
  - built-in fallback outcome: use built-in `spec-reviewer`, `code-quality-reviewer`, and `documentation-clarity-reviewer` as reviewer lanes
  - fallback rationale when a built-in persona is recommended: no project reviewer persona is stronger for contract fidelity, code/test quality, or docs guidance than the built-in reviewer-only personas
- `recommended_personas`:
  - `senior-backend-engineer`
    - runtime role: worker
    - source: project
    - owned scope: implement the missing-capability validator, tests, repo-suite integration, and scoped docs guidance
    - baseline fit rationale: validator behavior changes require maintainable Python implementation, fixture discipline, and contract-boundary correctness
    - project-priority or built-in-fallback rationale: project registry provides a worker-capable specialist with architecture, correctness, and maintainability strengths
    - enrichment fit rationale: the task affects validation and active workflow contract surfaces rather than frontend, data, release, or pure documentation
    - role binding: `worker` via `agents/worker-prompt.md`
    - workflow bindings: `superpowers:test-driven-development`, `superpowers:systematic-debugging`, `superpowers:verification-before-completion`
  - `spec-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: verify validator coverage matches the user-requested surfaces and exclusions
    - baseline fit rationale: this round must not activate task-runtime-v1 or widen runtime scope
    - project-priority or built-in-fallback rationale: built-in reviewer-only persona is the strongest available spec lane
    - enrichment fit rationale: durable acceptance depends on exact requirement coverage
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`
  - `code-quality-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: review validator implementation, fixture isolation, JSON contract, and repo-suite integration
    - baseline fit rationale: poor validator structure could create false positives or block unrelated future rounds
    - project-priority or built-in-fallback rationale: built-in reviewer-only persona is the strongest available code-quality lane
    - enrichment fit rationale: checks include executable Python and test harness changes
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`
  - `documentation-clarity-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: review SKILL/README guidance for dormant validation scope and non-activation wording
    - baseline fit rationale: users and maintainers must understand this is validation of dormant contract surfaces, not runtime activation
    - project-priority or built-in-fallback rationale: built-in reviewer-only persona is the strongest available documentation clarity lane
    - enrichment fit rationale: docs guidance is a required but bounded part of the user request
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`
- `recommended_worker_mode_by_section`:
  - section-missing-capability-validator-expansion: test-driven
- `worker_mode_reasoning_by_section`:
  - section-missing-capability-validator-expansion: implement validator rules with isolated regression tests first or alongside the validator, then integrate into the repo suite
- `goal_tuning_by_section`:
  - section-missing-capability-validator-expansion: validation-biased
- `constraint_override_notes_by_section`:
  - section-missing-capability-validator-expansion: if validator coverage would require runtime activation semantics, stop at dormant surface checks and record deferred activation-only checks for later rounds
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - implementation: `superpowers:test-driven-development`
  - debugging: `superpowers:systematic-debugging`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval for one serial validator/test/docs implementation section

## Grill-Me Decision Log

No `grill-me` trigger is active for this round.

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-missing-capability-validator-expansion: true
- `review_target_strategy`:
  - Freeze the validator, test module, repo-suite integration, and docs guidance after implementation; reviewers inspect the staged diff against the user request and dormant contract references.
- `controller_semantics_notes`:
  - This round remains `lifecycle_protocol: legacy`.
  - New validator rules may inspect dormant `task-runtime-v1` template/reference surfaces, but this round must not render active missing-capability authority records in its own dispatch plan.
  - Legacy guard checks should target active legacy dispatch authority surfaces, not design specs or reference examples that intentionally describe future dormant fields.
  - Negative fixtures should be isolated from the live repository so tests prove validator behavior rather than current repo contents.

## Rules

- Persist the working brief before dispatch-plan approval.
- Every writable file in `Planned Scope` must appear in `exclusive_write_scope`.
- No packet creation until the dispatch plan is approved.
- The implementation must keep missing-capability fields dormant and non-authorizing under `Lifecycle Protocol: legacy`.
