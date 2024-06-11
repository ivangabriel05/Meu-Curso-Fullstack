from django.db import models
class produtos(models.Model):
    nome = models.CharField(max_length=50)
    valor_produto = models.models.DecimalField(max_digits=5, decimal_places=2)
# Create your models here.
