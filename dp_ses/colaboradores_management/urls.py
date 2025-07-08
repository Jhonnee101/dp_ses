# colaboradores_management/urls.py
from django.urls import path
from . import views

app_name = 'colaboradores'

urlpatterns = [
  path('',               views.ColaboradorListView.as_view(),   name='list'),
  path('novo/',          views.ColaboradorCreateView.as_view(), name='create'),
  path('<int:pk>/editar/', views.ColaboradorUpdateView.as_view(), name='update'),
  path('<int:pk>/excluir/', views.ColaboradorDeleteView.as_view(), name='delete'),
]
