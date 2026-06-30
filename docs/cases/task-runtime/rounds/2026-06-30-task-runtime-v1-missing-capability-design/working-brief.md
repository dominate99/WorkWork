# Working Brief: Task Runtime V1 Missing Capability Design

## Artifact Metadata

- `schema_version`: 2
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: task-runtime-v1-missing-capability-design
- `case_slug`: task-runtime
- `round_slug`: 2026-06-30-task-runtime-v1-missing-capability-design
- `case_root`: `docs/cases/task-runtime/`
- `round_root`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/`
- `created_at`: 2026-06-30
- `updated_at`: 2026-06-30
- `derived_from_user_request`: `$ww round: task-runtime-v1 missing capability design. Based on the activation readiness audit, design the dormant contracts still required before task-runtime-v1 activation: internal hooks, quality gates/scoring, repair authorization/re-verification, close gates, final human judgment, and their relationship to lifecycle events and verifier evidence. Only produce design spec; do not implement activation, modify validators, add personas, add runtime binding, implement command execution, routing, or packet assembly.`

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

- `goal`: design the missing dormant task-runtime-v1 capability contracts needed before activation work can proceed
- `artifact_type`: design_spec
- `relevant_context`:
  - The approved activation readiness audit concluded WorkWork is not ready to activate `task-runtime-v1`.
  - Existing dormant lifecycle and verifier authority references are sufficient foundations, but hooks, quality gates/scoring, repair/re-verification, close gates, and final human judgment are still missing design contracts.
  - `task-runtime-lifecycle.md` already defines phase vocabulary, orchestrator-owned phase transitions, snapshots, event persistence, and the activation boundary.
  - `task-runtime-verification.md` defines verifier authority, lane schema, target identity, evidence freshness, and model capability resolution, but explicitly does not define repair, scoring, hooks, or close gates.
  - This round must design how the missing surfaces relate to lifecycle events and verifier evidence without activating the runtime.
- `constraints`:
  - Produce only a round-local design spec.
  - Do not implement `task-runtime-v1` activation.
  - Do not modify validators, active contract references, templates, packet contract, README, SKILL, runtime code, persona files, project registry, routing, command execution, or packet assembly.
  - Do not add verifier personas or runtime bindings.
  - Keep this round on `Lifecycle Protocol: legacy`.

## Risk And Structure

- `risk_lenses`:
  - designing hooks that accidentally imply system daemon behavior instead of invocation-scoped WorkWork guards
  - allowing quality scores to bypass hard blockers such as missing verification or unresolved critical findings
  - allowing repair to reuse stale verification or review evidence
  - confusing final human judgment with automated close approval
  - defining contract records too vaguely for later validator implementation
  - drifting into runtime implementation or validator changes before contract shape is approved
- `parallelism_assessment`:
  - Use one serial design section because hooks, scoring, repair, close, lifecycle events, and verifier evidence must be mutually consistent.
- `blocking_dependencies`:
  - approved lifecycle foundation
  - approved verifier/lane authority foundation
  - approved activation readiness audit
- `section_or_workstream_map`:
  - section-missing-capability-design: produce a design spec for dormant hooks, quality gates/scoring, repair/re-verification, close gates, final human judgment, and their relationship to lifecycle events and verifier evidence

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: missing_capability_design_spec
    - `artifact_kind`: design_spec
    - `artifact_path`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/design-spec.md`
    - `section_anchors`: internal hooks, quality gates, scoring, repair authorization, re-verification, close gates, final judgment, lifecycle event integration, verifier evidence integration, future validator implications
  - `artifact_id`: activation_readiness_audit
    - `artifact_kind`: design_spec
    - `artifact_path`: `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/design-spec.md`
    - `section_anchors`: blocking activation gaps and next-round recommendation
  - `artifact_id`: task_runtime_lifecycle_reference
    - `artifact_kind`: reference_doc
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
    - `section_anchors`: activation boundary, lifecycle events, phase/runtime compatibility, score and close transitions
  - `artifact_id`: task_runtime_verification_reference
    - `artifact_kind`: reference_doc
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
    - `section_anchors`: verifier evidence, freshness, non-pass evidence, re-verification constraints
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/task-runtime/case.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/working-brief.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/dispatch-plan.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-30-task-runtime-v1-missing-capability-design/design-spec.md`
- `shared_read_scope`:
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-27-workwork-task-runtime-v1-activation-readiness-audit/design-spec.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `path_glob`: `tools/validate_ww_round_lifecycle.py`
  - `path_glob`: `tools/validate_ww_repo.py`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `candidate_persona_sources`:
  - project registry checked: true
  - built-in fallback checked: true
  - project registry outcome: use project `senior-backend-engineer` as worker-capable specialist because this design affects service-like controller semantics, state machines, and correctness contracts
  - built-in fallback outcome: use built-in `spec-reviewer`, `code-quality-reviewer`, and `documentation-clarity-reviewer` as reviewer lanes
  - fallback rationale when a built-in persona is recommended: no project reviewer persona covers WorkWork runtime contract fidelity more specifically than the built-in reviewer lanes
- `recommended_personas`:
  - `senior-backend-engineer`
    - runtime role: worker
    - source: project
    - owned scope: design missing task-runtime-v1 capability contracts and keep them compatible with lifecycle/verifier authority
    - baseline fit rationale: this is controller/state-machine contract design with correctness and integration risk
    - project-priority or built-in-fallback rationale: project registry provides an eligible senior backend specialist with matching architecture/correctness strengths
    - role binding: `worker` via `agents/worker-prompt.md`
    - workflow bindings: `superpowers:writing-plans`, `superpowers:verification-before-completion`
  - `spec-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: verify every requested missing capability is designed and all exclusions are preserved
    - baseline fit rationale: the design must satisfy the user request and activation readiness findings
    - project-priority or built-in-fallback rationale: built-in fallback provides the strongest available spec-focused reviewer
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
  - `code-quality-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: inspect controller feasibility, state ownership, validator-readiness, and lifecycle/verifier consistency
    - baseline fit rationale: the design will drive later implementation and validation work
    - project-priority or built-in-fallback rationale: built-in fallback provides the strongest available runtime-contract reviewer
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
  - `documentation-clarity-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: verify that the design spec is actionable for a later implementation foundation round
    - baseline fit rationale: the output must clearly separate contract, runtime, validator, and dogfood implications
    - project-priority or built-in-fallback rationale: built-in fallback provides the strongest available documentation clarity reviewer
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
- `recommended_worker_mode_by_section`:
  - section-missing-capability-design: research-first
- `worker_mode_reasoning_by_section`:
  - section-missing-capability-design: existing lifecycle/verifier contracts must constrain the new dormant design before any new record shapes are proposed.
- `goal_tuning_by_section`:
  - section-missing-capability-design: validation-biased
- `constraint_override_notes_by_section`:
  - section-missing-capability-design: any implementation, validator, template, runtime binding, persona, routing, command execution, or packet assembly idea must be recorded as future work only.
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - design execution: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval for one serial design section that produces `design-spec.md`

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-missing-capability-design: true
- `review_target_strategy`:
  - Freeze the design spec before review; reviewers inspect it against the user request, activation readiness audit, lifecycle reference, and verifier reference.
- `controller_semantics_notes`:
  - This round remains `lifecycle_protocol: legacy`.
  - The design may define dormant future `task-runtime-v1` contracts, but the dispatch plan must not render active lifecycle snapshots, verifier lanes, hook records, score records, repair records, or close-gate authority.
  - `task-runtime-v1` remains dormant and must not be selected by this round.

## Rules

- Persist the working brief before dispatch-plan creation.
- Every writable file in `Planned Scope` must appear in `exclusive_write_scope`.
- No packet creation until the dispatch plan is approved.
- The design spec must define missing dormant contract surfaces without implementing or activating them.
