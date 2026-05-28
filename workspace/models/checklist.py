from django.db import models

from .card import Card


class Checklist(models.Model):
    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        related_name="checklists",
    )

    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)

    position = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return self.title
