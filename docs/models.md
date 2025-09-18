# Modelos de Dados

Esta seção descreve os modelos públicos expostos pela API.

## User

Usuário do sistema, extendendo `AbstractUser` com campos adicionais.

Campos principais:

- `id` (int, somente leitura)
- `username` (string, único)
- `email` (string)
- `nome` (string, obrigatório)
- `sobrenome` (string, obrigatório)
- `tipo_usuario` (string, enum: `profissional` | `cliente`)
- `sexo` (string, enum: `M` | `F` | `O`)
- `cpf` (string, único, formato `000.000.000-00`)
- `data_nascimento` (date, opcional)
- `telefone` (string, opcional)
- `endereco` (string, opcional)
- `is_active` (bool)
- `criado_em` (datetime, somente leitura)
- `atualizado_em` (datetime, somente leitura)

Propriedades calculadas:

- `nome_completo` (string, somente leitura)
- `is_profissional` (bool, somente leitura)
- `is_cliente` (bool, somente leitura)

## Profissional

Representa profissionais (fisioterapeutas) vinculados a um `User`.

Campos principais:

- `id` (int, somente leitura)
- `usuario` (objeto `User`, somente leitura nas respostas; criação via serializer dedicado)
- `nome_completo` (string, somente leitura)
- `registro_profissional` (string, único)
- `especialidade` (string)
- `formacao` (string)
- `experiencia_anos` (int)
- `clinica` (string)
- `horario_atendimento` (string)
- `ativo` (bool)

## Cliente

Representa clientes vinculados a um `User`.

Campos principais:

- `id` (int, somente leitura)
- `usuario` (objeto `User`, somente leitura nas respostas; criação via serializer dedicado)
- `nome_completo` (string, somente leitura)
- `responsavel` (string)
- `observacoes` (string)
- `historico_medico` (string)
- `alergias` (string)
- `medicamentos` (string)
- `ativo` (bool)

