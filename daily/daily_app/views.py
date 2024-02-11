from django.shortcuts import render

from .models import Topico

def index(request):
    """A página do SL Daily Logs."""
    return render(request, 'daily_app/index.xhtml')

def topicos(request):
    # & Mostra todos os tópicos:::
    topicos = Topico.objects.order_by('criado_em')
    contexto = {'topicos': topicos}
    return render(request, 'daily_app/topicos.xhtml', contexto)

def topico(request, topico_id):
    """Mostra um único tópico e todas as suas entradas."""
    topico = Topico.objects.get(id=topico_id)
    entradas = topico.entrada_set.order_by('-criado_em')
    contexto = {'topico': topico, 'entradas': entradas}
    return render(request, 'daily_app/topico.xhtml', contexto)