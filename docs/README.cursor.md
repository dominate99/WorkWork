# Installing WorkWork In Cursor

WorkWork ships a Cursor plugin manifest at `.cursor-plugin/plugin.json`.

The canonical packaged runtime skill lives under `plugins/workwork/skills/ww-subagent-orchestrator/`. Keep the full repository checkout intact instead of copying only the manifest file.

The local manifest path below is the current Cursor entry point described by this repository; validator-backed runtime confirmation is still pending in a later task.

## Install From A Local Checkout

Clone the repository, then point Cursor at the local plugin manifest:

```powershell
git clone https://github.com/dominate99/WorkWork.git
cd WorkWork
```

In Cursor, select the `.cursor-plugin/plugin.json` file inside the cloned repository.

If Cursor accepts a path relative to the cloned `WorkWork` directory after `cd WorkWork`, the equivalent manifest path is:

`./.cursor-plugin/plugin.json`

After adding the manifest, restart or reload Cursor so it picks up the new plugin entry point.

## Post-Install Check

Make sure Superpowers is already available in Cursor before testing `$ww`, or the command can fail even when this plugin is installed correctly.

Start a new Cursor session and trigger `$ww` once. If the workflow is available, Cursor should enter the WorkWork estimation/planning flow instead of treating `$ww` as plain text.

> Warning: avoid duplicate installs. Keep only one enabled WorkWork manifest or one enabled WorkWork checkout in Cursor at a time.
>
> If you already have another WorkWork copy enabled in Cursor, disable or remove that older copy before enabling this local checkout.

## Current Scope

This repository does not currently ship a one-command Cursor installer.
