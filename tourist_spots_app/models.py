from django.db import models
from attractions_app.models import Attraction


class TouristSpots(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    available = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attraction)

    def __str__(self):
        return self.name
