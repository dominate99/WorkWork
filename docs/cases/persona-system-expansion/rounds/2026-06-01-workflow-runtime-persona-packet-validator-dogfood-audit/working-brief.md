# Working Brief: Runtime Persona Packet Validator Dogfood Audit

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: workflow-runtime-persona-packet-validator-dogfood-audit
- `case_slug`: persona-system-expansion
- `round_slug`: 2026-06-01-workflow-runtime-persona-packet-validator-dogfood-audit
- `case_root`: `docs/cases/persona-system-expansion/`
- `round_root`: `docs/cases/persona-system-expansion/rounds/2026-06-01-workflow-runtime-persona-packet-validator-dogfood-audit/`
- `created_at`: 2026-06-01
- `updated_at`: 2026-06-01
- `derived_from_user_request`: `new $ww round: runtime persona packet validator dogfood audit. Based on the completed and pushed packet dogfood pilot and packet validator expansion, audit whether the new validator covers real packet artifacts, negative drift fixtures, full-file hash fallback, explicit-revision excerpt identity, repo-relative path containment, multi-section snapshot, secondary reviewer lane, and repo suite integration. Only audit and classify; do not change validator, packet contract, runtime code, personas, or routing. Judge whether a canonical slice resolver design round is truly needed.`

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

- `goal`: audit the pushed runtime persona packet validator against its real packet artifacts and focused negative fixtures, classify any residual evidence gaps, and decide whether a canonical slice resolver design round is justified
- `artifact_type`: dogfood audit gap report
- `relevant_context`:
  - Commit `b97f1b3` added the runtime persona packet dogfood artifacts, packet validator, regression fixtures, and repo suite integration.
  - The validator scans persisted `docs/cases/**/packets/*.md` artifacts and checks approved dispatch derivation, persona identity, runtime role binding, ordered worker principles, reviewer read-only authority, review-target identity, and dispatch snapshots.
  - The focused regression suite includes positive worker/reviewer artifacts plus negative drift fixtures for role prompts, worker principles, review target hash, dispatch snapshot, absolute paths, malformed nested binding, multi-section snapshots, and secondary reviewer lanes.
  - Full-file SHA-256 review targets and explicit-revision excerpt identities intentionally have different verification semantics.
  - The next decision is whether excerpt-backed target evidence is strong enough to justify a canonical slice resolver design round now, or whether that design should remain deferred until stable slice semantics and a real excerpt-backed packet exist.
- `constraints`:
  - Produce only an audit/classification artifact, expected as `design-spec.md` with a gap-report structure.
  - Do not edit `tools/validate_ww_persona_packets.py`.
  - Do not edit packet contract surfaces.
  - Do not implement runtime code.
  - Do not add, remove, or edit persona records.
  - Do not change `docs/superpowers/personas/registry.yaml`.
  - Do not expand `task_routing`.
  - Do not add secondary tags.
  - Record any follow-up as a recommendation only.

## Risk And Structure

- `risk_lenses`:
  - mistaking validator implementation coverage for artifact-level proof
  - overlooking that explicit-revision excerpt identity is format-checked but not slice-recomputed
  - recommending canonical slice resolution before stable anchor and normalization semantics exist
  - treating negative fixtures as exhaustive path-containment coverage when they may only sample representative cases
  - blurring audit recommendations into unapproved validator changes
- `parallelism_assessment`:
  - Single-section audit is preferred because the implementation, fixtures, real packet artifacts, and recommendation must be classified together in one coherent report.
- `blocking_dependencies`:
  - Completed and pushed runtime persona packet dogfood pilot.
  - Completed and pushed runtime persona packet validator expansion.
  - Real worker and reviewer packet artifacts from the pilot round.
  - Focused packet validator regression suite and aggregate repo suite integration.
- `section_or_workstream_map`:
  - section-runtime-persona-packet-validator-dogfood-audit: inspect implementation, fixtures, real artifacts, and repo integration; classify coverage; decide whether canonical slice resolver design is warranted

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: runtime_persona_packet_validator_dogfood_gap_report
    - `artifact_kind`: dogfood_gap_report
    - `artifact_path`: `docs/cases/persona-system-expansion/rounds/2026-06-01-workflow-runtime-persona-packet-validator-dogfood-audit/design-spec.md`
    - `section_anchors`: packet validator dogfood findings
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/persona-system-expansion/case.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-06-01-workflow-runtime-persona-packet-validator-dogfood-audit/working-brief.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-06-01-workflow-runtime-persona-packet-validator-dogfood-audit/dispatch-plan.md`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-06-01-workflow-runtime-persona-packet-validator-dogfood-audit/design-spec.md`
- `shared_read_scope`:
  - `path_glob`: `README.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
  - `path_glob`: `docs/superpowers/personas/registry.yaml`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/**`
  - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-validator-expansion/**`
  - `path_glob`: `tools/validate_ww_persona_packets.py`
  - `path_glob`: `tools/test_validate_ww_persona_packets.py`
  - `path_glob`: `tools/validate_ww_repo.py`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `candidate_persona_sources`:
  - project registry checked: true
  - built-in fallback checked: true
  - project registry outcome: no stronger documentation/audit specialist or spec reviewer exists in `docs/superpowers/personas/registry.yaml` for this validator evidence audit
  - built-in fallback outcome: use `technical-writer` for the audit artifact and `spec-reviewer` for required review
  - fallback rationale when a built-in persona is recommended: built-in personas carry the strongest required-field fit for evidence classification, source-of-truth clarity, and spec-contract review
- `recommended_personas`:
  - `technical-writer`
    - runtime role: worker
    - source: built-in
    - owned scope: dogfood gap report artifact
    - baseline fit rationale: the work product is a maintainer-facing evidence audit that must separate proven validator behavior, fixture coverage, and deferred design questions
    - project-priority or built-in-fallback rationale: built-in fallback is used because the project registry has no stronger eligible documentation/audit specialist with worker-capable fields
    - enrichment fit rationale: quality bar and failure modes favor precise evidence classification and stable source-of-truth wording
    - role binding: `worker` via `agents/worker-prompt.md`
    - workflow bindings: `superpowers:writing-plans`, `superpowers:verification-before-completion`
  - `spec-reviewer`
    - runtime role: reviewer
    - source: built-in
    - owned scope: review the dogfood gap report for contract fidelity, evidence quality, and boundary discipline
    - baseline fit rationale: the target is a validator audit artifact whose value depends on coherent, testable findings and a justified follow-up decision
    - project-priority or built-in-fallback rationale: built-in fallback is used because the project registry has no stronger eligible reviewer-only spec persona
    - enrichment fit rationale: contract-first review matches the need to distinguish current proof from future slice-resolution design
    - role binding: `reviewer` via `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`, `superpowers:verification-before-completion`
- `persona_selection_notes`:
  - The section should classify coverage and residual evidence gaps, not patch validators or contracts.
  - The report should distinguish current full-file verification from explicit-revision excerpt identity checks.
  - Canonical slice resolver design should be recommended only if present evidence establishes a real need and stable enough semantics.
- `recommended_worker_mode_by_section`:
  - section-runtime-persona-packet-validator-dogfood-audit: conservative-first
- `worker_mode_reasoning_by_section`:
  - section-runtime-persona-packet-validator-dogfood-audit: the round is a bounded evidence audit over pushed validator work, so the worker should avoid speculative redesign.
- `goal_tuning_by_section`:
  - section-runtime-persona-packet-validator-dogfood-audit: audit-biased
- `constraint_override_notes_by_section`:
  - section-runtime-persona-packet-validator-dogfood-audit: any validator, contract, runtime, persona, registry, routing, or secondary-tag change must be recorded as a follow-up, not performed in this round.
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - audit execution: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - request approval to produce a packet validator dogfood gap report in `design-spec.md`

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-runtime-persona-packet-validator-dogfood-audit: true
- `review_target_strategy`:
  - Review the completed dogfood gap report for accurate implementation and fixture classification, faithful scope boundaries, and a justified canonical-slice-resolver recommendation.
- `controller_semantics_notes`:
  - Standard `$ww` round. No strict-review target is active.
  - No audit artifact creation begins until the dispatch plan is approved.

## Rules

- Recommended personas are provisional until dispatch approval.
- Persona selection must cite the working brief, not just task keywords.
- Persona selection must record source, runtime role, baseline fit, and project-priority or built-in-fallback rationale.
- The working brief recommends `worker mode` by section, but it does not act as the final execution authority.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
