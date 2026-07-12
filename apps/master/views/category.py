from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.category import Category
from ..serializers.category import CategorySerializer


class CategoryListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categories = Category.objects.all()

        serializer = CategorySerializer(
            categories,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class CategoryDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(
            Category,
            pk=pk
        )

    def get(self, request, pk):
        category = self.get_object(pk)

        serializer = CategorySerializer(category)

        return Response(serializer.data)
    
    def put(self, request, pk):
        category = self.get_object(pk)

        serializer = CategorySerializer(
            category,
            data=request.data, partial=False
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk):
        category = self.get_object(pk)

        category.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )