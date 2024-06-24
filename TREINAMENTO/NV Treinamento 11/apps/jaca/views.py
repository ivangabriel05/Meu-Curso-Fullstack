from django.shortcuts import render
from .models import *

def PaginaInicial(request):
    return render(request, "index.html")

def PaginaCompras(request):
    busca = arvore.objects.all()
    return render(request, "Compras_plantas.html", {"Plantas": busca})

def PaginaClientes(request):
    busca = plantas.objects.all()
    return render(request, "Compras_arvores.html", {"Arvores": busca})