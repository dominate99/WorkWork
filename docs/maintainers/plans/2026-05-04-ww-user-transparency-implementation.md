# WW User Transparency And Subagent Progress Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement revision 5 of the `ww-subagent-orchestrator` transparency design so every `$ww` reply uses the new four-section status contract and renders subagent progress from persisted dispatch-plan state.

**Architecture:** Treat the design spec as the contract source, then update the three synchronized implementation artifacts in lockstep: `SKILL.md` for runtime behavior, `assets/dispatch-plan-template.md` for canonical persisted state, and `references/subagent-packet-contract.md` for packet-to-workstream identity. Validate the result with contract-level text checks plus skill validation.

**Tech Stack:** Markdown skill files, YAML metadata, PowerShell and `rg` validation commands, Python `quick_validate.py`

---

### Task 1: Upgrade the top-level skill contract

**Files:**
- Modify: `skills/ww-subagent-orchestrator/SKILL.md`

- [ ] **Step 1: Write the failing contract checks**

Run:

```powershell
rg -n "Status Summary|Subagent Progress|Decision Block|four-section" "C:\Users\domin\Documents\Codex\2026-04-25-create-a-local-repo-in-aiskill\skills\ww-subagent-orchestrator\SKILL.md"
```

Expected: no matches for the new reply-shape contract, because `SKILL.md` still only hard-requires `Document Summary`.

- [ ] **Step 2: Re-run the existing summary-only check to confirm the old contract is still dominant**

Run:

```powershell
rg -n "Document Summary" "C:\Users\domin\Documents\Codex\2026-04-25-create-a-local-repo-in-aiskill\skills\ww-subagent-orchestrator\SKILL.md"
```

Expected: matches in the existing `Document Summary Contract` section.

- [ ] **Step 3: Implement the four-section reply contract in `SKILL.md`**

Add or replace the user-facing reply contract so it includes the exact ordered shape and the persisted-state rule:

```md
## User-Facing Reply Contract

Every `$ww` reply must use these four sections in this order:

1. `Status Summary`
2. `Subagent Progress`
3. `Decision Block`
4. `Document Summary`

The dispatch plan is the canonical runtime state source. Update the dispatch plan first, then render the chat reply from the updated persisted state in the same turn.

### Status Summary

- Always include:
  - `current stage`
  - `primary owner`
  - `waiting on`
  - `next action`
  - `user decision needed`
- Derive all five fields from the critical-path workstream recorded in the dispatch plan.

### Subagent Progress

- Always include the section, even when no subagents are active.
- If no subagents have launched, output `no subagents launched`.
- Otherwise render each workstream from the dispatch plan `Progress Board`.

### Decision Block

- Always include the section.
- If `user decision needed` is `yes`, enumerate the available choice set.
- If `user decision needed` is `no`, output `No decision required right now`.

### Document Summary

- Always include:
  - `working brief`
  - `dispatch plan`
  - `design spec`
  - `implementation plan`
- Use `not created yet` for missing documents.
```

- [ ] **Step 4: Add deterministic rendering rules to `SKILL.md`**

Add the precedence and synchronization rules needed to keep the reply deterministic:

```md
## Runtime Rendering Rules

- `current stage`, `waiting on`, and `next action` must all derive from the same critical-path workstream.
- `waiting on` precedence:
  - human choice
  - orchestrator synthesis or routing
  - blocker owner or unresolved dependency
  - active workstream owner
  - queue gate
  - `nobody`
- `Decision Block` must derive from the same dispatch-plan state as `user decision needed`.
- Do not emit a rendered state that is more advanced than the persisted dispatch plan.
```

- [ ] **Step 5: Run the contract checks again to verify they now pass**

Run:

```powershell
rg -n "Status Summary|Subagent Progress|Decision Block|four-section|critical-path workstream|No decision required right now" "C:\Users\domin\Documents\Codex\2026-04-25-create-a-local-repo-in-aiskill\skills\ww-subagent-orchestrator\SKILL.md"
```

Expected: matches for the new reply contract and deterministic rendering rules.

- [ ] **Step 6: Commit**

```bash
git add skills/ww-subagent-orchestrator/SKILL.md
git commit -m "feat: add ww reply transparency contract"
```

### Task 2: Add the canonical `Progress Board` schema to the dispatch-plan template

**Files:**
- Modify: `skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`

- [ ] **Step 1: Write the failing schema check**

Run:

```powershell
rg -n "Progress Board|Workstream ID|Display Status|Review Pass ID|Scope:" "C:\Users\domin\Documents\Codex\2026-04-25-create-a-local-repo-in-aiskill\skills\ww-subagent-orchestrator\assets\dispatch-plan-template.md"
```

Expected: no matches, because the current template still has no canonical progress schema.

- [ ] **Step 2: Add the `Progress Board` section with all required fields**

Insert this section after `## Ordering And Parallelism` and before `## Approval Block`:

```md
## Progress Board

### Workstream: {{workstream_label}}

- Workstream ID: {{workstream_id}}
- Source Section ID: {{source_section_id}}
- Source Plan Revision: {{source_plan_revision}}
- Workstream Type: {{workstream_type}}
- Scope: {{scope}}
- Owner: {{owner}}
- Internal State Reference: {{internal_state_reference}}
- Display Status: {{display_status}}
- Last Update: {{last_update}}
- Blocker: {{blocker}}
- Next Handoff: {{next_handoff}}
- Review Pass ID: {{review_pass_id_or_none}}
```

- [ ] **Step 3: Preserve the existing audit log while making the progress board canonical**

Add this note immediately under the new `Progress Board` heading or immediately before `## Dispatch Log`:

```md
> The `Progress Board` is the canonical store for rendered-progress inputs. The reply must not invent values that are absent from this section.
```

- [ ] **Step 4: Run the schema check again to verify the template now exposes the required fields**

Run:

```powershell
rg -n "Progress Board|Workstream ID|Source Section ID|Source Plan Revision|Workstream Type|Scope:|Owner:|Internal State Reference|Display Status|Last Update:|Blocker:|Next Handoff:|Review Pass ID" "C:\Users\domin\Documents\Codex\2026-04-25-create-a-local-repo-in-aiskill\skills\ww-subagent-orchestrator\assets\dispatch-plan-template.md"
```

Expected: one `Progress Board` section and matches for all required field labels.

- [ ] **Step 5: Commit**

```bash
git add skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md
git commit -m "feat: add ww progress board schema"
```

### Task 3: Preserve packet-to-workstream identity without creating a second progress store

**Files:**
- Modify: `skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`

- [ ] **Step 1: Write the failing identity check**

Run:

```powershell
rg -n "workstream_id|review_pass_id|Progress Board|second progress store" "C:\Users\domin\Documents\Codex\2026-04-25-create-a-local-repo-in-aiskill\skills\ww-subagent-orchestrator\references\subagent-packet-contract.md"
```

Expected: no matches for the new identity-preservation rules.

- [ ] **Step 2: Add the required linkage fields**

Extend `## Required Fields` with:

```md
- `workstream_id`
- `review_pass_id` (required for reviewer packets; omit or set `none` for non-review workstreams)
```

- [ ] **Step 3: Add the packet/storage separation rules**

Append these rules under `## Packet Rules`:

```md
- Packets are not live progress stores. Live progress is persisted in the dispatch plan `Progress Board`.
- `workstream_id` must stay stable for the same workstream across turn updates.
- Reviewer workstreams must be keyed by `source_section_id + review_pass_id`.
- If more than one reviewer is used for the same section and review pass, append a stable reviewer-specific suffix to `workstream_id`.
```

- [ ] **Step 4: Update the reviewer defaults example**

Extend the reviewer example so it demonstrates the new identifiers:

```text
source_section_id: auth-review
workstream_id: auth-review-review-1-secure-software-engineer
review_pass_id: review-1
```

- [ ] **Step 5: Run the identity check again**

Run:

```powershell
rg -n "workstream_id|review_pass_id|Progress Board|stable for the same workstream|source_section_id \+ review_pass_id" "C:\Users\domin\Documents\Codex\2026-04-25-create-a-local-repo-in-aiskill\skills\ww-subagent-orchestrator\references\subagent-packet-contract.md"
```

Expected: matches for the new identity linkage and “packet is not a progress store” rules.

- [ ] **Step 6: Commit**

```bash
git add skills/ww-subagent-orchestrator/references/subagent-packet-contract.md
git commit -m "feat: link ww packets to progress workstreams"
```

### Task 4: Validate synchronized rollout across the three implementation artifacts

**Files:**
- Modify: `skills/ww-subagent-orchestrator/SKILL.md` if validation reveals gaps
- Modify: `skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md` if validation reveals gaps
- Modify: `skills/ww-subagent-orchestrator/references/subagent-packet-contract.md` if validation reveals gaps

- [ ] **Step 1: Run a synchronized contract check across all three files**

Run:

```powershell
rg -n "Status Summary|Subagent Progress|Decision Block|Document Summary|Progress Board|Workstream ID|Display Status|Review Pass ID|workstream_id|review_pass_id" `
  "C:\Users\domin\Documents\Codex\2026-04-25-create-a-local-repo-in-aiskill\skills\ww-subagent-orchestrator\SKILL.md" `
  "C:\Users\domin\Documents\Codex\2026-04-25-create-a-local-repo-in-aiskill\skills\ww-subagent-orchestrator\assets\dispatch-plan-template.md" `
  "C:\Users\domin\Documents\Codex\2026-04-25-create-a-local-repo-in-aiskill\skills\ww-subagent-orchestrator\references\subagent-packet-contract.md"
```

Expected: all three files expose the new reply contract and progress identity vocabulary. No file should be missing the concepts it is responsible for.

- [ ] **Step 2: Validate the skill package metadata**

Run:

```powershell
& 'C:\Users\domin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'C:/Users/domin/.codex/skills/.system/skill-creator/scripts/quick_validate.py' 'C:\Users\domin\Documents\Codex\2026-04-25-create-a-local-repo-in-aiskill\skills\ww-subagent-orchestrator'
```

Expected: `Skill is valid!`

- [ ] **Step 3: Run a placeholder scan against the touched files**

Run:

```powershell
rg -n "TBD|TODO|implement later|fill in details" `
  "C:\Users\domin\Documents\Codex\2026-04-25-create-a-local-repo-in-aiskill\skills\ww-subagent-orchestrator\SKILL.md" `
  "C:\Users\domin\Documents\Codex\2026-04-25-create-a-local-repo-in-aiskill\skills\ww-subagent-orchestrator\assets\dispatch-plan-template.md" `
  "C:\Users\domin\Documents\Codex\2026-04-25-create-a-local-repo-in-aiskill\skills\ww-subagent-orchestrator\references\subagent-packet-contract.md"
```

Expected: no matches.

- [ ] **Step 4: Commit**

```bash
git add skills/ww-subagent-orchestrator/SKILL.md skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md skills/ww-subagent-orchestrator/references/subagent-packet-contract.md
git commit -m "chore: validate ww transparency contracts"
```
