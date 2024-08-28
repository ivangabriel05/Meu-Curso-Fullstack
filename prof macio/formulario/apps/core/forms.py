from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'estado', 'municipio']

    def __init__(self, *args, **kwargs):
        # Adiciona as opções dinâmicas para estados e municípios
        estados = kwargs.pop('estados', [])
        municipios = kwargs.pop('municipios', [])
        super().__init__(*args, **kwargs)
        self.fields['estado'].choices = estados
        self.fields['municipio'].choices = municipios
