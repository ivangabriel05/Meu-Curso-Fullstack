from django .urls import path
from .views import *

urlpatterns = [
    path("",pageIndex, name="pagina_inicial"),
    path("compras",compras , name="pagina_compras")
]