from django.shortcuts import render
from .models import *

def PaginaInicial(request):
    return render(request, "index.html")

def PaginaPacientes(request):
    busca = .objects.all()
    return render(request, ".html", {"": busca})

def PaginaDoutores(request):
    busca = .objects.all()
    return render(request, ".html", {"": busca})