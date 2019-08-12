from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from attractions_app.models import Attraction
from .serializers import AttractionSerializer


class AttractionViewSet(ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'description']

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
