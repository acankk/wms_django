from django.db import models

from .outbound import Outbound

from apps.master.models.product import Product


class OutboundItem(models.Model):
    outbound = models.ForeignKey(
        Outbound,
        on_delete=models.CASCADE,
        related_name="items",
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="outbound_items",
    )

    quantity = models.PositiveIntegerField()

    batch_information = models.JSONField(
        default=list,
        blank=True,
    )

    class Meta:
        db_table = "outbound_items"
        ordering = [
            "id",
        ]
        verbose_name = "Outbound Item"
        verbose_name_plural = "Outbound Items"

    def __str__(self):
        return (
            f"{self.outbound.outbound_number} - "
            f"{self.product.name}"
        )