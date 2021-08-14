from django.db.models.aggregates import Count, Max, Min
from django.db.models.expressions import ExpressionWrapper, Func
from django.db.models.fields import DecimalField
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem


# Create your views here.


def say_hello(request):
    content_type = ContentType.objects.get_for_model(Product)

    # finding tags for product with id = 1
    query_set = TaggedItem.objects.select_related('tag').filter(
        content_type=content_type,
        object_id=1
    )

    return render(request, 'hello.html', {"name": "Vaibhav", "result": list(query_set)})
