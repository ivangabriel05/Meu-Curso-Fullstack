from django.db import models

class encomendas (models.Model):
    nome = models.CharField(max_length=50)
    quant_bolos = models.PositiveIntegerField()
    IVAN = models.DecimalField(_(""), max_digits=5, decimal_places=2)
    def __str__(self):
        return self.nome
    
