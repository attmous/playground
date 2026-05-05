_GREETING_TEMPLATES = {
    "friendly": "Hello, {name}!",
    "formal": "Salutations, {name}.",
    "farewell": "Goodbye, {name}.",
}


def _normalize_name(name: str) -> str:
    clean_name = name.strip()
    return clean_name or "Sprints"


def render_greeting_template(template_name: str, name: str = "Sprints") -> str:
    """Render a built-in greeting template with a normalized name."""
    template = _GREETING_TEMPLATES.get(template_name)
    if template is None:
        available = ", ".join(sorted(_GREETING_TEMPLATES))
        raise ValueError(
            f"Unknown greeting template: {template_name}. "
            f"Available templates: {available}."
        )

    return template.format(name=_normalize_name(name))


def greeting(name: str = "Sprints") -> str:
    """Return a predictable greeting for smoke tests."""
    return render_greeting_template("friendly", name)


def salutation(name: str = "Sprints") -> str:
    """Return the requested salutation helper."""
    return render_greeting_template("formal", name)
