from django.urls import path

from .views import BinListCreateView, BinDetailView

urlpatterns = [
    path("bins/", BinListCreateView.as_view(), name="bin-list"),
    path("bins/<int:pk>/", BinDetailView.as_view(), name="bin-detail"),
]