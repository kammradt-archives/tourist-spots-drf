from django.contrib.contenttypes.models import ContentType
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import TouristSpotsSerializer
from ..models import TouristSpot


class TouristSpotViewSet(ModelViewSet):
    serializer_class = TouristSpotsSerializer

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'description']

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return TouristSpot.objects.filter(available=True)
