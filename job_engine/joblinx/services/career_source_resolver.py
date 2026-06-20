from urllib.parse import urljoin
import requests


COMMON_PATHS = [
    "/careers",
    "/jobs",
    "/vacancies",
    "/openings",
]


def resolve_career_sources(company):
    """
    Legal-only resolver:
    - no scraping content
    - only checks HTTP existence
    - returns valid endpoints
    """

    sources = []

    base = company.website.rstrip("/") if hasattr(company, "website") else None

    # 1. manual override wins
    if getattr(company, "careers_url", None):
        sources.append({
            "type": "career_page",
            "url": company.careers_url
        })
        return sources

    # 2. try common patterns
    if base:
        for path in COMMON_PATHS:
            url = urljoin(base, path)

            try:
                r = requests.get(url, timeout=5)

                if r.status_code == 200:
                    sources.append({
                        "type": "career_page",
                        "url": url
                    })

            except Exception:
                continue

    return sources