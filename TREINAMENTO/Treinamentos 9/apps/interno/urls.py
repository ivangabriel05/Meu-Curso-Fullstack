from django.urls import path
from .views import *

urlpatterns = [
    path("", PaginaInicial, name="pg_inicial"),
    path("pacientes/", PaginaPacientes, name="pg_pacientes"),
    path("doutores/", PaginaDoutores, name="pg_doutores")
]
