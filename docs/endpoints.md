# Endpoints

Prefixo base: `/api/`

## Health Check

- Método/URL: `GET /api/health/`
- Auth: pública
- Resposta 200:

```json
{ "status": "ok", "message": "API is running" }
```

## Autenticação

- Registrar: `POST /api/auth/register/`
- Login: `POST /api/auth/login/`
- Token (DRF): `POST /api/auth/token/`
- Logout: `POST /api/auth/logout/` (requer token)
- Perfil: `GET /api/auth/profile/` (requer token)
- Atualizar perfil: `PUT /api/auth/profile/update/` (requer token)

## Usuários (apenas admin)

- Listar: `GET /api/usuarios/`
- Criar: `POST /api/usuarios/`
- Detalhar: `GET /api/usuarios/{id}/`
- Atualizar: `PUT /api/usuarios/{id}/`
- Parcial: `PATCH /api/usuarios/{id}/`
- Remover: `DELETE /api/usuarios/{id}/`

## Profissionais (autenticado)

- Listar: `GET /api/profissionais/`
  - Query params: `especialidade=<termo>` para filtrar
- Criar: `POST /api/profissionais/`
- Detalhar: `GET /api/profissionais/{id}/`
- Atualizar: `PUT /api/profissionais/{id}/`
- Parcial: `PATCH /api/profissionais/{id}/`
- Remover: `DELETE /api/profissionais/{id}/`

## Clientes (autenticado)

- Listar: `GET /api/clientes/`
- Criar: `POST /api/clientes/`
- Detalhar: `GET /api/clientes/{id}/`
- Atualizar: `PUT /api/clientes/{id}/`
- Parcial: `PATCH /api/clientes/{id}/`
- Remover: `DELETE /api/clientes/{id}/`

## Estatísticas (somente staff)

- `GET /api/stats/users/`

Resposta 200:

```json
{
  "total_usuarios": 10,
  "total_profissionais": 4,
  "total_clientes": 6,
  "usuarios_ativos": 9,
  "usuarios_inativos": 1
}
```

