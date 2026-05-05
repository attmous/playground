from playground.comet import comet_token


def test_comet_token_uses_default_name() -> None:
    assert comet_token() == "Comet: Sprints"


def test_comet_token_trims_custom_name() -> None:
    assert comet_token("  Hermes  ") == "Comet: Hermes"


def test_comet_token_uses_default_for_blank_name() -> None:
    assert comet_token("   ") == "Comet: Sprints"
