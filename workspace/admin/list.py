from django.contrib import admin

from workspace.models import List


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "board",
        "position",
        "created_at",
    )

    list_filter = ("board",)

    search_fields = (
        "title",
        "board__title",
    )

    ordering = (
        "board",
        "position",
    )
