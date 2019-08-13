from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from users_app.api.serializers import UserSerializer, ProfileSerializer
from users_app.models import Profile


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['username']

    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        try:
            if self.request.user.profile.user_type == 'MODERATOR':
                return User.objects.all()
        except:
            return User.objects.filter(id=self.request.user.id)


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['user', 'user_type', 'biography']

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        if self.request.user.profile.user_type == 'MODERATOR':
            return Profile.objects.all()
        return Profile.objects.filter(user=self.request.user)
