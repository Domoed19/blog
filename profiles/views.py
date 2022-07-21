from django.shortcuts import render

from django.http import HttpResponse


def profiles(request):
    if request.GET.get("key") == "test":
        return HttpResponse("Profiles with test key")
    elif request.POST.get("key"):
        return HttpResponse("test")
    elif request.GET.get("email") == "test@gmail.com":
        return HttpResponse("Profiles with test email")
    elif request.POST.get("email"):
        return HttpResponse("test@gmail.com")
    return HttpResponse("Profiles index view")
