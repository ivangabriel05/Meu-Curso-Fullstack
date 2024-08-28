from django.shortcuts import render, redirect
from .models import *
from .forms import *

def pageIndex(request):
    busca_compras = servico.objects.all()
    return render(request, "index.html", {"lista": busca_compras })

def Vercliente(request):    
    if request.method == "POST":
        nova_busca = ClientesForm(request.POST)  
        if nova_busca.is_valid():
            nova_busca.save()
            return redirect("pg_clientes")
    else:
        nova_busca = ClientesForm() 
    return render(request, "clientes.html",  {"clientes": nova_busca})
    
def VerHacker(request):
    if request.method == "POST":
        nova_busca = HackerForm(request.POST)  
        if nova_busca.is_valid():
            nova_busca.save()
            return redirect("pg_hacker")
    else:
        nova_busca =HackerForm() 
    return render(request, "hacker.html",  {"hacker": nova_busca})

def VerServiço(request):
    if request.method == "POST":
        nova_busca = ServicoForm(request.POST)
        if nova_busca.is_valid():
            nova_busca.save()
            return redirect("pg_servicos")
    else:
        nova_busca = ServicoForm() 
    return render(request, "servicos.html",  {"servicos": nova_busca})
