from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

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

    def get_queryset(self):
        return BlogPost.objects.filter(publicate=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blog_detail.html"
    context_object_name = "blog_post"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save(update_fields=["views"])
        if obj.views == 100 and not obj.notified:
            send_mail(
                subject="Ваша статья набрала 100 просмотров!",
                message=f"Поздравляем! Ваша статья '{obj.title}' набрала 100 просмотров!",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=True,
            )
            obj.notified = True
            obj.save(update_fields=["notified"])
        return obj


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
