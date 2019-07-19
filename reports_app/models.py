from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from rest_framework.response import Response


class Report(models.Model):
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f'{self.user_id}: {self.content}'

    @staticmethod
    def create_report(content_text, content_type, object_id):
        Report(
            content=content_text,
            content_type=content_type,
            object_id=object_id
        ).save()

        return Response({'message': 'Reported!'})

