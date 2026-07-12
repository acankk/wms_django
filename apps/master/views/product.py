from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.product import Product
from ..serializers.product import ProductSerializer


class ProductListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products = Product.objects.select_related(
            "category",
            "supplier"
        ).all()

        serializer = ProductSerializer(
            products,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class ProductDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(
            Product.objects.select_related(
                "category",
                "supplier"
            ),
            pk=pk
        )

    def get(self, request, pk):
        product = self.get_object(pk)

        serializer = ProductSerializer(product)

        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)

        serializer = ProductSerializer(
            product,
            data=request.data
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def patch(self, request, pk):
        product = self.get_object(pk)

        serializer = ProductSerializer(
            product,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk):
        product = self.get_object(pk)

        product.delete()

        return Response(
            {
                "message": "Product deleted successfully."
            },
            status=status.HTTP_200_OK
        )