from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .serializers import TouristSpotsSerializer
from tourist_spots_app.models import TouristSpot


class TouristSpotViewSet(ModelViewSet):
    serializer_class = TouristSpotsSerializer

    def get_queryset(self):
        # Better filters can be added here
        return TouristSpot.objects.filter(available=False)

    @action(methods=['post'], detail=True)
    def report(self, request, pk=None):
        # We will create a report page (form) for users that for some
        # reason want to report a SPECIFIC TouristSpot and then
        # the admins will verify
        pass
