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


def meetup_details(request: HttpRequest):
    selected_meetup = {
        "title": "A selected meetup",
        "description": "some description about something",
    }
    return render(
        request,
        "meetups/meetup-detail.html",
        {
            "meetup-title": selected_meetup["title"],
            "meetup-description": selected_meetup["description"],
        },
    )
