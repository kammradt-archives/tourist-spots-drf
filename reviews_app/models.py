from django.contrib.auth.models import User
from django.db import models

from tourist_spots_app.models import TouristSpot


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField(null=True, blank=True)
    stars = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    tourist_spot = models.ForeignKey(TouristSpot, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name}: {self.content}'
