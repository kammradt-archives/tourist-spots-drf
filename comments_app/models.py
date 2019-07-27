from django.contrib.auth.models import User
from django.db import models

from tourist_spots_app.models import TouristSpot


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    available = models.BooleanField(default=True)

    tourist_spot = models.ForeignKey(TouristSpot, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name}: {self.content}'
