from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Bin
from .serializers import BinSerializer


class BinListCreateView(generics.ListCreateAPIView):
    queryset = Bin.objects.all()
    serializer_class = BinSerializer
    permission_classes = [IsAuthenticated]


class BinDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bin.objects.all()
    serializer_class = BinSerializer
    permission_classes = [IsAuthenticated]