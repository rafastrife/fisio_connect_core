from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profissional, Cliente


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Admin customizado para o modelo User
    """
    list_display = ('username', 'email', 'nome', 'sobrenome', 'tipo_usuario', 
                   'cpf', 'is_active', 'criado_em')
    list_filter = ('tipo_usuario', 'sexo', 'is_active', 'is_staff', 'criado_em')
    search_fields = ('username', 'email', 'nome', 'sobrenome', 'cpf')
    ordering = ('nome', 'sobrenome')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {
            'fields': ('nome', 'sobrenome', 'email', 'tipo_usuario', 'sexo', 'cpf',
                      'data_nascimento', 'telefone', 'endereco')
        }),
        ('Permissões', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'nome', 'sobrenome',
                      'tipo_usuario', 'sexo', 'cpf', 'data_nascimento', 'telefone', 'endereco'),
        }),
    )


@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    """
    Admin para o modelo Profissional
    """
    list_display = ('usuario', 'registro_profissional', 'especialidade', 
                   'experiencia_anos', 'clinica', 'ativo')
    list_filter = ('ativo', 'especialidade', 'experiencia_anos')
    search_fields = ('usuario__nome', 'usuario__sobrenome', 'registro_profissional', 
                    'especialidade', 'clinica')
    ordering = ('usuario__nome', 'usuario__sobrenome')
    
    fieldsets = (
        ('Usuário', {
            'fields': ('usuario',)
        }),
        ('Dados Profissionais', {
            'fields': ('registro_profissional', 'especialidade', 'formacao', 'experiencia_anos')
        }),
        ('Dados de Trabalho', {
            'fields': ('clinica', 'horario_atendimento')
        }),
        ('Status', {
            'fields': ('ativo',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('usuario')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    """
    Admin para o modelo Cliente
    """
    list_display = ('usuario', 'responsavel', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('usuario__nome', 'usuario__sobrenome', 'responsavel')
    ordering = ('usuario__nome', 'usuario__sobrenome')
    
    fieldsets = (
        ('Usuário', {
            'fields': ('usuario',)
        }),
        ('Dados Pessoais', {
            'fields': ('responsavel', 'observacoes')
        }),
        ('Dados Médicos', {
            'fields': ('historico_medico', 'alergias', 'medicamentos')
        }),
        ('Status', {
            'fields': ('ativo',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('usuario')
