from playground.kappa import kappa_token


def test_kappa_token_uses_default_name() -> None:
    assert kappa_token() == "Kappa: Sprints"


def test_kappa_token_trims_custom_name() -> None:
    assert kappa_token("  Hermes  ") == "Kappa: Hermes"


def test_kappa_token_uses_default_for_blank_name() -> None:
    assert kappa_token("   ") == "Kappa: Sprints"
