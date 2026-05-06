def filter_by_domain(emails: list[str], domains: set[str]) -> list[str]:
    """Return well-formed emails whose domains are allowed."""
    allowed_domains = {domain.casefold() for domain in domains}
    accepted: list[str] = []

    for email in emails:
        normalized_email = email.strip()
        if normalized_email.count("@") != 1:
            continue

        local_part, domain_part = normalized_email.split("@")
        if not local_part or not domain_part:
            continue

        if domain_part.casefold() in allowed_domains:
            accepted.append(normalized_email)

    return accepted
