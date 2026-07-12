from django.urls import path

from .views import (
    InboundListCreateView,
    InboundDetailView,
)

urlpatterns = [
    path(
        "inbounds/",
        InboundListCreateView.as_view(),
        name="inbound-list",
    ),
    path(
        "inbounds/<int:pk>/",
        InboundDetailView.as_view(),
        name="inbound-detail",
    ),
]