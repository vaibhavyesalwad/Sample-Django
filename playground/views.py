from django.db.models.aggregates import Count, Max, Min
from django.shortcuts import render
from django.db.models import Q, F, Value
from django.db.models.aggregates import Min, Max, Sum, Count, Avg
from store.models import Order, OrderItem, Product


# Create your views here.


def say_hello(request):
    query_set = Product.objects.annotate(new_id=F('id') + 2)

    return render(request, 'hello.html', {"name": "Vaibhav", "query_set": list(query_set)})
