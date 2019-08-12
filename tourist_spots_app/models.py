from django.contrib.auth.models import User
from django.db import models


class TouristSpot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    available = models.BooleanField(blank=True, default=True)
    photo = models.ImageField(upload_to='tourist_spots_images', blank=True)

    def __str__(self):
        return self.name
