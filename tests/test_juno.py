from daedalus_playground.juno import juno_token


def test_juno_token_uses_default_name() -> None:
    assert juno_token() == "Juno: Daedalus"


def test_juno_token_trims_custom_name() -> None:
    assert juno_token("  Hermes  ") == "Juno: Hermes"


def test_juno_token_uses_default_for_blank_name() -> None:
    assert juno_token("   ") == "Juno: Daedalus"
