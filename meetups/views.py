from django.http import HttpRequest
from django.shortcuts import render

meetups = [
    {"title": "First Meetup", "location": "New York", "slug": "first-meetup"},
    {"title": "Second Meetup", "location": "London", "slug": "second-meetup"},
]


def index(request: HttpRequest):
    return render(
        request, "meetups/index.html", {"meetups": meetups, "show_meetups": True}
    )
