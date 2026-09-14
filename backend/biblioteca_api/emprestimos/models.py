from django.db import models
from livros.models import Livro


class Emprestimo(models.Model):

    livro = models.ForeignKey(
        Livro,
        on_delete=models.CASCADE,
        related_name='emprestimos'
    )

    aluno_nome = models.CharField(max_length=150)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)
    devolvido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.livro.titulo} - {self.aluno_nome}"
