from rest_framework.serializers import ModelSerializer

from addresses_app.api.serializers import AddressSerializer
from addresses_app.models import Address
from attractions_app.api.serializers import AttractionSerializer
from comments_app.api.serializers import CommentSerializer
from reviews_app.api.serializers import ReviewSerializer
from tourist_spots_app.models import TouristSpot
from users_app.api.serializers import UserSerializer


class TouristSpotsSerializer(ModelSerializer):
    user = UserSerializer(required=False, read_only=True)
    attractions = AttractionSerializer(source='attraction_set', many=True, required=False)
    comments = CommentSerializer(source='comment_set', many=True, required=False)
    reviews = ReviewSerializer(source='review_set', many=True, required=False)
    address = AddressSerializer(required=False)

    class Meta:
        model = TouristSpot
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        spot = TouristSpot.objects.create(**validated_data, user=user)
        TouristSpot.save(spot)
        return spot
