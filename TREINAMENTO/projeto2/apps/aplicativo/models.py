from django.db import models

class hacker(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.PositiveIntegerField()
    formacao = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
class clientes(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

class servico(models.Model):
    servico = models.CharField(max_length=50)
    descricao = models.TextField()
    tomador = models.ForeignKey(hacker, on_delete=models.CASCADE)
    cliente = models.ForeignKey(clientes, on_delete=models.CASCADE)

    def __str__(self):
        return self.servico
    


    


    
