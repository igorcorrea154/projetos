from django.db import models
from django.utils import timezone

class Token(models.Model):
    ip_address = models.GenericIPAddressField()  # <-- ESSA LINHA TEM QUE EXISTIR
    token = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return timezone.now() - self.created_at < timezone.timedelta(seconds=60)

    def __str__(self):
        return f"{self.ip_address} - {self.token}"
