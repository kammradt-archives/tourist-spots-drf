from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from users_app.models import Profile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'profile']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_date):
        user = User.objects.create_user(**validated_date)
        Profile.objects.create(user=user)
        return user
