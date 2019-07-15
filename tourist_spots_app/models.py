from django.db import models
from attractions_app.models import Attraction
from comments_app.models import Comment


class TouristSpots(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    available = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attraction)
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return self.name
