from rest_framework.serializers import ModelSerializer
from tourist_spots_app.models import TouristSpot


class TouristSpotsSerializer(ModelSerializer):
    class Meta:
        model = TouristSpot
        fields = ('id', 'name', 'description')