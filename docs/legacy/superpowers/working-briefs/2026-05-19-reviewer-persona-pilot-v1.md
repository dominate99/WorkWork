# Working Brief: Reviewer Persona Pilot

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: reviewer-persona-pilot
- `created_at`: 2026-05-19
- `updated_at`: 2026-05-19
- `derived_from_user_request`: `2` after the orchestrator pilot commit, meaning open a reviewer persona pilot round

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

- `goal`: execute the reviewer persona pilot by enriching `secure-software-engineer` with judgment-oriented fields that sharpen materiality, risk focus, and escalation posture without weakening findings-only role boundaries
- `artifact_type`: built-in persona registry update plus approval-ready dispatch plan for a reviewer pilot round
- `relevant_context`:
  - phase 1 already defined the optional enrichment fields and migration rules
  - the orchestrator pilot is complete, so the next planned pilot in the implementation sequence is the reviewer layer
  - `secure-software-engineer` is the primary built-in reviewer persona and still uses only the pre-enrichment baseline
  - reviewer personas should become more distinct in what they reject and what they treat as material, but reviewer behavior rules must stay in prompts and packet contracts
  - this revision should be judged by a Jobs-like bar: the reviewer should get better at killing weak, risky, or user-hostile outcomes instead of sounding more thorough
- `constraints`:
  - limit the pilot to `secure-software-engineer`
  - keep changes inside `built-in-personas.yaml` and the round's planning artifacts
  - do not change `reviewer-prompt.md`, packet contracts, `SKILL.md`, or validators in this round
  - do not add new reviewer personas in this round

## Risk And Structure

- `risk_lenses`:
  - reviewer enrichment can accidentally restate findings-only role behavior instead of sharpening judgment
  - a generic "security expert" profile adds little routing value if it does not narrow what is considered material
  - if escalation language is weak, the reviewer will still imply certainty when uncertainty should be elevated
  - widening this round into prompt or packet edits would blur the difference between persona enrichment and runtime-role behavior
  - a reviewer that merely becomes more verbose will still miss the real point if it cannot distinguish "technically valid" from "should not ship"
- `parallelism_assessment`:
  - this round is tightly coupled around one persona record
  - one implementation lane is preferable because the record should be judged as a focused reviewer pilot, not a broad registry sweep
- `blocking_dependencies`:
  - the phase 1 contract and migration rules must remain the source of truth
  - the existing reviewer role contract must remain unchanged during this pilot
- `section_or_workstream_map`:
  - section 1: enrich the reviewer pilot persona with sharper judgment structure
  - section 2: review the pilot for materiality clarity, risk focus, and contract compliance

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: `persona_strategy_design`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/legacy/superpowers/specs/2026-05-19-persona-enrichment-strategy-design.md`
  - `section_anchors`: `High-Leverage Enrichment Order`, `Phase 1 Contract Decisions`, `Phase 1 Migration Rules`
  - `artifact_id`: `persona_strategy_plan`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/legacy/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
  - `section_anchors`: `Enrich reviewer personas second`
  - `artifact_id`: `persona_registry_rules`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `section_anchors`: `Optional Persona Enrichment Fields`, `Phase 1 Compatibility Boundary`, `Migration Rules`
  - `artifact_id`: `built_in_personas`
  - `artifact_kind`: `data`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `section_anchors`: none
  - `artifact_id`: `reviewer_role_contract`
  - `artifact_kind`: `prompt`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/agents/reviewer-prompt.md`
  - `section_anchors`: `Responsibilities`, `Operating rules`
- `exclusive_write_scope`:
  - `path_glob`: `docs/legacy/superpowers/working-briefs/2026-05-19-reviewer-persona-pilot-v1.md`
  - `path_glob`: `docs/legacy/superpowers/dispatch-plans/2026-05-19-reviewer-persona-pilot.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
- `shared_read_scope`:
  - `path_glob`: `docs/legacy/superpowers/specs/2026-05-19-persona-enrichment-strategy-design.md`
  - `path_glob`: `docs/legacy/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/agents/reviewer-prompt.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff-engineer-orchestrator`
  - `secure-software-engineer`
  - `creative-director-orchestrator`
- `persona_selection_notes`:
  - `staff-engineer-orchestrator` fits the top-level artifact because this is a bounded registry-edit round with clear contract boundaries
  - `secure-software-engineer` is the direct pilot target and should be treated as a judgment-sharpening exercise, not a role rewrite
  - `creative-director-orchestrator` is the stronger revision lens here because this pilot needs a harsher bar for what should be rejected, not just a more organized checklist
- `recommended_worker_mode_by_section`:
  - section 1: `plan-first`
  - section 2: `validate-first`
- `worker_mode_reasoning_by_section`:
  - section 1 should design the reviewer persona around a coherent materiality posture instead of filling fields mechanically
  - section 2 should validate that the result sharpens judgment without leaking into prompt-level behavior
- `goal_tuning_by_section`:
  - section 1: `safety-biased`
  - section 2: `validation-biased`
- `constraint_override_notes_by_section`:
  - section 1: prefer sharper materiality judgment over generic reviewer completeness; if a field does not change what gets blocked or escalated, sharpen it or remove it
  - section 2: block any wording that merely repeats reviewer prompt behavior instead of defining viewpoint
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - approve one bounded registry-edit lane for the reviewer pilot
  - require the pilot to make `secure-software-engineer` more precise about materiality, risk focus, and escalation
  - review the pilot with a ruthless product-and-release bar: reject vague security gravitas, weak blocking criteria, and anything that does not help the reviewer kill bad outcomes faster
  - defer prompt, packet, and validator changes to later rounds

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-reviewer-pilot: true
- `review_target_strategy`:
  - review whether the reviewer persona gains a clearer materiality bar
  - review whether the enrichment makes risk focus more specific instead of more verbose
  - treat role-behavior duplication, generic reviewer prose, or "competent but not decisive" judgment as blocking
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
