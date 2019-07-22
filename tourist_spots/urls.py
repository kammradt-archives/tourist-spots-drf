from django.conf.urls.static import static
from django.contrib import admin
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
from reports_app.api.viewsets import ReportViewSet
from users_app.api.viewsets import UserViewSet

router = routers.DefaultRouter()
router.register(r'tourist-spots', TouristSpotViewSet, base_name='TouristSpot')
router.register(r'attractions', AttractionViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'comments', CommentViewSet, base_name='Comment')
router.register(r'reviews', ReviewViewSet)
router.register(r'reports', ReportViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('auth/', obtain_auth_token),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
