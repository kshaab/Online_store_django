from django.contrib import admin

from users.models import User


@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("email", "phone_number", "country")
    list_filter = ("country",)
    search_fields = (
        "email",
        "phone_number",
    )
