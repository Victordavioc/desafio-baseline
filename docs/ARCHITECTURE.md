# Arquitetura

Documento descritivo da arquitetura interna do projeto **Desafio da Baseline**.

## Visão geral

A aplicação é um único script Python (`src/main.py`) que lê variáveis de configuração de um arquivo `.env` e expõe quatro funções aritméticas básicas. O foco do projeto não é a complexidade da aplicação, e sim demonstrar o uso de **baseline** e **gerência de configuração** sobre um repositório real.

## Fluxo de execução

```
        ┌──────────────────────┐
        │  config/config.env   │
        └──────────┬───────────┘
                   │  carregar_config()
                   ▼
        ┌──────────────────────┐
        │       main.py        │
        │  ┌────────────────┐  │
        │  │ somar          │  │
        │  │ subtrair       │  │
        │  │ multiplicar    │  │
        │  │ dividir        │  │
        │  └────────────────┘  │
        └──────────┬───────────┘
                   │
                   ▼
              stdout (print)
```

## Componentes

| Componente         | Responsabilidade                                                |
| ------------------ | --------------------------------------------------------------- |
| `carregar_config`  | Lê e parseia o arquivo `config.env` em um dicionário Python.    |
| `somar`            | Operação de soma entre dois números.                            |
| `subtrair`         | Operação de subtração.                                          |
| `multiplicar`      | Operação de multiplicação.                                      |
| `dividir`          | Operação de divisão (com proteção contra divisão por zero).     |
| `main`             | Orquestra a leitura da configuração e a execução das operações. |

## Decisões de projeto

- **Sem dependências externas**: a aplicação utiliza apenas a biblioteca padrão do Python para reduzir o número de ICs a gerenciar nesta primeira baseline.
- **Configuração via arquivo `.env`**: separa parâmetros do código, facilitando alterações sem necessidade de novo deploy/build.
- **Versionamento semântico**: adotado para tornar evolução do projeto previsível (ver `CONFIG_MAP.md`).
