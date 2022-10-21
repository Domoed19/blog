from django.contrib import admin

from profiles.models import Address


@admin.register(Address)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "city", "address")
    search_fields = ("city", "address")
