from django.urls import path
from .views import *

urlpatterns = [
    path("", PaginaInicial, name="pg_inicial"),
    path("Compras_arvores/", PaginaCompras, name="pg_Arvores"),
    path("Compras_plantas/", PaginaClientes, name="pg_Plantas")
]