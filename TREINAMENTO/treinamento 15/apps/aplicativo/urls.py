from django .urls import path 
from .views import *

urlpatterns = [
    path("", Verindex),
    path("Login", Verlogin),
    path("Produtos",Verprodutos)
]



