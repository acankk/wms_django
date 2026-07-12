from django.db import models

from .inbound import Inbound

from apps.master.models.product import Product
from apps.inventory.models import Bin
from apps.stock.models import StockBatch


class InboundItem(models.Model):
    inbound = models.ForeignKey(
        Inbound,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="inbound_items"
    )

    bin = models.ForeignKey(
        Bin,
        on_delete=models.PROTECT,
        related_name="inbound_items"
    )

    quantity = models.PositiveIntegerField()

    expired_date = models.DateField()

    stock_batch = models.OneToOneField(
        StockBatch,
        on_delete=models.PROTECT,
        related_name="inbound_item",
        null=True,
        blank=True
    )

    class Meta:
        db_table = "inbound_items"
        ordering = ["id"]
        verbose_name = "Inbound Item"
        verbose_name_plural = "Inbound Items"

    def __str__(self):
        return f"{self.inbound.inbound_number} - {self.product.name}"