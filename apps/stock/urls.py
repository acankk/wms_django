from django.urls import path

from .views import (
    StockBatchListCreateView,
    StockBatchDetailView,
    ExpiredAlertView
)

urlpatterns = [
    path(
        "stock-batches/",
        StockBatchListCreateView.as_view(),
        name="stock-batch-list",
    ),

    path(
        "stock-batches/<int:pk>/",
        StockBatchDetailView.as_view(),
        name="stock-batch-detail",
    ),

    path(
        "expired-alert/",
        ExpiredAlertView.as_view()
    ),
]