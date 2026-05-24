# Working Brief: Orchestrator Persona Pilot

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: orchestrator-persona-pilot
- `created_at`: 2026-05-19
- `updated_at`: 2026-05-19
- `derived_from_user_request`: `开新的 $ww round 做 orchestrator pilot`

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

- `goal`: execute the first persona-enrichment pilot by enriching the three built-in orchestrator personas with the new optional judgment-oriented fields
- `artifact_type`: built-in persona registry updates plus approval-ready dispatch plan for the orchestrator pilot round
- `relevant_context`:
  - phase 1 already defined the optional enrichment fields, compatibility boundary, and migration rules
  - the implementation plan explicitly prioritizes orchestrator personas as the highest-leverage pilot set
  - the current built-in orchestrator records remain structurally valid but still lack `decision_style`, `quality_bar`, `tradeoff_bias`, `failure_modes_to_watch`, `escalation_triggers`, `collaboration_posture`, and `taste_criteria`
  - orchestrators influence routing, synthesis, escalation, and stopping behavior across the whole system, so contrast quality matters more than field-count completeness
  - this revision should be judged by a Jobs-like bar: kill average overlap, make each orchestrator's point of view feel inevitable, and reject enrichment that sounds richer without changing what the orchestrator protects
- `constraints`:
  - limit the pilot to `staff-engineer-orchestrator`, `pm-orchestrator`, and `creative-director-orchestrator`
  - keep changes inside `built-in-personas.yaml` and the round's planning artifacts
  - do not change `SKILL.md`, packet contracts, prompts, or validators in this round
  - do not add new personas in this round

## Risk And Structure

- `risk_lenses`:
  - enriched fields can become decorative if they do not create visible contrast between orchestrators
  - overfilling every field symmetrically can weaken routing instead of sharpening it
  - writing role behavior into persona fields would blur the contract model just established in phase 1
  - changing runtime surfaces in the same round would make it harder to tell whether the pilot itself is good
  - a "complete" pilot can still fail if all three orchestrators feel equally competent instead of decisively different
- `parallelism_assessment`:
  - this round is tightly coupled around one YAML registry file
  - one implementation lane is safer because all three orchestrator records should be designed as a contrasted set
- `blocking_dependencies`:
  - the phase 1 contract and migration rules must remain the source of truth
  - the current built-in orchestrator records must be read together before drafting enrichments so the contrast is deliberate
- `section_or_workstream_map`:
  - section 1: enrich the orchestrator pilot set with contrasted judgment fields
  - section 2: review the pilot for contrast quality, routing clarity, and contract compliance

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: `persona_strategy_design`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/legacy/superpowers/specs/2026-05-19-persona-enrichment-strategy-design.md`
  - `section_anchors`: `Phase 1 Contract Decisions`, `Phase 1 Migration Rules`, `High-Leverage Enrichment Order`
  - `artifact_id`: `persona_strategy_plan`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/legacy/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
  - `section_anchors`: `Pilot enrichment on orchestrator personas first`
  - `artifact_id`: `persona_registry_rules`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `section_anchors`: `Optional Persona Enrichment Fields`, `Phase 1 Compatibility Boundary`, `Migration Rules`
  - `artifact_id`: `built_in_personas`
  - `artifact_kind`: `data`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `section_anchors`: none
- `exclusive_write_scope`:
  - `path_glob`: `docs/legacy/superpowers/working-briefs/2026-05-19-orchestrator-persona-pilot-v1.md`
  - `path_glob`: `docs/legacy/superpowers/dispatch-plans/2026-05-19-orchestrator-persona-pilot.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
- `shared_read_scope`:
  - `path_glob`: `docs/legacy/superpowers/specs/2026-05-19-persona-enrichment-strategy-design.md`
  - `path_glob`: `docs/legacy/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff-engineer-orchestrator`
  - `creative-director-orchestrator`
  - `pm-orchestrator`
- `persona_selection_notes`:
  - `staff-engineer-orchestrator` is the execution anchor because this is a bounded registry-edit round with strong contract constraints
  - `creative-director-orchestrator` is elevated in this revision because the pilot needs a stronger taste-and-coherence bar, not just structurally valid fields
  - `pm-orchestrator` still matters as the product-judgment counterweight, but it should not flatten the pilot into balanced committee language
- `recommended_worker_mode_by_section`:
  - section 1: `plan-first`
  - section 2: `validate-first`
- `worker_mode_reasoning_by_section`:
  - section 1 should design the three orchestrator records as one contrasted set instead of filling them independently
  - section 2 should validate that the resulting records are sharp, non-overlapping, and contract-compliant
- `goal_tuning_by_section`:
  - section 1: `safety-biased`
  - section 2: `validation-biased`
- `constraint_override_notes_by_section`:
  - section 1: prefer contrast and real routing value over symmetric completeness; if one field adds no visible decision difference, omit or sharpen it
  - section 2: do not widen the round into reviewer, worker, or runtime-adoption work
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - approve one bounded registry-edit lane for the orchestrator pilot
  - require the pilot to produce visible contrast across the three orchestrators
  - review the pilot with a ruthless simplicity bar: fewer overlapping claims, sharper defaults, and clearer reasons to choose one orchestrator over another
  - defer runtime-selection logic, packet changes, and validator changes to later rounds

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-orchestrator-pilot: true
- `review_target_strategy`:
  - review whether each orchestrator gains a distinct decision posture
  - review whether the three enriched records are contrasted enough to improve routing
  - treat duplicated role behavior, decorative prose, or "everyone is great at everything" language as blocking
- `controller_semantics_notes`:
  - this round changes registry data only
  - no packet creation until the referenced dispatch plan is in `approved` state
  - no runtime contract adoption unless a follow-on round is explicitly approved

## Rules

- Recommended personas are provisional until dispatch approval.
- Persona selection must cite the working brief, not just task keywords.
- The working brief is an analysis artifact, not the runtime approval record.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
- If the user requests `Revise`, update the working brief only if the analysis changed, then issue a new brief version for the next dispatch plan revision.
