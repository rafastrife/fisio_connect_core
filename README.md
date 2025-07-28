# Fisio Connect Core

API REST desenvolvida em Django com Django REST Framework para o sistema Fisio Connect.

## 🚀 Tecnologias

- **Python 3.13+**
- **Django 5.1.3**
- **Django REST Framework 3.15.2**
- **PostgreSQL 15** (via Docker)
- **PgAdmin 4** (interface web para PostgreSQL)

## 📋 Pré-requisitos

- Python 3.13 ou superior
- pip (gerenciador de pacotes Python)
- Git
- Docker e Docker Compose (para PostgreSQL)

## 🔧 Instalação e Configuração

### Opção 1: Setup Rápido (Recomendado)

```bash
# Clone o repositório
git clone <url-do-repositorio>
cd fisio_connect_core

# Setup completo com PostgreSQL
make setup-dev

# Ou setup completo com SQLite
make setup
```

### Opção 2: Setup Manual

#### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd fisio_connect_core
```

#### 2. Crie um ambiente virtual (recomendado)

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# No Linux/Mac:
source venv/bin/activate
# No Windows:
venv\Scripts\activate
```

#### 3. Instale as dependências

```bash
make install
# ou
pip install -r requirements.txt
```

### 4. Configure o PostgreSQL com Docker

```bash
# Iniciar containers do PostgreSQL e PgAdmin
make docker-start

# Verificar status dos containers
make docker-status
```

**Acesso ao PgAdmin:**
- URL: http://localhost:8080
- Email: admin@fisioconnect.com
- Senha: admin123

### 5. Configure as variáveis de ambiente

Copie o arquivo de exemplo e configure suas variáveis:

```bash
cp env.example .env
# Edite o arquivo .env conforme necessário
```

### 6. Execute as migrações

```bash
# Para usar PostgreSQL (recomendado)
make migrate-dev

# Para usar SQLite (alternativo)
make migrate
```

### 7. Crie um superusuário (opcional)

```bash
python manage.py createsuperuser
```

### 8. Execute o servidor de desenvolvimento

```bash
# Para usar PostgreSQL
make run-dev

# Para usar SQLite (padrão)
make run
```

O servidor estará disponível em: http://localhost:8000

## 📚 Estrutura do Projeto

```
fisio_connect_core/
├── core/                    # App principal
│   ├── migrations/         # Migrações do banco de dados
│   ├── __init__.py
│   ├── admin.py           # Configuração do admin Django
│   ├── apps.py            # Configuração do app
│   ├── models.py          # Modelos de dados
│   ├── serializers.py     # Serializers do DRF
│   ├── tests.py           # Testes
│   ├── urls.py            # URLs do app
│   └── views.py           # Views da API
├── fisio_connect_core/     # Configurações do projeto
│   ├── __init__.py
│   ├── settings.py        # Configurações do Django
│   ├── settings_dev.py    # Configurações para desenvolvimento
│   ├── urls.py            # URLs principais
│   └── wsgi.py            # Configuração WSGI
├── manage.py              # Script de gerenciamento Django
├── Makefile               # Comandos de automação
├── docker-compose.yml     # Configuração do Docker Compose
├── requirements.txt       # Dependências do projeto
├── env.example           # Exemplo de variáveis de ambiente
├── .gitignore            # Arquivos ignorados pelo Git
└── README.md             # Este arquivo
```

## 🔌 Endpoints da API

### Health Check
- **URL:** `GET /api/health/`
- **Descrição:** Verificação de saúde da API
- **Resposta:**
```json
{
    "status": "ok",
    "message": "API is running"
}
```

### Admin Django
- **URL:** `GET /admin/`
- **Descrição:** Interface administrativa do Django

## 🛠️ Comandos Úteis

### Setup Rápido

```bash
# Ver todos os comandos disponíveis
make help

# Setup completo com PostgreSQL
make setup-dev

# Setup completo com SQLite
make setup

# Ambiente completo de desenvolvimento
make dev
```

### Docker

```bash
# Iniciar containers
make docker-start

# Parar containers
make docker-stop

# Reiniciar containers
make docker-restart

# Ver logs dos containers
make docker-logs

# Ver status dos containers
make docker-status

# Limpar containers e volumes
make docker-clean
```

### Desenvolvimento

```bash
# Executar servidor de desenvolvimento com PostgreSQL
make run-dev

# Executar servidor de desenvolvimento com SQLite
make run

# Executar testes
make test

# Abrir shell Django
make shell-dev  # PostgreSQL
make shell      # SQLite

# Criar superusuário
make superuser-dev  # PostgreSQL
make superuser      # SQLite
```

### Banco de Dados

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Ver status das migrações
python manage.py showmigrations

# Resetar banco de dados (cuidado!)
python manage.py flush
```

### Testes

```bash
# Executar todos os testes
python manage.py test

# Executar testes de um app específico
python manage.py test core

# Executar testes com verbosidade
python manage.py test --verbosity 2
```

### Shell Django

```bash
# Abrir shell interativo
python manage.py shell

# Abrir shell com contexto
python manage.py shell_plus  # Requer django-extensions
```

## 🔒 Configurações de Segurança

### Para Produção

1. **Altere a SECRET_KEY:**
   ```python
   # Em settings.py
   SECRET_KEY = 'sua-chave-secreta-muito-segura'
   ```

2. **Configure DEBUG=False:**
   ```python
   DEBUG = False
   ```

3. **Configure ALLOWED_HOSTS:**
   ```python
   ALLOWED_HOSTS = ['seu-dominio.com', 'www.seu-dominio.com']
   ```

4. **Configure HTTPS:**
   ```python
   SECURE_SSL_REDIRECT = True
   SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
   ```

## 📝 Adicionando Novos Endpoints

### 1. Crie um modelo em `core/models.py`

```python
from django.db import models

class Exemplo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
```

### 2. Crie um serializer em `core/serializers.py`

```python
from rest_framework import serializers
from .models import Exemplo

class ExemploSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exemplo
        fields = '__all__'
```

### 3. Crie uma view em `core/views.py`

```python
from rest_framework import viewsets
from .models import Exemplo
from .serializers import ExemploSerializer

class ExemploViewSet(viewsets.ModelViewSet):
    queryset = Exemplo.objects.all()
    serializer_class = ExemploSerializer
```

### 4. Adicione a URL em `core/urls.py`

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'exemplos', views.ExemploViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # ... outras URLs
]
```

### 5. Execute as migrações

```bash
# Para PostgreSQL
make migrate-dev

# Para SQLite
make migrate
```

## 🛠️ Comandos Makefile

O projeto usa um `Makefile` para facilitar o desenvolvimento. Execute `make help` para ver todos os comandos disponíveis.

### Comandos Principais

```bash
# Ver todos os comandos
make help

# Setup completo
make setup-dev    # PostgreSQL
make setup        # SQLite

# Desenvolvimento
make run-dev      # Servidor com PostgreSQL
make run          # Servidor com SQLite
make test         # Executar testes
make shell-dev    # Shell Django (PostgreSQL)
make shell        # Shell Django (SQLite)

# Docker
make docker-start # Iniciar containers
make docker-stop  # Parar containers
make docker-logs  # Ver logs

# Manutenção
make clean        # Limpar arquivos temporários
make backup       # Backup do banco
make restore FILE=backup.json  # Restaurar backup
```

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Autores

- **Rafaell Santana** - *Desenvolvimento inicial* - [SeuGitHub](https://github.com/rafastrife)

## 🙏 Agradecimentos

- Django Documentation
- Django REST Framework Documentation
- Comunidade Python/Django