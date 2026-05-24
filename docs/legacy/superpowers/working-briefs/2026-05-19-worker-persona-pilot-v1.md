# Working Brief: Worker Persona Pilot

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: worker-persona-pilot
- `created_at`: 2026-05-19
- `updated_at`: 2026-05-19
- `derived_from_user_request`: `$ww round 做 worker persona pilot`

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

- `goal`: execute the worker persona pilot by enriching `senior-backend-engineer` and `java-pro-engineer` so they make more visibly different implementation choices under the same worker `work_mode`
- `artifact_type`: built-in persona registry updates plus approval-ready dispatch plan for a worker pilot round
- `relevant_context`:
  - phase 1 already defined optional enrichment fields and migration rules
  - orchestrator and reviewer pilots are complete, so the next planned pilot in the implementation sequence is the worker layer
  - both worker-capable personas already have `implementation_principles`, but still lack the optional enrichment fields that would explain different judgment posture beyond language/domain labels
  - the implementation plan explicitly says worker enrichment should complement, not replace, `implementation_principles` and `work_mode`
- `constraints`:
  - limit the pilot to `senior-backend-engineer` and `java-pro-engineer`
  - keep changes inside `built-in-personas.yaml` and the round's planning artifacts
  - do not change `SKILL.md`, worker prompts, packet contracts, or validators in this round
  - do not alter `implementation_principles` in this round unless a field-level contradiction makes it necessary

## Risk And Structure

- `risk_lenses`:
  - worker enrichment can become redundant if the new fields merely paraphrase the existing `implementation_principles`
  - language specialization alone is too weak if both personas still make the same tradeoff decisions
  - if the pilot leans too hard on Java specifics, `senior-backend-engineer` may stop feeling like the broader system-integrity worker
  - widening this round into runtime adoption would make it harder to tell whether the worker personas themselves are genuinely differentiated
- `parallelism_assessment`:
  - this round is tightly coupled around one registry file and two intentionally contrasted records
  - one implementation lane is better because the two worker personas should be designed as a pair, not enriched independently
- `blocking_dependencies`:
  - phase 1 compatibility rules must remain the source of truth
  - the existing worker `implementation_principles` and `work_mode` model must remain unchanged while this pilot sharpens persona judgment
- `section_or_workstream_map`:
  - section 1: enrich the worker pilot pair with contrasted judgment structure
  - section 2: review the pilot for real implementation-choice contrast and contract compliance

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: `persona_strategy_design`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/legacy/superpowers/specs/2026-05-19-persona-enrichment-strategy-design.md`
  - `section_anchors`: `High-Leverage Enrichment Order`, `Phase 1 Contract Decisions`, `Phase 1 Migration Rules`
  - `artifact_id`: `persona_strategy_plan`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/legacy/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
  - `section_anchors`: `Enrich selected worker personas third`
  - `artifact_id`: `persona_registry_rules`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `section_anchors`: `Optional Persona Enrichment Fields`, `Phase 1 Compatibility Boundary`, `Migration Rules`, `Selection Rules`
  - `artifact_id`: `built_in_personas`
  - `artifact_kind`: `data`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `section_anchors`: none
  - `artifact_id`: `worker_contract_surfaces`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `section_anchors`: `Worker packets additionally require`, `Worker Packet Example`
- `exclusive_write_scope`:
  - `path_glob`: `docs/legacy/superpowers/working-briefs/2026-05-19-worker-persona-pilot-v1.md`
  - `path_glob`: `docs/legacy/superpowers/dispatch-plans/2026-05-19-worker-persona-pilot.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
- `shared_read_scope`:
  - `path_glob`: `docs/legacy/superpowers/specs/2026-05-19-persona-enrichment-strategy-design.md`
  - `path_glob`: `docs/legacy/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/agents/worker-prompt.md`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff-engineer-orchestrator`
  - `senior-backend-engineer`
  - `java-pro-engineer`
- `persona_selection_notes`:
  - `staff-engineer-orchestrator` fits the top-level artifact because this is a bounded worker-registry edit round with strong technical contract constraints
  - `senior-backend-engineer` should anchor the broader system-integrity viewpoint for worker decisions
  - `java-pro-engineer` should sharpen language/framework correctness without collapsing into a duplicate of the broader backend persona
- `recommended_worker_mode_by_section`:
  - section 1: `plan-first`
  - section 2: `validate-first`
- `worker_mode_reasoning_by_section`:
  - section 1 should design the two worker personas as a contrasted pair rather than fill fields independently
  - section 2 should validate that the resulting pair would make different implementation choices under the same `work_mode`
- `goal_tuning_by_section`:
  - section 1: `safety-biased`
  - section 2: `validation-biased`
- `constraint_override_notes_by_section`:
  - section 1: prefer implementation-choice contrast over catalog completeness
  - section 2: block wording that merely restates existing `implementation_principles` or worker prompt behavior
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - approve one bounded registry-edit lane for the worker pilot
  - require the pilot to make the two worker personas diverge in real tradeoff posture, not just domain labels
  - defer runtime-selection logic, packet changes, prompt changes, and validator changes to later rounds

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-worker-pilot: true
- `review_target_strategy`:
  - review whether the worker pair gains clearer implementation-choice contrast
  - review whether the new fields complement instead of duplicating `implementation_principles`
  - treat role-behavior duplication or pseudo-contrast as blocking
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
