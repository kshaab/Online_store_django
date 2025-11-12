from django import forms

from blog.models import BlogPost


class StyleFormMixin:
    fields: dict[str, forms.Field]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control", "placeholder": "Введите название статьи"})
        self.fields["content"].widget.attrs.update({"class": "form-control", "placeholder": "Тело статьи"})
        self.fields["notified"].widget.attrs.update({"class": "form-check-input"})


class BlogPostForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "content", "preview", "notified"]
