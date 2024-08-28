from django.shortcuts import render

from django.shortcuts import render

def Verindex (request):
    return render(request, "index.html")

def Verproduto (request):
    return render(request, "produtos.html")

def Vercompra (request):
    return render(request, "compras.html")

