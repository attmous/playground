# Code Workflow Concurrency 3 Smoke

Date: 2026-05-06
Smoke: issues #183-#187, PRs #188-#192
Workflow root: /home/radxa/.hermes/workflows/attmous-playground-code

## Issue

The simplified `code` workflow completed the five-ticket smoke only after
several runtime and workflow-contract fixes.

Concrete symptoms:

- Claimed issues were released because active detection still expected the
  entry `todo` label after claim removed it and added `in-progress`.
- Released lane IDs suppressed later re-intake, so reset smoke tickets were not
  eligible even after labels were restored.
- Orphaned engine actor runs from released lanes continued to consume `coder`
  capacity.
- `workspaceWrite` actor turns could not write linked-worktree git metadata
  under `/home/radxa/WS/playground/.git/worktrees/...`.
- Actor turns could not push or call GitHub until `networkAccess: true` was
  present in the turn sandbox policy.
- The workflow told actors to open `.codex/skills/land/SKILL.md`, but Sprints
  injects bundled skills into the prompt; the file does not exist in the lane
  worktree.
- The first three lanes consumed the default retry budget while the runtime
  issues were being fixed.

## Resolution

- Sprints local commit `61c7fc8` fixed claim-label active detection, re-intake
  after released terminal lanes, linked-worktree sandbox writable roots,
  workspace-write network access, bundled `land` skill wording, retry budget,
  and stale released runtime capacity accounting.
- Playground branch `sprints/bootstrap-code` applied the repo-owned `code`
  workflow contract through commit `dcf51b5`.
- The active contract was force-applied while lanes were active after verifying
  the changes were contract/runtime policy only.
- Operator retries were used to resume lanes after each fix.

Final result:

- PRs #188, #189, #190, #191, and #192 merged.
- Issues #183, #184, #185, #186, and #187 closed with labels
  `sprints-smoke` and `done`.
- `sprints status` ended with `active=0`, `dispatches=0`, `running=0`,
  `attention=0`, `retries=0`, and `status=idle`.

## Lesson Learned

For the actor-owned `code` workflow, Sprints must treat claim labels as active
lane evidence, and runtime capacity must be based on live active lane/session
state rather than stale engine rows. Codex app-server `workspaceWrite` turns
also need both the linked worktree git metadata roots and network access when
the actor owns push, PR creation, and merge.

Bundled skills are prompt content, not required files in the target repo. The
workflow contract should refer to the injected skill by name.

## Follow-Up

- Add focused tests for claim-label active detection, re-intake after released
  lanes, and stale released engine runtime capacity.
- Consider making actor success that closes/issues marks `done` surface as a
  clearer terminal state than `released` in `sprints status`.
- Keep retry budget high enough for full actor-owned implementation through
  merge, or separate setup/runtime failures from actor attempt limits.
