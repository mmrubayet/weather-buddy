from django.contrib import admin

from .models import District


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "dist_id", "division_id", "bn_name", "lat", "long")
    ordering = ["dist_id"]
    list_display_links = ["name"]
