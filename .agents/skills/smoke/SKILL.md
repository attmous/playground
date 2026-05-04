---
name: smoke
description: Run a fresh Sprints smoke test for daedalus-playground by syncing main, reinstalling the Sprints plugin, selecting the workflow root, applying the active workflow contract, starting managed daemons, creating or selecting a smoke issue, and observing until completion or operator attention.
---

# Smoke

Use this skill when the user asks to start or observe a Sprints smoke test for
`attmous/daedalus-playground`.

Prefer the managed daemon path. Use foreground one-shot ticks only when the
managed systemd user services are unavailable or the user explicitly asks for
manual observation.

## Inputs To Resolve

- Playground checkout: `/home/radxa/WS/daedalus-playground`
- Sprints checkout: `/home/radxa/WS/sprints`
- Workflow name: default `change-delivery`
- Workflow root: prefer `.hermes/sprints/workflow-root`

If `.hermes/sprints/workflow-root` is missing, bootstrap or scaffold the workflow
only after confirming the intended repo slug and workflow name.

## Procedure

1. Sync both repositories to `origin/main`.

```bash
git -C /home/radxa/WS/sprints status --short --branch
git -C /home/radxa/WS/sprints pull --ff-only origin main
git -C /home/radxa/WS/daedalus-playground status --short --branch
git -C /home/radxa/WS/daedalus-playground switch main
git -C /home/radxa/WS/daedalus-playground pull --ff-only origin main
```

If either checkout has local modifications, stop and report the dirty paths
unless the user already asked to discard or preserve them.

2. Reinstall the Sprints plugin from the synced Sprints checkout.

```bash
python3 /home/radxa/WS/sprints/scripts/install.py
```

3. Pick and validate the workflow.

```bash
WORKFLOW_ROOT="$(cat /home/radxa/WS/daedalus-playground/.hermes/sprints/workflow-root)"
python3 /home/radxa/WS/sprints/sprints_cli.py validate --workflow-root "$WORKFLOW_ROOT" --format text
python3 /home/radxa/WS/sprints/sprints_cli.py apply-contract --workflow-root "$WORKFLOW_ROOT" --source-ref origin/main --format text
python3 /home/radxa/WS/sprints/sprints_cli.py status --workflow-root "$WORKFLOW_ROOT" --format json
```

If `apply-contract` refuses because active lanes exist, use the
`prepare-playground` skill first or ask the user whether to force the contract.
Do not use `--force` silently.

4. Start or restart the managed services.

```bash
python3 /home/radxa/WS/sprints/sprints_cli.py codex-app-server up --workflow-root "$WORKFLOW_ROOT"
python3 /home/radxa/WS/sprints/sprints_cli.py daemon up --workflow-root "$WORKFLOW_ROOT"
python3 /home/radxa/WS/sprints/sprints_cli.py codex-app-server status --workflow-root "$WORKFLOW_ROOT" --format json
python3 /home/radxa/WS/sprints/sprints_cli.py daemon status --workflow-root "$WORKFLOW_ROOT" --json
```

If the managed daemon path is unavailable, use foreground one-shot ticks:

```bash
python3 /home/radxa/WS/sprints/sprints_cli.py daemon run --workflow-root "$WORKFLOW_ROOT" --once --json
```

Repeat one-shot ticks until the lane completes, enters `operator_attention`, or
there is no runnable work.

5. Create or select the smoke issue.

If the user supplied an issue, ensure it has the workflow-required label
`active`.

For a new issue, create a small scoped change and add `active` plus
`sprints-smoke`.

```bash
gh issue create --repo attmous/daedalus-playground --title "<smoke title>" --label active --label sprints-smoke --body '<issue body>'
```

Avoid Markdown backticks in double-quoted shell strings. Prefer single quotes or
a temporary body file when the body contains code.

6. Observe.

Poll the workflow and tracker state:

```bash
python3 /home/radxa/WS/sprints/sprints_cli.py status --workflow-root "$WORKFLOW_ROOT" --format json
python3 /home/radxa/WS/sprints/sprints_cli.py events --workflow-root "$WORKFLOW_ROOT" --limit 20 --format text
gh issue list --repo attmous/daedalus-playground --state open --label active --limit 20 --json number,title,url,labels
gh pr list --repo attmous/daedalus-playground --state open --limit 20 --json number,title,url,headRefName,statusCheckRollup
```

When a PR appears, inspect it:

```bash
gh pr view <number> --repo attmous/daedalus-playground --json number,title,state,url,headRefName,headRefOid,mergeable,isDraft,statusCheckRollup
```

7. Report outcome.

Include:

- Sprints commit used and whether plugin reinstall succeeded
- playground commit used
- workflow root and workflow name
- managed daemon/app-server status, or one-shot fallback used
- smoke issue URL
- PR URL, branch, commit, CI/check status
- final lane status: complete, running, retry, or operator_attention
- any anomalies observed, especially stale status fields, daemon lease behavior,
  or completed runs with misleading `error` fields

## When Starting Over

Run the `prepare-playground` skill first when the user asks to clean before a
new smoke. That skill stops services, closes open PRs, and removes active labels
without deleting workflow contracts or runtime state unless explicitly asked.
