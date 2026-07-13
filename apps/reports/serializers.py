from rest_framework import serializers

from apps.stock.models import StockBatch


class StockReportSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(
        source="product.name",
        read_only=True,
    )

    category_name = serializers.CharField(
        source="product.category.name",
        read_only=True,
    )

    supplier_name = serializers.CharField(
        source="product.supplier.name",
        read_only=True,
    )

    bin_name = serializers.CharField(
        source="bin.name",
        read_only=True,
    )

    class Meta:
        model = StockBatch
        fields = (
            "id",
            "batch_number",
            "product",
            "product_name",
            "category_name",
            "supplier_name",
            "bin",
            "bin_name",
            "initial_quantity",
            "remaining_quantity",
            "received_date",
            "expired_date",
        )

        read_only_fields = fields