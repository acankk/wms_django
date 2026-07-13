from django.urls import path

from .views import (
    OutboundListCreateView,
    OutboundDetailView,
)

urlpatterns = [
    path(
        "",
        OutboundListCreateView.as_view(),
        name="outbound-list-create",
    ),
    path(
        "<int:pk>/",
        OutboundDetailView.as_view(),
        name="outbound-detail",
    ),
]