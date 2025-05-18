from django.contrib import admin
from .models import Listing


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "price", "created_at")
    search_fields = ("title", "description", "location")
    list_filter = ("created_at",)
