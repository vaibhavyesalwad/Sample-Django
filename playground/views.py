from django.shortcuts import render
from django.db.models import Q
from store.models import Product


# Create your views here.


def say_hello(request):
    queryset = Product.objects.filter(
        Q(unit_price__range=(1, 5)) & ~Q(inventory__range=(10, 20)))

    return render(request, 'hello.html', {"name": "Vaibhav", "products": list(queryset)})
