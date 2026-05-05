import csv
from io import StringIO


def normalize_csv_rows(text: str) -> list[dict[str, str]]:
    """Parse CSV text into stripped dictionaries keyed by the header row."""
    reader = csv.reader(StringIO(text, newline=""))

    try:
        header_row = next(reader)
    except StopIteration:
        return []

    headers = [header.strip() for header in header_row]
    rows: list[dict[str, str]] = []

    for row in reader:
        cells = [cell.strip() for cell in row]
        if not any(cells):
            continue

        rows.append(
            {
                header: cells[index] if index < len(cells) else ""
                for index, header in enumerate(headers)
            }
        )

    return rows
