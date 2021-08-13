from django.db.models.aggregates import Count, Max, Min
from django.db.models.expressions import ExpressionWrapper, Func
from django.db.models.fields import DecimalField
from django.shortcuts import render
from django.db.models import Q, F, Value, Func, ExpressionWrapper
from django.db.models.functions import Concat
from django.db.models.aggregates import Min, Max, Sum, Count, Avg
from store.models import CartItem, Customer, Order, OrderItem, Product


# Create your views here.


def say_hello(request):
    discounted_price = ExpressionWrapper(
        F('unit_price')*0.8, output_field=DecimalField())
    query_set = Product.objects.annotate(discounted_price=discounted_price)

    return render(request, 'hello.html', {"name": "Vaibhav", "query_set": list(query_set)})
