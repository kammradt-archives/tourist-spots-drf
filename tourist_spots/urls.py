from django.conf.urls.static import static
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token

from tourist_spots_app.api.viewsets import TouristSpotViewSet
from attractions_app.api.viewsets import AttractionViewSet
from addresses_app.api.viewsets import AddressViewSet
from comments_app.api.viewsets import CommentViewSet
from reviews_app.api.viewsets import ReviewViewSet
from users_app.api.viewsets import UserViewSet, ProfileViewSet

router = routers.DefaultRouter()
router.register(r'tourist-spots', TouristSpotViewSet, base_name='TouristSpot')
router.register(r'attractions', AttractionViewSet, base_name='Attraction')
router.register(r'addresses', AddressViewSet, base_name='Address')
router.register(r'comments', CommentViewSet, base_name='Comment')
router.register(r'reviews', ReviewViewSet, 'Review')
router.register(r'users', UserViewSet, base_name='User')
router.register(r'profiles', ProfileViewSet, base_name='Profile')

urlpatterns = [
    path('api/', include(router.urls)),
    path('auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
