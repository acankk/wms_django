from rest_framework import serializers

from .models import StockBatch


class StockBatchSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(
        source="product.name",
        read_only=True
    )

    bin_name = serializers.CharField(
        source="bin.name",
        read_only=True
    )

    class Meta:
        model = StockBatch
        fields = (
            "id",
            "batch_number",
            "product",
            "product_name",
            "bin",
            "bin_name",
            "initial_quantity",
            "remaining_quantity",
            "received_date",
            "expired_date",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "batch_number",
            "product_name",
            "bin_name",
            "remaining_quantity",
            "created_at",
            "updated_at",
        )