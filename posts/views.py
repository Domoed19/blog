from django.http import HttpResponse

from posts.models import Post
from posts.forms import PostForm
from posts.models import Post
from django.shortcuts import render, redirect


def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})


def post_add(request):
    if not request.user.is_authenticated:
        return HttpResponse("You aren't authenticated!")

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            Post.objects.create(author=request.user, **form.cleaned_data)
            return redirect("index")
    else:
        form = PostForm()
    return render(request, "post_add.html", {"form": form})
