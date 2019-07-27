from django.db import models


class TouristSpot(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    available = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='tourist_spots_images', blank=True)

    def __str__(self):
        return self.name
