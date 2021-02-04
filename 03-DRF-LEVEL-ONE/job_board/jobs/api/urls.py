from django.urls import path
from jobs.api.views import JobOfferDetailApiView, JobOfferListCreateApiView

urlpatterns = [
    path("jobs/", JobOfferListCreateApiView.as_view(), name="job-list"),
    path("jobs/<int:pk>", JobOfferDetailApiView.as_view(), name="job-detail"),
]
