from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BinViewSet

router = DefaultRouter()
router.register(r"bins", BinViewSet, basename="bins")

urlpatterns = [
    path("", include(router.urls)),
]