from django.shortcuts import render
from .models import produtos
def VerProdutos(request):
    produtos_lista = produtos.objects.all()
    return render(request, 'index.html', {'produtos': produtos_lista})

# Create your views here.
