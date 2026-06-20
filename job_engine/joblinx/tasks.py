from celery import shared_task
from joblinx.services.fetch_layer import run_fetch_cycle



@shared_task
def run_fetch_cycle_task():
    """
    Runs full employer fetch pipeline.
    """
    from joblinx.services.fetch_layer import run_fetch_cycle

    return run_fetch_cycle()
