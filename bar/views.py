from django.shortcuts import render
from django.http import HttpResponse, Http404
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

def buy(request, product_id):
    try:
        product = Product.objects.get(pk = product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist.")

    template = loader.get_template('bar/buy.html')

    context = RequestContext(request, {
        'product' : product
    })

    return HttpResponse(template.render(context))


