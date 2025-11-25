from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (ContactsView, ProductByCategoryView, ProductCreateView, ProductDeleteView,
                           ProductDetailView, ProductListView, ProductUpdateView)

app_name = CatalogConfig.name
urlpatterns = [
    path("home/", ProductListView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("product/new/", ProductCreateView.as_view(), name="product_new"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path(
        "category/<str:category_name>/", cache_page(60)(ProductByCategoryView.as_view()), name="products_by_category"
    ),
]
