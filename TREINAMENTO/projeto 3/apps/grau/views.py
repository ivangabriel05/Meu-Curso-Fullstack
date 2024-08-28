from django.shortcuts import render

def Verindex (request):
    return render(request, "index.html")

def Verprodutos (request):
    return render(request, "produtos.html")

def Vervendas (request):
    return render(request, "vendas.html")

