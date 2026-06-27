# Working Brief: Verifier Lane Authority Validator Dogfood Audit

## Artifact Metadata

- `schema_version`: 2
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: verifier-lane-authority-validator-dogfood-audit
- `case_slug`: task-runtime
- `round_slug`: 2026-06-27-verifier-lane-authority-validator-dogfood-audit
- `case_root`: `docs/cases/task-runtime/`
- `round_root`: `docs/cases/task-runtime/rounds/2026-06-27-verifier-lane-authority-validator-dogfood-audit/`
- `created_at`: 2026-06-27
- `updated_at`: 2026-06-27
- `derived_from_user_request`: `$ww round: verifier lane authority validator dogfood audit. Based on the completed and pushed verifier lane authority validator expansion, audit whether the new validator truly covers task-runtime-verification reference linkage, legacy non-authority guard, dispatch template verifier lane block, packet dormant verifier gate, working brief verification preparation, negative fixtures, repo-suite integration, and whether checks are too broad or too narrow. Audit and classify only; do not modify the validator, add verifier personas, add runtime binding, implement command execution, repair/scoring/hooks, or activate task-runtime-v1. Decide whether a later validator hardening round is needed.`

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

- `goal`: dogfood the newly pushed verifier/lane authority validator by auditing its real coverage, drift-fixture quality, repo-suite integration, and over/under-enforcement risks
- `artifact_type`: audit report or design-spec-style gap classification
- `relevant_context`:
  - Verifier authority contract foundation is committed as `08378f4 Add task runtime verifier authority foundation`.
  - Verifier authority validator expansion is committed and pushed as `6b6eaf2 Add verifier authority contract validation`.
  - The validator under audit is `tools/validate_ww_verifier_authority_contracts.py`.
  - Its regression tests are `tools/test_validate_ww_verifier_authority_contracts.py`.
  - Repo-suite integration is in `tools/validate_ww_repo.py`.
  - Normative dormant contract surfaces include `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`, `SKILL.md`, `README.md`, `assets/dispatch-plan-template.md`, `references/subagent-packet-contract.md`, and `references/working-brief-template.md`.
  - `docs/cases/grill-me-inline-planning/` is an unrelated untracked local directory and is outside this round.
- `constraints`:
  - Audit and classify only.
  - Do not modify validator code, test fixtures, templates, packet contract, README, SKILL, project registry, or runtime bindings.
  - Do not add verifier personas.
  - Do not add verifier runtime binding or packet generation.
  - Do not implement command execution, repair, scoring, hooks, routing expansion, secondary tags, or `task-runtime-v1` activation.
  - Do not broaden or harden validator behavior in this round.

## Risk And Structure

- `risk_lenses`:
  - validator checks may be too string-fragment dependent and miss semantically equivalent drift
  - legacy non-authority guard may be too broad and block historical prose that is not an active authority surface
  - negative fixtures may prove only missing text rather than realistic drift
  - dispatch template field coverage may miss nesting or schema-shape failures
  - packet dormant verifier gate may preserve text while still allowing future binding ambiguity elsewhere
  - repo-suite integration may run the validator but not protect enough failure modes
  - hardening may not be justified yet if current coverage is sufficient for dormant-contract stage
- `parallelism_assessment`:
  - Use one serial audit section because the conclusion depends on comparing validator rules, fixtures, real contract files, and repo-suite behavior together.
- `blocking_dependencies`:
  - pushed validator expansion commit `6b6eaf2`
  - completed verifier/lane authority implementation foundation
  - current repo validation suite
  - current dormant verifier authority contract references
- `section_or_workstream_map`:
  - section-verifier-validator-dogfood-audit: inspect validator rules, test fixtures, target files, repo-suite integration, and classify gaps or sufficiency

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: verifier_authority_validator
    - `artifact_kind`: python_validator
    - `artifact_path`: `tools/validate_ww_verifier_authority_contracts.py`
    - `section_anchors`: WWVA001 through WWVA007 rule coverage
  - `artifact_id`: verifier_authority_validator_tests
    - `artifact_kind`: python_test
    - `artifact_path`: `tools/test_validate_ww_verifier_authority_contracts.py`
    - `section_anchors`: negative fixtures and CLI JSON failure schema
  - `artifact_id`: verifier_authority_dogfood_report
    - `artifact_kind`: design_spec
    - `artifact_path`: `docs/cases/task-runtime/rounds/2026-06-27-verifier-lane-authority-validator-dogfood-audit/design-spec.md`
    - `section_anchors`: coverage classification, false-positive risk, false-negative risk, and hardening recommendation
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/task-runtime/case.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-27-verifier-lane-authority-validator-dogfood-audit/working-brief.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-27-verifier-lane-authority-validator-dogfood-audit/dispatch-plan.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-27-verifier-lane-authority-validator-dogfood-audit/design-spec.md`
- `shared_read_scope`:
  - `path_glob`: `tools/validate_ww_verifier_authority_contracts.py`
  - `path_glob`: `tools/test_validate_ww_verifier_authority_contracts.py`
  - `path_glob`: `tools/validate_ww_repo.py`
  - `path_glob`: `README.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-25-verifier-lane-authority-validator-expansion/**/*`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `candidate_persona_sources`:
  - project registry checked: true
  - built-in fallback checked: true
  - project registry outcome: no eligible project persona is available for WorkWork validator coverage auditing
  - built-in fallback outcome: use `senior-backend-engineer` for audit classification, with `spec-reviewer`, `code-quality-reviewer`, and `documentation-clarity-reviewer` as review lanes
  - fallback rationale when a built-in persona is recommended: the work audits portable WorkWork validator contracts and persisted round evidence rather than project-specific product behavior
- `recommended_personas`:
  - `senior-backend-engineer`
    - runtime role: worker
    - source: built-in
    - owned scope: audit validator coverage against requested dogfood surfaces and produce the gap report/design spec
    - baseline fit rationale: validator semantics, fixtures, and repo-suite integration require backend/tooling judgment
    - project-priority or built-in-fallback rationale: no stronger eligible project worker persona covers WorkWork validator coverage auditing
    - role binding: `worker` via `agents/worker-prompt.md`
    - workflow bindings: `superpowers:writing-plans`, `superpowers:verification-before-completion`
  - `spec-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: verify that the audit addresses each requested coverage point and preserves all exclusions
    - baseline fit rationale: this round is primarily about requirement fidelity and scope boundaries
    - project-priority or built-in-fallback rationale: no stronger eligible project reviewer covers WorkWork dormant verifier contract fidelity
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
  - `code-quality-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: inspect the audit's validator/test reasoning for false-positive and false-negative risk
    - baseline fit rationale: validator hardening decisions depend on implementation and fixture quality
    - project-priority or built-in-fallback rationale: no stronger eligible project reviewer covers repo validator quality analysis
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
  - `documentation-clarity-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: verify the dogfood report is readable and actionably classifies whether a hardening round is needed
    - baseline fit rationale: the output is a persisted design-spec/gap report for later round planning
    - project-priority or built-in-fallback rationale: no stronger eligible project reviewer covers WorkWork audit report clarity
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
- `recommended_worker_mode_by_section`:
  - section-verifier-validator-dogfood-audit: research-first
- `worker_mode_reasoning_by_section`:
  - section-verifier-validator-dogfood-audit: inspect current validator behavior and fixtures before classifying gaps; do not edit validator surfaces.
- `goal_tuning_by_section`:
  - section-verifier-validator-dogfood-audit: validation-biased
- `constraint_override_notes_by_section`:
  - section-verifier-validator-dogfood-audit: any code or contract hardening discovered by the audit must be deferred to a later approved round.
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - audit execution: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval for one serial audit section that produces `design-spec.md` as a dogfood gap report and recommends whether a validator hardening round is warranted

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-verifier-validator-dogfood-audit: true
- `review_target_strategy`:
  - Freeze the dogfood report artifact before review; reviewers inspect the report against the validator code, fixtures, contract references, and user-requested exclusions.
- `controller_semantics_notes`:
  - This round remains `lifecycle_protocol: legacy`.
  - The audit may recommend a later hardening round but must not implement hardening.
  - No verifier persona, verifier packet, runtime binding, command runner, repair/scoring/hook logic, or `task-runtime-v1` activation may be added.

## Rules

- Persist the working brief before dispatch-plan creation.
- Every writable file in `Planned Scope` must appear in `exclusive_write_scope`.
- No packet creation until the dispatch plan is approved.
- The audit output must distinguish current sufficiency, false-positive risk, false-negative risk, and any recommended future hardening.
