from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from blog.models import BlogPost


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ["title", "content", "preview"]
    template_name = "blog_form.html"
    success_url = reverse_lazy("blog:blog")


class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog_list.html"
    context_object_name = "blog_posts"
    paginate_by = 2
    ordering = ["id"]


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blog_detail.html"
    context_object_name = "blog_post"


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ["title", "content", "preview"]
    template_name = "blog_form.html"
    success_url = reverse_lazy("blog:blog")

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = "blog_confirm_delete.html"
    success_url = reverse_lazy("blog:blog")

