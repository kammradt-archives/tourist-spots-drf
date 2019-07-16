from rest_framework.serializers import ModelSerializer

from reviews_app.models import Review


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
