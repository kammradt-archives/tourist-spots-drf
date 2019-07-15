from django.db import models
from attractions_app.models import Attraction
from comments_app.models import Comment
from reviews_app.models import Review


class TouristSpots(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    available = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attraction, blank=True)
    comments = models.ManyToManyField(Comment,blank=True)
    reviews = models.ManyToManyField(Review, blank=True)

    def __str__(self):
        return self.name
