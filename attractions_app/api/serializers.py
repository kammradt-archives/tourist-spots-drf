from rest_framework.serializers import ModelSerializer

from attractions_app.models import Attraction


class AttractionSerializer(ModelSerializer):
    class Meta:
        model = Attraction
        fields = [
            'name',
            'description',
            'working_period',
            'minimum_age',
            'photo',
            'tourist_spot'
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        attraction = Attraction.objects.create(**validated_data, user=user)
        Attraction.save(attraction)
        return attraction
