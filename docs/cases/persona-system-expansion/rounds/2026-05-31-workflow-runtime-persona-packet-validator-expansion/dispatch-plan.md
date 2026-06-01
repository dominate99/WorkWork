# Dispatch Plan: Runtime Persona Packet Validator Expansion

- Date: 2026-05-31
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: persona-system-expansion
- Round Slug: 2026-05-31-workflow-runtime-persona-packet-validator-expansion
- Case Root: `docs/cases/persona-system-expansion/`
- Round Root: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-validator-expansion/`
- Plan State: completed
- Last Approved Revision: 1
- Rollback Baseline Revision: 1
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

> Do not create packet artifacts or launch any real subagent until the preconditions are satisfied and `Plan State: approved`.

## Source Context

- User Request: `Open a new $ww round: runtime persona packet validator expansion. Based on the approved runtime persona packet dogfood pilot, add focused repository validation for packet artifacts and resolve the PKT-002 launch-snapshot validation strategy. Keep the round narrow: do not implement runtime assembly code, change the packet contract, add personas, change the project registry, expand routing, or add secondary tags.`
- Working Brief Reference: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-validator-expansion/working-brief.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`
- Approved Dogfood Evidence: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/design-spec.md`

## Dispatch Summary

- Goal: add generic packet-artifact validation, integrate it into the repository suite, and resolve PKT-002 with cross-checks rather than a generic dispatch-template expansion
- Relevant Context: the approved dogfood pilot created one worker packet and one reviewer packet with faithful persona provenance, role prompt binding, worker principles, and immutable reviewer-target evidence
- Constraints:
  - validate persisted packet artifacts under `docs/cases/**/packets/*.md`
  - cross-check prompt path from runtime role and worker principles from selected persona definition
  - validate approved dispatch launch snapshots as additional evidence when present
  - do not require new launch-snapshot fields in every dispatch template
  - do not implement runtime code or change packet contract, personas, project registry, routing, or secondary tags
- Risks:
  - one-off pilot validation instead of generic discovery
  - loose parsing that misses drift
  - validator behavior that overclaims runtime-code proof
  - accidental active-contract expansion beyond PKT-002
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Runtime Persona Packet Validator Expansion

- Section ID: section-runtime-persona-packet-validator-expansion
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: test-quality-engineer
- Planned Reviewer Persona: code-quality-reviewer
- Planned Reviewer Persona Source: built-in
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: validator parser correctness, invariant coverage, and repo-suite integration make the built-in code-quality reviewer the strongest eligible reviewer-only match
- Planned Specialist Personas:
  - Persona ID: test-quality-engineer
    - Source: built-in
    - Runtime Role: worker
    - Selection Rationale: the dominant work is regression-oriented packet validator implementation; built-in fallback is used because no stronger eligible project worker persona covers repository validation
- Planned Scope:
  - `tools/validate_ww_persona_packets.py`
  - `tools/test_validate_ww_persona_packets.py`
  - `tools/validate_ww_repo.py`
  - `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `README.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: convert the approved packet dogfood evidence into reusable repository checks while keeping packet contract and template shape stable
- Planned Workflow Bindings:
  - `superpowers:test-driven-development`
  - `superpowers:systematic-debugging`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: test-first
- Worker Mode Rationale: define packet drift checks against the real pilot artifacts before integrating the validator into the aggregate suite
- Goal Tuning: validation-biased
- Constraint Interaction Rule: packet contract, runtime assembly code, personas, project registry, routing, and secondary tags remain read-only; guidance edits must describe only the approved packet-validator behavior
- Planned Review Lanes:
  - Lane ID: lane-runtime-persona-packet-validator-expansion-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: inspect parser correctness, generic discovery, invariant coverage, failure messages, suite integration, and PKT-002 scope control
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/persona-system-expansion/case.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-validator-expansion/working-brief.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-validator-expansion/dispatch-plan.md`
    - `path_glob`: `tools/validate_ww_persona_packets.py`
    - `path_glob`: `tools/test_validate_ww_persona_packets.py`
    - `path_glob`: `tools/validate_ww_repo.py`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `README.md`
  - `shared_read_scope`:
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `path_glob`: `docs/superpowers/personas/registry.yaml`
    - `path_glob`: `docs/cases/**/packets/*.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/design-spec.md`
    - `path_glob`: `tools/validate_ww_persona_selection_contracts.py`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: runtime_persona_packet_validator
      - `artifact_kind`: python_validator
      - `artifact_path`: `tools/validate_ww_persona_packets.py`
      - `section_anchors`: packet artifact discovery and invariant checks
    - `artifact_id`: runtime_persona_packet_validator_suite_integration
      - `artifact_kind`: python_validator_suite
      - `artifact_path`: `tools/validate_ww_repo.py`
      - `section_anchors`: packet validator registration
    - `artifact_id`: runtime_persona_packet_validator_tests
      - `artifact_kind`: python_unittest
      - `artifact_path`: `tools/test_validate_ww_persona_packets.py`
      - `section_anchors`: packet validator regression cases
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Runtime Persona Packet Validator Expansion

- Section ID: section-runtime-persona-packet-validator-expansion
- Runtime State: complete
- Active Execution ID: execution-runtime-persona-packet-validator-expansion
- Active Packet ID:
- Active Agent ID:
- Active Attempt ID:
- Active Worker Mode: test-first
- Active Persona IDs: test-quality-engineer, code-quality-reviewer
- Active Persona Sources: test-quality-engineer=built-in, code-quality-reviewer=built-in
- Active Persona Role Bindings: test-quality-engineer=worker via `agents/worker-prompt.md`; code-quality-reviewer=reviewer via `agents/reviewer-prompt.md`
- Mode Change History:
  - Previous Mode:
  - New Mode:
  - Trigger Evidence:
  - Approved By:
  - Changed At:
- Execution Records:
  - Execution ID: execution-runtime-persona-packet-validator-expansion
  - Role: test-quality-engineer
  - Status: complete
  - Owned Scope: `tools/validate_ww_persona_packets.py`, `tools/test_validate_ww_persona_packets.py`, `tools/validate_ww_repo.py`, narrow `SKILL.md` and `README.md` guidance
  - Started At: 2026-05-31
  - Finished At: 2026-05-31
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
- Last Update At: 2026-05-31
- Next Action: round complete
- Active Write Scope: focused packet validator implementation, direct regression tests, aggregate suite integration, and narrow guidance only
- Result Summary: added generic `docs/cases/**/packets/*.md` discovery and eight packet invariant checks; integrated the validator into the repository suite; added thirteen regression tests; preserved packet contract and dispatch-template shape
- Canonical Result Artifact Location: `tools/validate_ww_persona_packets.py`
- Concerns:
  - keep packet artifact validation distinct from runtime assembly-code proof
  - preserve packet contract and generic dispatch template shape
  - explicit-revision excerpt target identities validate their SHA-256 format but cannot be recomputed without a canonical slice resolver
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Runtime Persona Packet Validator Expansion

- Section ID: section-runtime-persona-packet-validator-expansion
- Review Target Strategy:
  - Review the validator implementation and aggregate integration for generic packet discovery, exact role/persona cross-checks, stable failure messages, PKT-002 scope control, and no packet-contract changes.
- Review Lane Records:
  - Lane ID: lane-runtime-persona-packet-validator-expansion-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: review parser correctness, regression coverage, suite integration, and scope containment
  - Execution ID: execution-runtime-persona-packet-validator-expansion-review
  - Packet ID:
  - Attempt ID: local-code-quality-review-2026-05-31
  - Review Target Ref:
    - Artifact Path: `tools/validate_ww_persona_packets.py`
    - Artifact Kind: python_validator
    - Artifact Revision: sha256:225a18fb87b603ee964f71c6e70250dab3b2802a59b7bfd7a6f3c037b6b68c96
    - Schema Version: 1
    - Section Anchor: packet artifact discovery and invariant checks
    - Content Hash: sha256:225a18fb87b603ee964f71c6e70250dab3b2802a59b7bfd7a6f3c037b6b68c96
  - Reviewer Findings: no material findings after pre-commit fixes; generic packet discovery, source-section-scoped dispatch-copy checks, primary and secondary reviewer-lane matching, repo-relative path containment, malformed nested-binding handling, role prompt checks, worker and reviewer gates, full-file hash verification, explicit-revision excerpt identity handling, aggregate integration, and failure-path regression tests are present
  - Orchestrator Synthesis: implementation stays within the approved packet-artifact validator scope; PKT-002 is resolved through role/persona cross-checks plus optional launch-snapshot validation instead of a generic dispatch-template expansion; pre-commit review fixed multi-section snapshot selection, secondary reviewer-lane matching, repo path containment, and malformed-binding error handling; residual excerpt-slice recomputation is recorded as a non-blocking future design question
  - Strict Review Outcome: none
- Human Decision: Approve
- Revision Notes: user approved the reviewed packet validator expansion on 2026-05-31; section state is accepted, runtime state is complete, and plan state is completed
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level `plan_state` is derived from `required_for_goal`

## Ordering And Parallelism

- Blocking work first: section-runtime-persona-packet-validator-expansion
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
- Approved By: human
- Approval Time: 2026-05-31
- Notes: approval authorizes focused packet validator implementation, direct regression tests, repo-suite integration, and narrow SKILL/README guidance only; runtime code, packet contract, personas, project registry, routing, and secondary tags remain out of scope
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial runtime persona packet validator expansion round
- Supersedes Revision:

## Dispatch Log

- Agents Launched:
- Retry Events:
- Close Events:
  - 2026-05-31: user approved the reviewed packet validator expansion; section closed complete
- Review Lane Transitions:
  - 2026-05-31: local code-quality review completed with no material findings
- Launch Time:
  - 2026-05-31: approved focused validator implementation began; plan moved from `approved` to `dispatched`
- Revisions Since Approval: 0
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
