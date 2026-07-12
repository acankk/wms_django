from rest_framework import serializers

from ..models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source="category.name",
        read_only=True
    )

    supplier_name = serializers.CharField(
        source="supplier.name",
        read_only=True
    )

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "category",
            "category_name",
            "supplier",
            "supplier_name",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "category_name",
            "supplier_name",
            "created_at",
            "updated_at",
        )