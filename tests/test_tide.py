from playground.tide import tide_token


def test_tide_token_uses_default_name() -> None:
    assert tide_token() == "Tide: Sprints"


def test_tide_token_trims_custom_name() -> None:
    assert tide_token("  Hermes  ") == "Tide: Hermes"


def test_tide_token_uses_default_for_blank_name() -> None:
    assert tide_token("   ") == "Tide: Sprints"
