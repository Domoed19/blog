import logging
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from posts.models import Post

from django.shortcuts import render, redirect


def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})





