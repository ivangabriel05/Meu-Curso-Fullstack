from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    return render(request, "index.html")

def Cliente(request):
    busca = Clientes.objects.all()
    return render(request, "Pagina1.html", {"Cliente": busca})

def Usuario(request):
    busca = Usuarios.objects.all()
    return render(request, "Pagina2.html", {"Usuarios": busca})

def Compra(request):
    busca = Compras.objects.all()
    return render(request, "Pagina3.html", {"Compras": busca})
