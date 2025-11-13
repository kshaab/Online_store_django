from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class StyleFormMixin:
    fields: dict[str, forms.Field]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_styles = {
            "email": "Введите электронную почту",
            "password1": "Введите пароль",
            "password2": "Повторите пароль",
            "phone_number": "Введите номер телефона",
            "country": "Введите страну",
        }
        for name, placeholder in field_styles.items():
            if name in self.fields:
                self.fields[name].widget.attrs.update({"class": "form-control", "placeholder": placeholder})


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]


class UserUpdateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "phone_number", "country", "avatar"]
