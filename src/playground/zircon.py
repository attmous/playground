def group_notes(items: list[dict[str, str]]) -> dict[str, list[str]]:
    """Group release note text by normalized type."""
    groups: dict[str, list[str]] = {}

    for item in items:
        text = item.get("text", "").strip()
        if not text:
            continue

        note_type = item.get("type", "").strip() or "other"
        groups.setdefault(note_type, []).append(text)

    return {note_type: groups[note_type] for note_type in sorted(groups)}
