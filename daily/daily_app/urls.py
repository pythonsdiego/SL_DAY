from django.urls import path

from . import views

app_name = 'daily_app'

urlpatterns = [
    path('', views.index, name='index'),
    # & Página que mostra todos os tópicos:::
    path('topicos/', views.topicos, name='topicos'),
    # & Página de detalhes para um único tópico:::
    path('topicos/<int:topico_id>/', views.topico, name='topico'),
]