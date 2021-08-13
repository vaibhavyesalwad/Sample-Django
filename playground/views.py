from django.shortcuts import render
from django.db.models import Q, F
from store.models import Order, OrderItem, Product


# Create your views here.


def say_hello(request):
    orders = Order.objects.order_by(
        '-placed_at').select_related('customer').prefetch_related('orderitem_set__product')[:5]

    return render(request, 'hello.html', {"name": "Vaibhav", "orders": list(orders)})
