from django.core.management.base import BaseCommand
from joblinx.models import Employer


class Command(BaseCommand):
    help = "Seed employer database with EU/UA/USA companies (legal sources only)"

    def handle(self, *args, **options):

        employers = [

            # =========================================================
            # 🇺🇦 UKRAINE (10)
            # =========================================================
            {
                "name": "SoftServe",
                "country": "UA",
                "careers_url": "https://career.softserveinc.com/",
                "github_url": "https://github.com/SoftServeInc",
                "blog_url": "https://www.softserveinc.com/en-us/blog",
            },
            {
                "name": "EPAM Ukraine",
                "country": "UA",
                "careers_url": "https://careers.epam.com/",
                "github_url": "https://github.com/epam",
                "blog_url": "https://www.epam.com/blog",
            },
            {
                "name": "Ciklum",
                "country": "UA",
                "careers_url": "https://jobs.ciklum.com/",
                "github_url": "https://github.com/Ciklum",
                "blog_url": "https://www.ciklum.com/blog",
            },
            {
                "name": "GlobalLogic Ukraine",
                "country": "UA",
                "careers_url": "https://career.globallogic.com/",
                "github_url": "https://github.com/GlobalLogic",
                "blog_url": "https://www.globallogic.com/insights/blogs/",
            },
            {
                "name": "N-iX",
                "country": "UA",
                "careers_url": "https://careers.n-ix.com/jobs",
                "github_url": "https://github.com/N-iX",
                "blog_url": "https://www.n-ix.com/blog/",
            },
            {
                "name": "Intellias",
                "country": "UA",
                "careers_url": "https://careers.intellias.com/",
                "github_url": "https://github.com/intellias",
                "blog_url": "https://intellias.com/blog/",
            },
            {
                "name": "ELEKS",
                "country": "UA",
                "careers_url": "https://careers.eleks.com/",
                "github_url": "https://github.com/ELEKS",
                "blog_url": "https://eleks.com/blog/",
            },
            {
                "name": "Sigma Software",
                "country": "UA",
                "careers_url": "https://sigma.software/jobs/",
                "github_url": "https://github.com/SigmaSoftwareGroup",
                "blog_url": "https://sigma.software/about/media/",
            },
            {
                "name": "Genesis",
                "country": "UA",
                "careers_url": "https://gen.tech/jobs/",
                "github_url": "https://github.com/gen-tech",
                "blog_url": "https://gen.tech/blog/",
            },
            {
                "name": "MacPaw",
                "country": "UA",
                "careers_url": "https://macpaw.com/careers",
                "github_url": "https://github.com/macpaw",
                "blog_url": "https://macpaw.com/news",
            },

            # =========================================================
            # 🇪🇺 EUROPE (10)
            # =========================================================
            {
                "name": "SAP",
                "country": "EU",
                "careers_url": "https://jobs.sap.com/",
                "github_url": "https://github.com/SAP",
                "blog_url": "https://news.sap.com/",
            },
            {
                "name": "JetBrains",
                "country": "EU",
                "careers_url": "https://www.jetbrains.com/careers/jobs/",
                "github_url": "https://github.com/JetBrains",
                "blog_url": "https://blog.jetbrains.com/",
            },
            {
                "name": "Spotify",
                "country": "EU",
                "careers_url": "https://www.lifeatspotify.com/jobs",
                "github_url": "https://github.com/spotify",
                "blog_url": "https://engineering.atspotify.com/",
            },
            {
                "name": "Klarna",
                "country": "EU",
                "careers_url": "https://www.klarna.com/careers/",
                "github_url": "https://github.com/klarna",
                "blog_url": "https://www.klarna.com/international/blog/",
            },
            {
                "name": "Celonis",
                "country": "EU",
                "careers_url": "https://www.celonis.com/careers/",
                "github_url": "https://github.com/celonis",
                "blog_url": "https://www.celonis.com/blog/",
            },
            {
                "name": "Personio",
                "country": "EU",
                "careers_url": "https://www.personio.com/about-personio/careers/",
                "github_url": "https://github.com/personio",
                "blog_url": "https://www.personio.com/blog/",
            },
            {
                "name": "TeamViewer",
                "country": "EU",
                "careers_url": "https://careers.teamviewer.com/",
                "github_url": "https://github.com/teamviewer",
                "blog_url": "https://community.teamviewer.com/",
            },
            {
                "name": "Icinga",
                "country": "EU",
                "careers_url": "https://icinga.com/company/careers/",
                "github_url": "https://github.com/Icinga",
                "blog_url": "https://icinga.com/blog/",
            },
            {
                "name": "PrestaShop",
                "country": "EU",
                "careers_url": "https://prestashop.com/careers/",
                "github_url": "https://github.com/PrestaShop",
                "blog_url": "https://build.prestashop-project.org/",
            },
            {
                "name": "OVHcloud",
                "country": "EU",
                "careers_url": "https://careers.ovhcloud.com/",
                "github_url": "https://github.com/ovh",
                "blog_url": "https://blog.ovhcloud.com/",
            },

            # =========================================================
            # 🇺🇸 USA (10)
            # =========================================================
            {
                "name": "Microsoft",
                "country": "USA",
                "careers_url": "https://jobs.careers.microsoft.com/",
                "github_url": "https://github.com/microsoft",
                "blog_url": "https://devblogs.microsoft.com/",
            },
            {
                "name": "Google",
                "country": "USA",
                "careers_url": "https://www.google.com/about/careers/applications/jobs/",
                "github_url": "https://github.com/google",
                "blog_url": "https://blog.google/technology/",
            },
            {
                "name": "Amazon",
                "country": "USA",
                "careers_url": "https://www.amazon.jobs/",
                "github_url": "https://github.com/aws",
                "blog_url": "https://aws.amazon.com/blogs/aws/",
            },
            {
                "name": "Meta",
                "country": "USA",
                "careers_url": "https://www.metacareers.com/",
                "github_url": "https://github.com/facebook",
                "blog_url": "https://engineering.fb.com/",
            },
            {
                "name": "Apple",
                "country": "USA",
                "careers_url": "https://jobs.apple.com/",
                "github_url": "https://github.com/apple",
                "blog_url": "https://machinelearning.apple.com/",
            },
            {
                "name": "Netflix",
                "country": "USA",
                "careers_url": "https://jobs.netflix.com/",
                "github_url": "https://github.com/netflix",
                "blog_url": "https://netflixtechblog.com/",
            },
            {
                "name": "Salesforce",
                "country": "USA",
                "careers_url": "https://careers.salesforce.com/",
                "github_url": "https://github.com/salesforce",
                "blog_url": "https://engineering.salesforce.com/",
            },
            {
                "name": "Oracle",
                "country": "USA",
                "careers_url": "https://careers.oracle.com/",
                "github_url": "https://github.com/oracle",
                "blog_url": "https://blogs.oracle.com/",
            },
            {
                "name": "Adobe",
                "country": "USA",
                "careers_url": "https://careers.adobe.com/",
                "github_url": "https://github.com/adobe",
                "blog_url": "https://blog.developer.adobe.com/",
            },
            {
                "name": "NVIDIA",
                "country": "USA",
                "careers_url": "https://www.nvidia.com/en-us/about-nvidia/careers/",
                "github_url": "https://github.com/NVIDIA",
                "blog_url": "https://developer.nvidia.com/blog/",
            },
        ]

        created = 0
        updated = 0

        for emp in employers:
            obj, is_created = Employer.objects.update_or_create(
                name=emp["name"],
                defaults={
                    "country": emp["country"],
                    "careers_url": emp["careers_url"],
                    "github_url": emp["github_url"],
                    "blog_url": emp["blog_url"],
                }
            )

            if is_created:
                created += 1
            else:
                updated += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seed complete: created={created}, updated={updated}, total={len(employers)}"
            )
        )