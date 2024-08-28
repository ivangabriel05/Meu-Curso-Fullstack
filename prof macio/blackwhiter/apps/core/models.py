from django.db import models
from django import forms
from django.forms import ModelForm

class Item(models.Model):
 nome = models.CharField(max_length=100)
 descricao = models.TextField()
 preco = models.DecimalField(max_digits=10, decimal_places=2)
 criado_em = models.DateTimeField(auto_now_add=True)
 
def __str__(self):
        return self.nome

class clients(models.Model):
     id = models.AutoField(primary_key=True)
     name = models.CharField(max_length=150)
     cpf_cnpj = models.CharField(max_length=150)
     rg_ie = models.CharField(max_length=150)
     zip_code = models.TextField(max_length=150)
     address = models.TextField(max_length=150)
     neighborhood =models.TextField(max_length=5)
     number = models.TextField(max_length=5)
     city = models.TextField(max_length=50)
     state = models.TextField(max_length=3)
     ddd = models.TextField(null=True, blank=True, max_length=4)
     created_ad = models.DateTimeField(auto_now_add=True)
     updated_ad = models.DateTimeField(null=True, blank=True, auto_now_add=False)
     deleted_ad = models.DateTimeField(null=True, blank=True, auto_now_add=False)

     def __str__(self):
         return self.name
     
