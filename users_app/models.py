from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    USER_TYPES = (
        ("REGULAR", "REGULAR"),
        ("PREMIUM", "PREMIUM"),
        ("MODERATOR", "MODERATOR"),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default="REGULAR")
    biography = models.CharField(max_length=500, blank=True, default='')
