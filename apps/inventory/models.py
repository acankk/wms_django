from django.db import models


class Bin(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "bins"
        ordering = ["code"]
        verbose_name = "Bin"
        verbose_name_plural = "Bins"

    def __str__(self):
        return f"{self.code} - {self.name}"