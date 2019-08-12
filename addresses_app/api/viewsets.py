from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from addresses_app.models import Address
from .serializers import AddressSerializer


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['city', 'state', 'country', 'latitude', 'longitude']

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
