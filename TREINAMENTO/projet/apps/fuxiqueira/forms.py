from django import forms
from .models import *

class sensibilidade(forms.ModelForm):
    class Meta:
        model = freefire
        fields = '__all__'