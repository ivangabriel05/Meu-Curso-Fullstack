from django.shortcuts import render
from .models import *

def PaginaInicial(request):
    return render(request, "index.html")

def PaginaPacientes(request):
    busca = Paciente.objects.all()
    return render(request, "lista-paciente.html", {"paciente": busca})

def PaginaDoutores(request):
    busca = Doutor.objects.all()
    return render(request, "Lista-doutores.html", {"doutores": busca})