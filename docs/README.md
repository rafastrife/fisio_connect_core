# Fisio Connect Core — Documentação da API

Bem-vindo à documentação oficial da API do Fisio Connect Core.

Esta API é construída com Django 5 e Django REST Framework (DRF). Ela fornece recursos para autenticação, gestão de usuários, profissionais e clientes.

## Como usar esta documentação

- Consulte os modelos e serializers para entender o formato de dados
- Veja os endpoints para os caminhos HTTP, métodos e requisitos de autenticação
- Use os exemplos prontos de `curl` e Python para testar rapidamente

## Índice

- [Modelos (Models)](./models.md)
- [Serializers](./serializers.md)
- [ViewSets e Rotas](./viewsets.md)
- [Autenticação](./auth.md)
- [Endpoints](./endpoints.md)
- [Exemplos de Uso (curl e Python)](./examples.md)

## Ambiente padrão

- Base URL: `http://localhost:8000`
- Prefixo da API: `/api/`
- Ex.: Health check completo: `GET http://localhost:8000/api/health/`

## Convenções

- Autenticação por Token: envie o cabeçalho `Authorization: Token <seu_token>`
- Datas no formato ISO 8601 (`YYYY-MM-DD`)
- Conteúdo JSON com `Content-Type: application/json`

