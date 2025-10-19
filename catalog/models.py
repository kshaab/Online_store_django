from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование", help_text="Введите наименование категории")
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание категории", blank=True, null=True
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование", help_text="Введите наименование товара")
    description = models.TextField(verbose_name="Описание", help_text="Введите описание товара", blank=True, null=True)
    image = models.ImageField(
        upload_to="products/", verbose_name="Изображение", help_text="Загрузите изображение", blank=True, null=True
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена за покупку",
        help_text="Введите цену за покупку",
        blank=True,
        null=True,
    )
    created_at = models.DateField(
        verbose_name="Дата создания", help_text="Введите дату создания продукта", blank=True, null=True
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения",
        help_text="Введите дату последнего изменения продукта",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name


class Contacts(models.Model):
    country = models.CharField(max_length=150, verbose_name="Страна", help_text="Введите страну")
    inn = models.CharField(max_length=150, verbose_name="ИНН", help_text="Введите ИНН")
    address = models.CharField(max_length=150, verbose_name="Адрес", help_text="Введите адрес")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"{self.country}, {self.inn},{self.address}"
