from django.db import models
    
class Clientes(models.Model):
    nome = models.CharField("nome", max_length=50)
    foto = models.ImageField(upload_to="imagens/")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    
class Usuarios(models.Model):
    nome = models.CharField("nome", max_length=50)
    arquivo = models.FileField(upload_to="pdfs/")
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        
    
class Compras(models.Model):
    TIPO_SEXO = (
        ("Masculino", "Masculino"),
        ("Ferminino", "Ferminino")

    )
    nome = models.CharField("nome", max_length=50)
    sexo = models.CharField(max_length=15, choices=TIPO_SEXO)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"