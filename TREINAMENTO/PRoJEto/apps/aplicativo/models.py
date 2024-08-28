from django.db import models

class serviço(models.Model):
    nome = models.CharField(max_length=50)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome
    
class clinte(models.Model):
    nome = models.CharField(max_length=50)
    pedido = models.IntegerField()
    
    def __str__(self):
        return self.pedido
    
class hacker(models.Model):
    clintes = models.CharField(max_length=50)

    def __str__(self):
        return self.clintes