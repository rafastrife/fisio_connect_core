# Fisio Connect Core

API REST desenvolvida em Django com Django REST Framework para o sistema Fisio Connect.

## 🚀 Tecnologias

- **Python 3.13+**
- **Django 5.1.3**
- **Django REST Framework 3.15.2**
- **SQLite** (desenvolvimento)

## 📋 Pré-requisitos

- Python 3.13 ou superior
- pip (gerenciador de pacotes Python)
- Git

## 🔧 Instalação e Configuração

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd fisio_connect_core
```

### 2. Crie um ambiente virtual (recomendado)

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# No Linux/Mac:
source venv/bin/activate
# No Windows:
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto (opcional para desenvolvimento):

```bash
# Exemplo de arquivo .env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Execute as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crie um superusuário (opcional)

```bash
python manage.py createsuperuser
```

### 7. Execute o servidor de desenvolvimento

```bash
python manage.py runserver
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
│   ├── urls.py            # URLs principais
│   └── wsgi.py            # Configuração WSGI
├── manage.py              # Script de gerenciamento Django
├── requirements.txt       # Dependências do projeto
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

### Desenvolvimento

```bash
# Executar servidor de desenvolvimento
python manage.py runserver

# Executar servidor em porta específica
python manage.py runserver 8001

# Executar servidor em modo debug
python manage.py runserver --verbosity 2
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
python manage.py makemigrations
python manage.py migrate
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

- **Seu Nome** - *Desenvolvimento inicial* - [SeuGitHub](https://github.com/seugithub)

## 🙏 Agradecimentos

- Django Documentation
- Django REST Framework Documentation
- Comunidade Python/Django