from django.shortcuts import render, redirect
from .models import Aluno
from django.http import HttpResponse

def cadastro_aluno(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        
        # Cria um novo objeto Aluno e salva no banco de dados
        aluno = Aluno(nome=nome, estado=estado, cidade=cidade)
        aluno.save()
        
        return redirect('lista_alunos')  # Redireciona para a página de lista de alunos
    
    return render(request, 'cadastro_aluno.html')  # Renderiza o template de cadastro de aluno

def lista_alunos(request):
    alunos = Aluno.objects.all()  # Recupera todos os alunos do banco de dados
    return render(request, 'lista_alunos.html', {'alunos': alunos})

def editar_aluno(request, aluno_id):
    aluno = Aluno.objects.get(id=aluno_id)
    
    if request.method == 'POST':
        aluno.nome = request.POST.get('nome')
        aluno.estado = request.POST.get('estado')
        aluno.cidade = request.POST.get('cidade')
        aluno.save()
        
        return redirect('lista_alunos')
    
    return render(request, 'editar_aluno.html', {'aluno': aluno})

def excluir_aluno(request, aluno_id):
    aluno = Aluno.objects.get(id=aluno_id)
    
    if request.method == 'POST':
        aluno.delete()
        return redirect('lista_alunos')
    
    return render(request, 'excluir_aluno.html', {'aluno': aluno})

