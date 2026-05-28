from django.contrib import admin

from workspace.models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "list",
        "position",
        "created_at",
    )

    list_filter = ("list__board",)

    search_fields = (
        "title",
        "description",
        "list__title",
    )

    ordering = (
        "list",
        "position",
    )
