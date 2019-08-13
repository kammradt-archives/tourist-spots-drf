from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from attractions_app.models import Attraction
from .serializers import AttractionSerializer


class AttractionViewSet(ModelViewSet):
    serializer_class = AttractionSerializer

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'description']

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        try:
            if self.request.user.profile.user_type == 'MODERATOR':
                return Attraction.objects.all()
        except:
            return []

