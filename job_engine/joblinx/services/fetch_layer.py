import requests
import re
import xml.etree.ElementTree as ET
import time
import random

from django.utils import timezone

from joblinx.models import (
    Employer,
    SourceState,
    Job,
)

from joblinx.services.diff_engine import classify_job

from joblinx.models import Employer, Job

from joblinx.services.normalizer import (
    normalize_title,
    normalize_location,
    normalize_mode,
    is_valid_title,
)

from joblinx.services.signal_extractor import extract_signals


def run_fetch_cycle():
    """
    Main ingestion pipeline entry point.
    Diff-based ingestion version (v4 FIXED MODE/LOCATION SEPARATION)
    """

    import xml.etree.ElementTree as ET
    from urllib.parse import urljoin
    from html.parser import HTMLParser
    import hashlib

    class LinkParser(HTMLParser):

        def __init__(self):
            super().__init__()

            self.jobs = []

            self.current_href = None
            self.current_text = ""
            self.inside_a = False

        def handle_starttag(self, tag, attrs):

            if tag == "a":

                self.inside_a = True
                self.current_text = ""

                for attr, val in attrs:
                    if attr == "href":
                        self.current_href = val


        def handle_data(self, data):

            if self.inside_a:

                text = data.strip()

                if text:
                    self.current_text += " " + text


        def handle_endtag(self, tag):

            if tag == "a":

                title = self.current_text.strip()

                if title and self.current_href:
                    self.jobs.append(
                        {
                            "title": title,
                            "link": self.current_href
                        }
                    )

                self.inside_a = False
                self.current_href = None
                self.current_text = ""

    def make_fingerprint(title, link, employer_id):
        raw = f"{title}-{link}-{employer_id}"
        return hashlib.md5(raw.encode()).hexdigest()

    def make_content_hash(title, mode, location):
        raw = f"{title}-{mode}-{location}"
        return hashlib.md5(raw.encode()).hexdigest()

    import re

    def extract_job_meta(raw_text):
        raw_text = raw_text or ""
        text = raw_text.lower()

        # -------- MODE --------
        if "remote" in text:
            mode = "remote"
        elif "hybrid" in text or "mixed" in text:
            mode = "mixed"
        elif "onsite" in text or "on-site" in text or "office" in text:
            mode = "onsite"
        else:
            mode = "na"

        # -------- SENIORITY --------
        if any(x in text for x in ["junior", "jr.", "entry level", "intern"]):
            seniority = "junior"
        elif any(x in text for x in ["senior", "sr.", "lead", "principal", "staff"]):
            seniority = "senior"
        elif any(x in text for x in ["middle", "mid", "mid-level"]):
            seniority = "middle"
        else:
            seniority = "-"

        # -------- YEARS --------
        years = 0
        years_match = re.search(r"(\d+)\+?\s*(years|yrs|років|роки)", text)
        if years_match:
            years = int(years_match.group(1))

        # -------- SALARY --------
        salary = 0
        salary_match = re.search(
            r"(\$|€|eur|usd)?\s?(\d{3,6})\s?[-–]\s?(\d{3,6})",
            text
        )
        if salary_match:
            salary = int(salary_match.group(2))

        return {
            "mode": mode,
            "seniority": seniority,
            "years": years,
            "salary": salary,
        }

    def looks_like_job_link(title, link):
        if not title or not link:
            return False

        title_low = title.lower().strip()
        link_low = link.lower().strip()

        bad = [
            "mailto:", "javascript:", "void(", "#",
            "dashboard", "login", "signup", "saved",
            "alerts", "recommendations", "students",
            "teams", "how-we-hire", "press", "blog"
        ]

        if any(b in title_low for b in bad):
            return False

        if any(b in link_low for b in bad):
            return False

        good_link_tokens = [
            "job", "jobs", "career", "careers",
            "position", "opening", "vacancy", "apply"
        ]

        role_tokens = [
            "engineer", "developer", "manager", "designer",
            "analyst", "qa", "devops", "data", "product",
            "backend", "frontend", "full stack", "security",
            "intern", "architect"
        ]

        return (
                any(t in link_low for t in good_link_tokens)
                and any(t in title_low for t in role_tokens)
        )

    employers = Employer.objects.all()
    results = []

    for employer in employers:

        sources = [
            employer.careers_url,
            employer.github_url,
            employer.rss_url,
            employer.api_url,
            employer.blog_url,
        ]

        for url in sources:
            if not url:
                continue

            try:
                response = requests.get(
                    url,
                    timeout=10,
                    headers={"User-Agent": "JobLinxBot/0.1"}
                )

                print("=" * 80)
                print(employer.name)
                print(response.text[:5000])

                job_items = []
                content_type = response.headers.get("Content-Type", "")

                # ---------------- RSS ----------------
                if "xml" in content_type or "<rss" in response.text:
                    try:
                        root = ET.fromstring(response.text)
                        for item in root.findall(".//item"):
                            job_items.append({
                                "title": item.findtext("title"),
                                "link": item.findtext("link"),
                                "description": item.findtext("description"),
                            })
                    except Exception:
                        pass

                # ---------------- JSON ----------------
                if not job_items:
                    try:
                        data = response.json()
                        if isinstance(data, list):
                            job_items = data
                        elif isinstance(data, dict):
                            job_items = data.get("jobs") or data.get("results") or []
                    except Exception:
                        pass

                # ---------------- HTML ----------------
                if not job_items:
                    parser = LinkParser()
                    parser.feed(response.text)

                    job_items = []

                    for item in parser.jobs:
                        raw_title = item.get("title", "")
                        raw_link = item.get("link", "")

                        if not looks_like_job_link(raw_title, raw_link):
                            continue

                        item["link"] = urljoin(url, raw_link)
                        job_items.append(item)

                # ---------------- FALLBACK ----------------
                if not job_items:
                    job_items = [{
                        "title": response.text[:200],
                        "link": url
                    }]

                # =================================================
                # PROCESS JOBS
                # =================================================
                for item in job_items:

                    raw_title = (
                            item.get("title")
                            or item.get("name")
                            or item.get("job_title")
                            or item.get("description")
                            or ""
                    )

                    raw_meta_text = " ".join([
                        str(item.get("title", "")),
                        str(item.get("name", "")),
                        str(item.get("job_title", "")),
                        str(item.get("description", "")),
                        str(item.get("summary", "")),
                        str(item.get("location", "")),
                        str(item.get("mode", "")),
                    ])

                    title = normalize_title(raw_title)

                    if not title:
                        continue

                    if not is_valid_title(title):
                        continue

                    link = item.get("link") or item.get("url") or item.get("apply_url") or url

                    # reject bad non-real vacancy links
                    if not link or not str(link).startswith("http"):
                        continue

                    # ✅ FIX 1: location is ONLY employer geography
                    location = normalize_location(employer.country)

                    # ✅ FIX 2: mode ONLY comes from item (NEVER fallback)
                    meta = extract_job_meta(raw_meta_text)

                    mode = normalize_mode(meta["mode"])
                    seniority = meta["seniority"]
                    years = meta["years"]
                    salary = meta["salary"]

                    fingerprint = make_fingerprint(title, link, employer.id)

                    content_hash = make_content_hash(title, mode, location)

                    existing = Job.objects.filter(source=content_hash).first()

                    if existing:

                        # UPDATE PATH (REQUIRED EXACT FIELDS)
                        existing.url = link
                        existing.title = title
                        existing.location = location
                        existing.mode = mode
                        existing.seniority = seniority
                        existing.years = years
                        existing.salary = salary

                        if not existing.posted_date:
                            existing.posted_date = timezone.localdate()

                        existing.save()

                        job = existing

                    else:

                        # CREATE PATH (REQUIRED EXACT FIELDS)
                        job = Job.objects.create(
                            url=link,
                            source=content_hash,
                            title=title,
                            location=location,
                            mode=mode,
                            seniority=seniority,
                            years=years,
                            salary=salary,
                            posted_date=timezone.localdate(),
                            employer=employer,
                        )

                    signals = extract_signals(job)
                    job.signals = signals
                    job.save()

                    results.append({
                        "employer": employer.name,
                        "url": job.url,
                        "status": response.status_code,
                        "signals": signals,
                    })

                time.sleep(random.uniform(1.5, 3.0))

            except requests.RequestException as e:
                results.append({
                    "employer": employer.name,
                    "url": url,
                    "status": "ERROR",
                    "error": str(e)
                })
                continue

            SourceState.objects.update_or_create(
                employer=employer,
                url=url,
                defaults={"last_status": "fetched"}
            )

    return results