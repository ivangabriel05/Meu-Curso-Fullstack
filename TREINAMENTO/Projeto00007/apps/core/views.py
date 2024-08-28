from django.shortcuts import render, redirect
from .models import*
from .forms import*

def paginaInicial(request):
    busca_selecao = professor.objects.all()
    return render(request,'index.html',{"professores":busca_selecao})


def pagina_selecao(request):
    if request.method == "GET":
        nova_selecao = FormularioProfessor() 
    else:
        form_preenchido =FormularioProfessor (request.POST,request.FILES)
        if form_preenchido.is_valid():
            form_preenchido.save()
            return redirect("pagina_selecao")
   
   
    return redirect(request, "pagina_selecao.html",{"formulario":nova_selecao})


