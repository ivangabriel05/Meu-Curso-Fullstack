from django.contrib import admin
from .models import Item
from .models import clients

admin.site.register(Item)
admin.site.register(clients)
