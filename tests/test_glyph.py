from playground.glyph import format_glyph_token


def test_format_glyph_token_uses_default_name() -> None:
    assert format_glyph_token() == "Glyph: Sprints"


def test_format_glyph_token_trims_custom_name() -> None:
    assert format_glyph_token("  Hermes  ") == "Glyph: Hermes"


def test_format_glyph_token_uses_default_for_blank_name() -> None:
    assert format_glyph_token("   ") == "Glyph: Sprints"
