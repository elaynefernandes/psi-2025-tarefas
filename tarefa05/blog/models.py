from django.db import models

class Postagem(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='postagens/')
    texto = models.TextField()
    data_publicacao = models.DateField()

    def __str__(self):
        return self.titulo
