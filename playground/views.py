from django.db.models.aggregates import Count, Max, Min
from django.shortcuts import render
from django.db.models import Q, F
from django.db.models.aggregates import Min, Max, Sum, Count, Avg
from store.models import Order, OrderItem, Product


# Create your views here.


def say_hello(request):
    result = Product.objects.filter(
        collection__id=3).aggregate(min_price=Min('unit_price'), avg_price=Avg('unit_price'), max_price=Max('unit_price'))

    return render(request, 'hello.html', {"name": "Vaibhav", "result": result})
