from django.urls import path
from . import views

app_name = "meetups"

urlpatterns = [path("meetups/", views.index)]
