from django.urls import path
from . import views

app_name = "tarefas"

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("home/", views.home, name='home'),
    path('cadastrar_colaborador/', views.cadastrar_colaborador, name='cadastrar_colaborador'),
    path('colaboradores/', views.listar_colaboradores, name='listar_colaboradores'),
    path('colaboradores/editar/<int:id>/', views.editar_colaborador, name='editar_colaborador'),
]


