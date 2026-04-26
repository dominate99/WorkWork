# WW Subagent Orchestrator Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a local `$ww` skill that estimates work, creates a working brief, writes a tracked dispatch plan, and orchestrates persona-bound subagent workflows with explicit Superpowers bindings.

**Architecture:** Keep the skill lightweight and documentation-driven. Put core operating rules in `SKILL.md`, durable templates in `references/` and `assets/`, and metadata in `agents/openai.yaml` so the skill is discoverable and reusable.

**Tech Stack:** Markdown skill files, YAML metadata, local workspace docs

---

### Task 1: Finalize the design artifacts

**Files:**
- Create: `docs/superpowers/specs/2026-04-25-ww-subagent-orchestrator-design.md`
- Create: `docs/superpowers/plans/2026-04-25-ww-subagent-orchestrator.md`

- [ ] **Step 1: Write the design spec**

Add the approved routing model, stage order, working brief rules, dispatch plan gate, and section review loop to:

```md
# WW Subagent Orchestrator Design

## Required Stage Order
1. estimation
2. working brief
3. orchestrator routing
4. dispatch approval
5. section reviewer
6. orchestrator synthesis
7. human judgment
```

- [ ] **Step 2: Confirm the spec captures the approval gate**

Check that the spec explicitly states:

```text
Real dispatch only begins after Approve.
Revise returns to orchestrator editing.
Stop preserves the working brief and dispatch plan file.
```

Expected: the spec includes all three statements.

- [ ] **Step 3: Save this implementation plan**

Ensure this plan exists at:

```text
docs/superpowers/plans/2026-04-25-ww-subagent-orchestrator.md
```

- [ ] **Step 4: Commit**

```bash
git add docs/superpowers/specs/2026-04-25-ww-subagent-orchestrator-design.md docs/superpowers/plans/2026-04-25-ww-subagent-orchestrator.md
git commit -m "docs: add ww subagent orchestrator spec and plan"
```

### Task 2: Author the core skill contract

**Files:**
- Modify: `skills/ww-subagent-orchestrator/SKILL.md`
- Create: `skills/ww-subagent-orchestrator/agents/openai.yaml`

- [ ] **Step 1: Replace the template frontmatter and overview**

Write this frontmatter and opening in `skills/ww-subagent-orchestrator/SKILL.md`:

```md
---
name: ww-subagent-orchestrator
description: Use when a task should start with `$ww` to estimate work, choose an orchestrator persona, generate a working brief, create a dispatch plan file, and coordinate persona-bound subagents with Superpowers workflows.
---

# WW Subagent Orchestrator
```

- [ ] **Step 2: Add the mandatory operating workflow**

Include explicit rules for:

```md
- estimation before dispatch
- context-driven persona assignment
- file-backed dispatch plans
- reviewer findings only
- orchestrator synthesis before human judgment
```

- [ ] **Step 3: Add UI metadata**

Create `skills/ww-subagent-orchestrator/agents/openai.yaml` with:

```yaml
interface:
  display_name: "WW Subagent Orchestrator"
  short_description: "Plan and dispatch subagent work"
  default_prompt: "Use $ww to estimate the task, write the working brief, generate a dispatch plan file, and orchestrate persona-bound subagents until implementation finishes."
```

- [ ] **Step 4: Commit**

```bash
git add skills/ww-subagent-orchestrator/SKILL.md skills/ww-subagent-orchestrator/agents/openai.yaml
git commit -m "feat: add ww subagent orchestrator core skill"
```

### Task 3: Add reusable references and templates

**Files:**
- Create: `skills/ww-subagent-orchestrator/references/working-brief-template.md`
- Create: `skills/ww-subagent-orchestrator/references/persona-registry.md`
- Create: `skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
- Create: `skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`

- [ ] **Step 1: Write the working brief reference**

Add a fixed template with these headings:

```md
## Working Brief
- task routing
- orchestrator choice
- goal
- relevant context
- constraints
- risk lenses
- workstreams
- workflow bindings by stage
- dispatch recommendation
```

- [ ] **Step 2: Write the persona registry reference**

Document:

```md
- built-in registry
- project registry at docs/superpowers/personas/registry.yaml
- persona rationale requirement
- reviewer vs implementer separation
```

- [ ] **Step 3: Write the packet contract reference**

Document:

```md
- estimation_complete
- working_brief_ready
- dispatch_decision
- workflow_bindings[]
- handoff_rule
- requires_human_judgment
```

- [ ] **Step 4: Write the dispatch plan template**

Add a Markdown template that includes:

```md
- one approval state aligned to Approve / Revise / Stop
- explicit gate checks
- per-section review loop
- no real dispatch before approval
```

- [ ] **Step 5: Commit**

```bash
git add skills/ww-subagent-orchestrator/references/working-brief-template.md skills/ww-subagent-orchestrator/references/persona-registry.md skills/ww-subagent-orchestrator/references/subagent-packet-contract.md skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md
git commit -m "feat: add ww subagent orchestrator references and templates"
```

### Task 4: Validate the local skill package

**Files:**
- Modify: `skills/ww-subagent-orchestrator/SKILL.md` if validation reveals gaps

- [ ] **Step 1: Inspect the skill tree**

Run:

```bash
Get-ChildItem -Recurse skills/ww-subagent-orchestrator
```

Expected: `SKILL.md`, `agents/openai.yaml`, `references/*`, and `assets/dispatch-plan-template.md` all exist.

- [ ] **Step 2: Validate frontmatter and metadata if dependencies are available**

Run:

```bash
& 'C:\Users\domin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'C:/Users/domin/.codex/skills/.system/skill-creator/scripts/quick_validate.py' 'C:\Users\domin\Documents\Codex\2026-04-25-create-a-local-repo-in-aiskill\skills\ww-subagent-orchestrator'
```

Expected: validation passes. If Python dependencies are missing, record the blocker and perform a manual frontmatter check instead.

- [ ] **Step 3: Self-review against the spec**

Check that the skill explicitly covers:

```text
orchestrator routing, estimation gate, working brief, dispatch plan file, Approve/Revise/Stop, per-section reviewer loop, and Superpowers bindings
```

- [ ] **Step 4: Commit**

```bash
git add skills/ww-subagent-orchestrator
git commit -m "chore: validate ww subagent orchestrator skill"
```
