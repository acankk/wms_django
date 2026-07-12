from django.db import transaction

from rest_framework import serializers

from apps.stock.models import StockBatch

from .models.inbound import Inbound
from .models.inbound_item import InboundItem


class InboundItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(
        source="product.name",
        read_only=True
    )

    bin_name = serializers.CharField(
        source="bin.name",
        read_only=True
    )

    batch_number = serializers.CharField(
        source="stock_batch.batch_number",
        read_only=True
    )

    class Meta:
        model = InboundItem
        fields = (
            "id",
            "product",
            "product_name",
            "bin",
            "bin_name",
            "quantity",
            "expired_date",
            "batch_number",
        )

        read_only_fields = (
            "id",
            "product_name",
            "bin_name",
            "batch_number",
        )


class InboundSerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(
        source="supplier.name",
        read_only=True
    )

    items = InboundItemSerializer(
        many=True
    )

    class Meta:
        model = Inbound
        fields = (
            "id",
            "inbound_number",
            "supplier",
            "supplier_name",
            "received_date",
            "notes",
            "items",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "inbound_number",
            "supplier_name",
            "created_at",
            "updated_at",
        )

    @transaction.atomic
    def create(self, validated_data):
        items_data = validated_data.pop("items")

        inbound = Inbound.objects.create(**validated_data)

        for item in items_data:
            inbound_item = InboundItem.objects.create(
                inbound=inbound,
                product=item["product"],
                bin=item["bin"],
                quantity=item["quantity"],
                expired_date=item["expired_date"],
            )

            batch = StockBatch.objects.create(
                product=inbound_item.product,
                bin=inbound_item.bin,
                initial_quantity=inbound_item.quantity,
                remaining_quantity=inbound_item.quantity,
                received_date=inbound.received_date,
                expired_date=inbound_item.expired_date,
            )

            inbound_item.stock_batch = batch
            inbound_item.save(update_fields=["stock_batch"])

        return inbound