# Installing WorkWork In Claude Code

WorkWork ships a Claude Code plugin manifest at `.claude-plugin/plugin.json`.

That manifest resolves the shared workflow files from the repo-root `skills/` directory, so keep the full repository checkout intact instead of copying only the manifest file.

## Install From A Local Checkout

Clone the repository, then point Claude Code at the local plugin manifest:

```powershell
git clone https://github.com/dominate99/WorkWork.git
cd WorkWork
```

From the cloned `WorkWork` directory after `cd WorkWork`, use this local manifest path:

`./.claude-plugin/plugin.json`

After adding the manifest, restart or reload Claude Code so it picks up the new plugin entry point.

## Post-Install Check

Make sure Superpowers is already available in Claude Code before testing `$ww`, or the command can fail even when this plugin is installed correctly.

Start a new Claude Code session and trigger `$ww` once. If the workflow is available, Claude Code should enter the WorkWork estimation/planning flow instead of treating `$ww` as plain text.

> Warning: avoid duplicate installs. Enable only one WorkWork plugin entry or one WorkWork copy at a time.
>
> If you already have another WorkWork copy enabled in Claude Code, disable or remove that older copy before enabling this local checkout.

## Current Scope

This repository does not currently provide a marketplace package or a one-command Claude Code installer.

The supported Claude Code surface today is the local manifest path:

`./.claude-plugin/plugin.json`
