---
name: lessons
description: Document lessons learned after each Sprints smoke test in playground, especially observed failures, manual recoveries, product gaps, and follow-up hardening work, by writing a concise Markdown note under docs/lessons_learned.
---

# Lessons

Use this skill at the end of every Sprints smoke test in `attmous/playground`,
after the final workflow, GitHub PR, issue-label, and checkout status checks.

The goal is to preserve operator knowledge from the run without bloating the
workflow state or final chat response.

## Procedure

1. Identify the run.

Collect:

- Date in UTC.
- Issue range and PR range.
- Workflow root.
- Sprints commit and playground commit used.
- Final workflow status.
- Any manual intervention, retry, recovery, compaction, or anomaly.

2. Create or update one lesson file.

Write to:

```bash
docs/lessons_learned/YYYY-MM-DD-<short-topic>.md
```

Use a stable, descriptive topic such as:

- `concurrency-5-state-growth.md`
- `merge-readiness-retry.md`
- `issue-cleanup-inconsistency.md`

If the same topic already exists for the same date, update that file instead of
creating a near-duplicate.

3. Use this structure.

```markdown
# <Title>

Date: YYYY-MM-DD
Smoke: issues #N-#M, PRs #N-#M
Workflow root: <path>

## Issue

What happened, with concrete symptoms and command/log excerpts where useful.

## Resolution

What was done to unblock or complete the run.

## Lesson Learned

What this says about Sprints, the workflow contract, the adapter, GitHub
behavior, or operations.

## Follow-Up

Actionable hardening items. Use `None` only when there is genuinely no follow-up.
```

Keep entries factual and compact. Prefer durable details over narrative.

4. Verification.

After writing the lesson, run:

```bash
git -C /home/radxa/WS/playground status --short
```

Report the lesson file path in the smoke summary.
