from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    """
    Modelo de usuário customizado para o sistema Fisio Connect
    """
    TIPO_USUARIO_CHOICES = [
        ('profissional', 'Profissional'),
        ('cliente', 'Cliente'),
    ]
    
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    
    # Campos básicos
    nome = models.CharField(max_length=100, verbose_name="Nome")
    sobrenome = models.CharField(max_length=100, verbose_name="Sobrenome")
    tipo_usuario = models.CharField(
        max_length=20, 
        choices=TIPO_USUARIO_CHOICES,
        verbose_name="Tipo de Usuário"
    )
    sexo = models.CharField(
        max_length=1,
        choices=SEXO_CHOICES,
        verbose_name="Sexo"
    )
    
    # Documentos
    cpf = models.CharField(
        max_length=14,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
                message='CPF deve estar no formato: 000.000.000-00'
            )
        ],
        verbose_name="CPF"
    )
    
    # Campos adicionais
    data_nascimento = models.DateField(null=True, blank=True, verbose_name="Data de Nascimento")
    telefone = models.CharField(max_length=15, blank=True, verbose_name="Telefone")
    endereco = models.TextField(blank=True, verbose_name="Endereço")
    
    # Campos de auditoria
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ['nome', 'sobrenome']
    
    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
    
    @property
    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"
    
    @property
    def is_profissional(self):
        return self.tipo_usuario == 'profissional'
    
    @property
    def is_cliente(self):
        return self.tipo_usuario == 'cliente'


class Profissional(models.Model):
    """
    Modelo específico para profissionais (fisioterapeutas)
    """
    usuario = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name='profissional',
        verbose_name="Usuário"
    )
    
    # Dados profissionais
    registro_profissional = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Registro Profissional"
    )
    especialidade = models.CharField(max_length=100, blank=True, verbose_name="Especialidade")
    formacao = models.TextField(blank=True, verbose_name="Formação")
    experiencia_anos = models.PositiveIntegerField(default=0, verbose_name="Anos de Experiência")
    
    # Dados de trabalho
    clinica = models.CharField(max_length=200, blank=True, verbose_name="Clínica")
    horario_atendimento = models.TextField(blank=True, verbose_name="Horário de Atendimento")
    
    # Status
    ativo = models.BooleanField(default=True, verbose_name="Ativo")
    
    class Meta:
        verbose_name = "Profissional"
        verbose_name_plural = "Profissionais"
    
    def __str__(self):
        return f"Dr(a). {self.usuario.nome_completo}"
    
    @property
    def nome_completo(self):
        return self.usuario.nome_completo


class Cliente(models.Model):
    """
    Modelo específico para clientes (pessoas físicas)
    """
    usuario = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name='cliente',
        verbose_name="Usuário"
    )
    
    # Dados pessoais
    responsavel = models.CharField(max_length=200, blank=True, verbose_name="Responsável")
    observacoes = models.TextField(blank=True, verbose_name="Observações")
    
    # Dados médicos
    historico_medico = models.TextField(blank=True, verbose_name="Histórico Médico")
    alergias = models.TextField(blank=True, verbose_name="Alergias")
    medicamentos = models.TextField(blank=True, verbose_name="Medicamentos em Uso")
    
    # Status
    ativo = models.BooleanField(default=True, verbose_name="Ativo")
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    
    def __str__(self):
        return self.usuario.nome_completo
    
    @property
    def nome_completo(self):
        return self.usuario.nome_completo
