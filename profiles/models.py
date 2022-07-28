from django.db import models
from django.conf import settings


class Address(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="address",
        blank=True,
        null=True
    )
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )
    def __str__(self):
        return f"Address:{self.city}, {self.address}"

