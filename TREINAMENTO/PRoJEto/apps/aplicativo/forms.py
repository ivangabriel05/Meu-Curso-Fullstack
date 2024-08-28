from django import forms
from .models import *

class CompraForm(forms.ModelForm):
    class Meta:
        model = serviço
        fields = '__all__'

class CompraForm(forms.ModelForm):
    class Meta:
        model = hacker
        fields = '__all__'

class CompraForm(forms.ModelForm):
    class Meta:
        model = clinte
        fields = '__all__'