from django.contrib import admin
from .models import Job, TalentSubmission, Employer
from django.utils.html import format_html
from django.shortcuts import redirect
from joblinx.services.ranking import JobRankingEngine


# =================================================
# JOB ADMIN
# =================================================
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):

    list_display = (
        'num',
        'title_display',
        'employer',
        'location',
        'years',
        'mode_display',
        'seniority_display',
        'source_name',
        'posted_short',
        'updated_short',
        'url_short',
        'id',
        'salary',
        'engine_score',
        'why',   # ✅ NEW minimal UX ADDITION
    )

    ordering = ('-score', '-posted_date', '-id')
    change_list_template = "admin/job_change_list.html"

    search_fields = (
        "title",
        "employer__name",
        "location",
        "mode",
        "seniority",
    )


    # =================================================
    # MODE / SENIORITY DISPLAY
    # =================================================
    def title_display(self, obj):
        return obj.title or "-"

    # =================================================
    # MODE / SENIORITY DISPLAY
    # =================================================
    def mode_display(self, obj):
        return getattr(obj, "mode", "-")

    mode_display.short_description = "Mode"

    def seniority_display(self, obj):
        return getattr(obj, "seniority", "-")

    seniority_display.short_description = "Seniority"

    # =================================================
    # CONTEXT CACHE (UNCHANGED LOGIC)
    # =================================================
    def changelist_view(self, request, extra_context=None):

        self.request = request

        if request.GET.get("reset_ranking") == "1":
            Job.objects.all().update(
                score=0,
                why="-"
            )
            return redirect("admin:joblinx_job_changelist")

        extra_context = extra_context or {}

        extra_context["rank_role"] = request.GET.get("rank_role", "")
        extra_context["rank_work_mode"] = request.GET.get("rank_work_mode", "")
        extra_context["rank_seniority"] = request.GET.get("rank_seniority", "")
        extra_context["rank_posted"] = request.GET.get("rank_posted", "")

        return super().changelist_view(request, extra_context=extra_context)

    def get_queryset(self, request):

        qs = super().get_queryset(request)

        role = (
                request.GET.get("rank_role_other")
                or request.GET.get("rank_role")
                or ""
        ).strip().lower()

        work_mode = (
                request.GET.get("rank_work_mode_other")
                or request.GET.get("rank_work_mode")
                or ""
        ).strip().lower()

        seniority = (
                request.GET.get("rank_seniority_other")
                or request.GET.get("rank_seniority")
                or ""
        ).strip().lower()

        posted = (
                request.GET.get("rank_posted_other")
                or request.GET.get("rank_posted")
                or ""
        ).strip().lower()

        ranking_active = any([role, work_mode, seniority, posted])

        self._score_map = {}
        self._num_map = {}
        self._why_map = {}

        self._rank_inputs = {
            "role": role,
            "work_mode": work_mode,
            "seniority": seniority,
            "posted": posted,
        }

        # calculate same score as jobs.html manual ranking
        if ranking_active:
            for obj in qs:
                score = JobRankingEngine.score(
                    obj,
                    role=role,
                    work_mode=work_mode,
                    seniority=seniority,
                    posted=posted,
                )

                why = []

                if role and role in (obj.title or "").lower():
                    why.append("role")

                if work_mode:
                    job_mode = (obj.mode or "").lower()

                    if work_mode == "na" and job_mode in ("", "na", "n/a"):
                        why.append("mode")
                    elif job_mode not in ("", "na", "n/a") and work_mode in job_mode:
                        why.append("mode")

                if seniority:
                    job_seniority = (obj.seniority or "").lower()

                    if seniority == job_seniority:
                        why.append("seniority")

                if posted and obj.posted_date:
                    from datetime import date

                    days_old = (date.today() - obj.posted_date).days

                    if posted in ("1", "1d", "day") and days_old <= 1:
                        why.append("date")
                    elif posted in ("3", "3d") and days_old <= 3:
                        why.append("date")
                    elif posted in ("old", "older") and days_old > 3:
                        why.append("date")

                obj.score = score
                obj.why = ", ".join(why) if why else "-"
                obj.save(update_fields=["score", "why"])

                self._score_map[obj.id] = score
                self._why_map[obj.id] = ", ".join(why) if why else "-"

        qs = super().get_queryset(request).order_by("-score", "-posted_date", "-id")

        for idx, obj in enumerate(qs, start=1):
            self._num_map[obj.id] = idx

            if obj.id not in self._score_map:
                self._score_map[obj.id] = obj.score or 0

        return qs

    # =================================================
    # ROW NUMBER
    # =================================================
    def num(self, obj):

        # fallback safe numbering (NEVER disappears)
        if hasattr(self, "_num_map") and self._num_map:
            return self._num_map.get(obj.id, "-")

        # fallback stable ordering
        try:
            return obj.id
        except Exception:
            return "-"

    num.short_description = "#"

    # =================================================
    # SCORE
    # =================================================
    def engine_score(self, obj):

        score = getattr(self, "_score_map", {}).get(obj.id)

        if score is None:
            score = JobRankingEngine.score(obj)

        # ensure clean percent formatting
        try:
            score = float(score)
        except Exception:
            score = 0

        return f"{score:.0f}%"

    engine_score.short_description = "Score"

    # =================================================
    # 🔥 MINIMAL ADDITION — SCORE EXPLANATION (NO DEBUG MODE)
    # =================================================
    def score_hint(self, obj):
        return getattr(self, "_why_map", {}).get(obj.id, "-")

    score_hint.short_description = "Why"

    # =================================================
    # SOURCE CLEANING
    # =================================================
    def source_name(self, obj):

        if not obj.employer:
            return "-"

        sources = [
            ("careers", obj.employer.careers_url),
            ("github", obj.employer.github_url),
            ("blog", obj.employer.blog_url),
            ("rss", obj.employer.rss_url),
            ("api", obj.employer.api_url),
            ("atom", obj.employer.atom_url),
        ]

        for name, url in sources:
            if url:
                return name

        return "-"

    source_name.short_description = "Source"

    # =================================================
    # DATE FORMAT
    # =================================================
    def posted_short(self, obj):

        if not obj.posted_date:
            return "-"

        return obj.posted_date.strftime("%y-%m-%d")

    posted_short.short_description = "Posted"

    def updated_short(self, obj):
        if not obj.updated:
            return "-"
        return obj.updated.strftime("%Y-%m-%d | %H:%M")

    updated_short.short_description = "Updated"

    def url_short(self, obj):

        if not obj.url:
            return "-"

        # clean label instead of full URL
        label = "apply"

        # optional: show domain only (safe + compact)
        try:
            from urllib.parse import urlparse
            domain = urlparse(obj.url).netloc
            if domain:
                label = domain
        except Exception:
            pass

        return format_html(
            '<a href="{}" target="_blank" '
            'style="display:inline-block; max-width:120px; '
            'overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">'
            '{}'
            '</a>',
            obj.url,
            label
        )

    def get_changeform_initial_data(self, request):
        return {
            "rank_role": "",
            "rank_work_mode": "",
            "rank_seniority": "",
            "rank_posted": "",
        }


# =================================================
# TALENT ADMIN
# =================================================
@admin.register(TalentSubmission)
class TalentSubmissionAdmin(admin.ModelAdmin):

    change_list_template = "admin/talent_change_list.html"

    class Media:
        css = {
            "all": ("admin/css/talent_admin.css",)
        }

    list_display = (
        'full_name',
        'email',
        'phone',
        'city',
        'country',
        'experience_level',
        'linkedin_link',
        'created_short',
    )

    search_fields = (
        'first_name',
        'last_name',
        'email',
        'phone',
        'city',
        'country',
        'area_of_interest',
        'experience_level',
        'linkedin_url',
    )

    list_filter = (
        'experience_level',
        'country',
        'created_at',
        'consent_communications',
        'consent_privacy',
    )

    ordering = ('-created_at',)

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip()

    full_name.short_description = "Talent"

    def linkedin_link(self, obj):
        if not obj.linkedin_url:
            return "-"

        return format_html(
            '<a href="{}" target="_blank">LinkedIn</a>',
            obj.linkedin_url
        )

    linkedin_link.short_description = "LinkedIn"

    def created_short(self, obj):
        if not obj.created_at:
            return "-"

        return obj.created_at.strftime("%Y-%m-%d | %H:%M")

    created_short.short_description = "Created"


# =================================================
# EMPLOYER ADMIN
# =================================================
@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):

    list_display = (
        'employer_id',
        'name',
        'country',
        'careers_link',
        'github_link',
        'blog_link',
        'rss_link',
        'api_link',
        'atom_link',
        'updated_short',
    )

    ordering = ('employer_id',)
    list_display_links = ("name",)

    def _link(self, url, label):
        if not url:
            return "-"
        return format_html('<a href="{}" target="_blank">{}</a>', url, label)

    def careers_link(self, obj):
        return self._link(obj.careers_url, "careers")

    def github_link(self, obj):
        return self._link(obj.github_url, "github")

    def blog_link(self, obj):
        return self._link(obj.blog_url, "blog")

    def rss_link(self, obj):
        return self._link(obj.rss_url, "rss")

    def api_link(self, obj):
        return self._link(obj.api_url, "api")

    def atom_link(self, obj):
        return self._link(obj.atom_url, "atom")

    def updated_short(self, obj):
        if not obj.updated:
            return "-"
        return obj.updated.strftime("%Y-%m-%d | %H:%M")


# =================================================
# ADMIN BRANDING
# =================================================
admin.site.site_header = "Joblinx Admin"
admin.site.site_title = "Joblinx"
admin.site.index_title = "Joblinx Management"