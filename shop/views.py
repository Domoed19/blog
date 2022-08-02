
from django.http import HttpResponse

from shop.models import Product
from shop.models import Purchase
from django.db.models import Count, Sum, Max

def products(request):
    if request.GET.get('color'):
        product_list = Product.objects.filter(color=request.GET.get('color'))
    else:
        product_list = Product.objects.all()
    return HttpResponse(", ".join([x.title for x in product_list]))

def sort_of_product(request):
    if request.GET.get('cost'):
        sort_list = Product.objects.all().order_by('cost')
    if request.GET.get('count'):
        sort_list = Purchase.objects.aggregate(purchases=Sum("count"))
    return HttpResponse(", ".join([x.cost for x in sort_list]))