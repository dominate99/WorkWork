# Working Brief: Persona Enrichment Phase 1

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: persona-enrichment-phase1
- `created_at`: 2026-05-19
- `updated_at`: 2026-05-19
- `derived_from_user_request`: `$ww 把这份策略直接转成 implementation plan` followed by user approval to proceed with phase 1 execution

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

- `goal`: execute phase 1 of the approved persona-enrichment strategy by formalizing the enriched persona model and migration rules before any registry rollout or runtime adoption
- `artifact_type`: contract and design-document updates for persona enrichment phase 1
- `relevant_context`:
  - the persona-enrichment strategy has already been approved and translated into a staged implementation plan
  - that plan explicitly says phase 1 should define the enriched persona model and migration rules before registry pilots or runtime contract edits
  - current persona rules live primarily in `persona-registry.md`, while the current strategy intent is captured in the approved design spec
  - current built-in and project persona registries remain intentionally small and should not be mutated in this first execution phase
- `constraints`:
  - preserve the current separation between `persona`, `runtime_role`, role prompts, and worker `work_mode`
  - treat new enrichment fields as additive and documentation-level only in phase 1
  - do not update `built-in-personas.yaml` or `docs/superpowers/personas/registry.yaml` in this round
  - do not change `SKILL.md`, packet contracts, prompts, or validators in this round

## Risk And Structure

- `risk_lenses`:
  - if the new fields are underspecified, later pilots will either drift or become decorative
  - if migration rules are vague, partially enriched personas can distort routing without improving judgment
  - if phase 1 edits registry data too early, the repo will blur the difference between model definition and runtime adoption
  - if persona fields duplicate role behavior, the contract model will regress
- `parallelism_assessment`:
  - this round is documentation-heavy but tightly coupled
  - one implementation lane is preferable because persona-model definitions and migration rules must agree exactly
- `blocking_dependencies`:
  - the approved strategy design and implementation plan must remain the source of truth
  - the current persona registry rules must be read before changing required or optional field guidance
- `section_or_workstream_map`:
  - section 1: formalize enriched persona-model fields and compatibility boundary
  - section 2: define migration and rollout rules for phase 1 adoption

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: `persona_strategy_design`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/superpowers/specs/2026-05-19-persona-enrichment-strategy-design.md`
  - `section_anchors`: `What To Add To Personas`, `What Not To Do`, `Recommended Next Implementation Track`
  - `artifact_id`: `persona_strategy_plan`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
  - `section_anchors`: none
  - `artifact_id`: `persona_registry_rules`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `section_anchors`: `Required Persona Fields`, `Selection Rules`, `Prompt Binding Roles`
  - `artifact_id`: `built_in_personas`
  - `artifact_kind`: `data`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `section_anchors`: none
  - `artifact_id`: `project_personas`
  - `artifact_kind`: `data`
  - `artifact_path`: `docs/superpowers/personas/registry.yaml`
  - `section_anchors`: none
- `exclusive_write_scope`:
  - `path_glob`: `docs/superpowers/working-briefs/2026-05-19-persona-enrichment-phase1-v1.md`
  - `path_glob`: `docs/superpowers/dispatch-plans/2026-05-19-persona-enrichment-phase1.md`
  - `path_glob`: `docs/superpowers/specs/2026-05-19-persona-enrichment-strategy-design.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
- `shared_read_scope`:
  - `path_glob`: `docs/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `path_glob`: `docs/superpowers/personas/registry.yaml`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff-engineer-orchestrator`
  - `pm-orchestrator`
  - `senior-backend-engineer`
- `persona_selection_notes`:
  - `staff-engineer-orchestrator` fits the top-level artifact because this is a bounded contract-definition round inside the skill repository
  - `pm-orchestrator` remains useful as a specialist lens because persona enrichment is partly about product judgment, taste, and decision framing
  - `senior-backend-engineer` is the best systems-realism counterweight to keep the new schema implementable and non-theatrical
- `recommended_worker_mode_by_section`:
  - section 1: `validate-first`
  - section 2: `plan-first`
- `worker_mode_reasoning_by_section`:
  - section 1 should validate the current registry and strategy model before adding new contract fields
  - section 2 should plan a clean migration posture only after the enriched field set is stable
- `goal_tuning_by_section`:
  - section 1: `validation-biased`
  - section 2: `safety-biased`
- `constraint_override_notes_by_section`:
  - section 1: do not let new persona fields duplicate runtime-role behavior or prompt restrictions
  - section 2: do not start persona pilot enrichment or runtime adoption in this round
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - approve one bounded documentation lane for phase 1 persona-model contract work
  - require explicit migration rules before any persona registry records are enriched
  - defer runtime and validator changes until a later approved round

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-persona-model-contract: true
  - section-persona-migration-rules: true
- `review_target_strategy`:
  - review whether the enriched fields create stronger judgment structure instead of decorative prose
  - review whether migration rules preserve routing stability during partial adoption
  - treat any collapse between persona fields and role behavior as blocking
- `controller_semantics_notes`:
  - this round is phase 1 documentation work only
  - no packet creation until the referenced dispatch plan is in `approved` state
  - no runtime contract changes unless a follow-on round is explicitly approved

## Rules

- Recommended personas are provisional until dispatch approval.
- Persona selection must cite the working brief, not just task keywords.
- The working brief is an analysis artifact, not the runtime approval record.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
- If the user requests `Revise`, update the working brief only if the analysis changed, then issue a new brief version for the next dispatch plan revision.
