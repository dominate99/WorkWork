# Dispatch Plan: Persona Enrichment Phase 1

- Date: 2026-05-19
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Plan State: completed
- Last Approved Revision: none
- Rollback Baseline Revision: none
- Task Routing: code/programming
- Main Orchestrator: staff-engineer-orchestrator

## Strict Review Runtime State

```yaml
strict_review:
  mode: standard
  target: none
  state: idle
  cycle_count: 0
```

## Preconditions

- Estimation Complete: true
- Working Brief Status: ready

> Do not launch any real subagent until the preconditions are satisfied and `Plan State: approved`.

## Source Context

- User Request: `$ww 把这份策略直接转成 implementation plan` followed by user approval to proceed with phase 1 execution
- Working Brief Reference: `docs/legacy/superpowers/working-briefs/2026-05-19-persona-enrichment-phase1-v1.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: execute phase 1 of persona enrichment by formalizing enriched persona-model fields and migration rules before any registry rollout or runtime adoption
- Relevant Context: the repository already has an approved persona-enrichment design spec and implementation plan, but phase 1 still needs a bounded execution round to define contract-level fields and transition rules
- Constraints:
  - keep phase 1 additive and documentation-level only
  - preserve the separation between `persona`, `runtime_role`, role prompt behavior, and worker `work_mode`
  - do not mutate persona registry data, `SKILL.md`, packet contracts, prompts, or validators in this round
- Risks:
  - new fields could become stylistic decoration instead of operational judgment structure
  - migration rules could be too vague to protect routing during partial adoption
  - overreaching into registry data or runtime contracts would collapse phase boundaries and increase rollback cost
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Persona Model Contract Update

- Section ID: section-persona-model-contract
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: senior-backend-engineer
- Planned Reviewer Persona: pm-orchestrator
- Planned Specialist Personas: senior-backend-engineer
- Planned Scope:
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `docs/legacy/superpowers/specs/2026-05-19-persona-enrichment-strategy-design.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: the first execution step should define the enriched persona fields and the compatibility boundary in canonical documentation before any rollout starts
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: validate-first
- Worker Mode Rationale: this section should validate the current contract model before adding any new persona-field guidance
- Goal Tuning: validation-biased
- Constraint Interaction Rule: preserve the current role-contract model and keep all new fields additive and documentation-only
- Planned Review Lanes:
  - Lane ID: lane-persona-contract-review
  - Lane Type: spec-review
  - Reviewer Persona: pm-orchestrator
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/legacy/superpowers/working-briefs/2026-05-19-persona-enrichment-phase1-v1.md`
    - `path_glob`: `docs/legacy/superpowers/dispatch-plans/2026-05-19-persona-enrichment-phase1.md`
    - `path_glob`: `docs/legacy/superpowers/specs/2026-05-19-persona-enrichment-strategy-design.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `shared_read_scope`:
    - `path_glob`: `docs/legacy/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `path_glob`: `docs/superpowers/personas/registry.yaml`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: `persona_strategy_design`
    - `artifact_kind`: `doc`
    - `artifact_path`: `docs/legacy/superpowers/specs/2026-05-19-persona-enrichment-strategy-design.md`
    - `section_anchors`: `What To Add To Personas`, `What Not To Do`, `Recommended Next Implementation Track`
    - `artifact_id`: `persona_registry_rules`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - `section_anchors`: `Required Persona Fields`, `Selection Rules`, `Prompt Binding Roles`
    - `artifact_id`: `persona_strategy_plan`
    - `artifact_kind`: `doc`
    - `artifact_path`: `docs/legacy/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
    - `section_anchors`: none
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

### Section: Persona Migration Rules

- Section ID: section-persona-migration-rules
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: senior-backend-engineer
- Planned Reviewer Persona: pm-orchestrator
- Planned Specialist Personas: pm-orchestrator
- Planned Scope:
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `docs/legacy/superpowers/specs/2026-05-19-persona-enrichment-strategy-design.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: phase 1 is not complete unless the repo has explicit transition rules for partially enriched persona catalogs
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: plan-first
- Worker Mode Rationale: after the enriched field set is stable, the migration posture should be designed as one coherent rollout policy
- Goal Tuning: safety-biased
- Constraint Interaction Rule: do not turn migration guidance into implicit approval for registry rollout, runtime adoption, or validator expansion
- Planned Review Lanes:
  - Lane ID: lane-persona-migration-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/legacy/superpowers/working-briefs/2026-05-19-persona-enrichment-phase1-v1.md`
    - `path_glob`: `docs/legacy/superpowers/dispatch-plans/2026-05-19-persona-enrichment-phase1.md`
    - `path_glob`: `docs/legacy/superpowers/specs/2026-05-19-persona-enrichment-strategy-design.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `shared_read_scope`:
    - `path_glob`: `docs/legacy/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `path_glob`: `docs/superpowers/personas/registry.yaml`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `depends_on_sections`:
    - `section-persona-model-contract`
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: `persona_strategy_design`
    - `artifact_kind`: `doc`
    - `artifact_path`: `docs/legacy/superpowers/specs/2026-05-19-persona-enrichment-strategy-design.md`
    - `section_anchors`: `What To Add To Personas`, `Recommended Next Implementation Track`
    - `artifact_id`: `persona_registry_rules`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - `section_anchors`: `Required Persona Fields`, `Selection Rules`
    - `artifact_id`: `persona_strategy_plan`
    - `artifact_kind`: `doc`
    - `artifact_path`: `docs/legacy/superpowers/plans/2026-05-19-persona-enrichment-strategy.md`
    - `section_anchors`: none
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Persona Model Contract Update

- Section ID: section-persona-model-contract
- Runtime State: complete
- Active Execution ID:
- Active Packet ID:
- Active Agent ID:
- Active Attempt ID:
- Active Worker Mode: validate-first
- Mode Change History:
  - Previous Mode:
  - New Mode:
  - Trigger Evidence:
  - Approved By:
  - Changed At:
- Execution Records:
  - Execution ID:
  - Role:
  - Status:
  - Owned Scope:
  - Started At:
  - Finished At:
- Packet Records:
  - Packet ID:
  - Execution ID:
  - Stage:
  - Template Path:
  - Review Target Ref:
  - Supersedes Attempt ID:
  - Accepts Late Results:
- Attempt Records:
  - Attempt ID:
  - Packet ID:
  - Agent ID:
  - Return Status:
  - Runtime State After Return:
  - Launched At:
  - Closed At:
  - Result Summary:
  - Result Artifact Location:
- Attempt Count: 0
- Last Update At: 2026-05-19 America/Los_Angeles
- Next Action: none
- Active Write Scope:
- Result Summary: persona-registry contract updated with optional enrichment fields, compatibility boundary, selection posture, and migration rules for phase 1
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns:
  - enriched fields must remain judgment-oriented and non-theatrical
  - role behavior must not leak into persona-field definitions
- Blocker Reason:
- Close State: open
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

### Section: Persona Migration Rules

- Section ID: section-persona-migration-rules
- Runtime State: complete
- Active Execution ID:
- Active Packet ID:
- Active Agent ID:
- Active Attempt ID:
- Active Worker Mode: plan-first
- Mode Change History:
  - Previous Mode:
  - New Mode:
  - Trigger Evidence:
  - Approved By:
  - Changed At:
- Execution Records:
  - Execution ID:
  - Role:
  - Status:
  - Owned Scope:
  - Started At:
  - Finished At:
- Packet Records:
  - Packet ID:
  - Execution ID:
  - Stage:
  - Template Path:
  - Review Target Ref:
  - Supersedes Attempt ID:
  - Accepts Late Results:
- Attempt Records:
  - Attempt ID:
  - Packet ID:
  - Agent ID:
  - Return Status:
  - Runtime State After Return:
  - Launched At:
  - Closed At:
  - Result Summary:
  - Result Artifact Location:
- Attempt Count: 0
- Last Update At: 2026-05-19 America/Los_Angeles
- Next Action: none
- Active Write Scope:
- Result Summary: strategy design spec updated with explicit phase 1 contract decisions, migration rules, and exit criteria
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns:
  - partial enrichment must not bias routing without a documented fallback posture
  - migration rules must protect the repo from silent schema fragmentation
- Blocker Reason:
- Close State: open
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Persona Model Contract Update

- Section ID: section-persona-model-contract
- Review Target Strategy:
  - validate that the enriched fields define operational judgment rather than stylistic persona prose
  - validate that the compatibility boundary preserves current runtime-role and prompt semantics
  - validate that no phase 1 wording implies immediate registry or runtime rollout
- Review Lane Records:
  - Lane ID: lane-persona-contract-review
  - Lane Type: spec-review
  - Reviewer Persona: pm-orchestrator
  - Execution ID:
  - Packet ID:
  - Attempt ID:
  - Review Target Ref:
    - Artifact Path:
    - Artifact Kind:
    - Artifact Revision:
    - Schema Version:
    - Section Anchor:
    - Content Hash:
  - Reviewer Findings:
    - no material findings; the new persona fields remain additive, judgment-oriented, and clearly separated from runtime-role behavior
  - Orchestrator Synthesis:
    - phase 1 stayed within the approved documentation boundary and established a clean contract surface for later persona pilots
  - Strict Review Outcome: none
  - Persistence rule: pre-approval plans must preserve this review-lane structure and outcome field pattern; `Review Status` must not reappear here, and durable review-lane data must retain `Reviewer Findings`, `Orchestrator Synthesis`, and the `Strict Review Outcome` field pattern.
  - Applicability rule: `Strict Review Outcome` is required when a strict-review target or durable strict-review result applies; otherwise keep the same field pattern without creating a second schema for valid non-strict lanes.
  - Invalid state note: `Review Status` reappears or durable strict-review outcome data is dropped when applicable.

### Section: Persona Migration Rules

- Section ID: section-persona-migration-rules
- Review Target Strategy:
  - validate that migration guidance keeps non-enriched personas selectable during transition
  - validate that rollout boundaries stay explicit and phase-scoped
  - validate that migration rules are concrete enough to guide later persona pilots
- Review Lane Records:
  - Lane ID: lane-persona-migration-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Execution ID:
  - Packet ID:
  - Attempt ID:
  - Review Target Ref:
    - Artifact Path:
    - Artifact Kind:
    - Artifact Revision:
    - Schema Version:
    - Section Anchor:
    - Content Hash:
  - Reviewer Findings:
    - no material findings; migration guidance preserves required-field selection and prevents partial enrichment from becoming a silent hard gate
  - Orchestrator Synthesis:
    - the rollout posture is now concrete enough to guide orchestrator, reviewer, and worker pilot rounds without forcing premature runtime adoption
  - Strict Review Outcome: none
  - Persistence rule: pre-approval plans must preserve this review-lane structure and outcome field pattern; `Review Status` must not reappear here, and durable review-lane data must retain `Reviewer Findings`, `Orchestrator Synthesis`, and the `Strict Review Outcome` field pattern.
  - Applicability rule: `Strict Review Outcome` is required when a strict-review target or durable strict-review result applies; otherwise keep the same field pattern without creating a second schema for valid non-strict lanes.
  - Invalid state note: `Review Status` reappears or durable strict-review outcome data is dropped when applicable.

- Human Decision: Approve
- Revision Notes:
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level `plan_state` is derived from `required_for_goal`

## Ordering And Parallelism

- Blocking work first: `section-persona-model-contract`
- Parallel sections: none
- Review loop per section: draft -> reviewer findings -> orchestrator synthesis -> human judgment

## Approval Block

- Required Human Choice (rendered labels):
  - `1. Approve`
  - `2. Revise`
  - `3. Stop`
- Numeric Reply Mapping:
  - `1` -> `Approve`
  - `2` -> `Revise`
  - `3` -> `Stop`
- Canonical Decision Values: `Approve` | `Revise` | `Stop`
- Accepted Word Replies: `Approve` | `Revise` | `Stop`
- Current Choice: Approve
- Approved By: user
- Approval Time: 2026-05-19 America/Los_Angeles
- Notes: this phase-1 round is scoped to documentation-level persona-model and migration-rule work only
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial execution round for persona enrichment phase 1
- Supersedes Revision:

## Dispatch Log

- Agents Launched: none
- Retry Events:
- Close Events:
- Review Lane Transitions:
  - approved persona-enrichment strategy reviewed
  - implementation plan used to scope phase 1 work
  - working brief persisted for phase 1
  - dispatch plan drafted for documentation-only execution
  - `persona-registry.md` updated with optional enrichment fields, compatibility boundary, selection posture, and migration rules
  - phase 1 strategy design spec updated with contract decisions and exit criteria
  - bounded review found no material findings
- Launch Time: 2026-05-19 America/Los_Angeles
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record

