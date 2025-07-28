# Makefile para Fisio Connect Core
# Comandos disponíveis: make help

.PHONY: help install migrate run run-dev test clean docker-start docker-stop docker-restart docker-logs docker-status docker-clean

# Variáveis
PYTHON = python
MANAGE = $(PYTHON) manage.py
DOCKER_COMPOSE = docker-compose

# Cores para output
GREEN = \033[0;32m
YELLOW = \033[1;33m
RED = \033[0;31m
NC = \033[0m # No Color

help: ## Mostra esta ajuda
	@echo "$(GREEN)Fisio Connect Core - Comandos disponíveis:$(NC)"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "$(YELLOW)%-20s$(NC) %s\n", $$1, $$2}'

install: ## Instala as dependências do projeto
	@echo "$(GREEN)📦 Instalando dependências...$(NC)"
	$(PYTHON) -m pip install -r requirements.txt

migrate: ## Executa as migrações do banco de dados
	@echo "$(GREEN)🗄️ Executando migrações...$(NC)"
	$(MANAGE) makemigrations
	$(MANAGE) migrate

migrate-dev: ## Executa migrações com configurações de desenvolvimento
	@echo "$(GREEN)🗄️ Executando migrações (PostgreSQL)...$(NC)"
	$(MANAGE) makemigrations --settings=fisio_connect_core.settings_dev
	$(MANAGE) migrate --settings=fisio_connect_core.settings_dev

run: ## Inicia o servidor de desenvolvimento (SQLite)
	@echo "$(GREEN)🚀 Iniciando servidor Django (SQLite)...$(NC)"
	$(MANAGE) runserver

run-dev: ## Inicia o servidor de desenvolvimento (PostgreSQL)
	@echo "$(GREEN)🚀 Iniciando servidor Django (PostgreSQL)...$(NC)"
	$(MANAGE) runserver --settings=fisio_connect_core.settings_dev

test: ## Executa os testes
	@echo "$(GREEN)🧪 Executando testes...$(NC)"
	$(MANAGE) test

test-verbose: ## Executa os testes com verbosidade
	@echo "$(GREEN)🧪 Executando testes (verbose)...$(NC)"
	$(MANAGE) test --verbosity=2

shell: ## Abre o shell do Django
	@echo "$(GREEN)🐍 Abrindo shell Django...$(NC)"
	$(MANAGE) shell

shell-dev: ## Abre o shell do Django (PostgreSQL)
	@echo "$(GREEN)🐍 Abrindo shell Django (PostgreSQL)...$(NC)"
	$(MANAGE) shell --settings=fisio_connect_core.settings_dev

superuser: ## Cria um superusuário
	@echo "$(GREEN)👤 Criando superusuário...$(NC)"
	$(MANAGE) createsuperuser

superuser-dev: ## Cria um superusuário (PostgreSQL)
	@echo "$(GREEN)👤 Criando superusuário (PostgreSQL)...$(NC)"
	$(MANAGE) createsuperuser --settings=fisio_connect_core.settings_dev

clean: ## Limpa arquivos temporários
	@echo "$(GREEN)🧹 Limpando arquivos temporários...$(NC)"
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage

# Comandos Docker
docker-start: ## Inicia os containers Docker (PostgreSQL + PgAdmin)
	@echo "$(GREEN)🐳 Iniciando containers Docker...$(NC)"
	$(DOCKER_COMPOSE) up -d
	@echo "$(GREEN)✅ Containers iniciados!$(NC)"
	@echo "$(YELLOW)📊 PostgreSQL: localhost:5432$(NC)"
	@echo "$(YELLOW)🌐 PgAdmin: http://localhost:8080$(NC)"
	@echo "$(YELLOW)   Email: admin@fisioconnect.com$(NC)"
	@echo "$(YELLOW)   Senha: admin123$(NC)"

docker-stop: ## Para os containers Docker
	@echo "$(GREEN)🛑 Parando containers Docker...$(NC)"
	$(DOCKER_COMPOSE) down
	@echo "$(GREEN)✅ Containers parados!$(NC)"

docker-restart: ## Reinicia os containers Docker
	@echo "$(GREEN)🔄 Reiniciando containers Docker...$(NC)"
	$(DOCKER_COMPOSE) restart
	@echo "$(GREEN)✅ Containers reiniciados!$(NC)"

docker-logs: ## Mostra os logs dos containers
	@echo "$(GREEN)📋 Logs dos containers:$(NC)"
	$(DOCKER_COMPOSE) logs -f

docker-status: ## Mostra o status dos containers
	@echo "$(GREEN)📊 Status dos containers:$(NC)"
	$(DOCKER_COMPOSE) ps

docker-clean: ## Remove containers e volumes Docker
	@echo "$(RED)🧹 Removendo containers e volumes Docker...$(NC)"
	$(DOCKER_COMPOSE) down -v
	docker system prune -f
	@echo "$(GREEN)✅ Limpeza concluída!$(NC)"

# Comandos de setup completo
setup: ## Setup completo do projeto (instalar + migrar + rodar)
	@echo "$(GREEN)🚀 Setup completo do projeto...$(NC)"
	$(MAKE) install
	$(MAKE) migrate
	@echo "$(GREEN)✅ Setup concluído! Execute 'make run' para iniciar o servidor$(NC)"

setup-dev: ## Setup completo com PostgreSQL (Docker + instalar + migrar)
	@echo "$(GREEN)🚀 Setup completo com PostgreSQL...$(NC)"
	$(MAKE) docker-start
	@echo "$(YELLOW)⏳ Aguardando PostgreSQL inicializar...$(NC)"
	sleep 10
	$(MAKE) install
	$(MAKE) migrate-dev
	@echo "$(GREEN)✅ Setup concluído! Execute 'make run-dev' para iniciar o servidor$(NC)"

# Comandos de desenvolvimento
dev: ## Inicia ambiente completo de desenvolvimento
	@echo "$(GREEN)🚀 Iniciando ambiente de desenvolvimento...$(NC)"
	$(MAKE) docker-start
	@echo "$(YELLOW)⏳ Aguardando PostgreSQL inicializar...$(NC)"
	sleep 10
	$(MAKE) run-dev

# Comandos de produção
collectstatic: ## Coleta arquivos estáticos
	@echo "$(GREEN)📁 Coletando arquivos estáticos...$(NC)"
	$(MANAGE) collectstatic --noinput

check: ## Verifica se o projeto está configurado corretamente
	@echo "$(GREEN)🔍 Verificando configuração do projeto...$(NC)"
	$(MANAGE) check
	$(MANAGE) check --deploy

# Comandos de backup
backup: ## Cria backup do banco de dados
	@echo "$(GREEN)💾 Criando backup do banco...$(NC)"
	$(MANAGE) dumpdata > backup_$(shell date +%Y%m%d_%H%M%S).json

restore: ## Restaura backup do banco de dados
	@echo "$(RED)⚠️ Restaurando backup do banco...$(NC)"
	@echo "$(YELLOW)Use: make restore FILE=backup_file.json$(NC)"
ifdef FILE
	$(MANAGE) loaddata $(FILE)
else
	@echo "$(RED)❌ Arquivo de backup não especificado!$(NC)"
	@echo "$(YELLOW)Exemplo: make restore FILE=backup_20241201_143022.json$(NC)"
endif 