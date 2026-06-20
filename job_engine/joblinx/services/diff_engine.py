from joblinx.models import Job


def job_exists(url):

    return Job.objects.filter(
        url=url
    ).exists()


def classify_job(url, new_title=None, new_mode=None, existing_job=None):

    if not existing_job:
        return "NEW"

    changed = False

    if new_title and new_title != existing_job.title:
        changed = True

    if new_mode and new_mode != existing_job.mode:
        changed = True

    if changed:
        return "UPDATED"

    return "UNCHANGED"