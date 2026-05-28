from django.db import models

from .list import List


class Card(models.Model):
    list = models.ForeignKey(
        List,
        on_delete=models.CASCADE,
        related_name="cards",
    )

    title = models.CharField(max_length=255)

    position = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return self.title
