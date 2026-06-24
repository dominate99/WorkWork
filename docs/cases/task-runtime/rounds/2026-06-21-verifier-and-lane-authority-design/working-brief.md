# Working Brief: Verifier And Lane Authority Design

## Artifact Metadata

- `schema_version`: 2
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: verifier-and-lane-authority-design
- `case_slug`: task-runtime
- `round_slug`: 2026-06-21-verifier-and-lane-authority-design
- `case_root`: `docs/cases/task-runtime/`
- `round_root`: `docs/cases/task-runtime/rounds/2026-06-21-verifier-and-lane-authority-design/`
- `created_at`: 2026-06-21
- `updated_at`: 2026-06-21
- `derived_from_user_request`: `$ww round：verifier and lane authority design。基于已完成的 lifecycle foundation，设计 verifier 权限、worker/reviewer/verifier 身份隔离、verification lane schema、evidence records、baseline/risk-triggered lane selection，以及 model capability profiles。只产出 design spec；不实现 bindings/personas，不改 validator，不实现 hooks、repair、scoring 或 runtime activation。`

## Round Intent

- `quality_mode`: standard
- `lifecycle_protocol_recommendation`: legacy

## Gate State

- `estimation_complete`: true
- `brief_status`: ready
- `brief_version`: 1

## Routing

- `task_routing`: `design/ads/product`
- `orchestrator_choice`: `pm-orchestrator`

## Core Intent

- `goal`: produce an implementation-ready verifier and lane authority design that supplies the next mandatory capability layer without activating `task-runtime-v1`
- `artifact_type`: design specification
- `relevant_context`:
  - The umbrella runtime design already separates worker, verifier, reviewer, orchestrator, and human authority.
  - Lifecycle foundation revision 2 preserves `runtime_state` authority and requires formal verification before review and after artifact-changing fixes.
  - The packaged runtime currently has worker, reviewer, orchestrator, and explorer role bindings, but no verifier role binding or verifier persona.
  - Existing reviewer lanes and persona selection rules must remain active and unchanged during this design-only round.
  - `task-runtime-v1` cannot activate until verifier authority, required verification lanes, review progression, scoring, and close-gate handling are implemented, verified, and approved.
- `constraints`:
  - Produce only `design-spec.md` plus round-local lifecycle records.
  - Define verifier permissions, prohibitions, command authority, and evidence ownership.
  - Define worker/reviewer/verifier identity isolation at execution, agent, packet, attempt, and immutable-target layers.
  - Define verification lane records, command records, aggregate outcomes, and stale-evidence semantics.
  - Define baseline lane selection by task profile and additive risk-triggered lane selection with durable inclusion/exclusion rationale.
  - Define model capability profiles independently from persona and runtime role, including resolution, fallback, and capability-floor behavior.
  - Do not implement verifier bindings, prompts, personas, project-registry records, packets, or runtime controller code.
  - Do not modify active contracts, templates, validators, routing, hooks, repair policy, scoring, quality gates, or runtime activation.
  - Do not decide detailed model-to-provider mappings; design capability labels and resolution evidence only.

## Risk And Structure

- `risk_lenses`:
  - allowing worker self-checks to satisfy formal verification
  - allowing one agent or execution identity to produce and formally verify the same target
  - conflating verifier evidence with reviewer findings or human approval
  - lane records that cannot detect target drift or aggregate multi-artifact staleness
  - risk-triggered lanes becoming keyword heuristics without durable rationale
  - model profiles becoming hard-coded model names or silent below-floor fallbacks
  - verification commands mutating external state without renewed human approval
  - designing hooks, repair, scoring, or activation behavior prematurely
- `parallelism_assessment`:
  - Use one serial design section because authority, lane schema, evidence identity, and capability profiles form one coupled contract.
- `blocking_dependencies`:
  - approved umbrella task-runtime design
  - completed lifecycle foundation design revision 11
  - completed lifecycle foundation implementation revision 2
  - current persona registry, packet contract, role bindings, and reviewer lane rules as compatibility inputs
- `section_or_workstream_map`:
  - section-verifier-lane-authority-design: produce and review one cohesive design specification

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: verifier_lane_authority_design
    - `artifact_kind`: design_spec
    - `artifact_path`: `docs/cases/task-runtime/rounds/2026-06-21-verifier-and-lane-authority-design/design-spec.md`
    - `section_anchors`: authority model, identity isolation, lane schema, evidence, selection, model profiles, acceptance criteria
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/task-runtime/case.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-21-verifier-and-lane-authority-design/working-brief.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-21-verifier-and-lane-authority-design/dispatch-plan.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-21-verifier-and-lane-authority-design/design-spec.md`
- `shared_read_scope`:
  - `path_glob`: `docs/superpowers/specs/2026-06-19-workwork-task-runtime-design.md`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-19-task-runtime-lifecycle-foundation-design/**/*`
  - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/**/*`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/agents/**/*`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/**/*`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `path_glob`: `docs/superpowers/personas/registry.yaml`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `candidate_persona_sources`:
  - project registry checked: true
  - built-in fallback checked: true
  - project registry outcome: no eligible project worker or reviewer persona covers portable verifier authority and model-capability contract design
  - built-in fallback outcome: use `senior-backend-engineer` for technical contract drafting, `spec-reviewer` for requirement fidelity, and `secure-software-engineer` for authority-isolation review
  - fallback rationale when a built-in persona is recommended: the design is portable WorkWork runtime architecture, and the built-in personas provide the strongest eligible role and risk fit
- `recommended_personas`:
  - `senior-backend-engineer`
    - runtime role: worker
    - source: built-in
    - owned scope: draft the verifier authority, lane/evidence, selection, and model-profile design
    - baseline fit rationale: the work defines durable runtime interfaces, identity boundaries, command records, and resolution contracts
    - project-priority or built-in-fallback rationale: no project worker persona covers portable WorkWork runtime architecture, so built-in fallback applies
    - enrichment fit rationale: explicit interfaces and data-integrity bias fit evidence and authority contracts
    - role binding: `worker` via `agents/worker-prompt.md`
    - workflow bindings: `superpowers:brainstorming`, `superpowers:verification-before-completion`
  - `spec-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: review completeness, determinism, compatibility, acceptance criteria, and exclusions
    - baseline fit rationale: the target is an implementation-authorizing runtime specification
    - project-priority or built-in-fallback rationale: no project reviewer covers portable verifier contract fidelity, so built-in fallback applies
    - enrichment fit rationale: contract-first review fits authority and schema decisions
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`, `superpowers:verification-before-completion`
  - `secure-software-engineer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: review self-approval prevention, identity separation, command authority, fallback safety, and privilege escalation boundaries
    - baseline fit rationale: verifier authority is a trust-boundary design even though no security feature is being implemented
    - project-priority or built-in-fallback rationale: no stronger eligible project reviewer covers portable authority isolation, so built-in fallback applies
    - enrichment fit rationale: policy-integrity and least-authority posture fit the dominant failure modes
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`, `superpowers:verification-before-completion`
- `persona_selection_notes`:
  - Do not invent or add a verifier persona in this round; verifier persona coverage is an output requirement for the later implementation round.
  - Keep current reviewer runtime role for both review lanes; they inspect the design but do not exercise future verifier authority.
- `recommended_worker_mode_by_section`:
  - section-verifier-lane-authority-design: plan-first
- `worker_mode_reasoning_by_section`:
  - section-verifier-lane-authority-design: the approved lifecycle and umbrella design provide fixed constraints, but exact schemas and authority interactions must be resolved before prose production.
- `goal_tuning_by_section`:
  - section-verifier-lane-authority-design: validation-biased
- `constraint_override_notes_by_section`:
  - section-verifier-lane-authority-design: implementation, personas, bindings, validators, hooks, repair, scoring, and activation remain strictly excluded.
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - design drafting: `superpowers:brainstorming`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval for one serial design section, then draft one normative spec and run independent spec and authority-isolation reviews

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-verifier-lane-authority-design: true
- `review_target_strategy`:
  - Freeze the complete design spec as one immutable full-file target; run separate spec and authority-isolation reviewer packets against the same revision.
- `controller_semantics_notes`:
  - This design round remains `lifecycle_protocol: legacy` and does not activate `task-runtime-v1`.
  - The design spec is required for the round goal but is not a `$www` strict-review target.
  - No reviewer packet may be created until plan approval and a stable design revision exist.

## Rules

- Persist the working brief before dispatch-plan creation.
- Persona selection must cite source, runtime role, and project-priority or built-in-fallback rationale.
- Keep worker, reviewer, verifier, orchestrator, and human authorities distinct in the future design.
- No packet creation until the referenced dispatch plan is approved.
