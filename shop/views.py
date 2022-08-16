from django.http import HttpResponse
from django.shortcuts import render

from shop.models import Product
from shop.services import get_sorted_product

def products(request):
    if request.GET.get('color'):
        product_list = Product.objects.filter(color=request.GET.get('color'))
    else:
        product_list = Product.objects.all()
    order_by = request.GET.get('order_by')

    product_list = get_sorted_product(product_list, order_by)
    return render(request, "index.html", {"product_list": product_list})

