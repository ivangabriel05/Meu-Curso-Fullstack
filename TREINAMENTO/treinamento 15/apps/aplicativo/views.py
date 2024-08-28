from django.shortcuts import render

def Verindex (request):
    return render(request, "index.html")

def Verlogin (request):
    return render(request, "login.html")

def Verprodutos (request):
    return render(request, "produtos.html")
