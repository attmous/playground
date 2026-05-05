def chunk_by_weight(
    items: list[dict[str, object]], max_weight: int
) -> list[list[dict[str, object]]]:
    """Split items into ordered chunks constrained by item weight."""
    _validate_positive_integer("max_weight", max_weight)

    chunks: list[list[dict[str, object]]] = []
    current_chunk: list[dict[str, object]] = []
    current_weight = 0

    for item in items:
        weight = _item_weight(item)

        if weight > max_weight:
            if current_chunk:
                chunks.append(current_chunk)
                current_chunk = []
                current_weight = 0
            chunks.append([item])
            continue

        if current_chunk and current_weight + weight > max_weight:
            chunks.append(current_chunk)
            current_chunk = []
            current_weight = 0

        current_chunk.append(item)
        current_weight += weight

    if current_chunk:
        chunks.append(current_chunk)

    return chunks


def _item_weight(item: dict[str, object]) -> int:
    weight = item.get("weight", 1)
    _validate_positive_integer("weight", weight)
    return weight


def _validate_positive_integer(name: str, value: object) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} must be a positive integer")


__all__ = ["chunk_by_weight"]
