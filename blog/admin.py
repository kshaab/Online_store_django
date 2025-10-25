from django.contrib import admin

from blog.views import BlogPost


@admin.register(BlogPost)
class BlogPost(admin.ModelAdmin):
    list_display = ("id", "title")
    list_filter = ("publicate", "title")
    search_fields = (
        "title",
        "created_at",
    )
