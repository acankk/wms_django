from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models.outbound import Outbound
from .serializers import OutboundSerializer


class OutboundListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        outbounds = Outbound.objects.prefetch_related(
            "items__product"
        )

        serializer = OutboundSerializer(
            outbounds,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = OutboundSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class OutboundDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(
            Outbound.objects.prefetch_related(
                "items__product"
            ),
            pk=pk
        )

    def get(self, request, pk):
        outbound = self.get_object(pk)

        serializer = OutboundSerializer(
            outbound
        )

        return Response(serializer.data)