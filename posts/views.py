import logging
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    logger.info (f"MY_PATH: {settings.MY_PATH_ZNACH}")
    if request.GET.get("key") == "test":
        return HttpResponse("Posts with test key")
    elif request.GET.get("PEREMEN_01") == 21:
        logger.info(f"PEREMEN_02: {settings.PEREMEN_02}")
    else:
        logger.info(f"PEREMEN_03: {settings.PEREMEN_03}")
    return HttpResponse("Posts index view")

