from django.core.management.base import BaseCommand

from joblinx.services.fetch_layer import run_fetch_cycle


class Command(BaseCommand):

    def handle(self,*args,**kwargs):

        result = run_fetch_cycle()

        print(result)
