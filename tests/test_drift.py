from playground.drift import drift_token


def test_drift_token_uses_default_name() -> None:
    assert drift_token() == "Drift: Sprints"


def test_drift_token_trims_custom_name() -> None:
    assert drift_token("  Hermes  ") == "Drift: Hermes"


def test_drift_token_falls_back_for_blank_name() -> None:
    assert drift_token("   ") == "Drift: Sprints"
