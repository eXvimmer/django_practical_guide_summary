from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return "{} ({})".format(self.name, self.address)


class Meetup(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, allow_unicode=True)
    description = models.TextField()
    image = models.ImageField(upload_to="images")  # /uploads/images
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
