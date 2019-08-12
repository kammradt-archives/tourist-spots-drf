from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from reviews_app.models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['content']

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        if self.request.user.profile.user_type == 'MODERATOR':
            return Review.objects.all()
        return Review.objects.filter(user=self.request.user)
