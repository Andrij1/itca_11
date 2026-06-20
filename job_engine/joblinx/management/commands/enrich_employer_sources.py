from django.core.management.base import BaseCommand
from joblinx.models import Employer
from joblinx.services.career_source_resolver import resolve_career_sources


class Command(BaseCommand):
    help = "Resolve and enrich employer career sources"

    def handle(self, *args, **kwargs):

        for employer in Employer.objects.all():

            sources = resolve_career_sources(employer)

            for s in sources:
                if s["type"] == "career_page":
                    employer.careers_url = s["url"]

            employer.save()

        self.stdout.write(self.style.SUCCESS("Source enrichment complete"))