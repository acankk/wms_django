from django.db import models

from apps.master.models.supplier import Supplier


class Inbound(models.Model):
    inbound_number = models.CharField(
        max_length=20,
        unique=True,
        editable=False
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        related_name="inbounds"
    )

    received_date = models.DateField()

    notes = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "inbounds"
        ordering = ["-received_date", "-id"]
        verbose_name = "Inbound"
        verbose_name_plural = "Inbounds"

    def save(self, *args, **kwargs):
        if not self.inbound_number:
            last = Inbound.objects.order_by("-id").first()

            if last:
                last_number = int(last.inbound_number[2:])
                self.inbound_number = f"IN{last_number + 1:06d}"
            else:
                self.inbound_number = "IN000001"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.inbound_number