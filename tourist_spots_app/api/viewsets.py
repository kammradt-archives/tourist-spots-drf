from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .serializers import TouristSpotsSerializer
from tourist_spots_app.models import TouristSpot


class TouristSpotViewSet(ModelViewSet):
    serializer_class = TouristSpotsSerializer
    filter_fields = ['name', 'description']

    def get_queryset(self):
        return TouristSpot.objects.filter(available=True)

    @action(methods=['post'], detail=True)
    def report(self, request, pk=None):
        # We will create a report page (form) for users that for some
        # reason want to report a SPECIFIC TouristSpot and then
        # the admins will verify
        pass
