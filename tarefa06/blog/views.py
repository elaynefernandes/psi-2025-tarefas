from django.shortcuts import render
from .models import Postagem

def blog_view(request):
    postagens = Postagem.objects.all()
    return render(request, 'blog/postagens.html', {'postagens': postagens})