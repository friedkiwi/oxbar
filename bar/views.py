from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.template import RequestContext, loader
# Create your views here.

def index(request):
    products = Product.objects.order_by('name')
    output = ', '.join([p.name for p in products])
    template = loader.get_template('bar/index.html')
    context = RequestContext(request, {
        'products' : products
    })

    return HttpResponse(template.render(context))