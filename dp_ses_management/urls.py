from django.urls import path
from . import views

app_name = "tarefas"

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("home/", views.home, name='home'),
    path('cadastrar_colaborador/', views.cadastrar_colaborador, name='cadastrar_colaborador'),
    path("adicionar/", views.tarefas_adicionar, name="adicionar"),
    path("remover/<int:id>", views.tarefas_remover, name="remover")
    
]
