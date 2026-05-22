# Working Brief: Persona Runtime-Selection Guidance Pilot

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: persona-runtime-selection-guidance-pilot
- `created_at`: 2026-05-21
- `updated_at`: 2026-05-21
- `derived_from_user_request`: `新的 $ww round：persona runtime-selection guidance pilot`

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

- `goal`: connect the enriched persona fields to runtime persona-selection guidance so orchestrators know when and how to use them during selection, rationale writing, and tie-break decisions
- `artifact_type`: runtime-selection guidance updates plus approval-ready dispatch plan for a guidance-only pilot round
- `relevant_context`:
  - phase 1 contract is already complete
  - orchestrator, reviewer, and worker persona pilots are complete in the registry
  - `persona-registry.md` still says optional enrichment fields are advisory context only until runtime adoption rules are updated
  - `SKILL.md` still emphasizes deriving personas from the working brief, but it does not yet define how enriched fields should influence selection or rationale
- `constraints`:
  - treat this as a guidance-only runtime-adoption pilot
  - update selection rules and skill-level guidance before touching packet contracts, prompts, or validators
  - preserve the distinction between `persona`, `runtime_role`, role prompts, and worker `work_mode`
  - do not add new personas or rewrite existing persona records in this round

## Risk And Structure

- `risk_lenses`:
  - if the guidance is too weak, the enriched fields remain decorative registry metadata
  - if the guidance is too strong, optional fields could accidentally become hidden hard requirements
  - if selection guidance blurs into packet or prompt semantics, the repo will skip a needed adoption phase
  - if rationale rules are vague, orchestrators may keep defaulting to `strengths` and `use_when` even when enriched fields should decide
- `parallelism_assessment`:
  - this round is tightly coupled across the registry rules and the packaged skill contract
  - one implementation lane is better because the guidance needs one coherent decision hierarchy
- `blocking_dependencies`:
  - the existing persona-enrichment design and implementation plan remain the source of truth
  - the current registry rules and skill contract must be read together before redefining selection guidance
- `section_or_workstream_map`:
  - section 1: update persona-selection guidance in the registry rules
  - section 2: update packaged skill guidance so `$ww` planning can consume enriched fields intentionally

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: `persona_strategy_design`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/superpowers/specs/2026-05-19-persona-enrichment-strategy-design.md`
  - `section_anchors`: `Phase 1 Contract Decisions`, `Phase 1 Migration Rules`, `Recommended Next Implementation Track`
  - `artifact_id`: `persona_strategy_plan`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
  - `section_anchors`: `Update runtime-selection guidance after the pilot set is stable`
  - `artifact_id`: `persona_registry_rules`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `section_anchors`: `Selection Rules`, `Migration Rules`, `Built-In Routing Defaults`
  - `artifact_id`: `ww_skill_contract`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `section_anchors`: `Core Rules`, `Persona Planning`
- `exclusive_write_scope`:
  - `path_glob`: `docs/superpowers/working-briefs/2026-05-21-persona-runtime-selection-guidance-pilot-v1.md`
  - `path_glob`: `docs/superpowers/dispatch-plans/2026-05-21-persona-runtime-selection-guidance-pilot.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- `shared_read_scope`:
  - `path_glob`: `docs/superpowers/specs/2026-05-19-persona-enrichment-strategy-design.md`
  - `path_glob`: `docs/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff-engineer-orchestrator`
  - `pm-orchestrator`
  - `creative-director-orchestrator`
- `persona_selection_notes`:
  - `staff-engineer-orchestrator` fits the top-level artifact because this is a contract and guidance round inside the orchestration system itself
  - `pm-orchestrator` is a useful lens because runtime-selection guidance has to improve outcome-oriented persona choice, not just internal consistency
  - `creative-director-orchestrator` is a useful counterweight because the guidance should not collapse into purely technical tie-break rules once taste and coherence matter
- `recommended_worker_mode_by_section`:
  - section 1: `validate-first`
  - section 2: `plan-first`
- `worker_mode_reasoning_by_section`:
  - section 1 should validate the current registry guidance before changing what counts as selection-driving evidence
  - section 2 should then design a coherent skill-level adoption layer for `$ww` planning and rationale writing
- `goal_tuning_by_section`:
  - section 1: `validation-biased`
  - section 2: `safety-biased`
- `constraint_override_notes_by_section`:
  - section 1: do not let optional enrichment fields silently become hidden required fields
  - section 2: do not widen this round into packet, prompt, or validator changes
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - approve one bounded guidance lane for runtime persona selection
  - require explicit rules for when enriched fields are advisory versus decision-driving
  - defer packet, prompt, and validator consumption to later approved rounds

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-runtime-selection-guidance: true
- `review_target_strategy`:
  - review whether the new guidance makes enriched persona fields actually usable for selection
  - review whether the guidance preserves optionality and compatibility during transition
  - treat any hidden hard-requirement behavior or role-surface bleed as blocking
- `controller_semantics_notes`:
  - this round updates selection guidance only
  - no packet creation until the referenced dispatch plan is in `approved` state
  - packet, prompt, and validator adoption remain out of scope here

## Rules

- Recommended personas are provisional until dispatch approval.
- Persona selection must cite the working brief, not just task keywords.
- The working brief is an analysis artifact, not the runtime approval record.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
- If the user requests `Revise`, update the working brief only if the analysis changed, then issue a new brief version for the next dispatch plan revision.
