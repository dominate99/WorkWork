# WWW Strict Review Mode Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extend the packaged `ww-subagent-orchestrator` contract with a strict `$www` mode that reuses `$ww` but forces a deterministic high-standard review-and-patch loop for `design-spec` and `implementation-plan` artifacts.

**Architecture:** Keep `$www` as a strict layer on top of `$ww`, not a second workflow system. The implementation should update the packaged skill contract first, then add the minimal runtime-state extensions needed to represent strict mode cleanly: `quality_mode` in the working brief and a `strict_review` block in the dispatch plan. Finally, align template and maintainer docs and verify both `$ww` and `$www` against the new behavior so strict mode adds rigor without regressing the standard flow.

**Tech Stack:** Markdown skill files, Markdown templates, maintainer docs, PowerShell, `rg`, Git

---

### Task 1: Add `$www` trigger semantics and strict-mode rules to the packaged skill contract

**Files:**
- Modify: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`

- [ ] **Step 1: Confirm the packaged skill does not already define `$www`**

Run:

```powershell
rg -n "\$www|quality_mode|strict_review|no material findings" "C:\Users\domin\Documents\AI\AIskill\WorkWork\.worktrees\install-readiness-sandbox\plugins\workwork\skills\ww-subagent-orchestrator\SKILL.md"
```

Expected: no matches for `$www`, `quality_mode`, or `strict_review`; `no material findings` should only appear in the reviewer-convergence guidance.

- [ ] **Step 2: Add `$www` to the skill overview and core rules**

Update `SKILL.md` so it explicitly defines:

```md
- `$ww` = standard planning-and-dispatch workflow
- `$www` = strict mode layered on top of `$ww`
```

Also add rules equivalent to:

```md
- Treat `$www` as strict mode, not a separate orchestration system.
- `$www` applies the strict loop only to `design-spec` and `implementation-plan` targets.
- `$www` always runs `self-review -> reviewer-review -> patching -> re-review`.
- `$www` passes only on `no material findings`.
- `$www` allows exactly one patch cycle per strict-review target.
```

- [ ] **Step 3: Extend the required stage order to show where `$www` diverges**

Add wording that preserves the existing `$ww` stage order but inserts the strict-mode branch after `design-spec` or `implementation-plan` artifacts are produced:

```md
For `$www` on strict-review targets:
1. produce target artifact
2. run orchestrator self-review
3. run reviewer review
4. patch automatically if material findings exist
5. run one re-review
6. mark the target `passed` or `blocked`
```

Do not rewrite `$ww` into a separate system or imply that all artifacts use this branch.

- [ ] **Step 4: Add the objective pass/block contract**

Add wording that defines:

```md
- `passed` = reviewer reports `no material findings`
- `blocked` = re-review still reports unresolved material findings after the one allowed patch cycle
```

Also preserve the user-escalation rule by noting that blocked strict-review targets return to the higher-level round for human judgment or revision.

- [ ] **Step 5: Verify the packaged skill now contains the `$www` contract**

Run:

```powershell
rg -n "\$www|self-review|reviewer-review|patching|re-review|passed|blocked|quality_mode|no material findings" "C:\Users\domin\Documents\AI\AIskill\WorkWork\.worktrees\install-readiness-sandbox\plugins\workwork\skills\ww-subagent-orchestrator\SKILL.md"
```

Expected: matches for the new strict-mode trigger, the four-step loop, and the objective pass/block rules.

- [ ] **Step 6: Commit**

```bash
git add plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md
git commit -m "docs: define www strict review mode contract"
```

### Task 2: Add the minimal working-brief and dispatch-plan schema extensions

**Files:**
- Modify: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- Modify: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
- Modify: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`

- [ ] **Step 1: Add `quality_mode` to the working-brief template**

Update `references/working-brief-template.md` so the `Gate State` or top-level metadata guidance explicitly includes:

```md
- `quality_mode`: `standard` | `strict`
```

Keep this as the only strict-mode field in the working brief. Do not duplicate runtime loop details there.

- [ ] **Step 2: Add the `strict_review` block to the dispatch-plan template**

Insert a block in `assets/dispatch-plan-template.md` near the top-level runtime metadata with this exact shape:

```yaml
strict_review:
  mode: standard | strict
  target: none | design-spec | implementation-plan
  state: idle | self-review | reviewer-review | patching | re-review | passed | blocked
  cycle_count: 0
```

Represent it in Markdown-template form, but preserve the structure and allowed values exactly.

- [ ] **Step 3: Update `SKILL.md` so the schema extensions are part of the contract**

Add wording in the working-brief and dispatch-plan sections that states:

```md
- working briefs record `quality_mode`
- dispatch plans own the live `strict_review` runtime state
- `design-spec` and `implementation-plan` artifacts stay content-focused and do not carry strict-mode headers
```

- [ ] **Step 4: Verify the templates now reflect the approved minimal structure**

Run:

```powershell
rg -n "quality_mode|strict_review|design-spec|implementation-plan|cycle_count" `
  "C:\Users\domin\Documents\AI\AIskill\WorkWork\.worktrees\install-readiness-sandbox\plugins\workwork\skills\ww-subagent-orchestrator\SKILL.md" `
  "C:\Users\domin\Documents\AI\AIskill\WorkWork\.worktrees\install-readiness-sandbox\plugins\workwork\skills\ww-subagent-orchestrator\references\working-brief-template.md" `
  "C:\Users\domin\Documents\AI\AIskill\WorkWork\.worktrees\install-readiness-sandbox\plugins\workwork\skills\ww-subagent-orchestrator\assets\dispatch-plan-template.md"
```

Expected: `quality_mode` appears in the brief-related surfaces and the full `strict_review` block appears in the dispatch-plan surfaces.

- [ ] **Step 5: Commit**

```bash
git add plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md
git commit -m "docs: add www strict review schema surfaces"
```

### Task 3: Encode the deterministic strict-review state machine and transition events

**Files:**
- Modify: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- Modify: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md` if state fields need clarifying notes

- [ ] **Step 1: Add the target-scoped state-machine rules to `SKILL.md`**

Document that strict-review state is per target, not latched across the entire round. Include equivalent wording to:

```md
- `design-spec` and `implementation-plan` each run their own strict-review cycle
- when a new strict-review target starts, `strict_review.target` switches and `strict_review.state` resets from `idle`
- `passed` and `blocked` apply to the current target only
```

- [ ] **Step 2: Add the event-driven transitions**

Add a concise transition table or numbered rules covering these events and transitions:

```text
STRICT_TARGET_STARTED: idle -> self-review
SELF_REVIEW_COMPLETED: self-review -> reviewer-review
REVIEW_FOUND_NO_MATERIAL_FINDINGS: reviewer-review -> passed
REVIEW_FOUND_MATERIAL_FINDINGS: reviewer-review -> patching
PATCH_COMPLETED: patching -> re-review
REVIEW_FOUND_NO_MATERIAL_FINDINGS: re-review -> passed
REVIEW_FOUND_MATERIAL_FINDINGS: re-review -> blocked
```

Also state that entering `patching` increments `cycle_count` from `0` to `1`.

- [ ] **Step 3: Forbid alternate loop behavior**

Add explicit anti-ambiguity rules:

```md
- no direct `reviewer-review -> blocked` on the first material finding
- no direct `patching -> passed`
- no orchestrator-only shortcut from `re-review` to `passed`
- no second patch cycle
```

This closes the loopholes that would otherwise turn `$www` into a subjective mode.

- [ ] **Step 4: Verify the strict-review runtime contract is complete**

Run:

```powershell
rg -n "STRICT_TARGET_STARTED|SELF_REVIEW_COMPLETED|REVIEW_FOUND_NO_MATERIAL_FINDINGS|REVIEW_FOUND_MATERIAL_FINDINGS|PATCH_COMPLETED|no second patch cycle|no orchestrator-only shortcut" "C:\Users\domin\Documents\AI\AIskill\WorkWork\.worktrees\install-readiness-sandbox\plugins\workwork\skills\ww-subagent-orchestrator\SKILL.md"
```

Expected: matches for all event names and the anti-ambiguity rules.

- [ ] **Step 5: Commit**

```bash
git add plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md
git commit -m "docs: add deterministic www strict review transitions"
```

### Task 4: Align maintainer documentation and verification guidance with the new strict mode

**Files:**
- Create: `docs/maintainers/specs/2026-05-14-www-strict-review-mode-design.md` if no persisted design spec is written during implementation
- Modify: `README.md` if a user-facing mention of `$www` is added now
- Modify: `docs/maintainers/plans/2026-05-14-www-strict-review-mode.md`

- [ ] **Step 1: Decide whether the approved chat design must be persisted as a maintainer spec**

Before touching runtime docs, check whether the implementation round now needs a written design artifact for future reference:

```powershell
Test-Path "C:\Users\domin\Documents\AI\AIskill\WorkWork\.worktrees\install-readiness-sandbox\docs\maintainers\specs\2026-05-14-www-strict-review-mode-design.md"
```

Expected: likely `False` on the first pass.

If missing, create a short maintainer spec that captures the approved `$www` decisions from the working brief before finalizing implementation.

- [ ] **Step 2: Add explicit verification scenarios for both `$ww` and `$www`**

In this implementation plan and any companion spec, define verification commands or manual scenarios equivalent to:

```text
- `$ww make a plan ...` still follows the standard flow without strict-review state
- `$www make a plan ...` records `quality_mode: strict` and enters strict-review state only for design-spec / implementation-plan targets
- strict review reaches `passed` only on `no material findings`
- one unresolved material finding after re-review leads to `blocked`
```

Do not claim these scenarios pass until the later execution round actually runs them.

Verification scenarios and acceptance checks for the later execution round:

- Scenario: `$ww make a plan ...`
  Expected acceptance check: the round stays in standard mode, any persisted working brief records standard intent, and no live `strict_review` gate is activated for the normal `$ww` planning flow.
- Scenario: `$www make a plan ...`
  Expected acceptance check: the persisted working brief records `quality_mode: strict`, and the dispatch plan uses `strict_review` only when the active review target is a persisted `design-spec` or `implementation-plan`.
- Scenario: strict review returns `passed`
  Expected acceptance check: the active strict-review target reaches `passed` only when the reviewer output is exactly `no material findings`.
- Scenario: strict review fails after the allowed patch cycle
  Expected acceptance check: if material findings remain after `self-review -> reviewer-review -> patching -> re-review`, the target moves to `blocked` and requires revise or a later approved round or revision before further strict review work.

These are verification scenarios and acceptance checks only. This plan does not claim that runtime tests for them have been executed or are currently passing.

- [ ] **Step 3: Review the final diff for scope discipline**

Run:

```powershell
git -c safe.directory='C:/Users/domin/Documents/AI/AIskill/WorkWork/.worktrees/install-readiness-sandbox' -C 'C:\Users\domin\Documents\AI\AIskill\WorkWork\.worktrees\install-readiness-sandbox' diff -- plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md docs/maintainers/specs docs/maintainers/plans
```

Expected: only `$www` strict-mode contract, schema, spec, and plan changes appear; no unrelated packaging or install-doc edits.

- [ ] **Step 4: Run a final worktree check**

Run:

```powershell
git -c safe.directory='C:/Users/domin/Documents/AI/AIskill/WorkWork/.worktrees/install-readiness-sandbox' -C 'C:\Users\domin\Documents\AI\AIskill\WorkWork\.worktrees\install-readiness-sandbox' status --short
```

Expected: only the intended `$www` implementation artifacts remain staged or committed.

- [ ] **Step 5: Commit**

```bash
git add docs/maintainers/specs docs/maintainers/plans README.md
git commit -m "docs: align maintainer guidance for www strict mode"
```
