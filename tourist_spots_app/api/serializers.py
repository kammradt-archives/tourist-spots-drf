from rest_framework.serializers import ModelSerializer
from tourist_spots_app.models import TouristSpots


class TouristSpotsSerializer(ModelSerializer):
    class Meta:
        model = TouristSpots
        fields = ('id', 'name', 'description')