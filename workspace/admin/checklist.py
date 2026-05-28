from django.contrib import admin

from workspace.models import Checklist


@admin.register(Checklist)
class ChecklistAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "card",
        "is_completed",
        "position",
    )

    list_filter = ("is_completed",)

    search_fields = (
        "title",
        "card__title",
    )

    ordering = (
        "card",
        "position",
    )
