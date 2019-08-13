from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from addresses_app.models import Address
from .serializers import AddressSerializer


class AddressViewSet(ModelViewSet):
    serializer_class = AddressSerializer

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['city', 'state', 'country', 'latitude', 'longitude']

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        try:
            if self.request.user.profile.user_type == 'MODERATOR':
                return Address.objects.all()
        except:
            return []
