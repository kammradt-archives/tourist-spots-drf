from django.contrib.contenttypes.models import ContentType
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from reports_app.models import Report
from .serializers import TouristSpotsSerializer
from ..models import TouristSpot


class TouristSpotViewSet(ModelViewSet):
    serializer_class = TouristSpotsSerializer
    filter_fields = ['name', 'description']

    def get_queryset(self):
        return TouristSpot.objects.filter(available=True)

    @action(methods=['post'], detail=True)
    def report(self, request, pk=None):

        return Report.create_report(
            content_text=request.data['content'],
            content_type=ContentType.objects.get_for_model(TouristSpotsSerializer.Meta.model, for_concrete_model=False),
            object_id=pk
        )
