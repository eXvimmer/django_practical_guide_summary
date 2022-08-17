from django.urls import path
from . import views

app_name = "meetups"

urlpatterns = [
    path("meetups/", views.index, name="all-meetups"),
    path("meetups/success", views.confirm_registration, name="confirm-registration"),
    path("meetups/<slug:slug>", views.meetup_details, name="meetup-detail"),
]
