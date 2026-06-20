import re

TECH_STACK = [
    "python",
    "django",
    "aws",
    "azure",
    "gcp",
    "sql",
    "postgres",
    "docker",
    "kubernetes",
]


def extract_signals(job):

    text = " ".join([
        getattr(job, "title", "") or "",
        getattr(job, "location", "") or "",
        getattr(job, "mode", "") or ""
    ]).lower()

    tags = []

    for tech in TECH_STACK:
        if tech in text:
            tags.append(tech)

    remote = False

    mode = (job.mode or "").lower()

    if "remote" in mode:
        remote = True

    match = re.search(r"(\d+)\+?\s+years", text)

    years = 0

    if match:
        years = int(match.group(1))

    return {
        "tags": tags,
        "remote": remote,
        "years": years
    }