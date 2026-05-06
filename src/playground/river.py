def build_cursor(page: int, per_page: int, total: int) -> dict[str, int | bool]:
    """Return pagination cursor metadata for a result set."""
    clamped_per_page = max(per_page, 1)
    total_pages = max(1, (total + clamped_per_page - 1) // clamped_per_page)
    clamped_page = min(max(page, 1), total_pages)

    return {
        "page": clamped_page,
        "per_page": clamped_per_page,
        "total": total,
        "total_pages": total_pages,
        "has_previous": clamped_page > 1,
        "has_next": clamped_page < total_pages,
    }
