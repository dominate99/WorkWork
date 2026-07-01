# Working Brief: Task Runtime V1 Missing Capability Validator Dogfood Audit

## Artifact Metadata

- `schema_version`: 2
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: task-runtime-v1-missing-capability-validator-followup-dogfood-audit
- `case_slug`: task-runtime
- `round_slug`: 2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit
- `case_root`: `docs/cases/task-runtime/`
- `round_root`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/`
- `created_at`: 2026-06-30
- `updated_at`: 2026-06-30
- `derived_from_user_request`: `$ww round: task-runtime-v1 missing capability validator dogfood audit. Based on the completed and committed missing capability validator expansion, audit whether the new validator truly covers task-runtime-missing-capabilities reference linkage, SKILL/README guidance, dispatch template record families, working brief missing_capability_preparation, packet source-context dormant fields, legacy non-authority guard, negative fixtures, JSON output, repo-suite integration, and whether checks are too broad or too narrow. Audit and classify only; do not modify validators, add personas, add runtime binding, implement command execution/routing/packet assembly/repair/scoring/hooks, or activate task-runtime-v1. Decide whether a later validator hardening round is needed.`

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

- `goal`: audit the newly committed missing-capability validator for real coverage, fixture quality, repo-suite integration, and overbroad or underbroad checks
- `artifact_type`: dogfood_audit_gap_report
- `relevant_context`:
  - The missing-capability validator expansion commit added `tools/validate_ww_missing_capability_contracts.py`, `tools/test_validate_ww_missing_capability_contracts.py`, and repo-suite integration.
  - The validator currently reports seven rule families for dormant reference linkage, SKILL linkage, README guidance, dispatch template missing-capability block, packet dormant source context, working brief preparation, and legacy non-authority.
  - This audit should inspect real source, fixtures, JSON output, and repo-suite behavior against the user-requested coverage list.
  - The output should classify gaps and decide whether a focused validator hardening round is needed.
- `constraints`:
  - Audit and classification only.
  - Do not modify validator code, tests, templates, README, SKILL, packet contract, personas, routing, runtime binding, runtime behavior, command execution, packet assembly, repair/scoring/hooks, or project registry.
  - Do not activate `task-runtime-v1`.
  - Preserve `Lifecycle Protocol: legacy`.
  - If a gap is found, record it as future work in the audit report instead of fixing it in this round.

## Risk And Structure

- `risk_lenses`:
  - validator may check for fragments but not prove semantic linkage
  - legacy non-authority guard may be too broad and reject valid design/reference examples
  - legacy non-authority guard may be too narrow and miss active authority drift when headings differ
  - negative fixtures may prove only single-token removals rather than realistic drift
  - JSON output may pass standalone but not demonstrate aggregate repo-suite behavior
  - repo-suite integration may not include the new validator in every expected mode
  - audit could accidentally become a hardening implementation round
- `parallelism_assessment`:
  - Use one serial audit section because coverage findings and the hardening recommendation must be synthesized into one coherent gap report.
- `blocking_dependencies`:
  - committed missing capability validator expansion commit `55eeba6`
  - active validator source `tools/validate_ww_missing_capability_contracts.py`
  - validator fixtures `tools/test_validate_ww_missing_capability_contracts.py`
  - repo-suite integration `tools/validate_ww_repo.py`
- `section_or_workstream_map`:
  - section-missing-capability-validator-followup-dogfood-audit: inspect source and tests, run validator/repo-suite evidence, produce `design-spec.md` gap report and recommendation

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: missing_capability_validator
    - `artifact_kind`: validator
    - `artifact_path`: `tools/validate_ww_missing_capability_contracts.py`
    - `section_anchors`: rule families WWMC001-WWMC007, legacy dispatch guard, JSON output, repo-root argument
  - `artifact_id`: missing_capability_validator_tests
    - `artifact_kind`: test_module
    - `artifact_path`: `tools/test_validate_ww_missing_capability_contracts.py`
    - `section_anchors`: valid fixture, negative fixtures, CLI JSON failure schema
  - `artifact_id`: repo_validation_suite
    - `artifact_kind`: validator
    - `artifact_path`: `tools/validate_ww_repo.py`
    - `section_anchors`: Missing-capability contract validation check
  - `artifact_id`: missing_capability_reference
    - `artifact_kind`: reference_doc
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`
    - `section_anchors`: dormant record families, authority boundary, invalid states for later validators
  - `artifact_id`: dogfood_audit_report
    - `artifact_kind`: design_spec
    - `artifact_path`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/design-spec.md`
    - `section_anchors`: coverage matrix, fixture audit, overbroad/underbroad analysis, hardening recommendation
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/task-runtime/case.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/working-brief.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/dispatch-plan.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit/design-spec.md`
- `shared_read_scope`:
  - `path_glob`: `tools/validate_ww_missing_capability_contracts.py`
  - `path_glob`: `tools/test_validate_ww_missing_capability_contracts.py`
  - `path_glob`: `tools/validate_ww_repo.py`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `README.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-validator-expansion/dispatch-plan.md`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `candidate_persona_sources`:
  - project registry checked: true
  - built-in fallback checked: true
  - project registry outcome: project `senior-backend-engineer` is eligible, but built-in `test-quality-engineer` is a stronger match for fixture and validator dogfood analysis
  - built-in fallback outcome: use built-in `test-quality-engineer` as the audit specialist, with built-in reviewer lanes
  - fallback rationale when a built-in persona is recommended: validator fixture hardness and regression semantics are better covered by the built-in test-quality specialist than by the general project backend specialist
- `recommended_personas`:
  - `test-quality-engineer`
    - runtime role: worker
    - source: built-in
    - owned scope: audit the validator source, fixtures, JSON output, repo-suite integration, and false-positive/false-negative risks; produce the dogfood gap report
    - baseline fit rationale: this round is dominated by validator coverage, fixture design, and regression confidence rather than product, UI, or runtime implementation
    - project-priority or built-in-fallback rationale: built-in fallback is stronger than the available project specialist for test and fixture quality
    - enrichment fit rationale: the persona's evidence-first decision style and deterministic fixture preference directly match the dogfood audit risks
    - role binding: `worker` via `agents/worker-prompt.md`
    - workflow bindings: `superpowers:writing-plans`, `superpowers:verification-before-completion`
  - `spec-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: verify the gap report covers the requested audit dimensions and preserves all exclusions
    - baseline fit rationale: the audit report must answer the exact scope question and hardening decision
    - project-priority or built-in-fallback rationale: no project reviewer persona is stronger for requirement coverage
    - enrichment fit rationale: contract-first review fits coverage matrix validation
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`
  - `code-quality-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: review the audit's reasoning about validator false positives, false negatives, fixture isolation, and repo-suite behavior
    - baseline fit rationale: this audit assesses code/test quality without changing code
    - project-priority or built-in-fallback rationale: built-in reviewer-only persona is the strongest available code-quality lane
    - enrichment fit rationale: correctness-and-maintainability focus fits validator coverage risk
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`
  - `documentation-clarity-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: verify the gap report is clear, classifies gaps, and does not imply implementation or activation
    - baseline fit rationale: future hardening decisions depend on a readable source-of-truth report
    - project-priority or built-in-fallback rationale: built-in documentation clarity reviewer is the strongest available lane
    - enrichment fit rationale: reader-action-first style fits next-round recommendation clarity
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`
- `recommended_worker_mode_by_section`:
  - section-missing-capability-validator-followup-dogfood-audit: research-first
- `worker_mode_reasoning_by_section`:
  - section-missing-capability-validator-followup-dogfood-audit: inspect existing artifacts and classify evidence before drawing conclusions; do not implement fixes
- `goal_tuning_by_section`:
  - section-missing-capability-validator-followup-dogfood-audit: validation-biased
- `constraint_override_notes_by_section`:
  - section-missing-capability-validator-followup-dogfood-audit: any discovered validator improvement must be recorded as a future hardening item, not patched in this round
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - audit: `superpowers:verification-before-completion`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval for one serial dogfood audit section that produces `design-spec.md`

## Grill-Me Decision Log

No `grill-me` trigger is active for this round.

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-missing-capability-validator-followup-dogfood-audit: true
- `review_target_strategy`:
  - Review the produced `design-spec.md` gap report against the validator source, fixtures, repo-suite evidence, and user-requested coverage dimensions.
- `controller_semantics_notes`:
  - This round remains `lifecycle_protocol: legacy`.
  - The audit may discuss dormant missing-capability contract surfaces but must not render active missing-capability authority records in this round.
  - No packet creation is required for the dogfood audit.

## Rules

- Persist the working brief before dispatch-plan approval.
- Every writable file in `Planned Scope` must appear in `exclusive_write_scope`.
- No packet creation until the dispatch plan is approved.
- Do not modify validator, fixture, runtime, persona, routing, packet, repair/scoring/hook, or activation behavior in this round.
