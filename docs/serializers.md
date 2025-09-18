# Serializers

## HealthCheckSerializer

Saída padrão:

```json
{
  "status": "ok",
  "message": "API is running"
}
```

## UserSerializer

Campos: `id`, `username`, `email`, `nome`, `sobrenome`, `nome_completo`, `tipo_usuario`, `sexo`, `cpf`, `data_nascimento`, `telefone`, `endereco`, `criado_em`, `atualizado_em`, `is_active`

Somente leitura: `id`, `criado_em`, `atualizado_em`, `nome_completo`

## UserCreateSerializer

Criação de usuários. Campos:

- `username`, `email`, `password`, `password_confirmation`
- `nome`, `sobrenome`, `tipo_usuario` (`profissional` | `cliente`), `sexo` (`M` | `F` | `O`), `cpf`, `data_nascimento`, `telefone`, `endereco`

Validação: `password` deve ser igual a `password_confirmation`.

Exemplo de entrada:

```json
{
  "username": "joao",
  "email": "joao@example.com",
  "password": "SenhaForte123",
  "password_confirmation": "SenhaForte123",
  "nome": "João",
  "sobrenome": "Silva",
  "tipo_usuario": "cliente",
  "sexo": "M",
  "cpf": "123.456.789-10",
  "data_nascimento": "1990-05-20",
  "telefone": "+55 11 99999-9999",
  "endereco": "Rua Exemplo, 123"
}
```

## UserUpdateSerializer

Atualização parcial do usuário autenticado. Campos: `email`, `nome`, `sobrenome`, `sexo`, `data_nascimento`, `telefone`, `endereco`.

## ProfissionalSerializer

Saída do profissional. Campos: `id`, `usuario` (aninhado via `UserSerializer`), `nome_completo`, `registro_profissional`, `especialidade`, `formacao`, `experiencia_anos`, `clinica`, `horario_atendimento`, `ativo`.

## ProfissionalCreateSerializer

Criação de profissionais com usuário aninhado.

Entrada esperada:

```json
{
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
  "especialidade": "Fisioterapia Esportiva",
  "formacao": "USP",
  "experiencia_anos": 7,
  "clinica": "Clínica Movimento",
  "horario_atendimento": "Seg-Sex 8h-18h"
}
```

## ClienteSerializer

Saída do cliente. Campos: `id`, `usuario`, `nome_completo`, `responsavel`, `observacoes`, `historico_medico`, `alergias`, `medicamentos`, `ativo`.

## ClienteCreateSerializer

Criação de clientes com usuário aninhado.

Entrada esperada:

```json
{
  "usuario": {
    "username": "maria",
    "email": "maria@example.com",
    "password": "SenhaForte123",
    "password_confirmation": "SenhaForte123",
    "nome": "Maria",
    "sobrenome": "Ferreira",
    "tipo_usuario": "cliente",
    "sexo": "F",
    "cpf": "555.666.777-88"
  },
  "responsavel": "Pai/Mãe",
  "observacoes": "Paciente em acompanhamento",
  "historico_medico": "Sem cirurgias",
  "alergias": "Poeira",
  "medicamentos": "Nenhum"
}
```

## LoginSerializer

Entrada:

```json
{ "username": "joao", "password": "SenhaForte123" }
```

Saída (via view `login_user`): objeto `user` + `token`.

