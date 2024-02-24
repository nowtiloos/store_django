from django.shortcuts import render
from products.models import Product, ProductCategory


def index(request):
    context: dict = {
        'title': 'Магазин одежды',
    }
    return render(
        request=request,
        template_name='products/index.html',
        context=context,
    )


def products(request):
    context: dict = {
        'title': 'Магазин одежды каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(
        request=request,
        template_name='products/products.html',
        context=context,
    )
