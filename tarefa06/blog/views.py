from django.shortcuts import render
from .models import Postagem

def blog(request):
    postagens = Postagem.objects.all()
    context = {
        'postagens' : postagens
    }
    return render(request, 'blog/postagens.html', context)