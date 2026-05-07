# Dispatch Plan: WW Orchestrator Implementation

- Date: 2026-05-06
- Plan Revision: 1
- Schema Version: 1
- Working Brief Version: 1
- Plan State: completed
- Last Approved Revision: none
- Rollback Baseline Revision: none
- Task Routing: code/programming
- Main Orchestrator: staff engineer orchestrator

## Preconditions

- Estimation Complete: true
- Working Brief Status: ready

> Do not launch any real subagent until the preconditions are satisfied and `Plan State: approved`.

## Source Context

- User Request: `$ww based on implementation plan start the implementation`
- Working Brief Reference: `docs/superpowers/working-briefs/2026-05-06-ww-orchestrator-implementation-v1.md`
- Implementation Plan Reference: `2026-05-06-implementation-plan.md`

## Dispatch Summary

- Goal: implement the approved orchestration design into the ww skill artifacts with no semantic drift across controller semantics, packet contract, dispatch-plan template, and persona prompt assembly
- Relevant Context: implementation plan is complete and internally reviewed; no runtime docs existed before this round; skill root is `C:\Users\domin\.codex\skills\ww-subagent-orchestrator`
- Constraints: no launch before approval; serial first pass across overlapping contract files; reviewers stay findings-only; do not weaken the implementation plan semantics during edits
- Risks:
  - contract/template drift across `SKILL.md`, `references/`, and `assets/`
  - packet field names drifting from controller update procedure
  - review-target and artifact-registry semantics being implemented inconsistently
  - persona prompt assets being added without packet assembly wiring
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Core Runtime Contracts

- Section ID: section-core-runtime-contracts
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: codex skill contract implementer
- Planned Reviewer Persona: runtime policy reviewer
- Planned Specialist Personas: staff engineer orchestrator
- Planned Scope:
  - `SKILL.md`
  - `references/subagent-packet-contract.md`
  - `references/working-brief-template.md`
  - `assets/dispatch-plan-template.md`
- Planning Rationale: these files encode the canonical controller semantics, packet fields, persisted artifact rules, and dispatch runtime ledger; they must stabilize first
- Planned Workflow Bindings:
  - `superpowers:subagent-driven-development`
  - `superpowers:test-driven-development`
  - `superpowers:requesting-code-review`
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `SKILL.md`
    - `path_glob`: `references/*.md`
    - `path_glob`: `assets/*.md`
  - `shared_read_scope`:
    - `artifact_id`: `implementation_plan`
    - `artifact_id`: `working_brief`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
- Packet Created: true

### Section: Persona And Prompt Binding

- Section ID: section-persona-prompt-binding
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: codex skill contract implementer
- Planned Reviewer Persona: skill prompt systems reviewer
- Planned Specialist Personas: staff engineer orchestrator
- Planned Scope:
  - `references/persona-registry.md`
  - `agents/openai.yaml`
  - `agents/orchestrator-prompt.md`
  - `agents/worker-prompt.md`
  - `agents/reviewer-prompt.md`
  - `agents/explorer-prompt.md`
- Planning Rationale: this section wires selected personas into packet fields and final prompt assembly after the core packet/template contract is stable
- Planned Workflow Bindings:
  - `superpowers:subagent-driven-development`
  - `superpowers:test-driven-development`
  - `superpowers:requesting-code-review`
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `references/persona-registry.md`
    - `path_glob`: `agents/*`
  - `shared_read_scope`:
    - `artifact_id`: `implementation_plan`
    - `artifact_id`: `dispatch_plan`
  - `depends_on_sections`:
    - `section-core-runtime-contracts`
  - `parallel_safe_with_sections`: none
- Packet Created: false

### Section: Validation And Consistency Pass

- Section ID: section-validation-consistency
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: codex skill contract implementer
- Planned Reviewer Persona: runtime policy reviewer
- Planned Specialist Personas: staff engineer orchestrator
- Planned Scope:
  - validation pass across updated skill artifacts
  - dry-run examples where needed inside touched docs
- Planning Rationale: the implementation plan expects a final consistency pass after the contract and persona layers land
- Planned Workflow Bindings:
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `SKILL.md`
    - `path_glob`: `references/*.md`
    - `path_glob`: `assets/*.md`
    - `path_glob`: `agents/*`
  - `shared_read_scope`:
    - `artifact_id`: `working_brief`
    - `artifact_id`: `dispatch_plan`
    - `artifact_id`: `implementation_plan`
  - `depends_on_sections`:
    - `section-core-runtime-contracts`
    - `section-persona-prompt-binding`
  - `parallel_safe_with_sections`: none
- Packet Created: false

## Section Review Record

### Section: Core Runtime Contracts

- Section ID: section-core-runtime-contracts
- Review Status: completed
- Reviewer Findings:
  - no material findings
- Orchestrator Synthesis:
  - Recommendation: approve section 1 and proceed to the remaining sections.
  - Reason: the controller contract, packet contract, dispatch ledger, and scope fallback semantics are now internally consistent.
- Human Decision: Approve
- Revision Notes:
  - all section 1 findings resolved in the current artifact set
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped` and plan state becomes `stopped`

### Section: Persona And Prompt Binding

- Section ID: section-persona-prompt-binding
- Review Status: completed
- Reviewer Findings:
  - no material findings
- Orchestrator Synthesis:
  - Recommendation: approve section 2 and proceed to validation.
  - Reason: persona selection, runtime role binding, and prompt asset loading are now explicitly wired through the packet and `openai.yaml` contracts.
- Human Decision: Approve
- Revision Notes:
  - all section 2 findings resolved in the current artifact set
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped` and plan state becomes `stopped`

### Section: Validation And Consistency Pass

- Section ID: section-validation-consistency
- Section State: accepted
- Runtime State: complete
- Review Status: completed
- Reviewer Findings:
  - no material findings
- Orchestrator Synthesis:
  - Recommendation: approve section 3 and close the implementation round.
  - Reason: the core runtime contracts, persona binding, prompt assets, and dispatch tracker are now consistent with the implementation plan and with each other.
- Human Decision: Approve
- Revision Notes:
  - validation pass completed with no residual semantic drift
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped` and plan state becomes `stopped`

## Ordering And Parallelism

- Blocking work first: `section-core-runtime-contracts` -> `section-persona-prompt-binding` -> `section-validation-consistency`
- Parallel sections: none for revision 1; contract files and final validation have overlapping write surfaces
- Review loop per section: draft -> reviewer findings -> orchestrator synthesis -> human judgment

## Approval Block

- Required Human Choice: `Approve` | `Revise` | `Stop`
- Current Choice: Approve
- Approved By: user
- Approval Time: 2026-05-06 America/Los_Angeles
- Notes: approved in chat after working brief and dispatch plan review
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial implementation dispatch round from approved implementation plan
- Supersedes Revision: none

## Dispatch Log

- Agents Launched:
  - `section-core-runtime-contracts`: worker `Volta` (`019e0136-bb37-7bb0-b205-5aa8075c1001`) launched then shut down due to non-return
  - `section-core-runtime-contracts`: local orchestrator implementation completed and moved to review
  - `section-persona-prompt-binding`: local orchestrator implementation completed and moved to review
  - `section-validation-consistency`: validation pass completed locally with no material findings
- Launch Time: 2026-05-06 America/Los_Angeles
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
