from django.shortcuts import render, redirect
from .models import *
from .forms import *

def VerIndex(request):
    busca_tabela = serviço.objects.all()
    return render(request, "index.html", {"index": busca_tabela})

def VerHacker(request):
    if request.method == "POST":
        nova_busca = CompraForm()
    else:
        busca_nova = CompraForm(request.GET, request.FILES)
        if busca_nova.is_valid():
            busca_nova.save()
            return redirect("pg_index")
    return render(request, "hacker.html", {"hacker": nova_busca})

def VerClientes(request):
    if request.method == "POST":
        nova_busca = CompraForm()
    else:
        busca_nova = CompraForm(request.GET, request.FILES)
        if busca_nova.is_valid():
            busca_nova.save()
            return redirect("pg_index")
    return render(request, "clientes.html", {"clientes": nova_busca})

def VerServicos(request):
    if request.method == "POST":
        nova_busca = CompraForm()
    else:
        busca_nova = CompraForm(request.GET, request.FILES)
        if busca_nova.is_valid():
            busca_nova.save()
            return redirect("pg_index")
    return render(request, "servicos.html", {"servicos": nova_busca})