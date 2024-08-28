from django import forms
from .models import *

class FormularioProfessor(forms.ModelForm):
    class Meta:
        model =  professor 
        fields = '__all__'
        

class FormularioAluno(forms.ModelForm):
    class Meta:
        model =  aluno
        fields = '__all__'