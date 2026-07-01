# Working Brief: Missing Capability Legacy Guard Validator Hardening

## Artifact Metadata

- `schema_version`: 2
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: missing-capability-legacy-guard-validator-hardening
- `case_slug`: task-runtime
- `round_slug`: 2026-07-01-missing-capability-legacy-guard-validator-hardening
- `case_root`: `docs/cases/task-runtime/`
- `round_root`: `docs/cases/task-runtime/rounds/2026-07-01-missing-capability-legacy-guard-validator-hardening/`
- `created_at`: 2026-07-01
- `updated_at`: 2026-07-01
- `derived_from_user_request`: `$ww round: missing capability legacy guard validator hardening. Based on the task-runtime-v1 missing capability validator dogfood audit, fix the WWMC007 legacy non-authority guard coverage gap. Harden validate_ww_missing_capability_contracts.py and tests so any YAML-like active missing-capability record family in a legacy dispatch fails; add heading-only, single-family without heading, multi-family without heading, and dormant/prose-only allowed fixtures; avoid raw field-name prose false positives. Only change validator/tests and necessary test notes; do not change dormant contract, personas, project registry, routing, packet assembly, runtime command execution, repair/scoring/hooks, or activate task-runtime-v1.`

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

- `goal`: harden WWMC007 so legacy dispatch plans fail on YAML-like active missing-capability record-family authority while dormant prose stays allowed
- `artifact_type`: validator_and_test_hardening
- `relevant_context`:
  - The prior dogfood audit found that `legacy_dispatch_authority_violations()` can likely miss a legacy dispatch containing one YAML-like active missing-capability record-family assignment when the canonical heading is absent.
  - The prior audit also found that the existing legacy negative fixture does not isolate record-family fallback behavior because the heading alone is sufficient to trigger WWMC007.
  - The current fallback counts raw record family names in normalized dispatch-plan text, which can create false positives for prose that mentions multiple field names without rendering active authority.
  - This round should convert those audit findings into focused validator and test changes only.
- `constraints`:
  - Only change `tools/validate_ww_missing_capability_contracts.py`, `tools/test_validate_ww_missing_capability_contracts.py`, and necessary round planning artifacts.
  - Do not change dormant contract references, templates, README, SKILL, built-in or project personas, project registry, routing, packet assembly, runtime command execution, repair/scoring/hooks, or `task-runtime-v1` activation.
  - Keep this round `Lifecycle Protocol: legacy`.
  - Do not render active missing-capability authority blocks inside this legacy dispatch plan.

## Risk And Structure

- `risk_lenses`:
  - regex or text scanning may become too broad and reject dormant prose examples
  - tightening the guard may accidentally flag code snippets in the validator dogfood round docs
  - tests could pass by detecting the canonical heading instead of isolating assignment detection
  - the validator must stay cross-platform and repo-root aware
  - the round itself must avoid creating a legacy dispatch-plan false positive under the current validator
- `parallelism_assessment`:
  - Use one serial section because the validator logic and fixtures are tightly coupled.
- `blocking_dependencies`:
  - approved dogfood audit report at `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/design-spec.md`
  - current validator source at `tools/validate_ww_missing_capability_contracts.py`
  - current tests at `tools/test_validate_ww_missing_capability_contracts.py`
- `section_or_workstream_map`:
  - section-missing-capability-legacy-guard-hardening: add isolated regression fixtures, harden legacy dispatch detection, run focused and repo-wide validation

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: missing_capability_validator
    - `artifact_kind`: validator
    - `artifact_path`: `tools/validate_ww_missing_capability_contracts.py`
    - `section_anchors`: `legacy_dispatch_authority_violations`, WWMC007
  - `artifact_id`: missing_capability_validator_tests
    - `artifact_kind`: test_module
    - `artifact_path`: `tools/test_validate_ww_missing_capability_contracts.py`
    - `section_anchors`: legacy guard fixtures and CLI JSON regression coverage
  - `artifact_id`: dogfood_audit_report
    - `artifact_kind`: design_spec
    - `artifact_path`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/design-spec.md`
    - `section_anchors`: P2/P3 findings and hardening recommendation
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/task-runtime/case.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-07-01-missing-capability-legacy-guard-validator-hardening/working-brief.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-07-01-missing-capability-legacy-guard-validator-hardening/dispatch-plan.md`
  - `path_glob`: `tools/validate_ww_missing_capability_contracts.py`
  - `path_glob`: `tools/test_validate_ww_missing_capability_contracts.py`
- `shared_read_scope`:
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/design-spec.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`
  - `path_glob`: `tools/validate_ww_repo.py`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `candidate_persona_sources`:
  - project registry checked: true
  - built-in fallback checked: true
  - project registry outcome: project `senior-backend-engineer` is eligible but less specialized for regression fixture design than the built-in test specialist
  - built-in fallback outcome: use built-in `test-quality-engineer` as the worker
  - fallback rationale when a built-in persona is recommended: the work is dominated by validator edge cases, negative fixtures, and false-positive/false-negative regression confidence
- `recommended_personas`:
  - `test-quality-engineer`
    - runtime role: worker
    - source: built-in
    - owned scope: harden WWMC007 legacy guard logic and focused regression tests
    - baseline fit rationale: the main risk is validator/test behavior, not broad backend architecture
    - project-priority or built-in-fallback rationale: built-in fallback is stronger than the available project specialist for fixture isolation and regression semantics
    - enrichment fit rationale: validation-first decision style fits the round's narrow hardening goal
    - role binding: `worker` via `agents/worker-prompt.md`
    - workflow bindings: `superpowers:test-driven-development`, `superpowers:systematic-debugging`, `superpowers:verification-before-completion`
  - `spec-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: confirm the implementation honors the exact user constraints and does not expand dormant contracts
    - baseline fit rationale: the round is scoped by a precise audit-to-hardening contract
    - project-priority or built-in-fallback rationale: no project reviewer is stronger for requirement coverage
    - enrichment fit rationale: contract completeness is the main review axis
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`
  - `code-quality-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: review the guard logic and fixture isolation for false positives and false negatives
    - baseline fit rationale: validator correctness and maintainability are the highest-risk code concerns
    - project-priority or built-in-fallback rationale: built-in reviewer-only persona best matches code-quality lane
    - enrichment fit rationale: regression and maintainability focus match the validator hardening risk
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`
  - `documentation-clarity-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: review any necessary test-note wording and final handoff clarity
    - baseline fit rationale: the user allowed necessary test explanation only
    - project-priority or built-in-fallback rationale: built-in reviewer is the narrowest fit for clarity without expanding scope
    - enrichment fit rationale: reader-action-first review prevents ambiguous hardening claims
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`
- `recommended_worker_mode_by_section`:
  - section-missing-capability-legacy-guard-hardening: test-first
- `worker_mode_reasoning_by_section`:
  - section-missing-capability-legacy-guard-hardening: write failing fixtures for the dogfood gaps before changing the validator
- `goal_tuning_by_section`:
  - section-missing-capability-legacy-guard-hardening: validation-biased
- `constraint_override_notes_by_section`:
  - section-missing-capability-legacy-guard-hardening: do not change dormant contract surfaces or activate task-runtime-v1 even if validator semantics suggest broader cleanup
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - implementation: `superpowers:test-driven-development`, `superpowers:systematic-debugging`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval for one serial validator hardening section

## Grill-Me Decision Log

No `grill-me` trigger is active for this round.

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-missing-capability-legacy-guard-hardening: true
- `review_target_strategy`:
  - Review the final validator and test diff against the dogfood audit findings and user constraints.
- `controller_semantics_notes`:
  - This round remains `lifecycle_protocol: legacy`.
  - The worker may create test fixtures that contain active missing-capability assignments inside temporary test workspaces; those fixtures are test data, not WorkWork lifecycle authority.
  - No packet creation is required before dispatch plan approval.

## Rules

- Persist the working brief before dispatch-plan approval.
- Every writable file in `Planned Scope` must appear in `exclusive_write_scope`.
- No packet creation until the dispatch plan is approved.
- Keep the implementation limited to WWMC007 validator/test hardening.
