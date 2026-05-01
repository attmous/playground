# Daedalus Playground

Small target repository for smoke testing Daedalus workflow onboarding.

The code is intentionally simple: a tiny Python package under `src/` plus one
pytest file. Daedalus workflow smoke tests can safely create issues, bootstrap a
`WORKFLOW.md`, dispatch an agent, open a pull request, and run CI against this
repository without touching production code.

## Local Checks

```bash
python3 -m pip install -e .[test]
pytest
```

## Daedalus Smoke Path

This repository is bootstrapped with `WORKFLOW.md` for the Daedalus
`change-delivery` workflow. Create or reuse a small GitHub issue with the
`active-lane` and `daedalus-smoke` labels, then validate the contract:

```bash
hermes daedalus validate
```

For a local parser/runtime check when the Hermes top-level plugin command is not
available, invoke the plugin CLI directly:

```bash
python3 ~/.hermes/plugins/daedalus/daedalus_cli.py validate --format json
```

Good smoke issues are small, testable changes such as adding another greeting
format or calculator helper.
