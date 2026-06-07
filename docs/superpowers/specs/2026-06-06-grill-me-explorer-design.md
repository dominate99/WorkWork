# Grill-Me Explorer Design

## Goal

Add `grill-me` as a built-in WorkWork explorer persona for users who explicitly want a plan or design stress-tested through persistent, one-question-at-a-time interviewing.

The persona must reduce unresolved design ambiguity without taking write authority, silently deciding for the user, or changing ordinary explorer behavior.

## Trigger Boundary

`grill-me` is eligible only when the user explicitly asks for this interaction. Supported intent includes:

- `grill me`
- interview or question me relentlessly
- stress-test this plan or design
- challenge the plan one decision at a time
- equivalent Chinese requests such as `盘问我`, `逐项追问`, or `压力测试这个设计`

The orchestrator must not select `grill-me` merely because a plan appears incomplete.

## Persona And Runtime Binding

Add one built-in persona record with:

- `id: grill-me`
- `role_type: specialist`
- `review_only: false`
- no `implementation_principles`

The absence of `implementation_principles` keeps the persona out of the worker candidate set. When selected, it must resolve to:

- `runtime_role: explorer`
- `template_path: agents/explorer-prompt.md`
- empty write scope

The persona record describes its investigative viewpoint and selection fit. The explorer role prompt and packet contract continue to own read-only runtime behavior.

## Conditional Interview Protocol

The ordinary explorer prompt remains concise and evidence-oriented. It activates the following additional protocol only when `subagent_persona` is `grill-me`:

1. Inspect available code and artifacts before asking anything the repository can answer.
2. Return one unresolved question at a time to the orchestrator.
3. Prefer bounded options when they accurately represent the decision.
4. Include one recommended answer and a concise reason with every question.
5. Treat the recommendation as advice, never as user approval.
6. Keep the current decision branch open until the user explicitly confirms an option or supplies a replacement answer.
7. Resolve prerequisite decisions before dependent decisions.
8. Continue until material branches, dependencies, tradeoffs, and risks are resolved.
9. Allow the user to stop at any time.
10. End by returning a compact shared-understanding summary for user confirmation.

When repository evidence answers a would-be question, the explorer returns the evidence and conclusion to the orchestrator instead of asking the user to confirm a discoverable fact.

## Conversation Ownership

The explorer does not converse with the user directly. The interaction loop is:

1. The orchestrator launches or resumes the `grill-me` explorer with the current approved context.
2. The explorer investigates and returns either repository-resolved evidence or the next unresolved question with its recommendation.
3. The orchestrator briefly reports repository-resolved evidence when relevant.
4. The orchestrator asks the user exactly one unresolved question.
5. The user confirms the recommendation, selects another option, supplies a custom answer, or stops.
6. The orchestrator persists the decision and provides it to the next explorer turn.

This preserves the existing explorer-to-orchestrator return path and keeps final decision authority with the user.

## Artifact Coverage

`grill-me` may examine any current-round plan or design input, including:

- working brief
- dispatch plan
- design spec
- implementation plan
- conversational requirements that the orchestrator first captures in the working brief

It remains read-only across all of these artifacts.

## Decision Persistence

Add a `Grill-Me Decision Log` surface to the working brief template. The orchestrator, not the explorer, maintains it.

Each resolved entry records:

- decision identifier
- question
- user-confirmed answer
- recommendation offered
- rationale or evidence
- dependencies resolved
- dependent branches unblocked

Open branches remain visibly unresolved. Later design specs and implementation plans consume confirmed decisions from this log instead of reconstructing them from chat history.

The dispatch plan continues to own round approval and runtime lifecycle state; it must not become the authority for interview decisions.

## Contract And Documentation Changes

Implementation should update:

- `references/built-in-personas.yaml`
- `agents/explorer-prompt.md`
- `references/persona-registry.md`
- `references/working-brief-template.md`
- `SKILL.md`
- `README.md`

The active contract should explain the explicit trigger boundary, conditional protocol, orchestrator mediation, user confirmation requirement, and decision-log ownership.

No new runtime role or prompt asset is introduced.

## Validation

Add minimal repository validation that checks:

- the `grill-me` built-in persona exists with specialist, non-reviewer, non-worker-capable fields
- the persona is bound to the existing read-only explorer runtime role
- the conditional protocol preserves one-question-at-a-time behavior
- each question requires a recommended answer
- discoverable codebase facts are investigated instead of asked
- user confirmation is required before closing a decision branch
- the working brief template contains the durable `Grill-Me Decision Log`
- the packaged skill and user-facing guidance preserve the explicit user-trigger boundary

Register the validator in `validate_ww_repo.py` and add focused negative fixtures for contract drift.

## Non-Goals

- no standalone `grill-me` skill
- no direct explorer-to-user channel
- no automatic selection for merely incomplete plans
- no changes to ordinary explorer behavior
- no new runtime role
- no new prompt binding type
- no worker or reviewer authority
- no silent acceptance of recommended answers
- no fixed question-count stopping rule

## Acceptance Criteria

- An explicit `grill me` request can select the built-in persona for an explorer packet.
- Ordinary explorer packets retain their existing concise investigation behavior.
- The orchestrator asks at most one unresolved grill question per user turn.
- Every grill question includes a recommended answer and reason.
- Repository-answerable questions are replaced by investigation and evidence.
- A decision branch closes only after explicit user confirmation.
- Confirmed decisions are durably recorded in the working brief.
- The interview ends only after material branches are resolved and the user confirms the shared-understanding summary, unless the user stops early.
- Repository validation fails when any protected contract element is removed or weakened.
