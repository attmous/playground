from playground.hazel import filter_by_domain


def test_filter_by_domain_matches_domains_case_insensitively() -> None:
    emails = ["alice@Example.com", "bob@OTHER.test", "case@EXAMPLE.COM"]

    assert filter_by_domain(emails, {"example.COM"}) == [
        "alice@Example.com",
        "case@EXAMPLE.COM",
    ]


def test_filter_by_domain_strips_surrounding_whitespace() -> None:
    emails = ["  alice@example.com  ", "\tbob@example.com\n"]

    assert filter_by_domain(emails, {"example.com"}) == [
        "alice@example.com",
        "bob@example.com",
    ]


def test_filter_by_domain_ignores_malformed_emails() -> None:
    emails = [
        "missing-at.example.com",
        "too@many@example.com",
        "@example.com",
        "alice@",
        "valid@example.com",
    ]

    assert filter_by_domain(emails, {"example.com"}) == ["valid@example.com"]


def test_filter_by_domain_accepts_multiple_domains() -> None:
    emails = [
        "alice@example.com",
        "bob@sample.org",
        "carol@ignored.net",
        "dave@EXAMPLE.COM",
    ]

    assert filter_by_domain(emails, {"example.com", "sample.org"}) == [
        "alice@example.com",
        "bob@sample.org",
        "dave@EXAMPLE.COM",
    ]


def test_filter_by_domain_preserves_input_order() -> None:
    emails = [
        "first@example.com",
        "skip@other.net",
        "second@example.com",
        "third@example.com",
    ]

    assert filter_by_domain(emails, {"example.com"}) == [
        "first@example.com",
        "second@example.com",
        "third@example.com",
    ]


def test_filter_by_domain_returns_empty_list_for_empty_domains() -> None:
    assert filter_by_domain(["alice@example.com"], set()) == []


def test_filter_by_domain_does_not_mutate_inputs() -> None:
    emails = [" alice@example.com ", "bob@other.net"]
    domains = {"example.com"}
    original_emails = list(emails)
    original_domains = set(domains)

    filter_by_domain(emails, domains)

    assert emails == original_emails
    assert domains == original_domains
