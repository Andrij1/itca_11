def filter_jobs(jobs, query):
    """
    Lightweight search across ranked jobs.
    """

    if not query:
        return jobs

    query = query.lower().strip()

    return [
        job for job in jobs
        if query in str(job.title).lower()
        or query in str(job.employer).lower()
        or query in str(job.location).lower()
        or query in str(job.mode).lower()
        or query in str(job.salary).lower()
    ]