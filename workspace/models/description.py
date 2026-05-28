from django.db import models

from .card import Card


class Description(models.Model):
    card = models.OneToOneField(
        Card,
        on_delete=models.CASCADE,
        related_name="description_obj",
    )

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Description for {self.card}"
