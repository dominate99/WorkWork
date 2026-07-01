# Working Brief: Task Runtime V1 Activation Gate Validator Design

## Artifact Metadata

- `schema_version`: 2
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: task-runtime-v1-activation-gate-validator-design
- `case_slug`: task-runtime
- `round_slug`: 2026-07-01-task-runtime-v1-activation-gate-validator-design
- `case_root`: `docs/cases/task-runtime/`
- `round_root`: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/`
- `created_at`: 2026-07-01
- `updated_at`: 2026-07-01
- `derived_from_user_request`: `$ww round: task-runtime-v1 activation gate validator design. Based on lifecycle foundation, verifier/lane authority foundation, missing capability foundation, and the completed WWMC007 hardening, design a unified pre-activation gate validator for task-runtime-v1. Produce only a design spec; do not implement the validator, change contracts, add personas, add runtime binding, implement command execution/routing/packet assembly/repair/scoring/hooks. Focus on which dormant contract surfaces must be satisfied together, which legacy non-authority guards must remain, which validator suites must exist before activation, and which evidence can prove verifier evidence, missing-capability close gates, worker/reviewer/verifier isolation, and lifecycle_phase authority are sufficient to enter an activation round.`

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

- `goal`: design the unified validator gate WorkWork must pass before it can start a real `task-runtime-v1` activation round
- `artifact_type`: design_spec
- `relevant_context`:
  - Lifecycle foundation defines dormant lifecycle ownership, phase authority, and legacy non-authority boundaries.
  - Verifier/lane authority foundation defines dormant verifier lane schema, evidence records, model capability profile/floor/resolution, and verifier isolation boundaries.
  - Missing capability foundation defines dormant internal hook, quality gate/scoring, repair/re-verification, close gate, final judgment, recovery, and checkpoint contracts.
  - WWMC007 hardening now rejects YAML-like active missing-capability record-family assignments in legacy dispatch plans while allowing dormant prose.
  - Existing repo validation has separate suites for lifecycle, verifier/lane authority, missing capability, persona selection, packet artifacts, case artifacts, and round lifecycle; this round should design the activation-level aggregator and evidence thresholds, not implement it.
- `constraints`:
  - Produce only `design-spec.md`.
  - Do not implement a validator or tests in this round.
  - Do not change active contracts, dormant references, templates, README, SKILL, personas, project registry, routing, packet assembly, runtime binding, command execution, repair/scoring/hooks, or activation behavior.
  - Preserve `Lifecycle Protocol: legacy`.
  - Keep any future field examples descriptive or quoted; this legacy dispatch plan must not render dormant verifier or missing-capability fields as active authority.

## Risk And Structure

- `risk_lenses`:
  - activation gate could become too broad and duplicate every existing validator instead of orchestrating their results
  - activation gate could become too narrow and miss required cross-suite evidence, especially worker/reviewer/verifier isolation and close-gate readiness
  - design could accidentally imply `task-runtime-v1` is active because dormant contracts pass
  - evidence requirements might confuse contract existence with runtime behavior
  - validator design must preserve legacy non-authority guards while defining a path to activation readiness
- `parallelism_assessment`:
  - Use one serial design section because the gate boundaries depend on a single cross-suite synthesis.
- `blocking_dependencies`:
  - lifecycle foundation and validator rounds in `docs/cases/task-runtime/rounds/`
  - verifier/lane authority foundation and validator rounds
  - missing capability foundation, validator expansion, dogfood audit, and WWMC007 hardening
  - current validator sources under `tools/`
- `section_or_workstream_map`:
  - section-activation-gate-validator-design: synthesize the activation gate validator design and acceptance evidence into `design-spec.md`

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: activation_gate_design_spec
    - `artifact_kind`: design_spec
    - `artifact_path`: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/design-spec.md`
    - `section_anchors`: gate purpose, prerequisite surfaces, suite inventory, cross-suite evidence, non-authority guards, activation entry criteria
  - `artifact_id`: lifecycle_contract_reference
    - `artifact_kind`: reference_doc
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
    - `section_anchors`: lifecycle owner, phase authority, legacy non-authority
  - `artifact_id`: verifier_contract_reference
    - `artifact_kind`: reference_doc
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
    - `section_anchors`: verifier lanes, evidence records, model capability floor, isolation
  - `artifact_id`: missing_capability_contract_reference
    - `artifact_kind`: reference_doc
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`
    - `section_anchors`: hooks, gates, scoring, repair, close, final judgment, recovery, checkpoint
  - `artifact_id`: wwmc007_hardening_round
    - `artifact_kind`: completed_round
    - `artifact_path`: `docs/cases/task-runtime/rounds/2026-07-01-missing-capability-legacy-guard-validator-hardening/dispatch-plan.md`
    - `section_anchors`: approved WWMC007 hardening evidence
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/task-runtime/case.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/working-brief.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/dispatch-plan.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-07-01-task-runtime-v1-activation-gate-validator-design/design-spec.md`
- `shared_read_scope`:
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `README.md`
  - `path_glob`: `tools/validate_ww_round_lifecycle.py`
  - `path_glob`: `tools/validate_ww_verifier_authority_contracts.py`
  - `path_glob`: `tools/validate_ww_missing_capability_contracts.py`
  - `path_glob`: `tools/validate_ww_repo.py`
  - `path_glob`: `docs/cases/task-runtime/rounds/**`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `candidate_persona_sources`:
  - project registry checked: true
  - built-in fallback checked: true
  - project registry outcome: project `senior-backend-engineer` is eligible for validator architecture review, but built-in `test-quality-engineer` is stronger for validator gate and evidence design
  - built-in fallback outcome: use built-in `test-quality-engineer` as the design worker, with spec/code-quality/documentation review lanes
  - fallback rationale when a built-in persona is recommended: this round designs validator evidence boundaries and false-positive/false-negative prevention rather than implementing backend behavior
- `recommended_personas`:
  - `test-quality-engineer`
    - runtime role: worker
    - source: built-in
    - owned scope: design the activation gate validator's suite inventory, cross-suite evidence rules, failure classes, and pre-activation acceptance criteria
    - baseline fit rationale: validator design is dominated by regression evidence, suite composition, and activation guard semantics
    - project-priority or built-in-fallback rationale: built-in fallback is stronger than the available project specialist for test and validation architecture
    - enrichment fit rationale: evidence-first decision style fits activation gate design
    - role binding: `worker` via `agents/worker-prompt.md`
    - workflow bindings: `superpowers:writing-plans`, `superpowers:verification-before-completion`
  - `spec-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: confirm the design spec covers all requested activation-gate surfaces and exclusions
    - baseline fit rationale: requirement coverage is the primary acceptance risk
    - project-priority or built-in-fallback rationale: no project reviewer is stronger for contract completeness
    - enrichment fit rationale: contract-first review fits dormant/activation boundary design
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`
  - `code-quality-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: review whether the proposed validator design is implementable, maintainable, and avoids overbroad/underbroad checks
    - baseline fit rationale: the future validator must compose existing suites without fragile duplication
    - project-priority or built-in-fallback rationale: built-in reviewer-only persona best matches code-quality review
    - enrichment fit rationale: maintainability and correctness focus fit activation-gate design risk
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`
  - `documentation-clarity-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: ensure the design spec is usable as the source for later implementation without implying activation
    - baseline fit rationale: future implementers need crisp gate definitions and evidence vocabulary
    - project-priority or built-in-fallback rationale: built-in documentation clarity reviewer is the strongest fit for source-of-truth readability
    - enrichment fit rationale: reader-action-first review prevents ambiguous activation claims
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`
- `recommended_worker_mode_by_section`:
  - section-activation-gate-validator-design: research-first
- `worker_mode_reasoning_by_section`:
  - section-activation-gate-validator-design: inspect completed dormant contracts and validators before writing the activation gate design
- `goal_tuning_by_section`:
  - section-activation-gate-validator-design: validation-biased
- `constraint_override_notes_by_section`:
  - section-activation-gate-validator-design: do not implement the validator or alter any contract while designing the activation gate
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning/design: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval for one serial design section that creates `design-spec.md`

## Grill-Me Decision Log

No `grill-me` trigger is active for this round.

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-activation-gate-validator-design: true
- `review_target_strategy`:
  - Review the produced `design-spec.md` against the user request, existing dormant contracts, current validators, and activation readiness evidence needs.
- `controller_semantics_notes`:
  - This round remains `lifecycle_protocol: legacy`.
  - The design may name future `task-runtime-v1` authority surfaces, but this round must not activate them or render their authority records in the dispatch plan.
  - No packet creation is required before dispatch plan approval.

## Rules

- Persist the working brief before dispatch-plan approval.
- Every writable file in `Planned Scope` must appear in `exclusive_write_scope`.
- No packet creation until the dispatch plan is approved.
- Produce only `design-spec.md` after approval; no validator implementation in this round.
