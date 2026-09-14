from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    matricula = models.CharField(max_length=30, unique=True)
    email = models.EmailField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

