from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DeleteView, DetailView, ListView, TemplateView, UpdateView
from django.views.generic.edit import CreateView

from catalog.models import Contacts, Product


class BaseTemplateView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["last_products"] = Product.objects.order_by("-created_at")[:5]
        return context


class ContactsView(View):
    template_name = "contacts.html"

    def get(self, request, *args, **kwargs):
        contact = Contacts.objects.first()
        return render(request, self.template_name, {"contact": contact})

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение '{message}' получено.")


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "products"
    paginate_by = 4
    ordering = ["id"]


class ProductCreateView(CreateView):
    model = Product
    fields = ["name", "description", "category", "price", "image"]
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ["name", "description", "category", "price", "image"]
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:home")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")
