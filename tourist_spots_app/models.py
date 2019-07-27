from django.db import models


class TouristSpot(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    available = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='tourist_spots_images', null=True, blank=True)

    def __str__(self):
        return self.name
