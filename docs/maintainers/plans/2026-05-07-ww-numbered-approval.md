# WW Numbered Approval Prompt Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update the active `ww-subagent-orchestrator` contract surfaces so approval prompts prefer `1. Approve`, `2. Revise`, `3. Stop` while still accepting `Approve`, `Revise`, and `Stop` as aliases.

**Architecture:** Treat the approved design spec as the contract source, then update the three active wording surfaces in lockstep: `SKILL.md` for the canonical interaction contract, `assets/dispatch-plan-template.md` for the persisted approval block, and `README.md` for user-facing examples. Validate the rollout with targeted `rg` checks plus a final diff review to confirm the change stays documentation-and-contract-only.

**Tech Stack:** Markdown skill files, Markdown docs, PowerShell, `rg`, Git

---

### Task 1: Update the canonical approval contract in `SKILL.md`

**Files:**
- Modify: `skills/ww-subagent-orchestrator/SKILL.md`

- [ ] **Step 1: Confirm the new numbered contract is not already present**

Run:

```powershell
rg -n "1\\. Approve|2\\. Revise|3\\. Stop|aliases" "C:\Users\domin\Documents\AI\AIskill\WorkWork\skills\ww-subagent-orchestrator\SKILL.md"
```

Expected: no matches for the numbered approval block or explicit alias wording.

- [ ] **Step 2: Confirm the old words-only approval wording is still present**

Run:

```powershell
rg -n "Approve / Revise / Stop|Ask for `Approve / Revise / Stop`|re-request approval" "C:\Users\domin\Documents\AI\AIskill\WorkWork\skills\ww-subagent-orchestrator\SKILL.md"
```

Expected: matches showing the current contract still describes the approval step in words-only form.

- [ ] **Step 3: Replace the approval-prompt contract with the numbered form**

Update the relevant sections in `SKILL.md` so they use this wording wherever the preferred prompt format is defined:

```md
Use this approval block:

1. `Approve`
2. `Revise`
3. `Stop`

The words `Approve`, `Revise`, and `Stop` remain accepted aliases for the same decisions.
```

Also update any surrounding explanatory text so it says the numbered list is the preferred rendered prompt while the words remain valid responses.

- [ ] **Step 4: Preserve approval semantics while tightening the wording**

Keep the existing lifecycle meaning unchanged by preserving content equivalent to:

```md
- `Approve` advances to the next approved stage.
- `Revise` returns to orchestrator editing and requires approval again before launch.
- `Stop` preserves the working brief and dispatch plan and prevents new dispatch until planning is reopened.
```

Do not introduce parser, UI, checkbox, or runtime-execution claims.

- [ ] **Step 5: Verify the new contract is present**

Run:

```powershell
rg -n "1\\. `Approve`|2\\. `Revise`|3\\. `Stop`|accepted aliases|preferred rendered prompt" "C:\Users\domin\Documents\AI\AIskill\WorkWork\skills\ww-subagent-orchestrator\SKILL.md"
```

Expected: matches for the numbered approval block and alias rule.

- [ ] **Step 6: Commit**

```bash
git add skills/ww-subagent-orchestrator/SKILL.md
git commit -m "docs: add numbered ww approval contract"
```

### Task 2: Update the persisted approval block in the dispatch plan template

**Files:**
- Modify: `skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`

- [ ] **Step 1: Confirm the template still uses the words-only approval choice line**

Run:

```powershell
rg -n "Required Human Choice: `Approve` \\| `Revise` \\| `Stop`|Choice Mapping|Approval Block" "C:\Users\domin\Documents\AI\AIskill\WorkWork\skills\ww-subagent-orchestrator\assets\dispatch-plan-template.md"
```

Expected: matches for the current words-only `Required Human Choice` line.

- [ ] **Step 2: Update the `Approval Block` to show numbered choices**

Change the human-choice wording in the template so it renders the preferred prompt format like this:

```md
## Approval Block

- Required Human Choice:
  - `1. Approve`
  - `2. Revise`
  - `3. Stop`
- Accepted Aliases: `Approve` | `Revise` | `Stop`
- Current Choice: none
```

Keep the rest of the block structure intact unless a small wording adjustment is required for consistency.

- [ ] **Step 3: Preserve the existing choice mapping semantics**

Leave the transition meanings unchanged and keep content equivalent to:

```md
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`
```

Do not renumber or rename the plan-state transitions.

- [ ] **Step 4: Verify the template now matches the numbered contract**

Run:

```powershell
rg -n "1\\. Approve|2\\. Revise|3\\. Stop|Accepted Aliases|Plan State: approved|Plan State: revising|Plan State: stopped" "C:\Users\domin\Documents\AI\AIskill\WorkWork\skills\ww-subagent-orchestrator\assets\dispatch-plan-template.md"
```

Expected: matches for the numbered choices, the alias line, and the unchanged choice mapping.

- [ ] **Step 5: Commit**

```bash
git add skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md
git commit -m "docs: update ww approval template wording"
```

### Task 3: Update the README examples and workflow wording

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Locate the README approval-step wording**

Run:

```powershell
rg -n "Approve / Revise / Stop|approval|dispatch subagents only after approval" "C:\Users\domin\Documents\AI\AIskill\WorkWork\README.md"
```

Expected: matches showing the workflow currently references the approval step without the numbered prompt format.

- [ ] **Step 2: Update the README workflow description**

Revise the approval step so it describes the preferred prompt like this:

```md
5. request:
   1. `Approve`
   2. `Revise`
   3. `Stop`
   with `Approve`, `Revise`, and `Stop` also accepted as aliases
```

Adjust the surrounding sentence structure to keep the README readable, but do not claim a separate parser or GUI implementation.

- [ ] **Step 3: Update any README examples that imply a words-only prompt**

If the README includes explanatory approval examples, align them to this contract:

```md
Preferred approval prompt:

1. `Approve`
2. `Revise`
3. `Stop`

Users may also reply with `Approve`, `Revise`, or `Stop`.
```

If no explicit example exists, keep the change limited to the workflow description and any nearby explanation that defines the interaction.

- [ ] **Step 4: Verify the README now reflects the numbered contract**

Run:

```powershell
rg -n "1\\. `Approve`|2\\. `Revise`|3\\. `Stop`|accepted as aliases|users may also reply" "C:\Users\domin\Documents\AI\AIskill\WorkWork\README.md"
```

Expected: matches showing the numbered approval wording and alias note in the README.

- [ ] **Step 5: Commit**

```bash
git add README.md
git commit -m "docs: align readme with ww numbered approval prompt"
```

### Task 4: Validate that the three active surfaces stay in sync

**Files:**
- Modify: `skills/ww-subagent-orchestrator/SKILL.md` if consistency fixes are needed
- Modify: `skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md` if consistency fixes are needed
- Modify: `README.md` if consistency fixes are needed

- [ ] **Step 1: Run a cross-file consistency search**

Run:

```powershell
rg -n "1\\. `Approve`|2\\. `Revise`|3\\. `Stop`|Accepted Aliases|accepted aliases|Approve / Revise / Stop" `
  "C:\Users\domin\Documents\AI\AIskill\WorkWork\skills\ww-subagent-orchestrator\SKILL.md" `
  "C:\Users\domin\Documents\AI\AIskill\WorkWork\skills\ww-subagent-orchestrator\assets\dispatch-plan-template.md" `
  "C:\Users\domin\Documents\AI\AIskill\WorkWork\README.md"
```

Expected: numbered approval wording appears in all three files; any remaining `Approve / Revise / Stop` matches should be reviewed and kept only if they describe semantics rather than the preferred rendered prompt.

- [ ] **Step 2: Fix any wording drift revealed by the search**

If one file still presents the old words-only prompt as the preferred display, update it so the visible contract stays aligned to:

```md
1. `Approve`
2. `Revise`
3. `Stop`
```

with word aliases still accepted.

- [ ] **Step 3: Review the final diff**

Run:

```powershell
git -c safe.directory='C:/Users/domin/Documents/AI/AIskill/WorkWork' -C 'C:\Users\domin\Documents\AI\AIskill\WorkWork' diff -- skills/ww-subagent-orchestrator/SKILL.md skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md README.md
```

Expected: only wording and documentation-contract changes in the three approved files, with no unrelated runtime or structural edits.

- [ ] **Step 4: Run a final worktree check**

Run:

```powershell
git -c safe.directory='C:/Users/domin/Documents/AI/AIskill/WorkWork' -C 'C:\Users\domin\Documents\AI\AIskill\WorkWork' status --short
```

Expected: only the intended plan-execution changes remain staged or committed.

- [ ] **Step 5: Commit any final consistency fixes**

```bash
git add skills/ww-subagent-orchestrator/SKILL.md skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md README.md
git commit -m "docs: finalize ww numbered approval consistency"
```
