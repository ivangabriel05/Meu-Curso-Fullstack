from django .urls import path 
from .views import *

urlpatterns = [
    path("", Verindex),
    path("Login", Vervendas),
    path("Produtos",Verprodutos)
]