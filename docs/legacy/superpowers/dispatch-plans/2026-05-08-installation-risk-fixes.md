# Dispatch Plan: Installation Risk Fixes

- Date: 2026-05-08
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Plan State: completed
- Last Approved Revision: 1
- Rollback Baseline Revision: none
- Task Routing: code/programming
- Main Orchestrator: staff engineer orchestrator

## Preconditions

- Estimation Complete: true
- Working Brief Status: ready

> Do not launch any real subagent until the preconditions are satisfied and `Plan State: approved`.

## Source Context

- User Request: `$ww address these risks`
- Working Brief Reference: `docs/legacy/superpowers/working-briefs/2026-05-08-installation-risk-fixes-v1.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: fix the remaining packaging and install-doc risks before this installation work is considered complete
- Relevant Context: the isolated worktree already contains the installation-doc changes; the remaining work is a bounded remediation pass over three plugin manifests and four user-facing docs
- Constraints: keep Codex remote install wording as build-dependent fallback only, preserve the full-checkout requirement, keep docs honest, and do not add new installer flows
- Risks:
  - incorrect manifest `skills` paths can break every plugin surface
  - Codex remote GitHub-subdirectory wording can overpromise a path that does not preserve access to repo-root `skills/`
  - missing Superpowers prerequisite can make `$ww` fail after a correct install
  - untracked guide files can be missed during final integration if not handled carefully
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Packaging And Install Risk Remediation

- Section ID: section-installation-risk-fixes
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: staff engineer orchestrator
- Planned Reviewer Persona: runtime policy reviewer
- Planned Specialist Personas: documentation workflow implementer
- Planned Scope:
  - `README.md`
  - `docs/README.codex.md`
  - `docs/README.claude.md`
  - `docs/README.cursor.md`
  - `.codex-plugin/plugin.json`
  - `.claude-plugin/plugin.json`
  - `.cursor-plugin/plugin.json`
- Planning Rationale: the remaining risk is concentrated in one tightly-coupled install/package surface, so one bounded remediation lane is simpler and safer than splitting the work
- Planned Workflow Bindings:
  - `superpowers:brainstorming`
  - `superpowers:writing-plans`
  - `superpowers:subagent-driven-development`
  - `superpowers:requesting-code-review`
- Planned Review Lanes:
  - Lane ID: lane-installation-risk-review
  - Lane Type: code-quality-review
  - Reviewer Persona: runtime policy reviewer
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `README.md`
    - `path_glob`: `docs/README.codex.md`
    - `path_glob`: `docs/README.claude.md`
    - `path_glob`: `docs/README.cursor.md`
    - `path_glob`: `.codex-plugin/plugin.json`
    - `path_glob`: `.claude-plugin/plugin.json`
    - `path_glob`: `.cursor-plugin/plugin.json`
    - `path_glob`: `docs/legacy/superpowers/working-briefs/2026-05-08-installation-risk-fixes-v1.md`
    - `path_glob`: `docs/legacy/superpowers/dispatch-plans/2026-05-08-installation-risk-fixes.md`
  - `shared_read_scope`:
    - `path_glob`: `.opencode/INSTALL.md`
    - `path_glob`: `skills/**`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: `installation_risk_fix_set`
    - `artifact_kind`: `doc_and_config_bundle`
    - `artifact_path`: `README.md`
    - `section_anchors`: `Quick Start`
- Packet Created: false

## Section Runtime Ledger

### Section: Packaging And Install Risk Remediation

- Section ID: section-installation-risk-fixes
- Runtime State: complete
- Active Execution ID:
- Active Packet ID:
- Active Agent ID:
- Active Attempt ID:
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
  - Result Summary: remediation fixes were applied in the isolated worktree and the round is ready for closure
  - Result Artifact Location: `README.md`
- Attempt Count: 0
- Last Update At: 2026-05-08 America/Los_Angeles
- Next Action: none
- Active Write Scope:
- Result Summary: remediation round approved and completed against the current worktree
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns:
- Blocker Reason:
- Close State: open
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Packaging And Install Risk Remediation

- Section ID: section-installation-risk-fixes
- Review Status: completed
- Review Target Strategy: user reviews the bounded remediation scope before any more execution happens
- Review Lane Records:
  - Lane ID: lane-installation-risk-review
  - Lane Type: code-quality-review
  - Reviewer Persona: runtime policy reviewer
  - Execution ID:
  - Packet ID:
  - Attempt ID:
  - Review Target Ref:
    - Artifact Path: `docs/legacy/superpowers/dispatch-plans/2026-05-08-installation-risk-fixes.md`
    - Artifact Kind: `plan`
    - Artifact Revision: 1
    - Schema Version: 1
    - Section Anchor:
    - Content Hash:
  - Review Status: completed
  - Reviewer Findings:
    - no material scope findings; this was the correct bounded remediation surface
  - Orchestrator Synthesis:
    - Recommendation: approved and complete.
    - Reason: the manifest-path correction and doc hardening are already present in the isolated worktree, and final integrated review found no remaining blocking issues.
- Human Decision: Approve
- Revision Notes:
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level `plan_state` is derived from `required_for_goal`

## Ordering And Parallelism

- Blocking work first: `section-installation-risk-fixes`
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
- Approval Time: 2026-05-08 America/Los_Angeles
- Notes: user approved the remediation round after the bounded fixes had already been applied in the current isolated worktree
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial remediation round for packaging and install-doc risks
- Supersedes Revision:

## Dispatch Log

- Agents Launched: none
- Retry Events:
- Close Events:
- Review Lane Transitions:
  - remediation scope estimated
  - working brief persisted
  - dispatch plan drafted
  - bounded manifest and doc fixes applied in the isolated worktree
  - final integrated review returned no remaining findings
  - user approved the remediation round
- Launch Time:
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
