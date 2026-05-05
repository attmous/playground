---
name: clean
description: Clean the playground repository before a fresh Sprints smoke test by stopping active Sprints daemons, closing open playground PRs, and removing active workflow labels from open issues.
---

# Clean

Use this skill when starting over a Sprints smoke test in `attmous/playground`.

The goal is to leave the repository and tracker with no active Sprints work before a
new smoke issue is created.

## Preconditions

- Run from `/home/radxa/WS/playground` unless the user gives another checkout.
- Confirm the checkout is `attmous/playground`.
- Prefer the workflow root from `.hermes/sprints/workflow-root` when present.
- Do not delete branches, worktrees, state files, or workflow contracts unless the user explicitly asks.

## Procedure

1. Inspect local and remote state.

```bash
git status --short --branch
git remote -v
cat .hermes/sprints/workflow-root
gh pr list --repo attmous/playground --state open --limit 100 --json number,title,url,headRefName
gh issue list --repo attmous/playground --state open --label active --limit 100 --json number,title,url,labels
gh issue list --repo attmous/playground --state open --label active-lane --limit 100 --json number,title,url,labels
```

2. Stop active Sprints managed services for this workflow root.

Use the workflow root read from `.hermes/sprints/workflow-root`.

```bash
python3 /home/radxa/WS/sprints/sprints_cli.py daemon down --workflow-root "$WORKFLOW_ROOT"
python3 /home/radxa/WS/sprints/sprints_cli.py codex-app-server down --workflow-root "$WORKFLOW_ROOT"
python3 /home/radxa/WS/sprints/sprints_cli.py daemon status --workflow-root "$WORKFLOW_ROOT" --json
python3 /home/radxa/WS/sprints/sprints_cli.py codex-app-server status --workflow-root "$WORKFLOW_ROOT" --format json
```

If the services are not installed or already inactive, treat that as clean enough and continue.

3. Close open playground PRs.

Close every open PR in `attmous/playground` with a comment that this is
preparation for a fresh smoke test. Do not delete branches unless the user asks.

```bash
gh pr close <number> --repo attmous/playground --comment "Closing before starting a fresh Sprints smoke test."
```

4. Remove active workflow labels from open issues.

Remove both historical active labels if present:

- `active`
- `active-lane`

Do not close issues unless the user asks.

```bash
gh issue edit <number> --repo attmous/playground --remove-label active
gh issue edit <number> --repo attmous/playground --remove-label active-lane
```

If a label is absent on an issue, ignore that specific removal failure and continue.

5. Verify cleanup.

```bash
gh pr list --repo attmous/playground --state open --limit 100 --json number,title,url
gh issue list --repo attmous/playground --state open --label active --limit 100 --json number,title,url,labels
gh issue list --repo attmous/playground --state open --label active-lane --limit 100 --json number,title,url,labels
python3 /home/radxa/WS/sprints/sprints_cli.py status --workflow-root "$WORKFLOW_ROOT" --format json
```

Report:

- whether daemon and app-server services are stopped or were not installed
- PR numbers closed
- issues that had `active` or `active-lane` removed
- remaining open PRs or active-labeled issues, if any
