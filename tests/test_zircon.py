from playground.zircon import group_notes


def test_group_notes_groups_text_by_sorted_type() -> None:
    items = [
        {"type": "fix", "text": "repair login"},
        {"type": "feature", "text": "add dashboard"},
        {"type": "fix", "text": "handle timeout"},
    ]

    assert group_notes(items) == {
        "feature": ["add dashboard"],
        "fix": ["repair login", "handle timeout"],
    }


def test_group_notes_uses_other_for_missing_or_blank_type() -> None:
    items = [
        {"text": "document fallback"},
        {"type": "", "text": "empty type"},
        {"type": "  ", "text": "blank type"},
    ]

    assert group_notes(items) == {
        "other": ["document fallback", "empty type", "blank type"],
    }


def test_group_notes_strips_and_skips_blank_text() -> None:
    items = [
        {"type": "fix", "text": "  trim whitespace  "},
        {"type": "fix", "text": ""},
        {"type": "fix", "text": "   "},
        {"type": "feature"},
    ]

    assert group_notes(items) == {"fix": ["trim whitespace"]}


def test_group_notes_preserves_order_within_each_type() -> None:
    items = [
        {"type": "feature", "text": "first feature"},
        {"type": "fix", "text": "first fix"},
        {"type": "feature", "text": "second feature"},
        {"type": "fix", "text": "second fix"},
    ]

    assert group_notes(items) == {
        "feature": ["first feature", "second feature"],
        "fix": ["first fix", "second fix"],
    }
