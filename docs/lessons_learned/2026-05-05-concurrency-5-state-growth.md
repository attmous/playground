# Concurrency 5 State Growth

Date: 2026-05-05
Smoke: issues #88-#102, PRs #103-#117
Workflow root: /home/radxa/.hermes/workflows/attmous-playground-change-delivery

## Issue

The smoke created 15 more complex issues with workflow concurrency set to 5.
The first batch claimed exactly five lanes and actors ran concurrently, but the
orchestrator later failed once multiple lanes were decision-ready.

Observed failures:

```text
codex-app-server failed: Codex ran out of room in the model's context window.
codex-app-server request 'turn/start' failed: Input exceeds the maximum length of 1048576 characters.
```

The active workflow state still contained full terminal lane history from prior
smoke runs. As the new complex lanes completed, the hot state grew with actor
outputs, issue bodies, runtime sessions, transitions, and recovery artifacts.
That state was included in orchestrator prompts.

## Resolution

The run was manually unblocked by compacting workflow state:

- Removed terminal lanes from prior smoke runs.
- Later removed newly terminal lanes from the active state.
- Trimmed old orchestrator decisions and bulky runtime/session fields.

One manual compaction removed too much from active lanes by dropping
`actor_outputs`. Some lanes still had `last_actor_output`, but contract
validation expected stage-specific entries such as `actor_outputs.implementer`
or `actor_outputs.reviewer`. That produced temporary operator attention:

```text
delivery_contract_failed
completion_contract_failed
```

The affected lanes were recovered by restoring the minimal required actor output
into the expected actor slot, clearing operator attention, and returning the
lanes to `waiting`.

The smoke then completed with workflow status `idle`, active lanes `0`, running
actors `0`, decision-ready lanes `0`, and operator attention `0`. PRs #103-#117
were merged.

## Lesson Learned

Sprints needs a designed state-compaction boundary. Terminal lane history and
bulky runtime artifacts should remain available through audit or engine history,
but they should not stay in the hot orchestrator prompt payload.

Manual compaction must preserve the contract fields needed by stage validation.
For active lanes, `actor_outputs.<actor>` is not equivalent to
`last_actor_output`; both may be needed for current workflow mechanics.

Concurrency 5 works for intake and actor dispatch, but larger or more complex
runs expose prompt-size pressure quickly when prior lane history remains in hot
state.

## Follow-Up

- Add automatic hot-state compaction for terminal lanes.
- Keep only compact summaries of terminal lanes in orchestrator prompts.
- Move full actor outputs, runtime sessions, and recovery artifacts to audit or
  engine history outside the orchestrator prompt payload.
- Add a preflight prompt-size guard before starting an orchestrator turn.
- Add a compaction invariant that preserves active lane contract fields,
  especially `actor_outputs.<actor>`.
- Investigate inconsistent issue closing: all issues #88-#102 received `done`,
  but several remained GitHub-open.
