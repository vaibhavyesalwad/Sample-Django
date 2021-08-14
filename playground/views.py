from django.db.models.aggregates import Count, Max, Min
from django.db.models.expressions import ExpressionWrapper, Func
from django.db.models.fields import DecimalField
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem


# Create your views here.


def say_hello(request):
    query_set = Product.objects.all()

    # query is cached only if evaluate whole queryset
    query_set[0]        # Now 2 queries 1. first row
    list(query_set)     # 2. all rows

    # list(query_set)      # Now only one query all rows
    # query_set[0]         # first row from cached queryset

    # reads already cached queryset
    return render(request, 'hello.html', {"name": "Vaibhav", "result": list(query_set)})
