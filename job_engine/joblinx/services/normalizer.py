import re


def normalize_title(title):

    if not title:
        return ""

    title = str(title).strip()

    t_low = title.lower()

    bad_prefixes = (
        "javascript:",
        "mailto:",
        "void(",
        "./",
        "/",
        "#",
        "http",
        "www.",
        "~"
    )

    if t_low.startswith(bad_prefixes):
        return ""

    if "<html" in t_low or "<!doctype" in t_low:
        return ""

    title = re.sub(r"<[^>]*>", " ", title)

    # remove everything after common location separator
    title = re.split(
        r"\s+(amsterdam|belgrade|berlin|limassol|london|madrid|munich|paphos|prague|remote|warsaw|yerevan|kyiv|usa|uk|germany|poland|serbia|cyprus|netherlands|spain|czech republic)\b",
        title,
        maxsplit=1,
        flags=re.IGNORECASE,
    )[0]

    # remove location lists after semicolon
    title = title.split(";")[0]

    # remove location tail after closing bracket:
    if ")" in title:
        closing_bracket_pos = title.rfind(")")
        title = title[:closing_bracket_pos + 1]

    # remove location after long dash / pipe if present
    title = re.split(r"\s+[-|]\s+", title, maxsplit=1)[0]

    if "http" in title.lower() or "www." in title.lower():
        return ""

    title = title.lower()

    replacements = {
        "software engineer ii": "software engineer",
        "software engineer iii": "software engineer",
        "sr.": "senior",
        "jr.": "junior",
    }

    for old, new in replacements.items():
        title = title.replace(old, new)

    nav_tokens = [
        "jobs", "careers", "apply", "dashboard",
        "login", "signup", "alerts", "saved",
        "recommendations", "students", "teams",
        "how-we-hire", "search-results"
    ]

    if title in nav_tokens:
        return ""

    title = re.sub(r"\s+", " ", title)

    return title.strip()


def normalize_location(location):
    if not location:
        return ""

    location = location.lower().strip()

    forbidden = ["remote", "hybrid", "onsite", "full-time", "part-time"]
    if location in forbidden:
        return ""

    location = location.replace("united states", "usa")

    return location.strip()


def normalize_mode(mode):
    if not mode:
        return "na"

    mode = mode.lower()

    if "remote" in mode:
        return "remote"

    if "hybrid" in mode:
        return "mixed"

    if "onsite" in mode or "on-site" in mode:
        return "onsite"

    return mode.strip()


# =================================================
# NEW (CRITICAL ADDITION)
# =================================================
def is_valid_title(title: str) -> bool:
    if not title:
        return False

    title = title.strip().lower()

    if len(title) < 4:
        return False

    if len(title) > 90:
        return False

    bad_prefixes = (
        "http", "www.", "/", "./", "#",
        "mailto:", "javascript:", "void(", "~"
    )

    if title.startswith(bad_prefixes):
        return False

    bad_tokens = [
        "login", "signup", "careers", "apply",
        "dashboard", "students", "teams", "saved",
        "alerts", "recommendations", "how-we-hire",
        "search-results", "community-blog", "product-updates"
    ]

    if any(b in title for b in bad_tokens):
        return False

    location_noise = [
        "netherlands", "serbia", "germany", "cyprus",
        "united kingdom", "spain", "poland", "armenia",
        "czech republic"
    ]

    if sum(1 for word in location_noise if word in title) >= 2:
        return False

    role_words = [
        "engineer", "developer", "manager", "designer",
        "analyst", "qa", "devops", "data", "product",
        "backend", "frontend", "full stack", "security",
        "architect", "intern", "lead", "director"
    ]

    return any(word in title for word in role_words)