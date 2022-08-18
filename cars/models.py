
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
         related_name="cars",
         blank=True,
         null=True
    )
    title = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    color = models.CharField(max_length=200, blank=True, null=True)
    text = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )
    def __str__(self):
        return f"Post:{self.title}"