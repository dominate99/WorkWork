# Dispatch Plan Skill Review Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix the packaged `ww-subagent-orchestrator` skill and dispatch-plan template so future dispatch plans do not repeat the concrete failures found in `docs/superpowers/dispatch-plans/2026-05-14-www-strict-review-mode.md`.

**Architecture:** Treat the reviewed dispatch plan as evidence of contract drift, then harden the active contract surfaces rather than rewriting historical artifacts. The implementation should first encode a dispatch-plan self-audit in `SKILL.md`, then tighten `dispatch-plan-template.md` so required runtime and review-lane fields are hard to omit or misuse. Finally, add maintainer verification guidance tied directly to the observed failure modes: scope parity, deprecated field exclusion, strict-review runtime presence, and durable review-lane outcome recording.

**Staff Engineer Review:** The first draft had the right scope, but its verification bar was too generic. This revision adds regression-style checks tied to the exact bad dispatch-plan shape already observed, so the implementation must prove it prevents those failures rather than merely restating the contract.

**Tech Stack:** Markdown skill files, Markdown templates, maintainer docs, PowerShell, `rg`, Git

---

### Task 1: Add dispatch-plan self-audit rules to the packaged skill contract

**Files:**
- Modify: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`

- [ ] **Step 1: Encode the concrete reviewed failure modes as contract guardrails**

Add wording to `SKILL.md` near the dispatch-plan contract and/or controller update procedure that makes these checks mandatory before the approval block is rendered:

```md
- every writable path listed in `Planned Scope` must also appear in `exclusive_write_scope`
- dispatch plans must render the top-level `Strict Review Runtime State` block even when the round is standard and the gate is idle
- deprecated fields such as `Review Status` must not appear in new dispatch plans
- every review lane record must persist a durable outcome surface, including `Strict Review Outcome` when applicable
```

Keep the rules framed as dispatch-plan validation, not as informal style guidance.

- [ ] **Step 1a: Make the audit failure mode explicit**

Add wording that the orchestrator must treat a failed dispatch-plan self-audit as a blocking authoring defect:

```md
- if scope parity, required runtime-state surfaces, or required review-lane outcome fields are missing, the dispatch plan stays in authoring/revision and must not be shown for approval yet
```

This prevents the audit from degrading into a passive reminder.

- [ ] **Step 2: Add a pre-approval self-audit step**

Extend the stage order or controller procedure so the orchestrator must review the just-written dispatch plan for:

- scope parity
- required runtime-state surfaces
- review-lane completeness
- absence of deprecated state fields

This should happen after writing the dispatch plan and before asking the user to approve it.

- [ ] **Step 3: Verify the packaged skill now prevents the reviewed drift**

Run:

```powershell
rg -n "exclusive_write_scope|Planned Scope|Strict Review Runtime State|Review Status|Strict Review Outcome|self-audit|pre-approval" "C:\Users\domin\Documents\AI\AIskill\WorkWork\.worktrees\dispatch-plan-skill-review\plugins\workwork\skills\ww-subagent-orchestrator\SKILL.md"
```

Expected: matches for scope parity, required strict-review runtime rendering, deprecated-field exclusion, durable review-lane outcome persistence, and a pre-approval self-audit step.

- [ ] **Step 3a: Add a regression-oriented acceptance scan**

Run an additional targeted check after the edits to confirm the active contract now explicitly guards against the exact bad-plan failure modes:

```powershell
rg -n "must also appear|must render|must not appear|must persist|must not be shown for approval yet" "C:\Users\domin\Documents\AI\AIskill\WorkWork\.worktrees\dispatch-plan-skill-review\plugins\workwork\skills\ww-subagent-orchestrator\SKILL.md"
```

Expected: the contract uses hard requirement language, not soft recommendations.

- [ ] **Step 4: Commit**

```bash
git add plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md
git commit -m "docs: add dispatch plan self-audit guardrails"
```

### Task 2: Tighten the dispatch-plan template around scope parity and review-lane durability

**Files:**
- Modify: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`

- [ ] **Step 1: Make the strict-review runtime block unmistakably required**

Keep the existing `Strict Review Runtime State` block, but add short template guidance that makes two things explicit:

- standard `$ww` rounds still render the block with `mode: standard`, `target: none`, `state: idle`, `cycle_count: 0`
- omission of the block is invalid, even when no strict target is active

- [ ] **Step 2: Add scope-parity reminders directly where authors fill the plan**

Near `Planned Scope` and `Scope Declarations`, add succinct template guidance equivalent to:

```md
- every writable file listed in `Planned Scope` must also appear under `exclusive_write_scope`
- `shared_read_scope` is for read-only dependencies and must not hide writable ownership
```

Do not introduce a second scope schema; reinforce the existing one.

- [ ] **Step 2a: Make omission and drift visibly invalid in the template**

Add one short note near the affected template sections that makes these invalid states explicit:

- `Planned Scope` includes a writable file not mirrored in `exclusive_write_scope`
- the strict-review runtime block is omitted
- `Review Status` reappears
- `Strict Review Outcome` is omitted from review-lane persistence

- [ ] **Step 3: Make durable review-lane outcomes explicit**

Ensure the template’s review-lane record clearly preserves:

- no `Review Status` field
- `Reviewer Findings`
- `Orchestrator Synthesis`
- `Strict Review Outcome: none | passed | blocked`

If needed, add one short note clarifying that `Strict Review Outcome` remains `none` for non-strict review lanes rather than being omitted.

- [ ] **Step 4: Verify the template reflects the new guardrails**

Run:

```powershell
rg -n "Strict Review Runtime State|mode: standard|state: idle|Planned Scope|exclusive_write_scope|shared_read_scope|Review Status|Strict Review Outcome|none \\| passed \\| blocked" "C:\Users\domin\Documents\AI\AIskill\WorkWork\.worktrees\dispatch-plan-skill-review\plugins\workwork\skills\ww-subagent-orchestrator\assets\dispatch-plan-template.md"
```

Expected: the template requires the strict-review block, reinforces scope parity, does not reintroduce `Review Status`, and preserves durable review-lane outcome fields.

- [ ] **Step 4a: Compare against the historical bad plan pattern**

Use the previously reviewed dispatch plan as a regression reference and confirm the new template would have prevented its known defects:

```powershell
rg -n "Review Status|Strict Review Runtime State|exclusive_write_scope|Strict Review Outcome" `
  "C:\Users\domin\Documents\AI\AIskill\WorkWork\.worktrees\install-readiness-sandbox\docs\superpowers\dispatch-plans\2026-05-14-www-strict-review-mode.md" `
  "C:\Users\domin\Documents\AI\AIskill\WorkWork\.worktrees\dispatch-plan-skill-review\plugins\workwork\skills\ww-subagent-orchestrator\assets\dispatch-plan-template.md"
```

Expected: the historical artifact still shows the old defect markers, while the active template encodes the replacement guardrails.

- [ ] **Step 5: Commit**

```bash
git add plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md
git commit -m "docs: harden dispatch plan template guardrails"
```

### Task 3: Align maintainer verification guidance with the reviewed failures

**Files:**
- Modify: `docs/maintainers/plans/2026-05-15-dispatch-plan-skill-review.md`
- Create or modify additional maintainer notes only if strictly necessary

- [ ] **Step 1: Persist explicit acceptance checks**

In this implementation plan, add or retain verification checks proving the fix addresses the exact reviewed defects:

```text
- planned writable scope matches `exclusive_write_scope`
- no `Review Status` field appears in new dispatch plans
- every new dispatch plan renders the strict-review runtime block, even when idle
- review lane records preserve durable outcome data, including `Strict Review Outcome`
- failed dispatch-plan self-audit blocks approval rendering until the plan is fixed
```

Do not mark those checks as passing unless the later execution round runs them.

- [ ] **Step 2: Review final diff for scope discipline**

Run:

```powershell
git -c safe.directory='C:/Users/domin/Documents/AI/AIskill/WorkWork/.worktrees/dispatch-plan-skill-review' -C 'C:\Users\domin\Documents\AI\AIskill\WorkWork\.worktrees\dispatch-plan-skill-review' diff -- plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md docs/maintainers/plans
```

Expected: only the packaged skill contract, dispatch-plan template, and this maintainer plan are in scope.

- [ ] **Step 3: Run a final worktree check**

Run:

```powershell
git -c safe.directory='C:/Users/domin/Documents/AI/AIskill/WorkWork/.worktrees/dispatch-plan-skill-review' -C 'C:\Users\domin\Documents\AI\AIskill\WorkWork\.worktrees\dispatch-plan-skill-review' status --short
```

Expected: only the intended dispatch-plan-guardrail artifacts remain staged or committed.

- [ ] **Step 4: Commit**

```bash
git add docs/maintainers/plans/2026-05-15-dispatch-plan-skill-review.md
git commit -m "docs: record dispatch plan review verification guidance"
```
