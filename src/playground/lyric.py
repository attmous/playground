def count_phrases(text: str, phrases: list[str]) -> dict[str, int]:
    """Count non-overlapping phrase occurrences case-insensitively."""
    normalized_text = text.casefold()

    return {
        phrase: 0 if phrase == "" else normalized_text.count(phrase.casefold())
        for phrase in phrases
    }
