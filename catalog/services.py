from django.core.cache import cache

from catalog.models import Product
from online_store_django.settings import CACHE_ENABLED


class ProductService:

    @staticmethod
    def get_product_list(category_name=None):
        """Список продуктов по категориям с низкоуровневым кешированием"""
        if not CACHE_ENABLED:
            return Product.objects.all().order_by("id")
        key = f"products_{category_name or 'all'}"
        product_id = cache.get(key)
        if product_id is None:
            if category_name:
                qs = Product.objects.filter(category__name=category_name).order_by("id")
            else:
                qs = Product.objects.all().order_by("id")
            product_id = list(qs.values_list("id", flat=True))
            cache.set(key, product_id)
        return Product.objects.filter(id__in=product_id).order_by("id")

    @staticmethod
    def get_products_from_cache():
        """Список продуктов с низкоуровневым кешированием"""
        if not CACHE_ENABLED:
            return Product.objects.all()
        key = "product_list"
        products = cache.get(key)
        if products is not None:
            return products
        products = Product.objects.all()
        cache.set(key, products)
        return products
