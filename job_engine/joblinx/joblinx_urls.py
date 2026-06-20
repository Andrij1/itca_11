from django.urls import path
from . import joblinx_views

urlpatterns = [
    path("", joblinx_views.home, name="home"),
    path("jobs/", joblinx_views.job_list, name="job_list"),
    path("about/", joblinx_views.about, name="about"),
]