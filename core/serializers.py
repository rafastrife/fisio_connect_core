from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Profissional, Cliente


class HealthCheckSerializer(serializers.Serializer):
    """
    Serializer para verificação de saúde da API
    """
    status = serializers.CharField(default="ok")
    message = serializers.CharField(default="API is running")


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo User
    """
    nome_completo = serializers.ReadOnlyField()
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'nome', 'sobrenome', 'nome_completo',
            'tipo_usuario', 'sexo', 'cpf', 'data_nascimento', 'telefone',
            'endereco', 'criado_em', 'atualizado_em', 'is_active'
        ]
        read_only_fields = ['id', 'criado_em', 'atualizado_em']


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer para criação de usuários
    """
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password', 'password_confirmation',
            'nome', 'sobrenome', 'tipo_usuario', 'sexo', 'cpf',
            'data_nascimento', 'telefone', 'endereco'
        ]
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError("As senhas não coincidem.")
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer para atualização de usuários
    """
    class Meta:
        model = User
        fields = [
            'email', 'nome', 'sobrenome', 'sexo', 'data_nascimento',
            'telefone', 'endereco'
        ]


class ProfissionalSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Profissional
    """
    usuario = UserSerializer(read_only=True)
    nome_completo = serializers.ReadOnlyField()
    
    class Meta:
        model = Profissional
        fields = [
            'id', 'usuario', 'nome_completo', 'registro_profissional',
            'especialidade', 'formacao', 'experiencia_anos', 'clinica',
            'horario_atendimento', 'ativo'
        ]
        read_only_fields = ['id']


class ProfissionalCreateSerializer(serializers.ModelSerializer):
    """
    Serializer para criação de profissionais
    """
    usuario = UserCreateSerializer()
    
    class Meta:
        model = Profissional
        fields = ['usuario', 'registro_profissional', 'especialidade', 
                 'formacao', 'experiencia_anos', 'clinica', 'horario_atendimento']
    
    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = UserCreateSerializer().create(usuario_data)
        profissional = Profissional.objects.create(usuario=usuario, **validated_data)
        return profissional


class ClienteSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Cliente
    """
    usuario = UserSerializer(read_only=True)
    nome_completo = serializers.ReadOnlyField()
    
    class Meta:
        model = Cliente
        fields = [
            'id', 'usuario', 'nome_completo', 'responsavel', 'observacoes',
            'historico_medico', 'alergias', 'medicamentos', 'ativo'
        ]
        read_only_fields = ['id']


class ClienteCreateSerializer(serializers.ModelSerializer):
    """
    Serializer para criação de clientes
    """
    usuario = UserCreateSerializer()
    
    class Meta:
        model = Cliente
        fields = ['usuario', 'responsavel', 'observacoes', 'historico_medico',
                 'alergias', 'medicamentos']
    
    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = UserCreateSerializer().create(usuario_data)
        cliente = Cliente.objects.create(usuario=usuario, **validated_data)
        return cliente


class LoginSerializer(serializers.Serializer):
    """
    Serializer para autenticação
    """
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError('Credenciais inválidas.')
            if not user.is_active:
                raise serializers.ValidationError('Usuário desativado.')
            attrs['user'] = user
        else:
            raise serializers.ValidationError('Username e password são obrigatórios.')
        
        return attrs 