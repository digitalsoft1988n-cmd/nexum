from django.contrib import admin

from workspace.models import Board


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
    )

    prepopulated_fields = {"slug": ("title",)}

    ordering = ("-created_at",)
