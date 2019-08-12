from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from tourist_spots.src.permissions import IsAdminOrRegisterOnly
from users_app.api.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['username']

    permission_classes = [IsAdminOrRegisterOnly]
    authentication_classes = [TokenAuthentication]
