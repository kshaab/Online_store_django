from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product, Contacts


def home(request):
    last_products = Product.objects.order_by("-created_at")[:5]
    for product in last_products:
        print(product)
    return render(request, "home.html")


def contacts(request):
    contact = Contacts.objects.first()
    return render(request, "contacts.html", {"contact": contact})


def contacts_post(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "catalog/templates/contacts.html")
