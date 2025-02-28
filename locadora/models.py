from django.db import models


class Filme(models.Model):
    titulo = models.CharField(max_length=255)
    ano_lancamento = models.IntegerField()
    genero = models.CharField(max_length=255)
    diretor = models.CharField(max_length=255)
    sinopse = models.CharField(max_length=255)
    linguagens = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo