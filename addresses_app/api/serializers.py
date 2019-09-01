from rest_framework.serializers import ModelSerializer

from addresses_app.models import Address


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'line1',
            'line2',
            'city',
            'state',
            'country',
            'latitude',
            'longitude'
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        tourist_spot = validated_data['tourist_spot']
        address = Address.objects.create(**validated_data,
                                         user=user,
                                         tourist_spot_id=tourist_spot.id)
        Address.save(address)
        return address
