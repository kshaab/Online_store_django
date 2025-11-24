from typing import Optional

from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponseForbidden
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from blog.forms import BlogPostForm
from blog.models import BlogPost


class ContentManagerRequiredMixin(UserPassesTestMixin):
    request: Optional[HttpRequest]

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.groups.filter(name="Контент-менеджер").exists()

    def handle_no_permission(self):
        return HttpResponseForbidden("У вас нет прав для управления блог-постами.")


class BlogPostCreateView(ContentManagerRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_content_manager"] = self.request.user.groups.filter(name="Контент-менеджер").exists()
        return context


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


class BlogPostUpdateView(ContentManagerRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blog_form.html"
    success_url = reverse_lazy("blog:blog")

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])


class BlogPostDeleteView(ContentManagerRequiredMixin, DeleteView):
    model = BlogPost
    template_name = "blog_confirm_delete.html"
    success_url = reverse_lazy("blog:blog")
