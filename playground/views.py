from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product


# Create your views here.


def say_hello(request):
    queryset = Product.objects.filter(unit_price__range=(
        0, 15), inventory__range=(10, 30)).order_by('unit_price', '-title').reverse()

    first_product = queryset[0]
    last_product = list(queryset)[-1]

    return render(request, 'hello.html', {"name": "Vaibhav", "products": list(queryset),
                                          "first_product": first_product, "last_product": last_product})
