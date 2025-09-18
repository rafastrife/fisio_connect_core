# Autenticação

A API utiliza autenticação por Token (DRF TokenAuthentication).

## Obtendo Token

Existem duas formas:

1) Registrar e receber token:

- `POST /api/auth/register/`

Resposta (201):

```json
{
  "user": { "id": 1, "username": "joao", "nome": "João", "sobrenome": "Silva", "tipo_usuario": "cliente", "sexo": "M", "cpf": "123.456.789-10", ... },
  "token": "<token>"
}
```

2) Login e receber token:

- `POST /api/auth/login/`

Entrada:

```json
{ "username": "joao", "password": "SenhaForte123" }
```

Resposta (200): igual ao registro, com `user` e `token`.

3) Endpoint padrão do DRF para token:

- `POST /api/auth/token/` com `username` e `password` retornando `{ "token": "..." }`.

## Usando o Token

Envie o cabeçalho em todas as requisições protegidas:

```
Authorization: Token <token>
```

## Perfil e Logout

- `GET /api/auth/profile/` — dados do usuário autenticado
- `PUT /api/auth/profile/update/` — atualiza dados do usuário autenticado
- `POST /api/auth/logout/` — encerra a sessão; invalida token apenas se houver lógica adicional (por padrão, apenas faz logout da sessão)

Observação: `user_stats` exige que o usuário seja staff (`is_staff = True`).

