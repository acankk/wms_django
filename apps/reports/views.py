from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.stock.models import StockBatch

from .serializers import StockReportSerializer


class StockReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        stocks = StockBatch.objects.select_related(
            "product",
            "product__category",
            "product__supplier",
            "bin",
        ).order_by(
            "product__name",
            "received_date",
        )

        serializer = StockReportSerializer(
            stocks,
            many=True,
        )

        return Response(serializer.data)