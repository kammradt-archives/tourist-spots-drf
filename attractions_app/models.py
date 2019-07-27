from django.db import models

from tourist_spots_app.models import TouristSpot


class Attraction(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    working_period = models.TextField()
    minimum_age = models.IntegerField()
    photo = models.ImageField(upload_to='attractions_images', null=True, blank=True)

    tourist_spot = models.ForeignKey(TouristSpot, on_delete=models.CASCADE)

    def __str__(self):
        return self.name