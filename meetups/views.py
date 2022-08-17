from django.http import HttpRequest
from django.shortcuts import render
from .models import Meetup
from .forms import RegistrationForm


def index(request: HttpRequest):
    meetups = Meetup.objects.all()  # type: ignore
    return render(request, "meetups/index.html", {"meetups": meetups})


def meetup_details(request: HttpRequest, slug: str):
    try:
        selected_meetup = Meetup.objects.get(slug=slug)  # type: ignore
        if request.method == "GET":
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                participant = registration_form.save()
                selected_meetup.participants.add(participant)
                # TODO: redirecto to registration confirmation page

        return render(
            request,
            "meetups/meetup-detail.html",
            {
                "meetup_found": True,
                "meetup": selected_meetup,
                "form": registration_form,
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
