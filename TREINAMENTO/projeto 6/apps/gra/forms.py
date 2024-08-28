from django import forms
from .models import *

class FormularioEncomenda(forms.ModelForm):
    class Meta:
        model = encomendas
        fields = '__all__'