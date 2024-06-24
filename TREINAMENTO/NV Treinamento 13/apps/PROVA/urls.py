from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("Clientes/", Cliente, name="PG_1"),
    path("Usuarios/", Usuario, name="PG_2"),
    path("Compras/", Compra, name="PG_3")
]