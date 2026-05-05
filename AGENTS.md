# Repository Guidelines

This repository is a deliberately small Sprints smoke-test target.

- Keep changes small and easy to validate with `pytest`.
- Put package code in `src/playground/`.
- Put tests in `tests/` using `test_<feature>.py` names.
- Run `python3 -m pip install -e .[test]` and `pytest` before opening a PR.
- Do not commit generated Sprints runtime state, `.hermes/`, local databases,
  logs, or credentials.
