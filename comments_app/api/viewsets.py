from django.contrib.contenttypes.models import ContentType
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from comments_app.models import Comment
from reports_app.models import Report
from .serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    filter_fields = ['content']

    def get_queryset(self):
        # Better filters can be added here
        return Comment.objects.filter(available=True)

    @action(methods=['post'], detail=True)
    def report(self, request, pk=None):
        return Report.create_report(
            content_text=request.data['content'],
            content_type=ContentType.objects.get_for_model(CommentSerializer.Meta.model, for_concrete_model=False),
            object_id=pk
        )
