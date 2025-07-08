# dp_ses/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from colaboradores_management import views as app_views

app_name = 'dp_ses'  # ← ESSA LINHA REGISTRA O NAMESPACE!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',  auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', app_views.dashboard_view, name='dashboard'),

    path('colaboradores/', include(('colaboradores_management.urls', 'colaboradores_management'), namespace='colaboradores')),
]
