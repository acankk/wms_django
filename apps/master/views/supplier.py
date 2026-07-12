from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.supplier import Supplier
from ..serializers.supplier import SupplierSerializer


class SupplierListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        suppliers = Supplier.objects.all()

        serializer = SupplierSerializer(
            suppliers,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = SupplierSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class SupplierDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(
            Supplier,
            pk=pk
        )

    def get(self, request, pk):
        supplier = self.get_object(pk)

        serializer = SupplierSerializer(supplier)

        return Response(serializer.data)

    def put(self, request, pk):
        supplier = self.get_object(pk)

        serializer = SupplierSerializer(
            supplier,
            data=request.data
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk):
        supplier = self.get_object(pk)

        supplier.delete()

        return Response(
            {
                "message": "Supplier deleted successfully."
            },
            status=status.HTTP_200_OK
        )