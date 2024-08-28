from django .urls import path
from .views import * 

urlpatterns = [
    path("", Verindex ),
    path("Produtos", Verproduto ),
    path("Compras", Vercompra)
]