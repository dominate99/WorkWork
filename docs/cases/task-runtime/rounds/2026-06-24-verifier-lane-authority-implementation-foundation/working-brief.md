# Working Brief: Verifier Lane Authority Implementation Foundation

## Artifact Metadata

- `schema_version`: 2
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: verifier-lane-authority-implementation-foundation
- `case_slug`: task-runtime
- `round_slug`: 2026-06-24-verifier-lane-authority-implementation-foundation
- `case_root`: `docs/cases/task-runtime/`
- `round_root`: `docs/cases/task-runtime/rounds/2026-06-24-verifier-lane-authority-implementation-foundation/`
- `created_at`: 2026-06-24
- `updated_at`: 2026-06-24
- `derived_from_user_request`: `$ww round: verifier and lane authority implementation foundation. Based on the approved verifier and lane authority design, implement the dormant contract for verifier authority, lane schema, evidence records, baseline/risk-triggered lane selection, and model capability profile/floor/resolution across WorkWork active contract, templates, and docs. Only contract/template/docs implementation; do not add verifier personas, verifier runtime binding, command execution, repair/scoring/hooks, or activate task-runtime-v1. Sync SKILL.md, README, dispatch/working brief/packet contract or related references.`

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

- `goal`: implement the approved verifier and lane authority design as dormant WorkWork contract, template, and documentation surfaces without activating runtime behavior
- `artifact_type`: contract, template, and documentation implementation
- `relevant_context`:
  - Approved source design: `docs/cases/task-runtime/rounds/2026-06-21-verifier-and-lane-authority-design/design-spec.md`, revision 15.
  - Lifecycle foundation contract is already present as dormant active contract material and remains the base layer for this round.
  - Current WorkWork active contract already has persona selection, packet, lifecycle, and review-lane persistence surfaces that must remain compatible.
  - The worktree contains prior task-runtime/lifecycle changes; this round must work with those files and avoid reverting unrelated edits.
  - `task-runtime-v1` remains inactive; this round only makes future verifier/lane authority fields legible and durable.
- `constraints`:
  - Implement only dormant contract, template, and documentation changes.
  - Add no verifier persona and no verifier runtime binding.
  - Do not implement command execution, command runners, verifier packet launch, repair policy, scoring, hooks, or runtime activation.
  - Do not expand routing, project registry, or secondary tags.
  - Do not change validator behavior in this round.
  - Preserve existing worker/reviewer/persona authority rules and existing lifecycle ownership.
  - Keep verifier fields explicitly non-authoritative for legacy rounds unless a later approved activation round enables `task-runtime-v1`.
  - Keep model capability profile/floor/resolution separate from persona identity and provider/model-name bindings.

## Risk And Structure

- `risk_lenses`:
  - dormant verifier fields accidentally becoming active lifecycle authority
  - docs implying workers or reviewers can self-verify or self-approve
  - packet contract adding verifier-like fields without preserving runtime role isolation
  - template/schema text diverging from the approved revision 15 design
  - model profile/floor text collapsing into hard-coded model names or silent fallback permission
  - adding validator/runtime behavior before the contract is approved and dogfooded
- `parallelism_assessment`:
  - Use one serial implementation section because SKILL, README, references, templates, and packet contract must agree on the same dormant terminology.
- `blocking_dependencies`:
  - approved verifier and lane authority design revision 15
  - lifecycle foundation active contract and reference
  - current persona selection and packet contract rules
- `section_or_workstream_map`:
  - section-verifier-lane-authority-contract-foundation: update active contract, references, templates, and docs with dormant verifier/lane authority records

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: verifier_lane_authority_contract_foundation
    - `artifact_kind`: contract_docs
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
    - `section_anchors`: verifier authority, lane schema, evidence records, lane selection, model capability profiles
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/task-runtime/case.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-24-verifier-lane-authority-implementation-foundation/working-brief.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-24-verifier-lane-authority-implementation-foundation/dispatch-plan.md`
  - `path_glob`: `README.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
- `shared_read_scope`:
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-21-verifier-and-lane-authority-design/design-spec.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-19-task-runtime-lifecycle-foundation-design/**/*`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/**/*`
  - `path_glob`: `docs/superpowers/specs/2026-06-19-workwork-task-runtime-design.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `path_glob`: `docs/superpowers/personas/registry.yaml`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `candidate_persona_sources`:
  - project registry checked: true
  - built-in fallback checked: true
  - project registry outcome: no eligible project worker or reviewer persona covers portable WorkWork verifier contract implementation more strongly than the built-in specialists
  - built-in fallback outcome: use `senior-backend-engineer` for contract/template implementation, `spec-reviewer` for approved-design fidelity, `code-quality-reviewer` for repo/template consistency, and `documentation-clarity-reviewer` for reader/actionability review
  - fallback rationale when a built-in persona is recommended: this is portable WorkWork skill contract work rather than project-specific app behavior
- `recommended_personas`:
  - `senior-backend-engineer`
    - runtime role: worker
    - source: built-in
    - owned scope: implement dormant verifier authority, lane schema, evidence, lane selection, and model capability profile contract surfaces
    - baseline fit rationale: the work defines durable runtime interfaces and schema-like template fields across active contract documents
    - project-priority or built-in-fallback rationale: no stronger eligible project worker persona owns portable WorkWork runtime contracts
    - role binding: `worker` via `agents/worker-prompt.md`
    - workflow bindings: `superpowers:writing-plans`, `superpowers:verification-before-completion`
  - `spec-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: compare implemented contract surfaces against approved design revision 15 and explicit exclusions
    - baseline fit rationale: the target is contract implementation fidelity
    - project-priority or built-in-fallback rationale: no stronger eligible project reviewer covers portable WorkWork specification fidelity
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
  - `code-quality-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: review template consistency, naming, path scope, and validator compatibility risk without changing validators
    - baseline fit rationale: contract and template edits can break repository validation or downstream packet assembly
    - project-priority or built-in-fallback rationale: no stronger eligible project reviewer covers WorkWork template/code-quality consistency
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
  - `documentation-clarity-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: review README/SKILL/reference clarity for dormant verifier concepts and future activation boundaries
    - baseline fit rationale: this round changes user-facing and maintainer-facing guidance
    - project-priority or built-in-fallback rationale: no stronger eligible project reviewer covers WorkWork procedural documentation clarity
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
- `recommended_worker_mode_by_section`:
  - section-verifier-lane-authority-contract-foundation: contract-first
- `worker_mode_reasoning_by_section`:
  - section-verifier-lane-authority-contract-foundation: approved design already fixes the conceptual shape; implementation should preserve the contract before polishing prose.
- `goal_tuning_by_section`:
  - section-verifier-lane-authority-contract-foundation: validation-biased
- `constraint_override_notes_by_section`:
  - section-verifier-lane-authority-contract-foundation: any verifier persona, runtime binding, validator enforcement, command execution, repair, scoring, hook, routing expansion, or task-runtime-v1 activation is out of scope.
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - implementation: `superpowers:verification-before-completion`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval for one serial contract implementation section, then update the named active contract/template/docs files and run repository validation

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-verifier-lane-authority-contract-foundation: true
- `review_target_strategy`:
  - Freeze the full active-contract diff plus the new verifier reference as the review target after implementation.
- `controller_semantics_notes`:
  - This implementation round remains `lifecycle_protocol: legacy`.
  - Dormant verifier and lane fields are documentation/template contract surfaces only.
  - No verifier packet, command execution, runtime binding, repair, scoring, hooks, or task-runtime-v1 activation may occur in this round.

## Rules

- Persist the working brief before dispatch-plan creation.
- Persona selection must cite source, runtime role, and built-in fallback rationale.
- Every writable file in `Planned Scope` must appear in `exclusive_write_scope`.
- No packet creation until the dispatch plan is approved.
