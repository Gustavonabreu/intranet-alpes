# funcionarios/admin.py

from django.contrib import admin
from .models import Funcionario, Aviso

admin.site.register(Funcionario)
admin.site.register(Aviso)