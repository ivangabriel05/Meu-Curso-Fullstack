from django.urls import path
from  apps.core import views

urlpatterns = [
    path("",views.paginaInicial, name="pagina_inicial"),
    path("/paginaSelecao", views.pagina_selecao, name="pagina_selecao"),
]