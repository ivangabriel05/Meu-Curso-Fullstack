from django.shortcuts import render
from django.http import HttpResponse

def oi(request):
    return HttpResponse("Olá mundo!!!")

def salve(request):
    return HttpResponse("Olá tudo bem?")

def saudacao(request):
    return render(request, 'ola_mundo.html')

def paga(request):
    return render(request, 'novohtml.html')

def cell(request):
    return render(request, 'htmlnovo.html')

# Create your views here.
