# Installing WorkWork In Claude Code

WorkWork is loaded in Claude Code from the packaged plugin root at `plugins/workwork`.

The plugin-local manifest lives at `plugins/workwork/.claude-plugin/plugin.json`, and the canonical runtime skill lives under `plugins/workwork/skills/ww-subagent-orchestrator/`.

## Install From A Local Checkout

Clone the repository, then point Claude Code at the packaged plugin root:

```powershell
git clone https://github.com/dominate99/WorkWork.git
cd WorkWork
```

From the cloned `WorkWork` directory after `cd WorkWork`, use this local plugin path:

`./plugins/workwork`

If your Claude Code build asks for a manifest path instead of a plugin directory, use:

`./plugins/workwork/.claude-plugin/plugin.json`

After adding the packaged plugin, restart or reload Claude Code so it picks up the new plugin entry point.

## Post-Install Check

Make sure Superpowers is already available in Claude Code before testing `$ww`, or the command can fail even when this plugin is installed correctly.

Start a new Claude Code session and trigger `$ww` once. If the workflow is available, Claude Code should enter the WorkWork estimation/planning flow instead of treating `$ww` as plain text.

Verified CLI smoke test from the repository root:

```powershell
claude -p --plugin-dir ./plugins/workwork '$ww make a plan to rename one heading in this README'
```

> Warning: avoid duplicate installs. Enable only one WorkWork plugin entry or one WorkWork copy at a time.
>
> If you already have another WorkWork copy or an older root-level `.claude-plugin` install enabled in Claude Code, disable or remove that older copy before enabling this packaged local checkout.

## Current Scope

This repository does not currently provide a one-command Claude Code installer.

The verified local package root is:

`./plugins/workwork`
