from django.shortcuts import render, redirect
from .models import Job
from .models import TalentSubmission
from .services.ranking import JobRankingEngine
from django.db.models import Q
from django.contrib import messages
from .filters import filter_jobs
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def job_list(request):

    query = request.GET.get("q", "")
    force_refresh = request.GET.get("refresh", "") == "1"

    # =========================================
    # 1. GET RANKED JOBS (UNCHANGED LOGIC)
    # =========================================
    jobs = JobRankingEngine.get_ranked_jobs(
        force_refresh=force_refresh
    )

    # =========================================
    # 2. FILTER SEARCH
    # =========================================
    jobs = filter_jobs(jobs, query)

    # =========================================
    # 3. COLLECT RANKING INPUTS
    # =========================================
    rank_role = request.GET.get("rank_role", "")
    rank_role_other = request.GET.get("rank_role_other", "")

    rank_work_mode = request.GET.get("rank_work_mode", "")
    rank_work_mode_other = request.GET.get("rank_work_mode_other", "")

    rank_seniority = request.GET.get("rank_seniority", "")
    rank_seniority_other = request.GET.get("rank_seniority_other", "")

    rank_posted = request.GET.get("rank_posted", "")
    rank_posted_other = request.GET.get("rank_posted_other", "")

    # =========================================
    # 4. APPLY RANKING (UNCHANGED)
    # =========================================
    jobs = JobRankingEngine.rank_jobs(
        jobs,
        role=rank_role or rank_role_other,
        work_mode=rank_work_mode or rank_work_mode_other,
        seniority=rank_seniority or rank_seniority_other,
        posted=rank_posted or rank_posted_other,
    )

    # =========================================
    # 5. PAGINATION (NEW — CRITICAL FIX)
    # =========================================
    paginator = Paginator(jobs, 100)  # 100 jobs per page

    page = request.GET.get("page", 1)

    try:
        jobs_page = paginator.page(page)
    except PageNotAnInteger:
        jobs_page = paginator.page(1)
    except EmptyPage:
        jobs_page = paginator.page(paginator.num_pages)

    # =========================================
    # 6. SAFE QUERY PRESERVATION (IMPORTANT)
    # =========================================
    query_params = request.GET.copy()
    if "page" in query_params:
        query_params.pop("page")

    # =========================================
    # 7. RENDER
    # =========================================
    return render(request, "joblinx/jobs.html", {
        "jobs": jobs_page,
        "query": query,
        "query_params": query_params.urlencode(),
    })


def home(request):

    return render(request, "joblinx/home.html")


def resend(request):

    return redirect('job_list')


def about(request):

    submitted = False

    if request.method == "POST":

        TalentSubmission.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            city=request.POST.get("city"),
            country=request.POST.get("country"),
            area_of_interest=request.POST.get("area_of_interest"),
            linkedin_url=request.POST.get("linkedin_url"),
            experience_level=request.POST.get("experience_level"),
            consent_communications=bool(request.POST.get("consent_communications")),
            consent_privacy=bool(request.POST.get("consent_privacy")),
        )

        messages.success(
            request,
            "Thank you — your application has been received. We will contact you if suitable."
        )

        return redirect("about")  # 👈 THIS is the key fix (Post/Redirect/Get)

    return render(request, "joblinx/about.html")

