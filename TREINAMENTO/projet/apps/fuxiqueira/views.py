from django.shortcuts import render, redirect
from .models import *
from .forms import *

def pageInitical(request):
    busca_nick = freefire.objects.all()
    return render(request, "index.html", {"pack": busca_nick})

def pageCadastro(request):
    if request.method == "POST":
        nova_sensi = sensibilidade(request.POST)
        if nova_sensi.is_valid():
            nova_sensi.save()
            return redirect("pagina_inicial")
    else:
        nova_sensi= sensibilidade()
    
    return render(request, "cadastro.html", {"formulario": nova_sensi})