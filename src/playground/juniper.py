import re


_PLACEHOLDER_RE = re.compile(r"{{\s*(.*?)\s*}}")


def _lookup_value(path: str, values: dict[str, object]) -> object:
    current: object = values

    for part in path.split("."):
        if not isinstance(current, dict) or part not in current:
            raise KeyError(path)
        current = current[part]

    return current


def render_template(template: str, values: dict[str, object]) -> str:
    """Render double-brace placeholders from a dictionary of values."""

    def replace(match: re.Match[str]) -> str:
        path = match.group(1).strip()
        try:
            return str(_lookup_value(path, values))
        except KeyError:
            return match.group(0)

    return _PLACEHOLDER_RE.sub(replace, template)
