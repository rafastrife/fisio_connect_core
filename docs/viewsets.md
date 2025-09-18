# ViewSets e Rotas

A API utiliza `DefaultRouter` do DRF para registrar os seguintes recursos:

- `usuarios` → `UserViewSet` (apenas administradores)
- `profissionais` → `ProfissionalViewSet` (autenticado)
- `clientes` → `ClienteViewSet` (autenticado)

## Padrões de Rotas (DRF)

Considerando o prefixo `/api/` configurado no projeto:

- Listar: `GET /api/<recurso>/`
- Criar: `POST /api/<recurso>/`
- Detalhar: `GET /api/<recurso>/{id}/`
- Atualizar: `PUT /api/<recurso>/{id}/`
- Atualização parcial: `PATCH /api/<recurso>/{id}/`
- Remover: `DELETE /api/<recurso>/{id}/`

## Permissões

- `UserViewSet`: `IsAdminUser`
- `ProfissionalViewSet`: `IsAuthenticated`
- `ClienteViewSet`: `IsAuthenticated`

## Filtros e Query Params

- `ProfissionalViewSet`: `GET /api/profissionais/?especialidade=<termo>` filtra por especialidade (case-insensitive)

