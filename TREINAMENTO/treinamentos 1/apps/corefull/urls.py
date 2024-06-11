from django.urls import path
from .views import *

urlpatterns = [
    path('apresentacao/', saudacao),
    path('chamada/', chamada),
    path('celular/', celular)
]

