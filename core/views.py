from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, logout
from .serializers import (
    HealthCheckSerializer, UserSerializer, UserCreateSerializer, UserUpdateSerializer,
    ProfissionalSerializer, ProfissionalCreateSerializer,
    ClienteSerializer, ClienteCreateSerializer, LoginSerializer
)
from .models import User, Profissional, Cliente


# Create your views here.


@api_view(['GET'])
def health_check(request):
    """
    Endpoint para verificação de saúde da API
    """
    serializer = HealthCheckSerializer()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """
    Registro de usuários (profissionais ou clientes)
    """
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    """
    Login de usuários
    """
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    """
    Logout de usuários
    """
    logout(request)
    return Response({'message': 'Logout realizado com sucesso'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    """
    Perfil do usuário logado
    """
    serializer = UserSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    """
    Atualização do perfil do usuário logado
    """
    serializer = UserUpdateSerializer(request.user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciamento de usuários (apenas para administradores)
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return UserUpdateSerializer
        return UserSerializer


class ProfissionalViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciamento de profissionais
    """
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return ProfissionalCreateSerializer
        return ProfissionalSerializer
    
    def get_queryset(self):
        """
        Filtra profissionais ativos por padrão
        """
        queryset = Profissional.objects.filter(ativo=True)
        especialidade = self.request.query_params.get('especialidade', None)
        if especialidade:
            queryset = queryset.filter(especialidade__icontains=especialidade)
        return queryset


class ClienteViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciamento de clientes
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return ClienteCreateSerializer
        return ClienteSerializer
    
    def get_queryset(self):
        """
        Filtra clientes ativos por padrão
        """
        queryset = Cliente.objects.filter(ativo=True)
        return queryset


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_stats(request):
    """
    Estatísticas de usuários (apenas para administradores)
    """
    if not request.user.is_staff:
        return Response(
            {'error': 'Acesso negado'}, 
            status=status.HTTP_403_FORBIDDEN
        )
    
    total_users = User.objects.count()
    total_profissionais = Profissional.objects.filter(ativo=True).count()
    total_clientes = Cliente.objects.filter(ativo=True).count()
    
    return Response({
        'total_usuarios': total_users,
        'total_profissionais': total_profissionais,
        'total_clientes': total_clientes,
        'usuarios_ativos': User.objects.filter(is_active=True).count(),
        'usuarios_inativos': User.objects.filter(is_active=False).count(),
    }, status=status.HTTP_200_OK)
