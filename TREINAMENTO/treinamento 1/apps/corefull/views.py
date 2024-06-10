from django.shortcuts import render
from django.http import HttpResponse

def saudacao(request):
    return HttpResponse("olá mundo!!!")

def chamada(request):
    return HttpResponse("olá, tudo bem? ")

def celular(request):
    return HttpResponse("ai nobru")
# Create your views here.


