from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок", help_text="Введите заголовок поста")
    content = models.TextField(verbose_name="Содержимое", help_text="Введите содержимое поста")
    preview = models.ImageField(
        upload_to="preview/", verbose_name="Превью", help_text="Загрузите изображение", blank=True, null=True
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания записи",
        blank=True,
        null=True,
    )
    publicate = models.BooleanField(verbose_name="Признак публикации", default=True)
    views = models.IntegerField(default=0, verbose_name="Количество просмотров")
    notified = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title
