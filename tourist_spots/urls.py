from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from tourist_spots_app.api.viewsets import TouristSpotViewSet
from attractions_app.api.viewsets import AttractionViewSet
from addresses_app.api.viewsets import AddressViewSet
from comments_app.api.viewsets import CommentViewSet
from reviews_app.api.viewsets import ReviewViewSet


router = routers.DefaultRouter()
router.register(r'touristspot', TouristSpotViewSet)
router.register(r'attraction', AttractionViewSet)
router.register(r'address', AddressViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'review', ReviewViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
