from rest_framework.viewsets import ModelViewSet
from .serializers import TouristSpotsSerializer
from tourist_spots_app.models import TouristSpot


class TouristSpotViewSet(ModelViewSet):
    serializer_class = TouristSpotsSerializer

    def get_queryset(self):
        # Better filters can be added here
        return TouristSpot.objects.filter(available=True)
