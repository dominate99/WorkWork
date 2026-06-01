# Working Brief: Runtime Persona Packet Dogfood Pilot

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: workflow-runtime-persona-packet-dogfood-pilot
- `case_slug`: persona-system-expansion
- `round_slug`: 2026-05-31-workflow-runtime-persona-packet-dogfood-pilot
- `case_root`: `docs/cases/persona-system-expansion/`
- `round_root`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/`
- `created_at`: 2026-05-31
- `updated_at`: 2026-05-31
- `derived_from_user_request`: `new $ww round: runtime persona packet dogfood pilot. Based on completed persona runtime selection adoption and durable review lane rationale cleanup, create and review a minimal set of real packet artifacts: one worker packet and one reviewer packet. Verify that they copy subagent_persona, persona_source, persona_rationale, persona_binding.runtime_role, template_path, and worker implementation_principles correctly from an approved dispatch plan. Only do packet dogfood pilot and evidence classification; do not implement runtime code, change packet contract, change validators, add personas, change project registry, expand routing, or add secondary tags. Produce design-spec.md or gap report and judge whether packet assembly has enough evidence to enter a later validator round.`

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

- `goal`: create and audit one worker packet plus one reviewer packet as real persisted packet artifacts derived from this round's approved dispatch plan
- `artifact_type`: packet dogfood pilot evidence set and gap report
- `relevant_context`:
  - Runtime persona selection adoption now persists persona source, runtime role, and rationale across working brief, dispatch plan, and durable review lanes.
  - DG-004 remains open because recent rounds did not persist live packet artifacts.
  - The packet contract already defines worker and reviewer packet fields; this round should test that contract with minimal round-local artifacts.
  - Packet files must not be created until this dispatch plan is approved.
- `constraints`:
  - Create exactly one worker packet and one reviewer packet under this round root after approval.
  - Produce one `design-spec.md` gap report after inspecting those packet artifacts.
  - Do not implement runtime code.
  - Do not edit packet contract.
  - Do not edit validator scripts.
  - Do not add, remove, or edit persona records.
  - Do not modify `docs/superpowers/personas/registry.yaml`.
  - Do not expand `task_routing`.
  - Do not add secondary tags.

## Risk And Structure

- `risk_lenses`:
  - accidentally drafting packet files before dispatch approval
  - copying persona fields from the working brief instead of the approved dispatch plan snapshot
  - omitting worker `implementation_principles` or changing their order
  - giving the reviewer packet write authority
  - treating two fixtures as proof that runtime assembly code exists
- `parallelism_assessment`:
  - Single-section pilot is preferred because reviewer packet creation depends on a stable worker packet artifact and both feed one evidence report.
- `blocking_dependencies`:
  - Completed runtime persona selection adoption contract.
  - Completed durable review-lane rationale cleanup.
  - Current `subagent-packet-contract.md`.
  - Current built-in `technical-writer` and `spec-reviewer` persona records.
- `section_or_workstream_map`:
  - section-runtime-persona-packet-dogfood-pilot: after approval, persist worker packet, persist reviewer packet against the stable worker packet, audit both, and write gap report

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: runtime_persona_packet_worker_evidence
    - `artifact_kind`: worker_packet
    - `artifact_path`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/packets/worker-packet.md`
    - `section_anchors`: worker packet evidence
  - `artifact_id`: runtime_persona_packet_reviewer_evidence
    - `artifact_kind`: reviewer_packet
    - `artifact_path`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/packets/reviewer-packet.md`
    - `section_anchors`: reviewer packet evidence
  - `artifact_id`: runtime_persona_packet_dogfood_gap_report
    - `artifact_kind`: dogfood_gap_report
    - `artifact_path`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/design-spec.md`
    - `section_anchors`: packet dogfood findings
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/persona-system-expansion/case.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/working-brief.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/dispatch-plan.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/packets/worker-packet.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/packets/reviewer-packet.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/design-spec.md`
- `shared_read_scope`:
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `path_glob`: `docs/superpowers/personas/registry.yaml`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-28-workflow-runtime-persona-selection-dogfood-audit/design-spec.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-30-workflow-durable-review-lane-persona-rationale-cleanup/dispatch-plan.md`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `candidate_persona_sources`:
  - project registry checked: true
  - built-in fallback checked: true
  - project registry outcome: no stronger eligible packet-pilot documentation worker or spec reviewer exists in `docs/superpowers/personas/registry.yaml`
  - built-in fallback outcome: use `technical-writer` for worker packet evidence and `spec-reviewer` for reviewer packet evidence
  - fallback rationale when a built-in persona is recommended: built-in records provide the strongest required-field fit for a maintainer-facing packet artifact pilot and contract-focused review
- `recommended_personas`:
  - `technical-writer`
    - runtime role: worker
    - source: built-in
    - owned scope: round-local worker packet evidence and packet dogfood gap report
    - baseline fit rationale: the pilot produces persisted technical artifacts whose value depends on source-of-truth clarity
    - project-priority or built-in-fallback rationale: built-in fallback is used because no stronger eligible project worker persona covers packet evidence documentation
    - enrichment fit rationale: reader-task-first posture fits a minimal inspectable evidence set
    - role binding: `worker` via `agents/worker-prompt.md`
    - workflow bindings: `superpowers:writing-plans`, `superpowers:verification-before-completion`
  - `spec-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: review the stable worker packet artifact and the final evidence classification
    - baseline fit rationale: the review target is a persisted contract-shaped packet artifact with explicit required fields
    - project-priority or built-in-fallback rationale: built-in fallback is used because no stronger eligible project reviewer-only persona covers packet contract fidelity
    - enrichment fit rationale: contract-first review matches field-copy and scope-authority risks
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`, `superpowers:verification-before-completion`
- `persona_selection_notes`:
  - Packet files are approved-stage execution artifacts, not pre-approval planning artifacts.
  - Worker principles must be copied directly and in order from the built-in `technical-writer` record.
  - Reviewer packet write scope must remain empty.
  - The report must distinguish packet artifact proof from runtime assembly-code proof.
- `recommended_worker_mode_by_section`:
  - section-runtime-persona-packet-dogfood-pilot: conservative-first
- `worker_mode_reasoning_by_section`:
  - section-runtime-persona-packet-dogfood-pilot: create the smallest contract-complete evidence pair and classify what it proves without widening scope.
- `goal_tuning_by_section`:
  - section-runtime-persona-packet-dogfood-pilot: validation-biased
- `constraint_override_notes_by_section`:
  - section-runtime-persona-packet-dogfood-pilot: runtime code, packet contract, validators, personas, registry, routing, and secondary tags stay read-only.
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - packet evidence creation: `superpowers:verification-before-completion`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval to create the two round-local packet artifacts and audit their field-copy evidence

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-runtime-persona-packet-dogfood-pilot: true
- `review_target_strategy`:
  - Review the stable worker packet and reviewer packet for approved-dispatch derivation, persona source/rationale/role binding copying, ordered worker principles, reviewer read-only authority, and evidence classification accuracy.
- `controller_semantics_notes`:
  - Standard `$ww` round. No strict-review target is active.
  - Do not create packet artifacts before the referenced dispatch plan is approved.

## Rules

- Recommended personas are provisional until dispatch approval.
- Persona selection must cite the working brief, not just task keywords.
- Persona selection must record source, runtime role, baseline fit, and project-priority or built-in-fallback rationale.
- The working brief recommends `worker mode` by section, but it does not act as the final execution authority.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
