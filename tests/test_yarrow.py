from playground.yarrow import summarize_diff


def test_summarize_diff_counts_all_line_classes() -> None:
    lines = [
        "+added line",
        "-removed line",
        " unchanged line",
        "diff --git a/file b/file",
    ]

    assert summarize_diff(lines) == {
        "added": 1,
        "removed": 1,
        "context": 1,
        "metadata": 1,
    }


def test_summarize_diff_treats_file_headers_as_metadata() -> None:
    lines = [
        "+++ b/app.py",
        "--- a/app.py",
        "+real addition",
        "-real removal",
    ]

    assert summarize_diff(lines) == {
        "added": 1,
        "removed": 1,
        "context": 0,
        "metadata": 2,
    }


def test_summarize_diff_treats_hunk_headers_as_metadata() -> None:
    lines = [
        "@@ -1,2 +1,3 @@",
        " context",
        "+added",
    ]

    assert summarize_diff(lines) == {
        "added": 1,
        "removed": 0,
        "context": 1,
        "metadata": 1,
    }


def test_summarize_diff_counts_mixed_unified_diff() -> None:
    lines = [
        "diff --git a/example.txt b/example.txt",
        "index 1111111..2222222 100644",
        "--- a/example.txt",
        "+++ b/example.txt",
        "@@ -1,4 +1,5 @@",
        " kept",
        "-old",
        "+new",
        "+extra",
        "\\ No newline at end of file",
    ]

    assert summarize_diff(lines) == {
        "added": 2,
        "removed": 1,
        "context": 1,
        "metadata": 6,
    }


def test_summarize_diff_returns_zero_counts_for_empty_input() -> None:
    assert summarize_diff([]) == {
        "added": 0,
        "removed": 0,
        "context": 0,
        "metadata": 0,
    }


def test_summarize_diff_does_not_mutate_input() -> None:
    lines = [
        "--- a/file.txt",
        "+++ b/file.txt",
        "@@ -1 +1 @@",
        "-before",
        "+after",
    ]
    original = list(lines)

    summarize_diff(lines)

    assert lines == original
