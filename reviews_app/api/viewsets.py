from django.contrib.contenttypes.models import ContentType
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from reports_app.models import Report
from reviews_app.models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_fields = ['content']

    @action(methods=['post'], detail=True)
    def report(self, request, pk=None):
        return Report.create_report(
            content_text=request.data['content'],
            content_type=ContentType.objects.get_for_model(ReviewSerializer.Meta.model, for_concrete_model=False),
            object_id=pk
        )
