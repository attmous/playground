# Sprints Playground

Small target repository for smoke testing Sprints workflow onboarding.

The code is intentionally simple: a tiny Python package under `src/` plus one
pytest suite. Sprints workflow smoke tests can safely create issues, bootstrap a
`WORKFLOW.md`, dispatch an agent, open a pull request, and run CI against this
repository without touching production code.

## Usage

```python
from playground import greeting, render_greeting_template, salutation

greeting()
# 'Hello, Sprints!'
greeting("Hermes")
# 'Hello, Hermes!'

salutation()
# 'Salutations, Sprints.'
salutation("Hermes")
# 'Salutations, Hermes.'

render_greeting_template("farewell")
# 'Goodbye, Sprints.'
render_greeting_template("farewell", "Hermes")
# 'Goodbye, Hermes.'
```

## Local Checks

```bash
python3 -m pip install -e .[test]
pytest
```

## Sprints Smoke Path

This repository is bootstrapped with `WORKFLOW.md` for the Sprints
`change-delivery` workflow. Create or reuse a small GitHub issue with the
`active-lane` and `sprints-smoke` labels, then validate the contract:

```bash
hermes sprints validate
```

For a local parser/runtime check when the Hermes top-level plugin command is not
available, invoke the plugin CLI directly:

```bash
python3 ~/.hermes/plugins/sprints/sprints_cli.py validate --format json
```

Good smoke issues are small, testable changes such as adding another greeting
format or calculator helper.
