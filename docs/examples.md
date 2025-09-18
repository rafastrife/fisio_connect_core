# Exemplos de Uso

## curl

### Health check

```bash
curl -s http://localhost:8000/api/health/
```

### Registro de usuário (recebe token)

```bash
curl -s -X POST http://localhost:8000/api/auth/register/ \
  -H 'Content-Type: application/json' \
  -d '{
    "username": "joao",
    "email": "joao@example.com",
    "password": "SenhaForte123",
    "password_confirmation": "SenhaForte123",
    "nome": "João",
    "sobrenome": "Silva",
    "tipo_usuario": "cliente",
    "sexo": "M",
    "cpf": "123.456.789-10"
  }'
```

### Login

```bash
curl -s -X POST http://localhost:8000/api/auth/login/ \
  -H 'Content-Type: application/json' \
  -d '{"username": "joao", "password": "SenhaForte123"}'
```

### Listar profissionais (autenticado)

```bash
TOKEN=seu_token_aqui
curl -s http://localhost:8000/api/profissionais/ \
  -H "Authorization: Token $TOKEN"
```

### Filtrar profissionais por especialidade

```bash
curl -s 'http://localhost:8000/api/profissionais/?especialidade=esportiva' \
  -H "Authorization: Token $TOKEN"
```

### Criar profissional (com usuário aninhado)

```bash
curl -s -X POST http://localhost:8000/api/profissionais/ \
  -H 'Content-Type: application/json' \
  -H "Authorization: Token $TOKEN" \
  -d '{
    "usuario": {
      "username": "dra.ana",
      "email": "ana@example.com",
      "password": "SenhaForte123",
      "password_confirmation": "SenhaForte123",
      "nome": "Ana",
      "sobrenome": "Souza",
      "tipo_usuario": "profissional",
      "sexo": "F",
      "cpf": "111.222.333-44"
    },
    "registro_profissional": "CREFITO-12345",
    "especialidade": "Fisioterapia Esportiva"
  }'
```

## Python (requests)

```python
import requests

BASE = 'http://localhost:8000/api'

def register():
    payload = {
        "username": "joao",
        "email": "joao@example.com",
        "password": "SenhaForte123",
        "password_confirmation": "SenhaForte123",
        "nome": "João",
        "sobrenome": "Silva",
        "tipo_usuario": "cliente",
        "sexo": "M",
        "cpf": "123.456.789-10"
    }
    r = requests.post(f"{BASE}/auth/register/", json=payload)
    r.raise_for_status()
    return r.json()["token"]

def list_profissionais(token: str):
    r = requests.get(f"{BASE}/profissionais/", headers={"Authorization": f"Token {token}"})
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    token = register()
    print("Token:", token)
    print(list_profissionais(token))
```

