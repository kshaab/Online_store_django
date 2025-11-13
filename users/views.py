from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserUpdateForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        send_mail(
            subject="Добро пожаловать на сайт!",
            message="Приветствуем! Спасибо за регистрацию на нашем сайте!",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=True,
        )
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "profile_edit.html"
    success_url = reverse_lazy("users:profile_edit")

    def get_object(self, queryset=None):
        return self.request.user
