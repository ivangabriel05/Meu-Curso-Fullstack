from django .urls import path
from .views import *

urlpatterns = [
    path("", pageInitical, name="pagina_inicial"),
    path("cadastro", pageCadastro, name="pagina_cadastro")
]