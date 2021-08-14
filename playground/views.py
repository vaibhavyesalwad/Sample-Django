from django.db.models.aggregates import Count, Max, Min
from django.db.models.expressions import ExpressionWrapper, Func
from django.db.models.fields import DecimalField
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Collection, Product
from tags.models import TaggedItem


# Create your views here.


def say_hello(request):

    # Make sure to select primary key to update
    # Implementation 1
    # WE have to read row first and then update using traditional way to retain earlier values in row
    # collection = Collection.objects.get(pk=11)
    # collection.featured_product = None
    # collection.save()

    # Implementation 2
    # Only intended values will be changed
    Collection.objects.filter(pk=11).update(featured_product=None)

    return render(request, 'hello.html', {"name": "Vaibhav"})
