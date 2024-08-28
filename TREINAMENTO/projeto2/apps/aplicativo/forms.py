from django import forms
from .models import *


class HackerForm(forms.ModelForm):
    class Meta:
        model = hacker
        fields = '__all__'

class ClientesForm(forms.ModelForm):
    class Meta:
        model = clientes
        fields = '__all__'
        
class ServicoForm(forms.ModelForm):
    class Meta:
        model = servico
        fields = '__all__'