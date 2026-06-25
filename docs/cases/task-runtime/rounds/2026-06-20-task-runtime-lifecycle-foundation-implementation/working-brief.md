# Working Brief: Task Runtime Lifecycle Foundation Implementation

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 2
- `brief_status`: ready
- `topic_slug`: task-runtime-lifecycle-foundation-implementation
- `case_slug`: task-runtime
- `round_slug`: 2026-06-20-task-runtime-lifecycle-foundation-implementation
- `case_root`: `docs/cases/task-runtime/`
- `round_root`: `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/`
- `created_at`: 2026-06-20
- `updated_at`: 2026-06-20
- `derived_from_user_request`: `下一轮：Lifecycle foundation implementation。`

## Round Intent

- `quality_mode`: standard

## Gate State

- `estimation_complete`: true
- `brief_status`: ready
- `brief_version`: 2

## Routing

- `task_routing`: `code/programming`
- `orchestrator_choice`: `staff-engineer-orchestrator`

## Core Intent

- `goal`: implement the approved lifecycle foundation as a dormant, backwards-compatible contract and template layer without activating `task-runtime-v1`
- `artifact_type`: packaged workflow contract, templates, scaffold behavior, and regression tests
- `relevant_context`:
  - The approved lifecycle design is revision 11 at `docs/cases/task-runtime/rounds/2026-06-19-task-runtime-lifecycle-foundation-design/design-spec.md`.
  - The repository currently writes schema version 1 working briefs, dispatch plans, and packet examples.
  - The approved design requires a coordinated next schema version and a round-owned `lifecycle_protocol: legacy | task-runtime-v1` discriminator.
  - Ordinary rounds must continue using the legacy controller until verifier, review progression, scoring, and close-gate capabilities exist.
  - No scaffold regression test currently protects generated lifecycle compatibility metadata.
  - Pre-commit review found that the new scaffold regression test was not part of the repository validation entrypoint.
- `constraints`:
  - Assign schema version 2 as the current write schema for coordinated working-brief, dispatch-plan, and packet contract surfaces.
  - Default generated and ordinary rounds to `lifecycle_protocol: legacy`.
  - A legacy round must not persist or consult a canonical lifecycle snapshot or event history.
  - Document the approved phase vocabulary, ownership, snapshot/event shape, compatibility matrix, deterministic next-action contract, migration boundary, and recovery rules in one canonical lifecycle reference.
  - Do not activate `task-runtime-v1` in this round.
  - Do not add verifier personas or verifier packet/runtime bindings.
  - Do not add internal hook execution, quality scoring, repair policy, routing expansion, persona changes, or a dedicated lifecycle validator.
  - Do not rewrite historical schema-version-1 case artifacts.
  - Preserve `runtime_state` as the single canonical post-launch operational state.

## Risk And Structure

- `risk_lenses`:
  - accidentally activating an incomplete phase machine through template defaults
  - creating a second authority that competes with `runtime_state`
  - bumping one schema surface without coordinating the others
  - documenting migration as available before mandatory phase capabilities exist
  - allowing lifecycle fields to appear on legacy sections
  - weak scaffold tests that only assert text presence instead of default behavior and case updates
  - regression tests that pass locally but are absent from the CI entrypoint
- `parallelism_assessment`:
  - Use one serial implementation section because contract, templates, scaffold output, and tests share one schema and compatibility decision.
- `blocking_dependencies`:
  - approved lifecycle foundation design revision 11
  - current packaged skill contract and templates
  - current case scaffold behavior
  - existing repo validation suite
- `section_or_workstream_map`:
  - section-lifecycle-foundation-implementation: add dormant lifecycle contract support, coordinated schema defaults, scaffold coverage, and minimal README guidance

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: lifecycle_foundation_contract
    - `artifact_kind`: packaged_skill_contract
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `section_anchors`: lifecycle protocol and references
  - `artifact_id`: lifecycle_foundation_reference
    - `artifact_kind`: normative_reference
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
    - `section_anchors`: lifecycle ownership, protocol, transitions, persistence, migration
  - `artifact_id`: lifecycle_foundation_templates
    - `artifact_kind`: template_set
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `section_anchors`: lifecycle protocol and conditional section lifecycle records
  - `artifact_id`: lifecycle_foundation_scaffold
    - `artifact_kind`: python_tool
    - `artifact_path`: `tools/scaffold_ww_case_artifacts.py`
    - `section_anchors`: generated schema and lifecycle protocol defaults
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/task-runtime/case.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/working-brief.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/dispatch-plan.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `path_glob`: `tools/scaffold_ww_case_artifacts.py`
  - `path_glob`: `tools/validate_ww_repo.py`
  - `path_glob`: `tools/test_scaffold_ww_case_artifacts.py`
  - `path_glob`: `README.md`
- `shared_read_scope`:
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-19-task-runtime-lifecycle-foundation-design/**/*`
  - `path_glob`: `docs/superpowers/specs/2026-06-19-workwork-task-runtime-design.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `path_glob`: `docs/superpowers/personas/registry.yaml`
  - `path_glob`: `tools/validate_ww_*.py`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `candidate_persona_sources`:
  - project registry checked: true
  - built-in fallback checked: true
  - project registry outcome: no eligible project worker or reviewer persona covers packaged Python workflow-contract implementation
  - built-in fallback outcome: use `senior-backend-engineer` as worker, `spec-reviewer` for contract review, and `code-quality-reviewer` for implementation review
  - fallback rationale when a built-in persona is recommended: built-in records provide the strongest required-field and runtime-role fit after the project registry produced no eligible match
- `recommended_personas`:
  - `senior-backend-engineer`
    - runtime role: worker
    - source: built-in
    - owned scope: implement the coordinated lifecycle contract, templates, scaffold defaults, and regression tests
    - baseline fit rationale: the work changes a Python-backed packaged workflow contract with cross-file schema compatibility requirements
    - project-priority or built-in-fallback rationale: no project worker persona covers this contract-and-scaffold implementation, so the strongest eligible built-in worker is selected
    - enrichment fit rationale: explicit service boundaries and maintainable interfaces fit the separation between dormant schema support and runtime activation
    - role binding: `worker` via `agents/worker-prompt.md`
    - workflow bindings: `superpowers:test-driven-development`, `superpowers:verification-before-completion`
  - `spec-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: compare the implementation against approved lifecycle design revision 11 and the explicit exclusions
    - baseline fit rationale: correctness depends on faithful translation of an approved normative design into active contract surfaces
    - project-priority or built-in-fallback rationale: no eligible project reviewer covers lifecycle contract consistency, so built-in fallback applies
    - enrichment fit rationale: contract-first review fits state ownership, protocol activation, and migration boundaries
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`, `superpowers:verification-before-completion`
  - `code-quality-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: review scaffold code, regression tests, schema coordination, and backwards-compatibility risk
    - baseline fit rationale: the implementation includes Python behavior whose value depends on deterministic generated artifacts and regression coverage
    - project-priority or built-in-fallback rationale: no eligible project reviewer covers Python scaffold quality, so built-in fallback applies
    - enrichment fit rationale: correctness-and-maintainability-first review fits the coordinated schema bump and test harness
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`, `superpowers:verification-before-completion`
- `persona_selection_notes`:
  - Keep one worker across all writable implementation surfaces so schema version and lifecycle defaults remain atomic.
  - Use separate spec and code-quality lanes because neither lane should approve the concerns owned by the other.
- `recommended_worker_mode_by_section`:
  - section-lifecycle-foundation-implementation: test-first
- `worker_mode_reasoning_by_section`:
  - section-lifecycle-foundation-implementation: scaffold output is executable behavior; first pin schema version 2 and default legacy protocol, then update implementation and contract surfaces.
- `goal_tuning_by_section`:
  - section-lifecycle-foundation-implementation: compatibility-first and activation-averse
- `constraint_override_notes_by_section`:
  - section-lifecycle-foundation-implementation: later verifier, hooks, quality-gate, repair, validator-expansion, and activation work remains out of scope even when the design reference names those boundaries.
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - implementation: `superpowers:test-driven-development`
  - debugging: `superpowers:systematic-debugging`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval for one serial test-first implementation section, then run both required reviewer lanes and the full repository validator suite

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-lifecycle-foundation-implementation: true
- `review_target_strategy`:
  - Spec review targets the complete active-contract diff against design revision 11; code-quality review targets the scaffold and test diff plus coordinated schema references.
- `controller_semantics_notes`:
  - This is a standard legacy `$ww` round. It must not dogfood or activate `task-runtime-v1`.
  - No packet may be created before dispatch-plan approval.
  - The round-local planning artifacts remain schema version 1 because this round itself was scaffolded under the current active contract; schema version 2 applies to writes produced after this implementation is approved and lands.

## Rules

- Persona selection must cite the working brief, not task keywords.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
- Historical artifacts are evidence, not migration targets.
