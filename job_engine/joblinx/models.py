from django.db import models
from django.template.defaultfilters import length


class Employer(models.Model):

    employer_id = models.CharField(max_length=10, unique=True, blank=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100, blank=True)

    api_url = models.URLField(blank=True, null=True)
    rss_url = models.URLField(blank=True, null=True)
    atom_url = models.URLField(blank=True, null=True)

    careers_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    blog_url = models.URLField(blank=True, null=True)

    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

        if not self.employer_id:
            last = (
                Employer.objects.exclude(employer_id="")
                .order_by("-id")
                .first()
            )

            if last and last.employer_id.startswith("E"):
                num = int(last.employer_id[1:]) + 1
            else:
                num = 1

            self.employer_id = f"E{num:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name"], name="unique_employer_name")
        ]

class Job(models.Model):

    title = models.CharField(max_length=100)

    employer = models.ForeignKey(
        Employer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    years = models.PositiveIntegerField(
        default=0,
        help_text="Minimum years of experience required"
    )

    seniority = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        default=None
    )

    location = models.CharField(
        max_length=100,
        null=True
    )

    mode = models.CharField(
        max_length=100,
        null=True
    )

    salary = models.IntegerField(
        default=0
    )

    url = models.URLField(
        null=True,
        blank=True
    )

    source = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    # NEW
    posted_date = models.DateField(
        blank=True,
        null=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    is_active = models.BooleanField(
        default=True
    )

    idx = models.IntegerField(
        default=0
    )

    score = models.FloatField(
        default=0
    )

    why = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    def __str__(self):
        rank = getattr(self, "rank", self.pk)

        employer_name = self.employer.name if self.employer else "-"

        return f"#{rank} JOB - {self.title} - AT: {employer_name}"


class TalentSubmission(models.Model):

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    city = models.CharField(
        max_length=100,
        blank=True
    )

    country = models.CharField(
        max_length=100
    )

    area_of_interest = models.TextField(
        blank=False
    )

    linkedin_url = models.URLField(
        blank=True
    )

    experience_level = models.CharField(
        max_length=100,
        blank=False
    )

    consent_communications = models.BooleanField(
        default=False
    )

    consent_privacy = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return (
            f"{self.first_name} "
            f"{self.last_name} "
            f"({self.email})"
        )

class SourceState(models.Model):

    employer = models.ForeignKey("Employer", on_delete=models.CASCADE)
    url = models.URLField()

    etag = models.CharField(max_length=255, blank=True, null=True)
    last_modified = models.CharField(max_length=255, blank=True, null=True)

    last_status = models.CharField(
        max_length=20,
        default="unknown"
    )

    last_checked = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employer.name} - cache state"