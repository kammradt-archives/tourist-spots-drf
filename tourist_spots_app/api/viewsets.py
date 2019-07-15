from rest_framework.viewsets import ModelViewSet
from .serializers import TouristSpotsSerializer
from tourist_spots_app.models import TouristSpots


class TouristSpotViewSet(ModelViewSet):
    queryset = TouristSpots.objects.all()
    serializer_class = TouristSpotsSerializer
