from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product


# Create your views here.


def say_hello(request):
    queryset = Product.objects.filter(inventory=F('unit_price'))

    return render(request, 'hello.html', {"name": "Vaibhav", "products": list(queryset)})
