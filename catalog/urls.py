from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (ContactsView, ProductCreateView, ProductDeleteView, ProductDetailView, ProductListView,
                           ProductUpdateView)

app_name = CatalogConfig.name
urlpatterns = [
    path("home/", ProductListView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/new/", ProductCreateView.as_view(), name="product_new"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]
