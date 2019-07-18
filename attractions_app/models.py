from django.db import models


class Attraction(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    working_period = models.TextField()
    minimum_age = models.IntegerField()
    photo = models.ImageField(upload_to='attractions_images', null=True, blank=True)

    def __str__(self):
        return self.name