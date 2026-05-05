import pytest

from playground import greeting, render_greeting_template, salutation


def test_render_greeting_template_supports_built_in_templates() -> None:
    assert render_greeting_template("friendly", "Hermes") == "Hello, Hermes!"
    assert render_greeting_template("formal", "Hermes") == "Salutations, Hermes."
    assert render_greeting_template("farewell", "Hermes") == "Goodbye, Hermes."


def test_render_greeting_template_uses_default_for_blank_name() -> None:
    assert render_greeting_template("farewell", "   ") == "Goodbye, Sprints."


def test_render_greeting_template_rejects_unknown_templates() -> None:
    with pytest.raises(ValueError, match="Unknown greeting template: casual"):
        render_greeting_template("casual", "Hermes")


def test_existing_helpers_keep_their_outputs() -> None:
    assert greeting("  Hermes  ") == "Hello, Hermes!"
    assert greeting("   ") == "Hello, Sprints!"
    assert salutation("  Hermes  ") == "Salutations, Hermes."
    assert salutation("   ") == "Salutations, Sprints."
