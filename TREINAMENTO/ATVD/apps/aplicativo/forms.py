from django import forms
from .models import *

class CompraForm(forms.ModelForm):
    class Meta:
        model = compras
        fields = '__all__'