from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

# Configuração do router para ViewSets
router = DefaultRouter()
router.register(r'usuarios', views.UserViewSet)
router.register(r'profissionais', views.ProfissionalViewSet)
router.register(r'clientes', views.ClienteViewSet)

app_name = 'core'

urlpatterns = [
    # Health check
    path('health/', views.health_check, name='health_check'),
    
    # Autenticação
    path('auth/register/', views.register_user, name='register_user'),
    path('auth/login/', views.login_user, name='login_user'),
    path('auth/logout/', views.logout_user, name='logout_user'),
    path('auth/token/', obtain_auth_token, name='obtain_auth_token'),
    
    # Perfil do usuário
    path('auth/profile/', views.user_profile, name='user_profile'),
    path('auth/profile/update/', views.update_user_profile, name='update_user_profile'),
    
    # Estatísticas (apenas para administradores)
    path('stats/users/', views.user_stats, name='user_stats'),
    
    # ViewSets
    path('', include(router.urls)),
] 