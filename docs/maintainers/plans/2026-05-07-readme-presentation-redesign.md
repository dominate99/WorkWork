# README Presentation Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite the repository root `README.md` so it reads sharper, cleaner, and more human-friendly on GitHub while staying concise and working well for users of `Codex`, `Claude Code`, and similar agent-tool workflows.

**Architecture:** Treat the approved spec as the source of truth, then rewrite `README.md` in one bounded pass with a stronger opening, an explicit compatibility callout near the top, a skim-first section order, and light GitHub-native presentation polish. Keep all behavior and contract files untouched. Validate the result with targeted text searches and a final diff review against the old README so the change stays presentation-only.

**Tech Stack:** Markdown, GitHub README rendering, PowerShell, `rg`, Git

---

### Task 1: Rewrite the README structure and opening so the page leads with value

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Confirm the current opener and section order**

Run:

```powershell
rg -n "WW Subagent Orchestrator Skill|What This Skill Does|Install|Repository Contents|Validation" "C:\Users\domin\Documents\AI\AIskill\WorkWork\README.md"
```

Expected: matches showing the current inventory-first structure and the existing top-level sections.

- [ ] **Step 2: Rewrite the top of the README with a sharper product-style intro**

Replace the current opening with this concise, GitHub-friendly structure:

```md
# WW Subagent Orchestrator Skill

A reusable skill for turning `$ww` into a disciplined orchestration flow across `Codex`, `Claude Code`, and similar agent-tool workflows.

> Built for experienced agent-tool users who want a tighter, more predictable `$ww` process.
```

Keep the wording concise and technical. Do not add badges, custom fonts, or decorative styling.

- [ ] **Step 3: Add the compatibility callout immediately below the opening**

Insert a short compatibility note directly under the intro:

```md
> Works across `Codex`, `Claude Code`, and similar workflows without locking the repo to a single tool.
```

This callout should be short and direct. It should not become a platform guide.

- [ ] **Step 4: Reorder the body so practical orientation comes first**

Revise the section order to follow this rough flow:

1. opening value proposition
2. compatibility note
3. `What This Skill Does`
4. `Install`
5. `Repository Contents`
6. `Persona Registry`
7. `Maintainer Docs`
8. `Validation`
9. `Notes`

Use this content strategy inside the rewritten body:

```md
## What This Skill Does

The skill is designed to:

- estimate work before dispatch
- choose the right top-level orchestrator persona
- build a working brief
- create a tracked dispatch plan file
- coordinate persona-bound subagents
- bind Superpowers workflows at each stage
```

Keep the rest of the section concise and outcome-oriented. Avoid turning it into a long tutorial.

- [ ] **Step 5: Run a post-rewrite structure check**

Run:

```powershell
rg -n "^# |^## |^> Works across|^A reusable skill|^The skill is designed to:" "C:\Users\domin\Documents\AI\AIskill\WorkWork\README.md"
```

Expected: the opening, compatibility note, and `What This Skill Does` section appear before repository inventory and maintainer material.

- [ ] **Step 6: Commit**

```bash
git add README.md
git commit -m "docs: reshape readme for clearer product-style intro"
```

### Task 2: Add light GitHub-native polish and verify the README stays concise

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Confirm the README still has the compatibility and install sections after the rewrite**

Run:

```powershell
rg -n "Works across `Codex`, `Claude Code`, and similar workflows|Install From GitHub|Repository Contents|Maintainer Docs|Validation|Notes" "C:\Users\domin\Documents\AI\AIskill\WorkWork\README.md"
```

Expected: matches for the top compatibility callout and the downstream reference sections.

- [ ] **Step 2: Tighten the section rhythm with GitHub-native formatting only**

If the rewritten README still feels flat, add only low-risk Markdown structure such as:

```md
> This repository is intentionally concise: the README explains the workflow first, then points to reference material.
```

Keep any callout blocks short. Use them only where they improve scan speed or clarify audience boundaries.

- [ ] **Step 3: Preserve the existing install paths and maintainer references**

Keep the existing install guidance and repository references intact, but keep them lower in the page than the new opening and compatibility note.

Do not add:

- badges
- custom fonts
- CSS
- fragile color tricks
- platform-specific deep dives

- [ ] **Step 4: Run a final verification pass for readability and scope**

Run:

```powershell
rg -n "Codex|Claude Code|similar workflows|Install Manually|Install From GitHub|Repository Contents|Maintainer Docs|Validation|Notes" "C:\Users\domin\Documents\AI\AIskill\WorkWork\README.md"
```

Expected: the README clearly mentions cross-tool compatibility, keeps the install guidance intact, and still includes the repository/maintainer reference sections without letting them dominate the top of the page.

- [ ] **Step 5: Review the final diff**

Run:

```powershell
git -c safe.directory='C:/Users/domin/Documents/AI/AIskill/WorkWork' -C 'C:\Users\domin\Documents\AI\AIskill\WorkWork' diff -- README.md
```

Expected: only README wording and ordering changes, with no changes to skill behavior or other repository docs.

- [ ] **Step 6: Commit**

```bash
git add README.md
git commit -m "docs: polish readme for clearer cross-tool presentation"
```
