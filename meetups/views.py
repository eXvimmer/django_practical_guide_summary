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
            {"meetup_found": True, "meetup": selected_meetup},
        )
    except Exception:
        return render(
            request,
            "meetups/meetup-detail.html",
            {
                "meetup_found": False,
            },
        )
