from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from tourist_spots_app.api.viewsets import TouristSpotViewSet


router = routers.DefaultRouter()
router.register(r'touristspot', TouristSpotViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
