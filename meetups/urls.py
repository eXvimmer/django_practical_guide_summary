from django.urls import path
from . import views

app_name = "meetups"

urlpatterns = [
    path("", views.index, name="all-meetups"),
    path(
        "<slug:slug>/success",
        views.confirm_registration,
        name="confirm-registration",
    ),
    path("<slug:slug>", views.meetup_details, name="meetup-detail"),
]
