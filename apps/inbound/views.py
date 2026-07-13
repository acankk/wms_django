from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from .models.inbound import Inbound
from .serializers import InboundSerializer


class InboundListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
            responses=InboundSerializer(many=True)
    )
    def get(self, request):
        inbounds = Inbound.objects.select_related(
            "supplier"
        ).prefetch_related(
            "items__product",
            "items__bin"
        )

        serializer = InboundSerializer(
            inbounds,
            many=True
        )

        return Response(serializer.data)
    

    def post(self, request):
        serializer = InboundSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class InboundDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(
            Inbound.objects.select_related(
                "supplier"
            ).prefetch_related(
                "items__product",
                "items__bin"
            ),
            pk=pk
        )

    def get(self, request, pk):
        inbound = self.get_object(pk)

        serializer = InboundSerializer(
            inbound
        )

        return Response(serializer.data)

    def put(self, request, pk):
        inbound = self.get_object(pk)

        serializer = InboundSerializer(
            inbound,
            data=request.data
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk):
        inbound = self.get_object(pk)

        inbound.delete()

        return Response(
            {
                "message": "Inbound deleted successfully."
            },
            status=status.HTTP_200_OK
        )