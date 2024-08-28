from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro_aluno, name='cadastro_aluno'),
    path('alunos/', views.lista_alunos, name='lista_alunos'),
    path('aluno/editar/<int:aluno_id>/', views.editar_aluno, name='editar_aluno'),
    path('aluno/excluir/<int:aluno_id>/', views.excluir_aluno, name='excluir_aluno'),
]
