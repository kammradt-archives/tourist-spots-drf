from django.contrib.auth.models import User
from django.db import models

from tourist_spots_app.models import TouristSpot


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    content = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    tourist_spot = models.ForeignKey(TouristSpot, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name}: {self.content}'
