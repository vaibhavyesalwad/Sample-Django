from django.db.models.aggregates import Count, Max, Min
from django.db.models.expressions import ExpressionWrapper, Func
from django.db.models.fields import DecimalField
from django.shortcuts import render
from store.models import Collection, Order, OrderItem, Product
from django.db import transaction

# Create your views here.


def say_hello(request):

    with transaction.atomic():
        order = Order()
        order.customer_id = 1
        order.save()

        item = OrderItem()
        item.order = order
        item.product_id = 1
        item.quantity = 1
        item.unit_price = 10
        item.save()

    return render(request, 'hello.html', {"name": "Vaibhav"})
