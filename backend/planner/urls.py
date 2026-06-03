# planner/urls.py

from django.urls import path
from .views import GeneratePlanView

urlpatterns = [
    path(
        "generate/",
        GeneratePlanView.as_view(),
        name="generate-plan",
    ),
    path("history/", GroceryPlanHistoryView.as_view()),
]