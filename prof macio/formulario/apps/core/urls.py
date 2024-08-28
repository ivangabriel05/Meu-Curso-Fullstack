from django.urls import path
from .views import aluno_list, adicionar_aluno

urlpatterns = [
    path('', aluno_list, name='aluno_list'),
    path('adicionar/', adicionar_aluno, name='adicionar_aluno'),
]