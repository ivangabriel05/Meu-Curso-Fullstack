from django.db import models

class Paciente(models.models):
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    diagnostico = models.TextField()

    def __str__(self):
        return self.nome
    
class Doutor(models.Model):
    nome = models.CharField(max_length=50)
    especializacao = models.CharField(max_length=50)    
    crm = models.PositiveIntegerField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Doutor"
        verbose_name_plural = "Doutores"
    
    