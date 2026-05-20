# Working Brief: Persona Enrichment Strategy

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: persona-enrichment-strategy
- `created_at`: 2026-05-19
- `updated_at`: 2026-05-19
- `derived_from_user_request`: `$ww 你现在是乔布斯，你觉得persona 如何丰富 让我们的能力更强更好`

## Round Intent

- `quality_mode`: standard

## Gate State

- `estimation_complete`: true
- `brief_status`: ready
- `brief_version`: 1

## Routing

- `task_routing`: `design/ads/product`
- `orchestrator_choice`: `pm-orchestrator`

## Core Intent

- `goal`: define a stronger persona system strategy for WorkWork so personas improve capability instead of just increasing catalog size
- `artifact_type`: strategy brief plus approval-ready dispatch plan for a persona-system design round
- `relevant_context`:
  - current built-in persona data is intentionally small and mostly role-oriented
  - recent repository work strengthened worker `work_mode` contracts and added reviewer/explorer contract validators
  - persona selection rules already distinguish `persona`, `runtime_role`, and role prompt behavior
  - current persona records are useful but still relatively flat: they capture strengths and use cases, but not enough differentiation in taste, decision style, escalation style, and collaboration posture
  - the user's ask is qualitative and directional: make personas richer so the system becomes stronger overall
- `constraints`:
  - avoid making persona richness equal to raw persona count growth
  - keep compatibility with the current packet contract and role-binding model
  - prefer high-leverage structural enrichment over decorative personality text
  - treat this round as strategy/design first, not immediate implementation

## Risk And Structure

- `risk_lenses`:
  - adding more personas without a stronger model will increase routing noise instead of capability
  - conflating `persona`, `runtime_role`, and `work_mode` would blur the contract model that the repo just clarified
  - over-indexing on style or tone would create "theater personas" that sound distinct but do not produce better decisions
  - a Jobs-style answer can become vague inspiration unless converted into concrete system layers
- `parallelism_assessment`:
  - this is a tightly coupled strategy problem
  - a single design lane is better than parallel implementation lanes because the key work is prioritization and system shape
- `blocking_dependencies`:
  - existing persona registry and built-in persona structure must be understood before recommending changes
  - the strategy should stay consistent with the current packet and runtime-role contract model
- `section_or_workstream_map`:
  - section 1: define what "better personas" should optimize for
  - section 2: define a richer persona model and prioritization
  - section 3: define likely implementation tracks after approval

## Scope Preparation

- `artifact_mappings`:
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
  - `artifact_id`: `ww_skill_contract`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `section_anchors`: `Persona Planning`, `Subagent Packet Contract`
- `exclusive_write_scope`:
  - `path_glob`: `docs/superpowers/working-briefs/2026-05-19-persona-enrichment-strategy-v1.md`
  - `path_glob`: `docs/superpowers/dispatch-plans/2026-05-19-persona-enrichment-strategy.md`
  - `path_glob`: `docs/superpowers/specs/2026-05-19-persona-enrichment-strategy-design.md`
  - `path_glob`: `docs/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
- `shared_read_scope`:
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `path_glob`: `docs/superpowers/personas/registry.yaml`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `pm-orchestrator`
  - `creative-director-orchestrator`
  - `senior-backend-engineer`
- `persona_selection_notes`:
  - `pm-orchestrator` fits the top-level artifact because the user is asking for a product/system strategy, not a code patch
  - `creative-director-orchestrator` is a useful specialist lens because the user explicitly wants a sharper, more taste-driven viewpoint
  - `senior-backend-engineer` remains useful as a systems-realism counterweight so the strategy stays implementable
- `recommended_worker_mode_by_section`:
  - section 1: `validate-first`
  - section 2: `plan-first`
  - section 3: `validate-first`
- `worker_mode_reasoning_by_section`:
  - section 1 should validate what the current persona system does and does not express
  - section 2 should plan the richer persona model as a cohesive system
  - section 3 should validate feasibility before recommending implementation tracks
- `goal_tuning_by_section`:
  - section 1: `validation-biased`
  - section 2: `speed-biased`
  - section 3: `safety-biased`
- `constraint_override_notes_by_section`:
  - section 1: do not jump into adding new persona fields before defining the decision-quality problem
  - section 2: do not confuse richer personas with more verbose bios
  - section 3: do not commit to implementation work in this round without explicit approval
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - approve a design-focused round that first sharpens the persona model before changing registry schema or runtime contracts
  - prioritize system-level enrichment dimensions such as decision style, risk posture, collaboration posture, taste, and escalation behavior
  - treat implementation as a later round unless the user explicitly wants immediate execution
  - if the user requests execution planning directly, convert the approved strategy into a staged implementation plan before editing runtime contracts

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-persona-strategy: true
- `review_target_strategy`:
  - review whether the proposed persona-enrichment strategy improves capability, not just taxonomy size
  - review whether the proposal stays compatible with the current role and packet model
  - review whether the recommendations are concrete enough to drive a later implementation plan
- `controller_semantics_notes`:
  - this round is design-first and should stop before implementation unless the user explicitly approves a follow-on execution round

## Rules

- Recommended personas are provisional until dispatch approval.
- Persona selection must cite the working brief, not just task keywords.
- The working brief is an analysis artifact, not the runtime approval record.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
- If the user requests `Revise`, update the working brief only if the analysis changed, then issue a new brief version for the next dispatch plan revision.
