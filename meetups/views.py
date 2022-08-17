from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Meetup, Participant
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
                user_email = registration_form.cleaned_data["email"]
                # NOTE: the second return value for get_or_create is "was_created" boolean
                participant, _ = Participant.objects.get_or_create(email=user_email)  # type: ignore
                selected_meetup.participants.add(participant)
                return redirect("meetups:confirm-registration")

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


def confirm_registration(request: HttpRequest):
    return render(request, "meetups/registration-success.html")
