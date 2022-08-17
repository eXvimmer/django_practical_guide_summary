from django.http import HttpRequest
from django.shortcuts import render
from .models import Meetup


def index(request: HttpRequest):
    meetups = Meetup.objects.all()  # type: ignore
    return render(request, "meetups/index.html", {"meetups": meetups})


def meetup_details(request: HttpRequest, slug: str):
    try:
        selected_meetup = Meetup.objects.get(slug=slug)  # type: ignore
        return render(
            request,
            "meetups/meetup-detail.html",
            {
                "meetup_title": selected_meetup.title,
                "meetup_description": selected_meetup.description,
                "meetup_found": True,
            },
        )
    except Exception:
        return render(
            request,
            "meetups/meetup-detail.html",
            {
                "meetup_found": False,
            },
        )
