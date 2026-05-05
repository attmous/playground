from playground.umbra import umbra_token


def test_umbra_token_uses_default_name() -> None:
    assert umbra_token() == "Umbra: Sprints"


def test_umbra_token_trims_custom_name() -> None:
    assert umbra_token("  Hermes  ") == "Umbra: Hermes"


def test_umbra_token_uses_default_for_blank_name() -> None:
    assert umbra_token("   ") == "Umbra: Sprints"
