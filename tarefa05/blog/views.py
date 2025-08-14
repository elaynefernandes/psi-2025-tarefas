from django.shortcuts import render, get_object_or_404
from .models import Post, Blog

def index(request):
    context = {
        "posts": Post.objects.all(),
        "blog": Blog.objects.first(),
    }
    return render(request, "blog/index.html", context)


def detalhe_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post.html', {'post': post})
