# funcionarios/views.py
from django.shortcuts import render
from .models import Funcionario, Aviso
import datetime

def homepage(request):
    # Pega a data de hoje
    data_hoje = datetime.date.today()

    # 2. Busque os 5 avisos mais recentes
    avisos = Aviso.objects.order_by('-data_publicacao')[:5]

    # Filtra os funcionários que fazem aniversário no mês atual
    aniversariantes_do_mes = Funcionario.objects.filter(data_nascimento__month=data_hoje.month)

    # Cria um "contexto" para enviar os dados para o HTML
    context = {
        'aniversariantes': aniversariantes_do_mes,
        'avisos': avisos,
    }

    print("--- INÍCIO DO DEBUG ---")
    print(aniversariantes_do_mes)
    print("--- FIM DO DEBUG ---")

    return render(request, 'funcionarios/homepage.html', context)