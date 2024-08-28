from django.db import models

class compras(models.Model):
    nome_item = models.CharField(max_length=50)
    numero = models.PositiveIntegerField()

    def __str__(self):
        return self.nome_item
    

    
