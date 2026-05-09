# Installing WorkWork In Codex

WorkWork ships a Codex plugin entry point at `.codex-plugin/`.

That entry point resolves the shared workflow files from the repo-root `skills/` directory via `../skills/`, so the recommended Codex install path is a full local checkout with the local `.codex-plugin` directory kept in place.

## Recommended Install Path

Use a full local checkout, then point Codex at the cloned repo's `.codex-plugin` directory.

```powershell
git clone https://github.com/dominate99/WorkWork.git
cd WorkWork
```

In Codex, select the cloned repo's `.codex-plugin` folder directly. If Codex accepts paths relative to the cloned `WorkWork` directory, the equivalent local plugin path is:

`./.codex-plugin`

After adding the local path, restart or reload Codex so it picks up the new entry point.

## Build-Dependent Fallback

The GitHub subdirectory URL below is not the normal supported path for this package layout. It is only a fallback to try if your Codex build both accepts repository subdirectory installs and preserves access from `.codex-plugin/` to repo-root sibling files such as `../skills/`.

That behavior is build-dependent and not verified across Codex environments.

`https://github.com/dominate99/WorkWork/tree/main/.codex-plugin`

If your Codex build does not satisfy those conditions, use the local checkout flow above instead.

After adding the plugin, restart or reload Codex so it picks up the new entry point.

## Post-Install Check

Make sure Superpowers is already available in Codex before testing `$ww`, or the command can fail even when this plugin is installed correctly.

Start a new Codex session and trigger `$ww` once. If the workflow is available, Codex should enter the WorkWork estimation/planning flow instead of treating `$ww` as plain text.

> Warning: avoid duplicate installs. Enable only one WorkWork install method at a time.
>
> If you are migrating from an older manually installed or native-skills-based WorkWork setup, disable or remove that older WorkWork copy before enabling this plugin-based install.


## Current Scope

This repository does not currently ship a one-command Codex installer.
