# WW Numbered Approval Prompt Design

**Date:** 2026-05-07

## Goal

Adjust the `ww-subagent-orchestrator` skill contract so approval prompts prefer numbered choices while still accepting the words `Approve`, `Revise`, and `Stop` as aliases.

## Problem

The current repo surfaces describe the approval lifecycle in words only:

- `Approve`
- `Revise`
- `Stop`

That is semantically correct, but it leaves the preferred reply format underspecified. The user wants a simpler interaction where the prompt explicitly shows numbered choices and those numbers map one-to-one to the same decisions.

Without a clear contract, three problems remain:

- the skill prompt can continue to ask for words only
- the dispatch plan template can drift from the skill's preferred interaction format
- the README can show outdated examples that do not match the active contract

## Scope

This design covers:

- the preferred approval prompt format in `skills/ww-subagent-orchestrator/SKILL.md`
- the approval-facing wording in `skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
- the user-facing examples and wording in `README.md`
- the alias rule that the words `Approve`, `Revise`, and `Stop` remain valid inputs

This design does not cover:

- a parser or runtime command handler outside the skill contract text
- clickable controls, checkboxes, or GUI widgets
- changes to historical maintainer docs that are not active contract surfaces
- any change to approval state semantics, plan-state transitions, or stop behavior

## Chosen Interaction Contract

The preferred approval block becomes:

```md
1. Approve
2. Revise
3. Stop
```

The interaction contract also preserves the existing word commands:

- `Approve`
- `Revise`
- `Stop`

Acceptance rule:

- numbers are the preferred displayed response format
- words remain accepted aliases
- both forms map to the same existing approval semantics

## Alternative Approaches Considered

### Option 1: Minimal wording patch

Update only one or two prompt lines in `SKILL.md`.

Pros:

- lowest edit volume
- fastest to implement

Cons:

- leaves the template and README inconsistent
- does not create a clear repo-wide contract

### Option 2: Consistency update across active surfaces

Update the skill contract, the dispatch plan template, and the README together.

Pros:

- keeps the canonical contract and examples aligned
- satisfies the requested repo-only scope
- avoids over-engineering into runtime implementation

Cons:

- touches three files instead of one

This is the selected approach.

### Option 3: Broader historical doc sweep

Update old maintainer specs, plans, and archived dispatch examples too.

Pros:

- maximizes global wording consistency

Cons:

- higher churn for low-value historical files
- risks blurring the boundary between active contract surfaces and historical records

## Surface-by-Surface Design

### 1. `SKILL.md`

`SKILL.md` remains the canonical contract source.

Required changes:

- replace wording that asks for `Approve / Revise / Stop` with wording that presents `1. Approve`, `2. Revise`, `3. Stop`
- explicitly state that the words `Approve`, `Revise`, and `Stop` are still accepted as aliases
- keep the lifecycle semantics unchanged
- update any preferred examples so the numbered format is what future users see first

Contract rule:

- if the file describes how to ask for a user decision, it should treat the numbered list as the preferred rendering and the words as accepted aliases

### 2. `dispatch-plan-template.md`

The dispatch plan template is the main persisted approval-facing artifact.

Required changes:

- update the `Approval Block` so the required human choice section reflects the numbered form
- keep the existing choice mapping semantics unchanged
- add wording that makes the alias rule explicit when needed

Template rule:

- the template should render the same preferred approval choices that the skill asks for in chat

### 3. `README.md`

The README is the user-facing explanation layer for the repo.

Required changes:

- update the workflow description so the approval step reflects numbered choices
- update any examples or explanatory text so the visible interaction matches the canonical skill contract
- avoid promising runtime behavior beyond the repo wording change

Documentation rule:

- the README should describe the preferred numbered interaction without implying a separate implemented parser or UI

## Non-Goals And Guardrails

- Do not change the meaning of `Approve`, `Revise`, or `Stop`.
- Do not remove the word commands.
- Do not introduce partial numbering such as `1`, `2`, and plain `Stop`.
- Do not add checkbox syntax or markdown task-list semantics to the approval block.
- Do not change historical records just to match the new copy.

## Verification Requirements For The Later Implementation Plan

The implementation plan should require:

- a targeted search for approval-prompt wording in the three in-scope files
- edits that make all three files agree on the numbered prompt contract
- a final search confirming no active in-scope example still shows the old words-only prompt as the preferred form
- a git diff review to confirm the change stayed documentation-and-contract-only

## Expected Outcome

After implementation:

- the active `$ww` skill contract will prefer `1. Approve`, `2. Revise`, `3. Stop`
- the words `Approve`, `Revise`, and `Stop` will still be accepted as aliases in the contract wording
- the dispatch plan template and README examples will match that contract
- no approval semantics or runtime state behavior will change
