from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from comments_app.models import Comment
from tourist_spots.src.permissions import IsModerator
from .serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['content']

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        try:
            if self.request.user.profile.user_type == 'MODERATOR':
                return Comment.objects.all()
        except:
            return Comment.objects.filter(user=self.request.user).filter(available=True)

    @action(methods=['put'], detail=True, permission_classes=[IsModerator])
    def hide(self, request, pk=None):
        try:
            tourist_spot = self.get_object()
            tourist_spot.available = False
            tourist_spot.save()
            response = {'success': True,
                        'message': f'Comment #{pk} is now unavailable!'}
            return JsonResponse(response)
        except Exception as e:
            response = {'success': False, 'message': e}
            return JsonResponse(response)

    @action(methods=['put'], detail=True, permission_classes=[IsModerator])
    def show(self, request, pk=None):
        try:
            tourist_spot = self.get_object()
            tourist_spot.available = True
            tourist_spot.save()
            response = {'success': True,
                        'message': f'Comment #{pk} is now available!'}
            return JsonResponse(response)
        except Exception as e:
            response = {'success': False, 'message': e}
            return JsonResponse(response)
