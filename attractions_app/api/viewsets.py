from django.contrib.contenttypes.models import ContentType
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from attractions_app.models import Attraction
from reports_app.models import Report
from .serializers import AttractionSerializer


class AttractionViewSet(ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    filter_fields = ['name', 'description']

    @action(methods=['post'], detail=True)
    def report(self, request, pk=None):
        return Report.create_report(
            content_text=request.data['content'],
            content_type=ContentType.objects.get_for_model(AttractionSerializer.Meta.model, for_concrete_model=False),
            object_id=pk
        )
