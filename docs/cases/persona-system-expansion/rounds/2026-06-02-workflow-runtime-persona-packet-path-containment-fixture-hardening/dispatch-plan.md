# Dispatch Plan: Runtime Persona Packet Path Containment Fixture Hardening

- Date: 2026-06-02
- Schema Version: 1
- Plan Revision: 2
- Working Brief Version: 1
- Case Slug: persona-system-expansion
- Round Slug: 2026-06-02-workflow-runtime-persona-packet-path-containment-fixture-hardening
- Case Root: `docs/cases/persona-system-expansion/`
- Round Root: `docs/cases/persona-system-expansion/rounds/2026-06-02-workflow-runtime-persona-packet-path-containment-fixture-hardening/`
- Plan State: completed
- Last Approved Revision: 2
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

> Do not launch any real subagent until the preconditions are satisfied and `Plan State: approved`.

Path identity rules:

- `Case Root` must resolve to `docs/cases/<case_slug>/`
- `Round Root` must resolve to `docs/cases/<case_slug>/rounds/<round_slug>/`
- new dispatch-round artifacts are canonically written under `Round Root`
- legacy type-based paths are legacy history only; they are not canonical targets or ongoing generation defaults

## Source Context

- User Request: `new $ww round: runtime persona packet path containment fixture hardening. Based on the approved packet validator dogfood audit, add negative fixtures for repository-relative path containment in validate_ww_persona_packets.py, focusing on ../ traversal escape. Evaluate whether symlink escape should be covered and include it only if cross-platform stability supports it. Add tests and necessary test notes only; do not change validator behavior, packet contract, runtime code, personas, routing, or open canonical slice resolver design.`
- Working Brief Reference: `docs/cases/persona-system-expansion/rounds/2026-06-02-workflow-runtime-persona-packet-path-containment-fixture-hardening/working-brief.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`
- Approved Audit Evidence: `docs/cases/persona-system-expansion/rounds/2026-06-01-workflow-runtime-persona-packet-validator-dogfood-audit/design-spec.md`

## Dispatch Summary

- Goal: add direct repository-relative traversal escape fixtures for packet dispatch-source and reviewer-target containment without changing validator behavior
- Relevant Context: the approved audit found that containment logic exists and absolute-path fixtures pass, but direct `../` traversal escape fixtures are not yet persisted
- Constraints:
  - edit only `tools/test_validate_ww_persona_packets.py` outside round-local records
  - add focused negative regression fixtures for traversal escape
  - assess symlink escape fixture stability and include it only if deterministic across supported platforms
  - do not edit validator behavior, packet contract, runtime code, personas, project registry, routing, secondary tags, or canonical slice resolver design
- Risks:
  - testing missing-file rejection instead of containment rejection
  - unstable symlink setup on Windows or privilege-sensitive environments
  - scope creep into validator implementation
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Runtime Persona Packet Path Containment Fixture Hardening

- Section ID: section-runtime-persona-packet-path-containment-fixture-hardening
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: test-quality-engineer
- Planned Reviewer Persona: code-quality-reviewer
- Planned Reviewer Persona Source: built-in
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: deterministic fixture correctness, portability judgment, and scope containment make the built-in code-quality reviewer the strongest eligible reviewer-only match
- Planned Specialist Personas:
  - Persona ID: test-quality-engineer
    - Source: built-in
    - Runtime Role: worker
    - Selection Rationale: the dominant work is narrow regression-harness hardening; built-in fallback is used because no stronger eligible project worker persona covers targeted packet-validator fixtures
- Planned Scope:
  - `tools/test_validate_ww_persona_packets.py`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: pin the already-implemented path containment invariant with direct traversal fixtures and avoid widening behavior or contract scope
- Planned Workflow Bindings:
  - `superpowers:test-driven-development`
  - `superpowers:systematic-debugging`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: test-first
- Worker Mode Rationale: add focused regression fixtures first because validator behavior already exists and must remain unchanged
- Goal Tuning: validation-biased
- Constraint Interaction Rule: validator behavior, packet contract, runtime code, personas, project registry, routing, secondary tags, and canonical slice resolver design remain read-only
- Planned Review Lanes:
  - Lane ID: lane-runtime-persona-packet-path-containment-fixture-hardening-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: inspect whether fixtures directly exercise traversal containment, remain deterministic across platforms, and avoid validator or contract changes
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/persona-system-expansion/case.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-06-02-workflow-runtime-persona-packet-path-containment-fixture-hardening/working-brief.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-06-02-workflow-runtime-persona-packet-path-containment-fixture-hardening/dispatch-plan.md`
    - `path_glob`: `tools/test_validate_ww_persona_packets.py`
  - `shared_read_scope`:
    - `path_glob`: `tools/validate_ww_persona_packets.py`
    - `path_glob`: `tools/validate_ww_repo.py`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-06-01-workflow-runtime-persona-packet-validator-dogfood-audit/design-spec.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `path_glob`: `docs/superpowers/personas/registry.yaml`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: runtime_persona_packet_path_containment_fixtures
      - `artifact_kind`: python_unittest
      - `artifact_path`: `tools/test_validate_ww_persona_packets.py`
      - `section_anchors`: repository-relative path containment negative fixtures
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Runtime Persona Packet Path Containment Fixture Hardening

- Section ID: section-runtime-persona-packet-path-containment-fixture-hardening
- Runtime State: complete
- Active Execution ID: execution-runtime-persona-packet-path-containment-fixture-hardening
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
  - Execution ID: execution-runtime-persona-packet-path-containment-fixture-hardening
  - Role: test-quality-engineer
  - Status: complete
  - Owned Scope: `tools/test_validate_ww_persona_packets.py`
  - Started At: 2026-06-02
  - Finished At: 2026-06-02
- Packet Records:
- Attempt Records:
- Attempt Count: 0
- Last Update At: 2026-06-02
- Next Action: round complete
- Active Write Scope: `tools/test_validate_ww_persona_packets.py`
- Result Summary: revision 2 makes both traversal fixtures isolate containment by creating valid repository-external artifacts; the dispatch fixture copies a complete approved plan, and the reviewer fixture carries matching full-file SHA-256 identity; symlink escape remains omitted because Windows symlink creation can require Developer Mode or elevated privileges
- Canonical Result Artifact Location: `tools/test_validate_ww_persona_packets.py`
- Concerns:
  - preserve validator behavior and packet contract as read-only
  - symlink fixture omitted because setup is not reliably privilege-free across supported Windows environments
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Runtime Persona Packet Path Containment Fixture Hardening

- Section ID: section-runtime-persona-packet-path-containment-fixture-hardening
- Review Target Strategy:
  - Review the focused unittest diff for direct traversal-containment evidence, rule-specific assertions, portability, and absence of validator behavior changes.
- Review Lane Records:
  - Lane ID: lane-runtime-persona-packet-path-containment-fixture-hardening-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: review deterministic regression-fixture quality and strict scope containment
  - Execution ID: execution-runtime-persona-packet-path-containment-fixture-hardening-review
  - Packet ID:
  - Attempt ID: local-code-quality-review-2026-06-02
  - Review Target Ref:
    - Artifact Path: `tools/test_validate_ww_persona_packets.py`
    - Artifact Kind: python_unittest
    - Artifact Revision: sha256:43220da7ef961acba9e7d6d842e3835363d343049c6d36fff444eda904929585
    - Schema Version: 1
    - Section Anchor: repository-relative path containment negative fixtures
    - Content Hash: sha256:43220da7ef961acba9e7d6d842e3835363d343049c6d36fff444eda904929585
  - Reviewer Findings: no material findings after revision 2; the external dispatch plan now exists and is otherwise valid, while the external reviewer target exists with matching full-file SHA-256 identity; an in-memory mutation that removes repository containment makes both traversal tests fail, proving the fixtures isolate the intended guard
  - Orchestrator Synthesis: revision 2 resolves both P2 findings without changing validator behavior; normal focused tests pass 15 of 15, the full repo suite passes, and the containment-removal mutation causes both revised fixtures to fail as required
  - Strict Review Outcome: none
- Human Decision: Approve
- Revision Notes: user approved revision 2 on 2026-06-06 after both P2 fixture-isolation findings were resolved; section state accepted, runtime state complete, and plan state completed
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level `plan_state` is derived from `required_for_goal`

## Ordering And Parallelism

- Blocking work first: section-runtime-persona-packet-path-containment-fixture-hardening
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
- Approval Time: 2026-06-06
- Notes: user authorized revision 2 to address the two P2 fixture-isolation findings; validator behavior, packet contract, runtime code, personas, project registry, routing, secondary tags, and canonical slice resolver design remain out of scope
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial runtime persona packet path containment fixture hardening round
- Supersedes Revision:
- Revision 2 Created From Brief Version: 1
- Revision Reason: address pre-commit P2 findings that missing outside artifacts allowed false-positive containment tests
- Supersedes Revision: 1

## Dispatch Log

- Agents Launched:
- Retry Events:
- Close Events:
  - 2026-06-02: user approved the reviewed traversal-containment fixture hardening; section closed complete
  - 2026-06-06: user approved revision 2 after the two P2 fixture-isolation fixes; section closed complete
- Review Lane Transitions:
- Launch Time:
- 2026-06-02: user approved revision 1; focused traversal-containment fixture hardening authorized
- 2026-06-02: approved focused fixture hardening began; plan moved from `approved` to `dispatched`
- 2026-06-02: direct traversal fixtures added and locally code-quality reviewed with no material findings
- 2026-06-02: user approved reviewed fixture hardening; plan moved from `dispatched` to `completed`
- 2026-06-06: user requested revision for two P2 fixture-isolation findings; revision 2 reopened the section and replaced missing outside targets with valid external artifacts
- 2026-06-06: revision 2 local code-quality review found no material findings; mutation check confirmed both tests fail when repository containment is removed
- 2026-06-06: user approved revision 2; plan moved from `dispatched` to `completed`
- Revisions Since Approval: 0
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
