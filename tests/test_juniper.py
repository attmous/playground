from copy import deepcopy

from playground.juniper import render_template


def test_render_template_replaces_simple_placeholder() -> None:
    assert render_template("Hello, {{ name }}!", {"name": "Ada"}) == "Hello, Ada!"


def test_render_template_supports_dotted_lookup() -> None:
    values = {"user": {"name": "Grace"}}

    assert render_template("Hello, {{ user.name }}!", values) == "Hello, Grace!"


def test_render_template_leaves_unknown_placeholders_unchanged() -> None:
    result = render_template("Hello, {{ missing }} and {{ user.email }}.", {"user": {}})

    assert result == "Hello, {{ missing }} and {{ user.email }}."


def test_render_template_replaces_repeated_placeholders() -> None:
    template = "{{ name }} scored for {{ name }}."

    assert render_template(template, {"name": "Juniper"}) == "Juniper scored for Juniper."


def test_render_template_strips_whitespace_inside_braces() -> None:
    template = "{{name}} {{   name   }}"

    assert render_template(template, {"name": "Maple"}) == "Maple Maple"


def test_render_template_stringifies_non_string_values() -> None:
    template = "{{ count }} {{ enabled }}"

    assert render_template(template, {"count": 3, "enabled": True}) == "3 True"


def test_render_template_does_not_mutate_values() -> None:
    values = {"user": {"name": "Ada"}, "count": 2}
    original = deepcopy(values)

    render_template("{{ user.name }} {{ count }}", values)

    assert values == original
