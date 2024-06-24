from django.db import models

class produto(models.Model):
    nome_Produto = models.CharField(max_length=50)
    valor_Produtor = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome_Produto
