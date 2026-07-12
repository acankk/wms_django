from django.db import models

from apps.master.models.product import Product
from apps.inventory.models import Bin


class StockBatch(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="stock_batches"
    )

    bin = models.ForeignKey(
        Bin,
        on_delete=models.PROTECT,
        related_name="stock_batches"
    )

    batch_number = models.CharField(
        max_length=20,
        unique=True,
        editable=False
    )

    initial_quantity = models.PositiveIntegerField()

    remaining_quantity = models.PositiveIntegerField()

    received_date = models.DateField()

    expired_date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "stock_batches"
        ordering = [
            "received_date",
            "id"
        ]
        verbose_name = "Stock Batch"
        verbose_name_plural = "Stock Batches"

    def save(self, *args, **kwargs):
        if not self.batch_number:
            last_batch = StockBatch.objects.order_by("-id").first()

            if last_batch:
                last_number = int(last_batch.batch_number[2:])
                self.batch_number = f"BT{last_number + 1:06d}"
            else:
                self.batch_number = "BT000001"

        if not self.pk:
            self.remaining_quantity = self.quantity

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.batch_number} - {self.product.name}"