from django.shortcuts import render, redirect
from .models import *
from .forms import *

def pageIndex(request):
    busca_compras = compras.objects.all()
    return render(request, "index.html", {"lista": busca_compras })

def Vercliente(request):
    if request.method == "POST":
        nova_busca = CompraForm(request.POST)  
        if nova_busca.is_valid():
            nova_busca.save()
            return redirect("pagina_inicial")
    else:
        nova_busca =CompraForm () 
    
        return render(request, "clientes.html",  {"clientes": nova_busca})
    
def VerHacker(request):
    if request.method == "POST":
        nova_busca = CompraForm(request.POST)  
        if nova_busca.is_valid():
            nova_busca.save()
            return redirect("pagina_inicial")
    else:
        nova_busca =CompraForm () 
    
        return render(request, "hacker.html",  {"hacker": nova_busca})

def VerServiço(request):
    if request.method == "POST":
        nova_busca = CompraForm(request.POST)  
        if nova_busca.is_valid():
            nova_busca.save()
            return redirect("pagina_inicial")
    else:
        nova_busca =CompraForm () 
    
        return render(request, "servicos.html",  {"servicos": nova_busca})