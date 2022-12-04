from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.january),
    # path("february", views.february),
    # Dynamic URL Patterns
    path("", views.index),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]
