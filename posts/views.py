import logging
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from posts.models import Post, Address

logger = logging.getLogger(__name__)

# def index(request):
#     logger.info (f"MY_PATH: {settings.MY_PATH_ZNACH}")
#     if request.GET.get("key") == "test":
#         return HttpResponse("Posts with test key")
#     elif request.GET.get("PEREMEN_01") == 21:
#         logger.info(f"PEREMEN_02: {settings.PEREMEN_02}")
#     else:
#         logger.info(f"PEREMEN_03: {settings.PEREMEN_03}")
#     return HttpResponse("Posts index view")

def index(request):
    if request.GET.get('title'):
        post_list = Post.objects.filter(title__icontains=request.GET.get('title'))
    else:
        post_list = Post.objects.all()
    return HttpResponse(", ".join([x.title for x in post_list]))



def get_search(request):
    if request.GET.get('city'):
        city_list = Address.objects.filter(city__icontains=request.GET.get('city'))
    else:
        city_list = Address.objects.all()
    return HttpResponse(", ".join([x.city for x in city_list]))

def filt_post(request):
    filtr = Post.objects.filter(author_id=request.user)
    return HttpResponse(filtr)


