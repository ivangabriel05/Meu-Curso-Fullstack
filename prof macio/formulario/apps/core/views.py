import requests
from django.shortcuts import render, redirect
from .models import Aluno
from .forms import AlunoForm

def obter_estados_municipios():
    # Obtendo estados
    estados_response = requests.get("https://brasilapi.com.br/api/v2/ufs")
    estados_data = estados_response.json()
    estados = [(estado['sigla'], estado['nome']) for estado in estados_data if estado['sigla'] in ['PI', 'MA']]

    # Obtendo municípios dos estados especificados
    municipios = {}
    for estado_sigla in ['PI', 'MA']:
        municipios_response = requests.get(f"https://brasilapi.com.br/api/v2/municipios?uf={estado_sigla}")
        municipios_data = municipios_response.json()
        municipios[estado_sigla] = [(municipio['ibge_id'], municipio['nome']) for municipio in municipios_data]

    return estados, municipios

def aluno_list(request):
    estados, municipios = obter_estados_municipios()
    
    if request.method == 'POST':
        if 'delete' in request.POST:
            aluno_id = request.POST.get('delete')
            aluno = Aluno.objects.get(id=aluno_id)
            aluno.delete()
            return redirect('aluno_list')

    alunos = Aluno.objects.all()
    form = AlunoForm(estados=estados)
    return render(request, 'index.html', {'alunos': alunos, 'form': form})

def adicionar_aluno(request):
    estados, municipios = obter_estados_municipios()
    
    if request.method == 'POST':
        form = AlunoForm(request.POST, estados=estados)
        if form.is_valid():
            form.save()
            return redirect('aluno_list')
    else:
        form = AlunoForm(estados=estados)

    return render(request, 'index.html', {'form': form})
