import pytest

from playground.grove import make_slug


def test_make_slug_replaces_punctuation_with_hyphens() -> None:
    assert make_slug("Hello, Grove!") == "hello-grove"


def test_make_slug_collapses_repeated_separators() -> None:
    assert make_slug("alpha --- beta___gamma") == "alpha-beta-gamma"


def test_make_slug_transliterates_unicode_accents() -> None:
    assert make_slug("Crème Brûlée déjà vu") == "creme-brulee-deja-vu"


def test_make_slug_trims_to_max_length_without_trailing_hyphen() -> None:
    assert make_slug("alpha beta gamma", max_length=11) == "alpha-beta"


def test_make_slug_returns_item_for_empty_result() -> None:
    assert make_slug("") == "item"
    assert make_slug(" !!! ") == "item"


def test_make_slug_requires_positive_max_length() -> None:
    with pytest.raises(ValueError, match="max_length must be positive"):
        make_slug("grove", max_length=0)
