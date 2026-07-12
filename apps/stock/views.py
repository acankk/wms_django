from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import timedelta

from django.utils import timezone

from .models import StockBatch
from .serializers import StockBatchSerializer, ExpiredAlertSerializer


class StockBatchListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        stock_batches = StockBatch.objects.select_related(
            "product",
            "bin"
        ).all()

        serializer = StockBatchSerializer(
            stock_batches,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = StockBatchSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class StockBatchDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(
            StockBatch.objects.select_related(
                "product",
                "bin"
            ),
            pk=pk
        )

    def get(self, request, pk):
        stock_batch = self.get_object(pk)

        serializer = StockBatchSerializer(stock_batch)

        return Response(serializer.data)

    def put(self, request, pk):
        stock_batch = self.get_object(pk)

        serializer = StockBatchSerializer(
            stock_batch,
            data=request.data
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def patch(self, request, pk):
        stock_batch = self.get_object(pk)

        serializer = StockBatchSerializer(
            stock_batch,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk):
        stock_batch = self.get_object(pk)

        stock_batch.delete()

        return Response(
            {
                "message": "Stock batch deleted successfully."
            },
            status=status.HTTP_200_OK
        )
    

class ExpiredAlertView(APIView):

    def get(self, request):

        today = timezone.now().date()

        alert_date = today + timedelta(days=30)

        batches = StockBatch.objects.filter(
            remaining_quantity__gt=0,
            expired_date__lte=alert_date
        ).order_by("expired_date")

        serializer = ExpiredAlertSerializer(
            batches,
            many=True
        )

        return Response(serializer.data)