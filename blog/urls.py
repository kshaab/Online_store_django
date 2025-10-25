from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogPostCreateView, BlogPostDeleteView, BlogPostDetailView, BlogPostListView, BlogPostUpdateView

app_name = BlogConfig.name

urlpatterns = [
    path("", BlogPostListView.as_view(), name="blog"),
    path("new/", BlogPostCreateView.as_view(), name="blog_new"),
    path("<int:pk>/update/", BlogPostUpdateView.as_view(), name="blog_update"),
    path("<int:pk>/delete/", BlogPostDeleteView.as_view(), name="blog_delete"),
    path("<int:pk>/detail/", BlogPostDetailView.as_view(), name="blog_detail"),
]
