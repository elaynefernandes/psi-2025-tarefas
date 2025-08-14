from django.db import models

class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    desenvolvedor = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='posts/', blank=True)
    data = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo
