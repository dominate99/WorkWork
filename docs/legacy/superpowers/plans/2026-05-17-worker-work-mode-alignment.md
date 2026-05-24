# Worker Work-Mode Alignment Implementation Plan

Goal: align the worker work-mode contract across the packaged skill contract, working brief template, dispatch plan template, packet contract, and worker prompt so the second-layer worker behavior model becomes executable instead of descriptive.

Architecture: keep one explicit propagation chain. `SKILL.md` records the canonical workflow contract, the working brief recommends section-level worker mode, the dispatch plan records the effective section decision, the worker packet freezes one execution snapshot, and the worker prompt consumes packet state in a fixed order.

Review focus: prevent contract drift between the five files. The review should look for mismatched field names, duplicated authority, missing skill-level contract updates, and any prompt wording that allows `goal_tuning` or persona style to bypass `work_mode`.

Tech stack: Markdown contracts, templates, prompt files, PowerShell, `rg`

---

- [ ] Update `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
Add the worker-mode ordering and authority-chain rules to the packaged skill contract. Keep the skill-level wording high-level, but make it explicit that `task_mode` and `work_mode` are separate and that the worker prompt must consume packet state rather than re-deriving mode from the brief.

- [ ] Update `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
Add the section-level worker-mode recommendation fields and rules. Make the working brief explicit about recommending mode from task structure while leaving final authority to the dispatch plan.

- [ ] Update `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
Add planned worker-mode fields under each section, add `Active Worker Mode` plus `Mode Change History` to the runtime ledger, and encode the authority and logging rules for mode changes.

- [ ] Update `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
Require `work_mode`, `work_mode_rationale`, `goal_tuning`, and `constraint_precedence_note` for worker packets. Keep `task_mode` separate from `work_mode`, and update the worker packet example so the new launch payload is demonstrated instead of implied.

- [ ] Update `plugins/workwork/skills/ww-subagent-orchestrator/agents/worker-prompt.md`
Reorder the worker operating rules so constraints come first, `work_mode` comes second, persona principles come third, and `goal_tuning` remains a light modifier. Add one-line behavioral definitions for all four work modes.

- [ ] Run alignment scans
Use `rg` to confirm all five files agree on the new field names, authority chain, and ordering surfaces.

Recommended checks:

```powershell
rg -n "work_mode|goal_tuning|task_mode|worker mode|authority chain|implementation_principles" `
  "plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md" `
  "plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md" `
  "plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md" `
  "plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md" `
  "plugins/workwork/skills/ww-subagent-orchestrator/agents/worker-prompt.md"
```

- [ ] Run a bounded review pass
Review the diff specifically for authority drift:
  - the skill contract must describe the same authority chain as the lower-level surfaces
  - the brief must recommend, not decide
  - the plan must decide and log
  - the packet must freeze execution state
  - the prompt must consume packet state only

- [ ] Run final verification
Check `git diff --stat` and targeted `rg` output, then confirm no unrelated skill behavior was introduced.

Recommended checks:

```powershell
git diff --stat
```

```powershell
rg -n "Worker Packet Example|work_mode|goal_tuning|constraint_precedence_note" `
  "plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md"
```

```powershell
rg -n "first obey|then apply `work_mode`|goal_tuning|plan-first|validate-first|iterate-first|conservative-first" `
  "plugins/workwork/skills/ww-subagent-orchestrator/agents/worker-prompt.md"
```
