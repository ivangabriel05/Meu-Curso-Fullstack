from django .urls import path
from .views import *

urlpatterns = [
    path("", pageInicial, name="pagina_inicial")
]
