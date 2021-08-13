from django.shortcuts import render
from django.db.models import Q, F
from store.models import OrderItem, Product


# Create your views here.


def say_hello(request):
    products = Product.objects.defer('title')
    # print(products)

    # products = Product.objects.only('id')
    print(products)

    return render(request, 'hello.html', {"name": "Vaibhav", "products": list(products)})
