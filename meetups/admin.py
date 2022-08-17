from django.contrib import admin
from .models import Meetup


class MeetupAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    list_filter = ("title",)  # TODO: filter by location
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Meetup, MeetupAdmin)
