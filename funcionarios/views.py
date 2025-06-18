# funcionarios/views.py
from django.shortcuts import render
from .models import Funcionario, Aviso
import datetime
from django.contrib.auth.decorators import login_required

@login_required 
def homepage(request):
    # Pega a data de hoje
    data_hoje = datetime.date.today()

    # Busque os 5 avisos mais recentes
    avisos = Aviso.objects.order_by('-data_publicacao')[:5]

    # Filtra os funcionários que fazem aniversário no mês atual
    aniversariantes_do_mes = Funcionario.objects.filter(data_nascimento__month=data_hoje.month)

    # Cria um "contexto" para enviar os dados para o HTML
    context = {
        'aniversariantes': aniversariantes_do_mes,
        'avisos': avisos,
    }

    return render(request, 'funcionarios/homepage.html', context)

@login_required  # <--- AJUSTE 1: Adicionamos o segurança aqui também
def quadro_funcionarios(request):
    # Busca TODOS os funcionários e ordena por nome
    todos_os_funcionarios = Funcionario.objects.all().order_by('nome_completo')

    context = {
        'funcionarios': todos_os_funcionarios
    }

    # AJUSTE 2: Esta linha agora está indentada corretamente (com 4 espaços)
    return render(request, 'funcionarios/quadro_funcionarios.html', context)