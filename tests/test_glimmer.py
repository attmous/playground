from daedalus_playground.glimmer import glimmer_token


def test_glimmer_token_uses_default_name() -> None:
    assert glimmer_token() == "Glimmer: Daedalus"


def test_glimmer_token_trims_custom_name() -> None:
    assert glimmer_token("  Hermes  ") == "Glimmer: Hermes"


def test_glimmer_token_uses_default_for_blank_name() -> None:
    assert glimmer_token("   ") == "Glimmer: Daedalus"
