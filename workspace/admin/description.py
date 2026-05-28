from django.contrib import admin

from workspace.models import Description


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "card",
        "updated_at",
    )

    search_fields = (
        "card__title",
        "content",
    )

    ordering = ("-updated_at",)
