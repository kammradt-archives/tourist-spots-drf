from django.db import models


class TouristSpots(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.name
