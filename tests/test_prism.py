from playground.prism import prism_token


def test_prism_token_uses_default_name() -> None:
    assert prism_token() == "Prism: Sprints"


def test_prism_token_trims_custom_name() -> None:
    assert prism_token("  Hermes  ") == "Prism: Hermes"


def test_prism_token_uses_default_for_blank_name() -> None:
    assert prism_token("   ") == "Prism: Sprints"
