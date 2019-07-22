from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from reports_app.models import Report
from users_app.api.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = ['username']

    @action(methods=['post'], detail=True)
    def report(self, request, pk=None):
        return Report.create_report(
            content_text=request.data['content'],
            content_type=ContentType.objects.get_for_model(UserSerializer.Meta.model, for_concrete_model=False),
            object_id=pk
        )
