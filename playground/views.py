from django.db.models.aggregates import Count, Max, Min
from django.db.models.expressions import ExpressionWrapper, Func
from django.db.models.fields import DecimalField
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Collection, Product
from tags.models import TaggedItem


# Create your views here.


def say_hello(request):
    # Make sure to select primary key to delete

    # Implementation 1
    # collection = Collection(pk=12)
    # collection.delete()

    # Implementation 2
    Collection.objects.filter(pk=12).delete()

    return render(request, 'hello.html', {"name": "Vaibhav"})
