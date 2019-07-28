from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from reports_app.api.serializers import ReportSerializer
from reports_app.models import Report


class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['content', 'content_type']

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    http_method_names = ['get', 'put', 'delete']
