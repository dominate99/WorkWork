# Working Brief Template

Use this template after estimation and before any persona dispatch.

## Artifact Metadata

- `schema_version: 2`
- `brief_version`
- `brief_status`
- `topic_slug`
- `case_slug`
- `round_slug`
- `case_root`
- `round_root`
- `created_at`
- `updated_at`
- `derived_from_user_request`

## Round Intent

- `quality_mode: standard | strict`
- `lifecycle_protocol_recommendation: legacy | task-runtime-v1`

Lifecycle recommendation rules:

- the working brief records analysis and recommendation only; it does not own the active lifecycle protocol
- default the recommendation to `legacy`
- recommend `task-runtime-v1` only when the round intends explicit activation and every mandatory capability in `task-runtime-lifecycle.md`, `task-runtime-verification.md`, and `task-runtime-missing-capabilities.md` is available
- the approved dispatch plan owns the final round protocol

## Gate State

- `estimation_complete: true|false`
- `brief_status: draft|ready`
- `brief_version`

## Routing

- `task_routing`: `code/programming` | `design/ads/product` | `video/creative`
- `orchestrator_choice`

## Core Intent

- `goal`
- `artifact_type`
- `relevant_context`
- `constraints`

## Risk And Structure

- `risk_lenses`
- `parallelism_assessment`
- `blocking_dependencies`
- `section_or_workstream_map`

## Scope Preparation

- `artifact_mappings`
- `exclusive_write_scope`
- `shared_read_scope`
- `depends_on_sections`
- `parallel_safe_with_sections`

Required inline artifact-mapping fields when registry fallback is used:

- `artifact_id`
- `artifact_kind`
- `artifact_path`
- `section_anchors` when `doc_section` will be referenced

Rules:

- resolve `artifact_id` through `docs/superpowers/artifact-registry.yaml` when available
- if the registry is absent, define inline artifact mappings before dispatch
- aggregate multi-file work must not hide behind a single multi-path `artifact_id`
- canonical scope grammar:
  - `path_glob`
  - `doc_section`
  - `artifact_id`
- `doc_section` resolves to `artifact_path + section_anchor`
- one `artifact_id` resolves to exactly one canonical `artifact_path`
- non-file-centric fallback still requires a persisted `artifact_path`; `section_anchor` is optional, but a bare conceptual scope cannot be marked parallel-safe or used for reviewer targeting
- collision rules:
  - write/write overlap blocks parallel worker dispatch
  - write/read overlap is allowed only for reviewer or explorer lanes that are read-only
  - cross-type collisions are checked after normalization, not by original label
- `doc_section` overlapping a file matched by a `path_glob` is a collision unless the packet is read-only

Artifact-layout rules:

- `case_slug` identifies the long-lived workstream for this round
- `round_slug` identifies this bounded `$ww` or `$www` cycle inside that case
- `case_root` must resolve to `docs/cases/<case_slug>/`
- `round_root` must resolve to `docs/cases/<case_slug>/rounds/<round_slug>/`
- new rounds write their canonical artifacts under `round_root`; pre-cutover type-based artifacts are legacy history only and must not be treated as active generation targets

## Persona And Workflow Guidance

- `candidate_persona_sources`
- `recommended_personas`
- `persona_selection_notes`
- `recommended_worker_mode_by_section`
- `worker_mode_reasoning_by_section`
- `goal_tuning_by_section`
- `constraint_override_notes_by_section`
- `workflow_bindings_by_stage`
- `dispatch_recommendation`
- `verification_authority_notes` when a future `task-runtime-v1` round will need formal verifier lanes
- `missing_capability_preparation` when a future `task-runtime-v1` round will need internal hooks, quality gates/scoring, repair/re-verification, close gates, final human judgment, recovery requirements, or checkpoints

`candidate_persona_sources` should record:

- project registry checked: true|false
- built-in fallback checked: true|false
- project registry outcome
- built-in fallback outcome
- fallback rationale when a built-in persona is recommended

Each `recommended_personas` entry should record:

- persona id
- runtime role: `orchestrator` | `worker` | `reviewer` | `explorer`
- source: `project` | `built-in`
- owned scope, review target, or investigation target
- baseline required-field fit rationale grounded in the working brief
- project-priority or built-in-fallback rationale
- enrichment fit rationale when optional enrichment fields affected the recommendation
- role binding from `agents/openai.yaml`
- prompt asset used for launch assembly
- workflow bindings

Persona recommendation rules:

- project registry priority applies only after the persona satisfies the relevant runtime-role gate and required-field fit
- use a project persona only when it is stronger than the built-in fallback or adds project-specific value the built-in cannot carry
- record built-in fallback explicitly when no project persona is eligible or stronger
- worker recommendations must pass the worker-capability gate before appearing as worker candidates
- reviewer recommendations must pass the reviewer-only gate before appearing as review-lane candidates
- do not recommend a persona from keywords alone; cite the working brief goal, constraints, risks, scope, or artifact type

## Grill-Me Decision Log

The orchestrator owns this log. The `grill-me` explorer remains read-only and is applied inline during planning.

Use one entry per decision:

- Decision ID:
- State: open | confirmed | deferred
- Question:
- User-Confirmed Answer:
- Recommendation Offered:
- Rationale Or Repository Evidence:
- Dependencies Resolved:
- Dependent Branches Unblocked:

Rules:

- create or update an entry only when `grill-me` is explicitly active
- keep `State: open` until the user explicitly confirms an answer
- do not treat the recommended answer as confirmation
- record repository-resolved facts as evidence without asking the user to decide them
- use confirmed entries as inputs to later design specs and implementation plans
- keep round approval and runtime lifecycle state in `dispatch-plan.md`
- when the user stops grilling, mark the current unresolved branch `deferred`

## Runtime Preparation

- `required_for_goal_by_section`
- `review_target_strategy`
- `controller_semantics_notes`
- `verification_lane_preparation` when `lifecycle_protocol_recommendation: task-runtime-v1`

`verification_lane_preparation` is dormant planning analysis unless the approved
dispatch plan selects `task-runtime-v1`. When present, it should record:

- candidate baseline verifier lanes by task profile
- candidate risk-triggered verifier lanes with rationale
- expected target selector inputs
- expected evidence kinds: command, artifact, and/or environment
- expected model capability profile and minimum floor
- explicit note that legacy rounds do not use these records as lifecycle authority

`missing_capability_preparation` is dormant planning analysis unless the approved
dispatch plan selects `task-runtime-v1`. When present, it should record:

- expected internal hooks by lifecycle phase
- expected quality gate profile and hard blockers
- expected score dimensions and required evidence inputs
- expected repair authorization triggers and target-lineage rules
- expected re-verification requirements after repair
- expected close-gate inputs and final human judgment package
- expected recovery requirement and checkpoint triggers
- explicit note that legacy rounds do not use these records as lifecycle authority

## Rules

- Recommended personas are provisional until dispatch approval.
- Persona selection must cite the working brief, not just task keywords.
- Persona selection must record source, runtime role, baseline fit, and project-priority or built-in-fallback rationale.
- The working brief recommends `worker mode` by section, but it does not act as the final execution authority.
- `recommended_worker_mode_by_section` must be derived from task structure, scope shape, and risk, not from persona labels alone.
- User-provided scope limits, prohibitions, and delivery boundaries must be captured in `constraints` before any worker-mode recommendation is made.
- If a recommended `worker mode` conflicts with user constraints, record the tension and the best-effort fallback in `constraint_override_notes_by_section`.
- `goal_tuning_by_section` may only soften or sharpen the recommended mode posture; it must not replace the structure-driven recommendation inside the working brief.
- The working brief is an analysis artifact, not the runtime approval record.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
- If the user requests `Revise`, update the working brief only if the analysis changed, then issue a new brief version for the next dispatch plan revision.
- Formal verifier lane planning follows `task-runtime-verification.md` and remains dormant unless the approved dispatch plan selects `task-runtime-v1`.
- Missing capability planning follows `task-runtime-missing-capabilities.md` and remains dormant unless the approved dispatch plan selects `task-runtime-v1`.
