# Working Brief: Runtime Persona Packet Path Containment Fixture Hardening

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: workflow-runtime-persona-packet-path-containment-fixture-hardening
- `case_slug`: persona-system-expansion
- `round_slug`: 2026-06-02-workflow-runtime-persona-packet-path-containment-fixture-hardening
- `case_root`: `docs/cases/persona-system-expansion/`
- `round_root`: `docs/cases/persona-system-expansion/rounds/2026-06-02-workflow-runtime-persona-packet-path-containment-fixture-hardening/`
- `created_at`: 2026-06-02
- `updated_at`: 2026-06-02
- `derived_from_user_request`: `new $ww round: runtime persona packet path containment fixture hardening. Based on the approved packet validator dogfood audit, add negative fixtures for repository-relative path containment in validate_ww_persona_packets.py, focusing on ../ traversal escape. Evaluate whether symlink escape should be covered and include it only if cross-platform stability supports it. Add tests and necessary test notes only; do not change validator behavior, packet contract, runtime code, personas, routing, or open canonical slice resolver design.`

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

- `goal`: harden runtime persona packet path-containment regression evidence with repository-relative traversal escape fixtures while preserving validator behavior
- `artifact_type`: focused Python unittest fixture hardening and completed round records
- `relevant_context`:
  - The approved runtime persona packet validator dogfood audit classified path containment as implemented with a narrow fixture-hardening opportunity.
  - Existing regression fixtures reject absolute `source_dispatch_plan` and reviewer-target paths.
  - `resolve_repo_relative_path` already resolves candidate paths against repository root and rejects resolved paths outside that root.
  - The missing evidence is direct `../` traversal escape coverage for both dispatch-source and reviewer-target path surfaces.
  - Symlink escape behavior should be included only if the fixture is deterministic across supported platforms and does not require privilege assumptions.
- `constraints`:
  - Add focused negative regression fixtures only.
  - Do not change `tools/validate_ww_persona_packets.py`.
  - Do not change packet contract surfaces.
  - Do not implement runtime code.
  - Do not add, remove, or edit persona records.
  - Do not modify `docs/superpowers/personas/registry.yaml`.
  - Do not expand `task_routing`.
  - Do not add secondary tags.
  - Do not open canonical slice resolver design.
  - Record symlink fixture inclusion or exclusion reasoning in the completed round record.

## Risk And Structure

- `risk_lenses`:
  - adding fixtures that accidentally test missing-file behavior instead of repository escape containment
  - changing validator behavior while intending only test hardening
  - introducing a symlink fixture that is unstable on Windows or privilege-sensitive environments
  - widening into canonical slice resolution or packet contract work
- `parallelism_assessment`:
  - Single-section implementation is preferred because the two traversal fixtures share one regression harness and the symlink decision is a small compatibility assessment.
- `blocking_dependencies`:
  - Approved packet validator dogfood audit.
  - Existing `resolve_repo_relative_path` containment behavior.
  - Existing focused packet validator unittest harness.
- `section_or_workstream_map`:
  - section-runtime-persona-packet-path-containment-fixture-hardening: add traversal escape fixtures, assess symlink fixture stability, run focused and aggregate verification, and record the result

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: runtime_persona_packet_path_containment_fixtures
    - `artifact_kind`: python_unittest
    - `artifact_path`: `tools/test_validate_ww_persona_packets.py`
    - `section_anchors`: repository-relative path containment negative fixtures
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/persona-system-expansion/case.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-06-02-workflow-runtime-persona-packet-path-containment-fixture-hardening/working-brief.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-06-02-workflow-runtime-persona-packet-path-containment-fixture-hardening/dispatch-plan.md`
  - `path_glob`: `tools/test_validate_ww_persona_packets.py`
- `shared_read_scope`:
  - `path_glob`: `tools/validate_ww_persona_packets.py`
  - `path_glob`: `tools/validate_ww_repo.py`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-06-01-workflow-runtime-persona-packet-validator-dogfood-audit/design-spec.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `path_glob`: `docs/superpowers/personas/registry.yaml`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `candidate_persona_sources`:
  - project registry checked: true
  - built-in fallback checked: true
  - project registry outcome: no stronger eligible project worker or reviewer persona covers focused regression-harness hardening
  - built-in fallback outcome: use `test-quality-engineer` for fixture implementation and `code-quality-reviewer` for review
  - fallback rationale when a built-in persona is recommended: the built-in records provide the strongest required-field fit for deterministic fixture design and narrow implementation review
- `recommended_personas`:
  - `test-quality-engineer`
    - runtime role: worker
    - source: built-in
    - owned scope: add path-containment negative fixtures and run focused verification
    - baseline fit rationale: the dominant work is deterministic regression-harness hardening around an already-implemented invariant
    - project-priority or built-in-fallback rationale: built-in fallback is used because no stronger eligible project worker persona covers targeted validation fixtures
    - enrichment fit rationale: evidence-first posture and explicit fixture boundaries match the traversal-containment gap
    - role binding: `worker` via `agents/worker-prompt.md`
    - workflow bindings: `superpowers:test-driven-development`, `superpowers:verification-before-completion`
  - `code-quality-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: review fixture correctness, cross-platform stability judgment, and scope containment
    - baseline fit rationale: the result is Python regression-test code whose value depends on proving the intended invariant without accidental behavior changes
    - project-priority or built-in-fallback rationale: built-in fallback is used because no stronger eligible project reviewer-only persona covers regression fixture quality
    - enrichment fit rationale: correctness-and-maintainability-first posture fits this narrow harness change
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`, `superpowers:verification-before-completion`
- `persona_selection_notes`:
  - Prefer two direct traversal fixtures: dispatch-source escape and reviewer-target escape.
  - Evaluate symlink escape as a portability question; omit it if deterministic setup cannot be guaranteed.
  - Preserve validator and packet contract surfaces as read-only.
- `recommended_worker_mode_by_section`:
  - section-runtime-persona-packet-path-containment-fixture-hardening: test-first
- `worker_mode_reasoning_by_section`:
  - section-runtime-persona-packet-path-containment-fixture-hardening: the round exists to pin an existing invariant with focused negative fixtures.
- `goal_tuning_by_section`:
  - section-runtime-persona-packet-path-containment-fixture-hardening: validation-biased
- `constraint_override_notes_by_section`:
  - section-runtime-persona-packet-path-containment-fixture-hardening: validator behavior, packet contract, runtime code, personas, project registry, routing, secondary tags, and canonical slice design remain out of scope.
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - implementation: `superpowers:test-driven-development`
  - debugging: `superpowers:systematic-debugging`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval for one narrow implementation section that adds direct traversal escape fixtures and records the symlink stability decision

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-runtime-persona-packet-path-containment-fixture-hardening: true
- `review_target_strategy`:
  - Review the focused unittest diff for direct containment coverage, failure-rule specificity, cross-platform stability, and absence of validator behavior changes.
- `controller_semantics_notes`:
  - Standard `$ww` round. No strict-review target is active.
  - Do not edit the test file before dispatch-plan approval.

## Rules

- Persona selection must cite the working brief, not just task keywords.
- Persona selection must record source, runtime role, baseline fit, and project-priority or built-in-fallback rationale.
- The working brief recommends worker mode by section, but it does not act as final execution authority.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
