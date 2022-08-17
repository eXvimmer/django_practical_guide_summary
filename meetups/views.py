from django.http import HttpRequest
from django.shortcuts import render

meetups = [{"title": "First Meetup"}, {"title": "Second Meetup"}]


def index(request: HttpRequest):
    return render(
        request, "meetups/index.html", {"meetups": meetups, "show_meetups": True}
    )
