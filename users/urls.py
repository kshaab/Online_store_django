from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UserConfig
from users.views import UserCreateView, UserUpdateView

app_name = UserConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("profile/edit/", UserUpdateView.as_view(), name="profile_edit"),
]
