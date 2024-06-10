from django.shortcuts import render
from .models import compras

def VerCompras(request):
    produtos_lista = compras.objects.all()
    return render(request, 'index.html', {'produtos': produtos_lista})

# Create your views here.
