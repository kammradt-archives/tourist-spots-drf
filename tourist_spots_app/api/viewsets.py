from rest_framework.viewsets import ModelViewSet
from .serializers import TouristSpotsSerializer
from tourist_spots_app.models import TouristSpot


class TouristSpotViewSet(ModelViewSet):
    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotsSerializer
