from django.db.models.aggregates import Count, Max, Min
from django.db.models.expressions import ExpressionWrapper, Func
from django.db.models.fields import DecimalField
from django.shortcuts import render
from store.models import Collection, Order, OrderItem, Product
from django.db import transaction, connection

# Create your views here.


def say_hello(request):

    # Implementation 1
    queryset = Product.objects.raw('SELECT * FROM store_product')

    # Implementation 2
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM store_product')
    cursor.close()

    # Implementation 3
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM store_product')
        # cursor.callproc       # for calling stored procedure

    return render(request, 'hello.html', {"name": "Vaibhav", "result": list(queryset)})
