from django.urls import path

from .views import (
    StockBatchListCreateView,
    StockBatchDetailView,
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
]