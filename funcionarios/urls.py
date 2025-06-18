# funcionarios/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views # Importe as views de autenticação

urlpatterns = [
    path('', views.homepage, name='homepage'),
    # URL de Login
    path('login/', auth_views.LoginView.as_view(template_name='funcionarios/login.html'), name='login'),
    # URL de Logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('quadro/', views.quadro_funcionarios, name='quadro_funcionarios'),
]