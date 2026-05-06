from playground.ivor import normalize_ivor_key


def test_normalize_ivor_key_uses_default_fallback() -> None:
    assert normalize_ivor_key() == "sprints"


def test_normalize_ivor_key_trims_and_lowercases_mixed_case_input() -> None:
    assert normalize_ivor_key("  Ivor Key  ") == "ivor-key"


def test_normalize_ivor_key_replaces_repeated_whitespace_with_hyphen() -> None:
    assert normalize_ivor_key("Ivor   Key\tAlpha\nBeta") == "ivor-key-alpha-beta"


def test_normalize_ivor_key_uses_blank_fallback() -> None:
    assert normalize_ivor_key("   \t\n  ") == "sprints"
