from django.contrib.auth.models import User
from django.db import models

from tourist_spots_app.models import TouristSpot


class Attraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tourist_spot = models.ForeignKey(TouristSpot, on_delete=models.CASCADE)

    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    working_period = models.CharField(max_length=250)
    minimum_age = models.IntegerField(blank=True, default=10)
    photo = models.ImageField(upload_to='attractions_images', null=True, blank=True)

    def __str__(self):
        return self.name
