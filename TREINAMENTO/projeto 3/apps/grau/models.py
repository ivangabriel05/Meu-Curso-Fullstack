from django.db import models

class lojinha(models.Model):
    nome = models.CharField(max_length=20)
    itens = models.TextField()
    valor = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome



