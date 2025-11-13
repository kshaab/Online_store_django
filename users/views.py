from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import UserRegisterForm
from users.models import User
from django.conf import settings




class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        send_mail(
            subject="Добро пожаловать на сайт!",
            message=f"Приветствуем! Спасибо за регистрацию на нашем сайте!",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=True,
        )
        return super().form_valid(form)


