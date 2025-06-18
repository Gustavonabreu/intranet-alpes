# funcionarios/views.py
from django.shortcuts import render
from .models import Funcionario
import datetime

def homepage(request):
    # Pega a data de hoje
    data_hoje = datetime.date.today()

    # Filtra os funcionários que fazem aniversário no mês atual
    aniversariantes_do_mes = Funcionario.objects.filter(data_nascimento__month=data_hoje.month)

    # Cria um "contexto" para enviar os dados para o HTML
    context = {
        'aniversariantes': aniversariantes_do_mes,
    }

    return render(request, 'funcionarios/homepage.html', context)