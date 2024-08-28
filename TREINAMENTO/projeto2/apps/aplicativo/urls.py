from django.urls import path
from .views import *

urlpatterns = [
    path("",  pageIndex, name = "pg_index"),
    path("clientes", Vercliente, name = "pg_clientes"),
    path("hacker", VerHacker, name = "pg_hacker"),
    path("servicos", VerServiço, name = "pg_servicos")
]
