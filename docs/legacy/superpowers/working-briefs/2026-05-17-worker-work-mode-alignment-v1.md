# Working Brief: Worker Work-Mode Alignment

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: worker-work-mode-alignment
- `created_at`: 2026-05-17
- `updated_at`: 2026-05-17
- `derived_from_user_request`: `$ww 用$ww 开始修改并且review`

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

- `goal`: align worker persona and worker work-mode behavior across the packaged `ww-subagent-orchestrator` contract surfaces so worker execution becomes structure-aware, packet-driven, and reviewable
- `artifact_type`: Markdown skill contract templates and worker prompt
- `relevant_context`:
  - the current packaged skill already enforces worker `implementation_principles`
  - the next gap is second-layer worker execution posture: the worker still lacks one explicit execution-order contract
  - the agreed model is `user constraints -> work_mode -> persona -> goal_tuning`
  - the agreed work-mode authority chain is:
    - working brief recommends
    - dispatch plan decides and records
    - packet freezes execution state
    - worker prompt consumes packet state only
  - the files that need aligned edits are:
    - `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `plugins/workwork/skills/ww-subagent-orchestrator/agents/worker-prompt.md`
- `constraints`:
  - keep `task_mode` separate from `work_mode`
  - do not expand this round into reviewer or explorer work modes
  - preserve the existing worker-persona enforcement model instead of replacing it
  - keep the new fields aligned across all four files
  - do not introduce ambiguous duplicate authority between brief, plan, packet, and prompt

## Risk And Structure

- `risk_lenses`:
  - field-name drift across the four files could make the new mode chain decorative instead of executable
  - if the dispatch plan and packet disagree about authority, the worker could still re-derive behavior ad hoc
  - if the worker prompt consumes persona principles before `work_mode`, the new layer collapses back into persona-only behavior
  - if `goal_tuning` is written too strongly, it can silently replace the structure-driven mode default
- `parallelism_assessment`:
  - this is a small but tightly coupled contract change
  - one bounded implementation lane is safer than parallel edits because all four files describe one shared runtime chain
- `blocking_dependencies`:
  - the design spec and implementation plan must exist before the dispatch round is approved
  - the working brief and dispatch plan must be persisted before any packet or real edit work begins
  - the worker prompt wording should be updated only after the packet-contract fields are settled
- `section_or_workstream_map`:
  - section 1: align the four worker-mode contract surfaces
  - section 2: run a bounded review and verification pass over naming, authority, and execution-order consistency

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: `worker_mode_design_spec`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/legacy/superpowers/specs/2026-05-17-worker-work-mode-alignment-design.md`
  - `section_anchors`: `Design`, `Required Contract Changes`
  - `artifact_id`: `worker_mode_impl_plan`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/legacy/superpowers/plans/2026-05-17-worker-work-mode-alignment.md`
  - `section_anchors`: none
  - `artifact_id`: `working_brief_template`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `section_anchors`: `Persona And Workflow Guidance`, `Rules`
  - `artifact_id`: `dispatch_plan_template`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `section_anchors`: `Planned Sections`, `Section Runtime Ledger`
  - `artifact_id`: `subagent_packet_contract`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `section_anchors`: `Required Fields`, `Packet Rules`, `Worker Packet Defaults`
  - `artifact_id`: `worker_prompt`
  - `artifact_kind`: `prompt`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/agents/worker-prompt.md`
  - `section_anchors`: `Responsibilities`, `Operating rules`
- `exclusive_write_scope`:
  - `path_glob`: `docs/legacy/superpowers/specs/2026-05-17-worker-work-mode-alignment-design.md`
  - `path_glob`: `docs/legacy/superpowers/plans/2026-05-17-worker-work-mode-alignment.md`
  - `path_glob`: `docs/legacy/superpowers/working-briefs/2026-05-17-worker-work-mode-alignment-v1.md`
  - `path_glob`: `docs/legacy/superpowers/dispatch-plans/2026-05-17-worker-work-mode-alignment.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/agents/worker-prompt.md`
- `shared_read_scope`:
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `path_glob`: `docs/superpowers/personas/registry.yaml`
  - `path_glob`: `docs/legacy/superpowers/specs/2026-05-15-worker-persona-enforcement-design.md`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff-engineer-orchestrator`
  - `senior-backend-engineer`
  - `secure-software-engineer`
- `persona_selection_notes`:
  - `staff-engineer-orchestrator` fits because the primary artifact is a runtime contract change across multiple coupled skill surfaces
  - `senior-backend-engineer` is the best worker-capable built-in specialist because the task is boundary- and correctness-heavy rather than language-specific
  - `secure-software-engineer` is a reasonable reviewer persona for checking contract safety, drift, and unintended execution ambiguity
- `recommended_worker_mode_by_section`:
  - section 1: `validate-first`
  - section 2: `validate-first`
- `worker_mode_reasoning_by_section`:
  - section 1 modifies existing contract behavior and should verify the current authority chain before rewriting it
  - section 2 is a review and verification step, so validation posture should dominate over speed or iteration
- `goal_tuning_by_section`:
  - section 1: `validation-biased`
  - section 2: `safety-biased`
- `constraint_override_notes_by_section`:
  - section 1: if any implementation shortcut would merge `task_mode` and `work_mode`, preserve the existing `task_mode` boundary and reject the shortcut
  - section 2: if review suggests widening scope into reviewer or explorer behavior, keep this round bounded to worker behavior only
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - implementation execution: `superpowers:subagent-driven-development`
  - skill editing discipline: `superpowers:writing-skills`
  - code and contract changes: `superpowers:test-driven-development`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - approve one bounded implementation section covering the four aligned worker-mode contract surfaces
  - require a review pass that checks naming alignment, authority alignment, and worker execution-order alignment
  - keep the round standard `$ww` because it does not require strict-review treatment of a design-spec or implementation-plan target

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-worker-mode-contract-alignment: true
- `review_target_strategy`:
  - review the four modified runtime contract surfaces together
  - prioritize authority alignment over prose polish
  - treat any attempt to let the prompt re-derive mode from the brief as a blocking defect
- `controller_semantics_notes`:
  - no packet creation until the referenced dispatch plan is in `approved` state
  - if implementation evidence requires a worker-mode override, that override must first land in the dispatch plan before a new packet is created

## Rules

- Recommended personas are provisional until dispatch approval.
- Persona selection must cite the working brief, not just task keywords.
- The working brief is an analysis artifact, not the runtime approval record.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
- If the user requests `Revise`, update the working brief only if the analysis changed, then issue a new brief version for the next dispatch plan revision.
