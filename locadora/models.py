from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Usuario(AbstractBaseUser):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255, default='')
    numero = models.IntegerField(default='')
    filmes_alugados = models.ManyToManyField('Filme', through='Aluguel', related_name='usuarios_alugados')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

class filme(models.Model):
    titulo = models.CharField(max_length=255)
    ano_lancamento = models.IntegerField()
    genero = models.CharField(max_length=255)
    diretor = models.CharField(max_length=255)
    sinopse = models.CharField(max_length=255)
    linguagens = models.CharField(max_length=255)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.titulo

class Aluguel(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    filme = models.ForeignKey(filme, on_delete=models.CASCADE)
    data_aluguel = models.DateTimeField(auto_now_add=True)