from django.urls import path

from .views import StockReportView

urlpatterns = [
    path(
        "stocks/",
        StockReportView.as_view(),
        name="stock-report",
    ),
]