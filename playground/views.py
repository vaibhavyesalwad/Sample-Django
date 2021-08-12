from django.shortcuts import render
from django.db.models import Q, F
from store.models import OrderItem, Product


# Create your views here.


def say_hello(request):
    products = Product.objects.filter(
        pk__in=OrderItem.objects.values('product')).values('title').order_by('title')

    return render(request, 'hello.html', {"name": "Vaibhav", "products": list(products)})
