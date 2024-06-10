from django.urls import path
from .views import *

urlpatterns = [
    path('apresentacao/', saudacao),
    path('novohtml/', paga),
    path('htmlnovo/', cell)
]
