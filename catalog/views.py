from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView
from catalog.models import Contacts, Product
from django.urls import reverse_lazy
from django.core.paginator import Paginator


def home(request):
    last_products = Product.objects.order_by("-created_at")[:5]
    for product in last_products:
        print(product)
    return render(request, "base.html")


def contacts(request):
    contact = Contacts.objects.first()
    return render(request, "contacts.html", {"contact": contact})


def contacts_post(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение {message} получено.")
    return render(request, "catalog/templates/contacts.html")


def products_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "products_detail.html", context)


def products_list(request):
    products = Product.objects.all().order_by('id')
    paginator = Paginator(products, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "products_list.html", context)


class ProductCreateView(CreateView):
    model = Product
    fields = ["name", "description", "category" ,"price", "image"]
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:home")
