from django.db import models
from django.utils.text import slugify

from django.contrib.auth import get_user_model

User = get_user_model()


class Board(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="boards")
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
