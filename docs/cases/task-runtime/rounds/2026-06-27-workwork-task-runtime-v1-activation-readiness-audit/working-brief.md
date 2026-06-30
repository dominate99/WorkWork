# Working Brief: Task Runtime V1 Activation Readiness Audit

## Artifact Metadata

- `schema_version`: 2
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: task-runtime-v1-activation-readiness-audit
- `case_slug`: task-runtime
- `round_slug`: 2026-06-27-workwork-task-runtime-v1-activation-readiness-audit
- `case_root`: `docs/cases/task-runtime/`
- `round_root`: `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/`
- `created_at`: 2026-06-27
- `updated_at`: 2026-06-27
- `derived_from_user_request`: `$ww round: task-runtime-v1 activation readiness audit. Based on completed lifecycle foundation, verifier/lane authority foundation, validator expansion, and dogfood audit, audit what WorkWork still lacks before real task-runtime-v1 activation across contract, validator, runtime behavior, and dogfood evidence. Audit and classify only; do not implement activation, modify validators, add personas, or implement hooks/repair/scoring/command execution. Focus on lifecycle_phase authority, verifier lane authority, internal hooks, quality gates, worker/reviewer/verifier isolation, packet assembly, evidence freshness, close gates, what dormant contract is sufficient, and what must get design first. Produce an activation readiness gap report and decide whether the next round should be design, implementation foundation, or dogfood.`

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

- `goal`: audit WorkWork's readiness to activate `task-runtime-v1` by classifying sufficient dormant contract surfaces, missing design work, missing validators, missing runtime behavior, and missing dogfood evidence
- `artifact_type`: activation readiness gap report
- `relevant_context`:
  - Lifecycle foundation design and implementation introduced dormant `task-runtime-v1` lifecycle contract surfaces and kept ordinary rounds on `legacy`.
  - Verifier/lane authority design and implementation introduced dormant verifier authority, lane schema, evidence records, model capability profiles/floors/resolutions, and authority isolation rules.
  - Verifier/lane authority validator expansion added a repo-level dormant-contract sentinel.
  - Verifier/lane authority validator dogfood audit concluded the current validator is sufficient for dormant stage and that hardening should wait until activation becomes concrete or schema changes.
  - `task-runtime-lifecycle.md` says `task-runtime-v1` may be selected only after verifier authority, review/stale-target handling, repair/re-verification, score/blocker evaluation, close gates, and final human judgment are implemented, verified end-to-end, and approved.
  - `task-runtime-verification.md` explicitly says it does not define repair, scoring, hooks, or close gates.
  - `docs/cases/grill-me-inline-planning/` is an unrelated untracked local directory and is outside this round.
- `constraints`:
  - Audit and classify only.
  - Do not implement `task-runtime-v1` activation.
  - Do not modify validators, active contract, templates, packet contract, README, SKILL, or runtime code.
  - Do not add verifier personas or runtime bindings.
  - Do not implement internal hooks, repair, scoring, close gates, command execution, routing, secondary tags, or project registry changes.
  - Do not convert any current round to `task-runtime-v1`.

## Risk And Structure

- `risk_lenses`:
  - mistaking dormant contracts for activation readiness
  - treating validator sentinel coverage as runtime behavior
  - missing the gap between packet contract fields and actual packet assembly/runtime binding
  - underestimating freshness, wrong-target, stale review, and re-verification requirements
  - conflating internal hooks/quality gates with implemented controller behavior
  - recommending implementation before missing design contracts are settled
- `parallelism_assessment`:
  - Use one serial audit section because readiness depends on cross-cutting comparison among lifecycle, verification, packet, validator, hook, scoring, and close-gate surfaces.
- `blocking_dependencies`:
  - committed lifecycle foundation rounds
  - committed verifier/lane authority design and implementation foundation
  - committed verifier authority validator expansion and dogfood audit
  - current dormant task-runtime references and templates
- `section_or_workstream_map`:
  - section-task-runtime-v1-readiness-audit: inspect existing dormant contracts and dogfood evidence, classify readiness by activation capability, and recommend the next round type

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: activation_readiness_report
    - `artifact_kind`: design_spec
    - `artifact_path`: `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/design-spec.md`
    - `section_anchors`: readiness matrix, activation blockers, sufficient dormant surfaces, missing design, missing validator/runtime/dogfood evidence, next-round recommendation
  - `artifact_id`: task_runtime_lifecycle_reference
    - `artifact_kind`: reference_doc
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
    - `section_anchors`: activation boundary, lifecycle_phase authority, phase/runtime compatibility, event model, close conditions
  - `artifact_id`: task_runtime_verification_reference
    - `artifact_kind`: reference_doc
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
    - `section_anchors`: verifier authority, evidence records, freshness, isolation, model capability, non-defined repair/scoring/hooks/close gates
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/task-runtime/case.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/working-brief.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/dispatch-plan.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/design-spec.md`
- `shared_read_scope`:
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `path_glob`: `tools/validate_ww_repo.py`
  - `path_glob`: `tools/validate_ww_round_lifecycle.py`
  - `path_glob`: `tools/validate_ww_verifier_authority_contracts.py`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-19-task-runtime-lifecycle-foundation-design/**/*`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/**/*`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-21-verifier-and-lane-authority-design/**/*`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-24-verifier-lane-authority-implementation-foundation/**/*`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-25-verifier-lane-authority-validator-expansion/**/*`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-27-verifier-lane-authority-validator-dogfood-audit/**/*`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `candidate_persona_sources`:
  - project registry checked: true
  - built-in fallback checked: true
  - project registry outcome: no eligible project persona is available for WorkWork task-runtime activation readiness auditing
  - built-in fallback outcome: use `senior-backend-engineer` for readiness audit classification, with `spec-reviewer`, `code-quality-reviewer`, and `documentation-clarity-reviewer` as review lanes
  - fallback rationale when a built-in persona is recommended: this is portable WorkWork contract/runtime readiness analysis rather than product-specific behavior
- `recommended_personas`:
  - `senior-backend-engineer`
    - runtime role: worker
    - source: built-in
    - owned scope: audit activation readiness across dormant contract, validator, runtime behavior, and dogfood evidence
    - baseline fit rationale: activation readiness crosses controller semantics, validator boundaries, packet assembly, and runtime behavior
    - project-priority or built-in-fallback rationale: no stronger eligible project worker persona covers WorkWork runtime readiness analysis
    - role binding: `worker` via `agents/worker-prompt.md`
    - workflow bindings: `superpowers:writing-plans`, `superpowers:verification-before-completion`
  - `spec-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: verify that every requested readiness surface is classified and exclusions are preserved
    - baseline fit rationale: readiness audit must match activation boundary and user-requested scope
    - project-priority or built-in-fallback rationale: no stronger eligible project reviewer covers WorkWork task-runtime spec fidelity
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
  - `code-quality-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: inspect runtime/validator feasibility reasoning and next-round recommendation
    - baseline fit rationale: activation planning must not skip runtime or validator prerequisites
    - project-priority or built-in-fallback rationale: no stronger eligible project reviewer covers WorkWork controller implementation readiness
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
  - `documentation-clarity-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: verify the readiness report is actionable and clearly separates design, implementation, validator, and dogfood gaps
    - baseline fit rationale: the output guides the next WorkWork round sequence
    - project-priority or built-in-fallback rationale: no stronger eligible project reviewer covers readiness report clarity
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
- `recommended_worker_mode_by_section`:
  - section-task-runtime-v1-readiness-audit: research-first
- `worker_mode_reasoning_by_section`:
  - section-task-runtime-v1-readiness-audit: inspect existing contracts and evidence before recommending whether the next round is design, implementation foundation, or dogfood.
- `goal_tuning_by_section`:
  - section-task-runtime-v1-readiness-audit: validation-biased
- `constraint_override_notes_by_section`:
  - section-task-runtime-v1-readiness-audit: any implementation or validator change discovered by the audit must be deferred to a later approved round.
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - audit execution: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval for one serial readiness audit section that produces `design-spec.md` as the activation readiness gap report

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-task-runtime-v1-readiness-audit: true
- `review_target_strategy`:
  - Freeze the activation readiness report artifact before review; reviewers inspect the report against lifecycle, verifier, packet, validator, and prior dogfood evidence.
- `controller_semantics_notes`:
  - This round remains `lifecycle_protocol: legacy`.
  - The audit may recommend later design or implementation work but must not implement it.
  - `task-runtime-v1` remains dormant and must not be selected by this round.

## Rules

- Persist the working brief before dispatch-plan creation.
- Every writable file in `Planned Scope` must appear in `exclusive_write_scope`.
- No packet creation until the dispatch plan is approved.
- The readiness report must separate sufficient dormant contract, missing design, missing implementation/runtime, missing validator, and missing dogfood evidence.
