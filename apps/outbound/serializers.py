from django.db import transaction

from rest_framework import serializers

from .models.outbound import Outbound
from .models.outbound_item import OutboundItem

from .service.fifo import consume_fifo


class OutboundItemSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(
        source="product.name",
        read_only=True,
    )

    class Meta:
        model = OutboundItem
        fields = (
            "id",
            "product",
            "product_name",
            "quantity",
            "batch_information",
        )

        read_only_fields = (
            "id",
            "product_name",
            "batch_information",
        )

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Jumlah barang harus lebih dari 0."
            )

        return value


class OutboundSerializer(serializers.ModelSerializer):

    items = OutboundItemSerializer(
        many=True
    )

    class Meta:
        model = Outbound
        fields = (
            "id",
            "outbound_number",
            "destination",
            "outbound_date",
            "notes",
            "items",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "outbound_number",
            "created_at",
            "updated_at",
        )

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError(
                "Minimal harus terdapat satu item outbound."
            )

        return value

    @transaction.atomic
    def create(self, validated_data):
        items_data = validated_data.pop("items")

        batch_results = []

        try:
            for item in items_data:

                batch_information = consume_fifo(
                    item["product"],
                    item["quantity"],
                )

                batch_results.append(
                    {
                        "product": item["product"],
                        "quantity": item["quantity"],
                        "batch_information": batch_information,
                    }
                )

        except ValueError as e:
            raise serializers.ValidationError(
                {
                    "message": str(e)
                }
            )

        outbound = Outbound.objects.create(
            **validated_data
        )

        for item in batch_results:

            OutboundItem.objects.create(
                outbound=outbound,
                product=item["product"],
                quantity=item["quantity"],
                batch_information=item["batch_information"],
            )

        return outbound