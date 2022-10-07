
from django.core.cache import cache
from django.db.models import Count, F, QuerySet, Sum
from django.shortcuts import render

from django.http import HttpResponse
from shop.models import Purchase, Product


def products(request):
    if request.GET.get("color"):
        product_list = Product.objects.filter(color=request.GET.get("color"))
    else:
        product_list = Product.objects.all()
    order_by = request.GET.get("order_by")

    product_list = product_sorting(product_list, order_by)
    return render(request, "index.html", {"product_list": product_list})


def product_sorting(queryset: QuerySet, order_by: str):
    if order_by == "cost":
        return queryset.order_by("cost")
    elif order_by == "-cost":
        return queryset.order_by("cost")
    elif order_by == "sold":
        queryset = queryset.annotate(sold=Sum(F("cost") * F("purchase__count")))
        return queryset.order_by("sold")
    elif order_by == "popular":
        queryset = queryset.annotate(popular=Sum("purchase__count"))
        return queryset.order_by("popular")
    return queryset


def product_get(request):
    if request.POST.get("title"):
        product_info = Product.objects.filter(title=request.GET.get("title"))
        user_info = Product.objects.filter(purchase__user=request.user)
    else:
        product_info = "Title did not found"
        user_info = "Not available"
    order_by = request.GET.get("order_by")

    # product_info = product_sorting(product_info, order_by)
    return render(request, "product.html", {"product_info": product_info, "user_info": user_info})

#
# def products(request):
#     color = request.GET.get("color")
#     order_by = request.GET.get("order_by")
#     cache_key =f"products-view.{color}.{order_by}"
#
#     result = cache.get("products-view")
#     if result is not None:
#         return result
#
#     if color:
#         product_list = Product.objects.filter(color=color)
#     else:
#         product_list = Product.objects.all()
#
#
#     product_list = product_sorting(product_list, order_by)
#     response = render(request, "index.html", {"product_list": product_list})
#     cache.set("products-view", response, 60 * 60)
#     return response

# Create your views here.

