from playground.beacon import beacon_token


def test_beacon_token_uses_default_name() -> None:
    assert beacon_token() == "Beacon: Sprints"


def test_beacon_token_trims_custom_name() -> None:
    assert beacon_token("  Hermes  ") == "Beacon: Hermes"


def test_beacon_token_falls_back_for_blank_name() -> None:
    assert beacon_token("   ") == "Beacon: Sprints"
