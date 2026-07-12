from rest_framework import serializers
from .models import Bin


class BinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bin
        fields = [
            "id",
            "code",
            "name",
            "description",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]