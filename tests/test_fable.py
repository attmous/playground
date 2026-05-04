from daedalus_playground.fable import fable_token


def test_fable_token_uses_default_name() -> None:
    assert fable_token() == "Fable: Daedalus"


def test_fable_token_trims_custom_name() -> None:
    assert fable_token("  Hermes  ") == "Fable: Hermes"


def test_fable_token_uses_default_for_blank_name() -> None:
    assert fable_token("   ") == "Fable: Daedalus"
