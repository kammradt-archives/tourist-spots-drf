from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from tourist_spots.src.permissions import IsAdminOrRegisterOnly
from users_app.api.serializers import UserSerializer, ProfileSerializer
from users_app.models import Profile


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['username']

    permission_classes = [IsAdminOrRegisterOnly]
    authentication_classes = [TokenAuthentication]


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['user', 'user_type', 'biography']

    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]
