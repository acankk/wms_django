from django.db import models


class Outbound(models.Model):
    outbound_number = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
    )

    destination = models.CharField(
        max_length=100,
    )

    outbound_date = models.DateField()

    notes = models.TextField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        db_table = "outbounds"
        ordering = [
            "-outbound_date",
            "-id",
        ]
        verbose_name = "Outbound"
        verbose_name_plural = "Outbounds"

    def save(self, *args, **kwargs):
        if not self.outbound_number:
            last = Outbound.objects.order_by("-id").first()

            if last:
                last_number = int(last.outbound_number[3:])
                self.outbound_number = f"OUT{last_number + 1:06d}"
            else:
                self.outbound_number = "OUT000001"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.outbound_number