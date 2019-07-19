from django.contrib.contenttypes.models import ContentType
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from addresses_app.models import Address
from reports_app.models import Report
from .serializers import AddressSerializer


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_fields = ['city', 'state', 'country', 'latitude', 'longitude']

    @action(methods=['post'], detail=True)
    def report(self, request, pk=None):
        return Report.create_report(
            content_text=request.data['content'],
            content_type=ContentType.objects.get_for_model(AddressSerializer.Meta.model, for_concrete_model=False),
            object_id=pk
        )
