from rest_framework.viewsets import ModelViewSet
from attractions_app.models import Attraction
from .serializers import AttractionSerializer


class AttractionViewSet(ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    filter_fields = ['name', 'description']
