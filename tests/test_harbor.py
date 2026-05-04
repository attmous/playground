from daedalus_playground.harbor import harbor_token


def test_harbor_token_uses_default_name() -> None:
    assert harbor_token() == "Harbor: Daedalus"


def test_harbor_token_trims_custom_name() -> None:
    assert harbor_token("  Hermes  ") == "Harbor: Hermes"


def test_harbor_token_uses_default_for_blank_name() -> None:
    assert harbor_token("   ") == "Harbor: Daedalus"
