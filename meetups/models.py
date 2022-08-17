from django.db import models


class Meetup(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, allow_unicode=True)
    description = models.TextField()

    def __str__(self):
        return self.title
