from rest_framework import serializers
from apps.core.models import clients

class PostSerializer(serializers.ModelSerializer):
 class Meta:
    model = clients
    fields = ["name", "cpf_cnpj", "rg_ie", "zip_code", "address", "neighborhood", "number", "city", "state" ]
