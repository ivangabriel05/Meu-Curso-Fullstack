from django.shortcuts import render
from .models import *

def VerProdutos(request):
    produtos_lista = jogo.objects.all()
    return render(request, "lista_produtos.html", {"produtos": produtos_lista})

def DetalhesProduto(request, id_produto):
    busca = jogo.objects.get(id=id_produto)
    return render(request, "detalhes_produto.html", {"produtos": busca})