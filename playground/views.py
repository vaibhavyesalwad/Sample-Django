from django.db.models.aggregates import Count, Max, Min
from django.db.models.expressions import ExpressionWrapper, Func
from django.db.models.fields import DecimalField
from django.shortcuts import render
from store.models import Collection, Order, OrderItem, Product
from django.db import transaction, connection

# Create your views here.


def say_hello(request):

    # Implementation 1
    # queryset = Product.objects.raw('SELECT * FROM store_product')

    # Implementation 2
    # cursor = connection.cursor()
    # queryset = cursor.execute('SELECT * FROM store_product')
    # cursor.close()

    # Implementation 3
    with connection.cursor() as cursor:
        # queryset = cursor.execute("SELECT * FROM sql_invoicing.invoices")
        # for calling stored procedure
        queryset = cursor.callproc('sql_invoicing.make_payment', [
                                   2, 150, '2019-01-01'])

    print(queryset, type(queryset))

    return render(request, 'hello.html', {"name": "Vaibhav", "result": queryset})
