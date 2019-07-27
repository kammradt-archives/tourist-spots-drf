from rest_framework.serializers import ModelSerializer

from addresses_app.api.serializers import AddressSerializer
from attractions_app.api.serializers import AttractionSerializer
from comments_app.api.serializers import CommentSerializer
from reviews_app.api.serializers import ReviewSerializer
from tourist_spots_app.models import TouristSpot


class TouristSpotsSerializer(ModelSerializer):
    attractions = AttractionSerializer(source='attraction_set', many=True)
    comments = CommentSerializer(source='comment_set', many=True)
    reviews = ReviewSerializer(source='review_set', many=True)
    address = AddressSerializer()

    class Meta:
        model = TouristSpot
        fields = '__all__'
