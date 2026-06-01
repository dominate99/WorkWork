# Working Brief: Runtime Persona Packet Validator Expansion

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: workflow-runtime-persona-packet-validator-expansion
- `case_slug`: persona-system-expansion
- `round_slug`: 2026-05-31-workflow-runtime-persona-packet-validator-expansion
- `case_root`: `docs/cases/persona-system-expansion/`
- `round_root`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-validator-expansion/`
- `created_at`: 2026-05-31
- `updated_at`: 2026-05-31
- `derived_from_user_request`: `Open a new $ww round: runtime persona packet validator expansion. Based on the approved runtime persona packet dogfood pilot, add focused repository validation for packet artifacts and resolve the PKT-002 launch-snapshot validation strategy. Keep the round narrow: do not implement runtime assembly code, change the packet contract, add personas, change the project registry, expand routing, or add secondary tags.`

## Round Intent

- `quality_mode`: standard

## Gate State

- `estimation_complete`: true
- `brief_status`: ready
- `brief_version`: 1

## Routing

- `task_routing`: `code/programming`
- `orchestrator_choice`: `staff-engineer-orchestrator`

## Core Intent

- `goal`: add focused repository validation for persisted runtime persona packet artifacts and resolve PKT-002 without widening the packet contract
- `artifact_type`: Python validator, repository-suite integration, narrow contract guidance, and completed round records
- `relevant_context`:
  - The approved packet dogfood pilot created one real worker packet and one real reviewer packet.
  - DG-004 is resolved at the persisted packet-artifact layer.
  - PKT-002 asks whether generic dispatch plans must persist prompt-template-path and worker-principles launch snapshots.
  - The current packet contract already defines role-specific prompt bindings and requires worker principles to come directly from the selected persona definition.
  - The validator should inspect real packet artifacts under `docs/cases/**/packets/*.md`, not hard-code one pilot path.
- `constraints`:
  - Add packet-artifact validation only.
  - Prefer cross-checking packet prompt binding from `persona_binding.runtime_role` and worker principles from the selected persona definition.
  - When an approved dispatch plan explicitly persists launch snapshots, validate them as additional evidence.
  - Do not require generic dispatch templates to persist launch snapshots in this round.
  - Do not implement runtime assembly code.
  - Do not change the packet contract.
  - Do not add, remove, or edit persona records.
  - Do not modify `docs/superpowers/personas/registry.yaml`.
  - Do not expand `task_routing`.
  - Do not add secondary tags.

## Risk And Structure

- `risk_lenses`:
  - validating only the pilot filenames instead of discovering packet artifacts generically
  - confusing packet artifact validation with runtime assembly-code validation
  - weakening PKT-002 by silently inferring source or rationale instead of checking approved dispatch records
  - requiring new launch-snapshot template fields despite the narrower cross-check strategy
  - parsing Markdown-shaped packet artifacts too loosely to catch missing or drifted fields
- `parallelism_assessment`:
  - One implementation section is preferred because validator parsing, fixture checks, repo-suite integration, and guidance must agree on one invariant set.
- `blocking_dependencies`:
  - Approved packet dogfood pilot.
  - Current `subagent-packet-contract.md`.
  - Current built-in persona records.
  - Existing repository validators and aggregate runner.
- `section_or_workstream_map`:
  - section-runtime-persona-packet-validator-expansion: implement packet artifact validator, integrate it into the repo suite, update narrow guidance, and verify against the pilot artifacts

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: runtime_persona_packet_validator
    - `artifact_kind`: python_validator
    - `artifact_path`: `tools/validate_ww_persona_packets.py`
    - `section_anchors`: packet artifact discovery and invariant checks
  - `artifact_id`: runtime_persona_packet_validator_suite_integration
    - `artifact_kind`: python_validator_suite
    - `artifact_path`: `tools/validate_ww_repo.py`
    - `section_anchors`: packet validator registration
  - `artifact_id`: runtime_persona_packet_validator_tests
    - `artifact_kind`: python_unittest
    - `artifact_path`: `tools/test_validate_ww_persona_packets.py`
    - `section_anchors`: packet validator regression cases
  - `artifact_id`: runtime_persona_packet_validator_guidance
    - `artifact_kind`: active_contract_guidance
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `section_anchors`: packet validation guidance
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/persona-system-expansion/case.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-validator-expansion/working-brief.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-validator-expansion/dispatch-plan.md`
  - `path_glob`: `tools/validate_ww_persona_packets.py`
  - `path_glob`: `tools/test_validate_ww_persona_packets.py`
  - `path_glob`: `tools/validate_ww_repo.py`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `README.md`
- `shared_read_scope`:
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `path_glob`: `docs/superpowers/personas/registry.yaml`
  - `path_glob`: `docs/cases/**/packets/*.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/design-spec.md`
  - `path_glob`: `tools/validate_ww_persona_selection_contracts.py`
  - `path_glob`: `tools/validate_ww_repo.py`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `candidate_persona_sources`:
  - project registry checked: true
  - built-in fallback checked: true
  - project registry outcome: no stronger eligible project persona covers repository validation and regression-harness work
  - built-in fallback outcome: use `test-quality-engineer` for implementation and `code-quality-reviewer` for review
  - fallback rationale when a built-in persona is recommended: the built-in records provide the strongest required-field fit for validation logic and implementation review
- `recommended_personas`:
  - `test-quality-engineer`
    - runtime role: worker
    - source: built-in
    - owned scope: packet validator implementation, repo-suite integration, and targeted verification
    - baseline fit rationale: the dominant risk is unverified packet drift and missing regression coverage
    - project-priority or built-in-fallback rationale: built-in fallback is used because no stronger eligible project worker persona covers repository validator implementation
    - enrichment fit rationale: evidence-first posture and deterministic-fixture bias fit the pilot-backed validator
    - role binding: `worker` via `agents/worker-prompt.md`
    - workflow bindings: `superpowers:test-driven-development`, `superpowers:verification-before-completion`
  - `code-quality-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: review parser correctness, invariant coverage, regression risk, and suite integration
    - baseline fit rationale: the result is Python validator code whose quality depends on maintainable, testable behavior
    - project-priority or built-in-fallback rationale: built-in fallback is used because no stronger eligible project reviewer-only persona covers validator implementation review
    - enrichment fit rationale: correctness-and-maintainability-first posture fits parser and integration review
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`, `superpowers:verification-before-completion`
- `persona_selection_notes`:
  - Preserve the packet contract as read-only.
  - Treat pilot packet artifacts as real discovered inputs, not hand-coded fixtures.
  - Keep artifact-level validation distinct from runtime assembly-code proof.
- `recommended_worker_mode_by_section`:
  - section-runtime-persona-packet-validator-expansion: test-first
- `worker_mode_reasoning_by_section`:
  - section-runtime-persona-packet-validator-expansion: define failing packet-drift scenarios before implementing parser and integration behavior.
- `goal_tuning_by_section`:
  - section-runtime-persona-packet-validator-expansion: validation-biased
- `constraint_override_notes_by_section`:
  - section-runtime-persona-packet-validator-expansion: runtime code, packet contract, personas, project registry, routing, and secondary tags remain read-only.
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - implementation: `superpowers:test-driven-development`
  - debugging: `superpowers:systematic-debugging`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval for one narrow implementation section that adds and integrates generic packet-artifact validation

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-runtime-persona-packet-validator-expansion: true
- `review_target_strategy`:
  - Review the focused validator and repo-suite integration for generic packet discovery, exact contract-aligned checks, PKT-002 cross-check behavior, and no out-of-scope contract expansion.
- `controller_semantics_notes`:
  - Standard `$ww` round. No strict-review target is active.
  - Do not create subagent packets or edit implementation files before dispatch-plan approval.

## Rules

- Persona selection must cite the working brief, not just task keywords.
- Persona selection must record source, runtime role, baseline fit, and project-priority or built-in-fallback rationale.
- The working brief recommends worker mode by section, but it does not act as final execution authority.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
