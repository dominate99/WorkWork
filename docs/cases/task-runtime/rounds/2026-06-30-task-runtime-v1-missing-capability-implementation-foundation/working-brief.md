# Working Brief: Task Runtime V1 Missing Capability Implementation Foundation

## Artifact Metadata

- `schema_version`: 2
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: task-runtime-v1-missing-capability-implementation-foundation
- `case_slug`: task-runtime
- `round_slug`: 2026-06-30-task-runtime-v1-missing-capability-implementation-foundation
- `case_root`: `docs/cases/task-runtime/`
- `round_root`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-implementation-foundation/`
- `created_at`: 2026-06-30
- `updated_at`: 2026-06-30
- `derived_from_user_request`: `$ww round: task-runtime-v1 missing capability implementation foundation. Based on the approved missing capability design, land dormant contracts for internal hooks, quality gates/scoring, repair authorization/re-verification, close gates, final human judgment, recovery/checkpoint records into WorkWork active references, templates, and docs guidance. Sync SKILL.md, README, dispatch-plan-template, working-brief-template, subagent-packet-contract, or related references. Contract/template/docs implementation only; do not activate task-runtime-v1, modify validators, add personas, add runtime binding, implement command execution, routing, or packet assembly.`

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

- `goal`: implement the approved missing-capability design as dormant WorkWork contract/template/docs surfaces without activating runtime behavior
- `artifact_type`: contract_docs_implementation
- `relevant_context`:
  - The approved missing capability design defines dormant record families for internal hooks, quality gates/scoring, repair authorization/re-verification, close gates, final human judgment, recovery requirements, and checkpoints.
  - The design says the next round should copy those approved dormant contracts into active WorkWork references, templates, and user-facing guidance without activating runtime behavior.
  - Existing `task-runtime-lifecycle.md` and `task-runtime-verification.md` already define lifecycle and verifier authority foundations.
  - This round should make the missing capability surfaces discoverable from SKILL/README/templates/references while preserving the `legacy` default and activation boundary.
- `constraints`:
  - Contract/template/docs implementation only.
  - Do not activate `task-runtime-v1`.
  - Do not modify validators or tests.
  - Do not add personas, verifier runtime binding, command execution, routing, or packet assembly.
  - Do not change project registry.
  - Do not make legacy rounds render active hook, score, repair, close, final judgment, recovery, or checkpoint authority.

## Risk And Structure

- `risk_lenses`:
  - accidentally making dormant records mandatory for legacy rounds
  - weakening the activation boundary by implying `task-runtime-v1` can now launch
  - duplicating lifecycle or verifier authority in a new reference
  - spreading contradictory field names across SKILL, templates, and references
  - over-editing validator/runtime files that are explicitly out of scope
  - failing to give future validator rounds concrete anchor text
- `parallelism_assessment`:
  - Use one serial implementation section because SKILL, README, templates, packet contract, and references must stay internally consistent.
- `blocking_dependencies`:
  - approved task-runtime lifecycle foundation
  - approved verifier/lane authority foundation
  - approved missing capability design
- `section_or_workstream_map`:
  - section-missing-capability-implementation-foundation: update active WorkWork references, templates, and docs guidance for the dormant missing capability contracts

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: missing_capability_design
    - `artifact_kind`: design_spec
    - `artifact_path`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/design-spec.md`
    - `section_anchors`: dormant record families, hooks, quality gates, scoring, repair, re-verification, close gates, final judgment, recovery, checkpoints, lifecycle event integration, verifier evidence integration
  - `artifact_id`: missing_capability_reference
    - `artifact_kind`: reference_doc
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`
    - `section_anchors`: dormant hooks, gate records, score records, repair records, close records, final judgment, recovery, checkpointing, non-authority rules
  - `artifact_id`: dispatch_template
    - `artifact_kind`: template
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `section_anchors`: task-runtime-v1 only missing capability blocks and legacy omission guidance
  - `artifact_id`: working_brief_template
    - `artifact_kind`: template
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `section_anchors`: missing capability preparation guidance
  - `artifact_id`: packet_contract
    - `artifact_kind`: reference_doc
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `section_anchors`: dormant packet relationship and non-activation note
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/task-runtime/case.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-implementation-foundation/working-brief.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-implementation-foundation/dispatch-plan.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `README.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`
- `shared_read_scope`:
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/design-spec.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/dispatch-plan.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/design-spec.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
  - `path_glob`: `tools/validate_ww_round_lifecycle.py`
  - `path_glob`: `tools/validate_ww_repo.py`
  - `path_glob`: `tools/validate_ww_verifier_authority_contracts.py`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `candidate_persona_sources`:
  - project registry checked: true
  - built-in fallback checked: true
  - project registry outcome: use project `senior-backend-engineer` as worker-capable specialist because this implementation changes controller contracts, docs, and templates with state-machine risk
  - built-in fallback outcome: use built-in `spec-reviewer`, `code-quality-reviewer`, and `documentation-clarity-reviewer` as reviewer lanes
  - fallback rationale when a built-in persona is recommended: no project reviewer persona covers WorkWork contract/template fidelity more specifically than the built-in reviewer lanes
- `recommended_personas`:
  - `senior-backend-engineer`
    - runtime role: worker
    - source: project
    - owned scope: implement dormant missing capability contracts across active WorkWork references, templates, and docs guidance
    - baseline fit rationale: this is controller/state-machine contract implementation with correctness and integration risk
    - project-priority or built-in-fallback rationale: project registry provides an eligible senior backend specialist with architecture and maintainability strengths
    - role binding: `worker` via `agents/worker-prompt.md`
    - workflow bindings: `superpowers:test-driven-development`, `superpowers:verification-before-completion`
  - `spec-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: verify implementation faithfully reflects the approved missing capability design and preserves exclusions
    - baseline fit rationale: the contract implementation must match the approved design and user scope
    - project-priority or built-in-fallback rationale: built-in fallback provides the strongest available spec-focused reviewer
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
  - `code-quality-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: inspect contract/template consistency, lifecycle/verifier authority boundaries, and validator-readiness
    - baseline fit rationale: later validators will rely on stable, unambiguous contract anchors
    - project-priority or built-in-fallback rationale: built-in fallback provides the strongest available runtime-contract reviewer
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
  - `documentation-clarity-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: verify user-facing and maintainer-facing guidance is coherent and avoids activation ambiguity
    - baseline fit rationale: dormant capability guidance must be easy to follow in future rounds
    - project-priority or built-in-fallback rationale: built-in fallback provides the strongest available documentation clarity reviewer
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
- `recommended_worker_mode_by_section`:
  - section-missing-capability-implementation-foundation: test-driven
- `worker_mode_reasoning_by_section`:
  - section-missing-capability-implementation-foundation: make contract/template/docs changes, then validate the repository suite; do not add new validator tests in this round.
- `goal_tuning_by_section`:
  - section-missing-capability-implementation-foundation: validation-biased
- `constraint_override_notes_by_section`:
  - section-missing-capability-implementation-foundation: any validator, runtime behavior, persona, routing, binding, command execution, or packet assembly change must be deferred.
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - implementation: `superpowers:test-driven-development`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval for one serial contract/template/docs implementation section

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-missing-capability-implementation-foundation: true
- `review_target_strategy`:
  - Freeze the modified contract/template/docs set before review; reviewers inspect against the approved design and scope exclusions.
- `controller_semantics_notes`:
  - This round remains `lifecycle_protocol: legacy`.
  - The implementation may add dormant `task-runtime-v1` reference/template surfaces, but must not render active hook, score, repair, close, judgment, recovery, or checkpoint records in legacy rounds.
  - `task-runtime-v1` remains dormant and must not be selected by this round.

## Rules

- Persist the working brief before dispatch-plan creation.
- Every writable file in `Planned Scope` must appear in `exclusive_write_scope`.
- No packet creation until the dispatch plan is approved.
- The implementation must preserve legacy non-authority boundaries and activation gating.
