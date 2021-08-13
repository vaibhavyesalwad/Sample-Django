from django.db.models.aggregates import Count, Max, Min
from django.db.models.expressions import Func
from django.shortcuts import render
from django.db.models import Q, F, Value, Func
from django.db.models.functions import Concat
from django.db.models.aggregates import Min, Max, Sum, Count, Avg
from store.models import CartItem, Customer, Order, OrderItem, Product


# Create your views here.


def say_hello(request):
    query_set = Customer.objects.annotate(orders_count=Count('order'))

    return render(request, 'hello.html', {"name": "Vaibhav", "query_set": list(query_set)})
