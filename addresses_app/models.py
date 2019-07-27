from django.db import models

from tourist_spots_app.models import TouristSpot


class Address(models.Model):
    tourist_spot = models.OneToOneField(TouristSpot, on_delete=models.CASCADE)

    line1 = models.CharField(max_length=250)
    line2 = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=70)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.line1
