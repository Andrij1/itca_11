from django.core.cache import cache
from joblinx.models import Job
from datetime import date


class JobRankingEngine:

    CACHE_KEY = "ranked_jobs_cache"

    WORK_MODE = {
        "na": 1,
        "mixed": 2,
        "remote": 3,
        "onsite": 1,
    }

    SENIORITY = {
        "senior": 3,
        "mid": 2,
        "junior": 1,
    }

    ROLE_TYPE = {
        "python": 5,
        "django": 5,
        "backend": 4,
        "engineer": 4,
        "data": 3,
        "analyst": 2,
        "other": 1,
    }

    # =========================================================
    # CORE SCORE ENGINE (NOW SIGNAL-AWARE + EVENT DRIVEN)
    # =========================================================
    @staticmethod
    def score(job, role=None, work_mode=None, seniority=None, posted=None):

        def norm(v):
            return (v or "").strip().lower()

        title = norm(job.title)

        job_work = (getattr(job, "mode", "") or "").lower().strip()
        job_sen = norm(getattr(job, "seniority", None))

        # fallback seniority from years
        if not job_sen:
            years = getattr(job, "years", 0) or 0

            if years >= 5:
                job_sen = "senior"
            elif years >= 2:
                job_sen = "mid"
            elif years > 0:
                job_sen = "junior"

        score = 0

        # ================= ROLE =================
        if role:
            r = norm(role)

            if r in title:
                score += 1

        # ================= MODE (FIXED MULTI-TOKEN MATCH) =================

        if work_mode:
            w = norm(work_mode)

            # user explicitly wants unknown mode jobs
            if w == "na":
                if job_work in ("", "na", "n/a"):
                    score += 1

            # normal matching
            elif job_work not in ("", "na", "n/a"):
                if w in job_work:
                    score += 1

        # ================= SENIORITY =================
        if seniority:
            s = norm(seniority)

            if s == job_sen:
                score += 1

        # ================= POSTED =================
        if posted and getattr(job, "posted_date", None):

            days_old = (date.today() - job.posted_date).days
            p = norm(posted)

            if p in ("1", "1d", "day") and days_old <= 1:
                score += 1

            elif p in ("3", "3d") and days_old <= 3:
                score += 1

            elif p in ("old", "older") and days_old > 3:
                score += 1

        return min(score * 25, 100)

    # =========================================================
    # CACHE-AWARE REBUILD (ONLY WHEN DIRTY)
    # =========================================================
    @staticmethod
    def get_ranked_jobs(force_refresh=False):

        from django.core.cache import cache

        if not force_refresh:
            cached = cache.get(JobRankingEngine.CACHE_KEY)
            if cached:
                return cached

        jobs = list(Job.objects.filter(is_active=True))

        ranked = []

        for job in jobs:
            score = JobRankingEngine.score(job)

            job.score = score
            job.save(update_fields=["score"])

            ranked.append(job)

        ranked.sort(key=lambda j: j.score, reverse=True)

        for idx, job in enumerate(ranked, start=1):
            job.rank = idx

        cache.set(JobRankingEngine.CACHE_KEY, ranked, timeout=300)

        return ranked

    # =========================================================
    # EVENT-DRIVEN UPDATE ENTRYPOINT (NEW)
    # =========================================================
    @staticmethod
    def update_job_score(job):

        """
        Called ONLY when job changes (from diff engine).
        """

        job.score = JobRankingEngine.score(job)
        job.save(update_fields=["score"])

        JobRankingEngine.invalidate_cache()

    # =========================================================
    # CACHE INVALIDATION
    # =========================================================
    @staticmethod
    def invalidate_cache():
        cache.delete(JobRankingEngine.CACHE_KEY)

    @staticmethod
    def apply_custom_ranking(
            jobs,
            rank_role, rank_role_other,
            rank_work_mode, rank_work_mode_other,
            rank_seniority, rank_seniority_other,
            rank_posted, rank_posted_other
    ):

        role = (rank_role_other or rank_role or "").lower().strip()
        work_mode = (rank_work_mode_other or rank_work_mode or "").lower().strip()
        seniority = (rank_seniority_other or rank_seniority or "").lower().strip()
        posted = (rank_posted_other or rank_posted or "").lower().strip()

        for job in jobs:
            job.score = JobRankingEngine.score(
                job,
                role=role,
                work_mode=work_mode,
                seniority=seniority,
                posted=posted
            )

        jobs.sort(key=lambda j: j.score, reverse=True)

        for idx, job in enumerate(jobs, start=1):
            job.rank = idx

        return jobs


    @staticmethod
    def rank_jobs(
        jobs,
        role="",
        work_mode="",
        seniority="",
        posted="",
        custom_boost=None
    ):

        ranked = []

        for job in jobs:

            # base score
            score = JobRankingEngine.score(
                job,
                role=role,
                work_mode=work_mode,
                seniority=seniority,
                posted=posted
            )

            signals = getattr(job, "signals", {}) or {}

            # --------------------------
            # SIGNAL BOOST (GLOBAL LAYER)
            # --------------------------
            tags = signals.get("tags", [])
            remote = signals.get("remote", False)

            for t in tags:
                if t in JobRankingEngine.ROLE_TYPE:
                    score += 10

            if remote:
                score += 10

            # --------------------------
            # CUSTOM BOOST (UI / ADMIN)
            # --------------------------
            if custom_boost:
                score += custom_boost(job)

            job.score = min(score, 100)
            ranked.append(job)

        ranked.sort(key=lambda j: j.score, reverse=True)

        for idx, job in enumerate(ranked, start=1):
            job.rank = idx

        return ranked
