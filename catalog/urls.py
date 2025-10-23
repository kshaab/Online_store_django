from django.urls import path

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name
urlpatterns = [
    path("home/", views.products_list, name="home"),
    path("contacts/", views.contacts, name="contacts"),
    path("contacts_post/", views.contacts_post, name="contacts_post"),
    path("products/<int:pk>/", views.products_detail, name="products_detail"),
]
