from playground.lyric import count_phrases


def test_count_phrases_is_case_insensitive() -> None:
    assert count_phrases("La LA la", ["la", "LA"]) == {"la": 3, "LA": 3}


def test_count_phrases_counts_repeated_non_overlapping_occurrences() -> None:
    assert count_phrases("aaaa", ["aa"]) == {"aa": 2}


def test_count_phrases_counts_multi_word_phrases() -> None:
    text = "We will rock you, we WILL rock you"

    assert count_phrases(text, ["we will rock you", "rock you"]) == {
        "we will rock you": 2,
        "rock you": 2,
    }


def test_count_phrases_returns_zero_for_empty_phrase() -> None:
    assert count_phrases("anything", [""]) == {"": 0}


def test_count_phrases_returns_zero_when_no_matches() -> None:
    assert count_phrases("quiet verse", ["chorus", "bridge"]) == {
        "chorus": 0,
        "bridge": 0,
    }
