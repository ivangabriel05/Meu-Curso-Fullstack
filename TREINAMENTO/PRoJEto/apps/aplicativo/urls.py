from django.urls import path
from .views import *

urlpatterns = [
    path("", VerIndex, name="pg_index"),
    path("hacker", VerHacker, name="pg_hacker"),
    path("clientes", VerClientes, name="pg_clientes"),
    path("servicos", VerServicos, name="pg_servicos")
    
]
