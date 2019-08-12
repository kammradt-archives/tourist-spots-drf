from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from comments_app.models import Comment
from .serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['content']

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        if self.request.user.profile.user_type == 'MODERATOR':
            return Comment.objects.all()
        return Comment.objects.filter(user=self.request.user).filter(available=True)
