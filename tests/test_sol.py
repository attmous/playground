from playground.sol import sol_token


def test_sol_token_uses_default_name() -> None:
    assert sol_token() == "Sol: Sprints"


def test_sol_token_trims_custom_name() -> None:
    assert sol_token("  Hermes  ") == "Sol: Hermes"


def test_sol_token_uses_default_for_blank_name() -> None:
    assert sol_token("   ") == "Sol: Sprints"
