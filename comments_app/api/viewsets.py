from rest_framework.viewsets import ModelViewSet

from comments_app.models import Comment
from .serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    filter_fields = ['content']

    def get_queryset(self):
        # Better filters can be added here
        return Comment.objects.filter(available=True)
