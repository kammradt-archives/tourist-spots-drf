from django.contrib.auth.models import User
from django.db import models

from tourist_spots_app.models import TouristSpot


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tourist_spot = models.ForeignKey(TouristSpot, on_delete=models.CASCADE)

    content = models.CharField(max_length=500)
    stars = models.DecimalField(max_digits=3, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.first_name}: {self.content}'
