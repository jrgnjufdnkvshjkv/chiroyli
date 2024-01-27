from django.shortcuts import render
from .models import Products, Client
# Create your views here.
def index(request):
    products = Products.objects.all()
    clients = Client.objects.all()
    context = {
        "products": products,
        "clients": clients,
    }
    return render(request, "index.html", context=context)

def product(request):
    products = Products.objects.all()
    context = {
        "products": products,
    }
    return render(request, "products.html", context=context)

def about(request):
    return render(request, "about.html", context={})

def client(request):
     clients = Client.objects.all()
     context = {
         "clients": clients,
     }
     return render(request, "client.html", context=context)

def contact(request):
    return render(request, "contact.html", context={})


