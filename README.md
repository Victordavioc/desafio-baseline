# Desafio da Baseline

Repositório criado como parte da atividade **Desafio da Baseline** da disciplina de Gerência de Configuração de Software (GCS). O objetivo é estabelecer uma estrutura de diretórios padronizada, identificar todos os Itens de Configuração (ICs) do projeto e congelar uma baseline através de uma tag Git.

## Estrutura do projeto

```
desafio-baseline/
├── src/
│   └── main.py          # Código-fonte da aplicação (calculadora simples)
├── config/
│   └── config.env       # Arquivo de configuração com variáveis de ambiente
├── docs/
│   └── ARCHITECTURE.md  # Documentação adicional sobre a arquitetura
├── README.md            # Este arquivo
├── CONFIG_MAP.md        # Mapa de Itens de Configuração e política de versão
└── .gitignore
```

## Sobre a aplicação

A aplicação é uma **calculadora simples** escrita em Python que lê suas configurações a partir do arquivo `config/config.env` e executa as quatro operações básicas: soma, subtração, multiplicação e divisão.

## Pré-requisitos

- Python 3.9 ou superior
- Sistema operacional: Linux, macOS ou Windows

Não há dependências externas — o projeto utiliza apenas a biblioteca padrão do Python.

## Como executar

A partir da raiz do repositório:

```bash
python3 src/main.py
```

Saída esperada:

```
=== Calculadora Baseline v1.0.0 ===
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.33
```

## Configuração

As variáveis de ambiente do projeto são definidas em `config/config.env`. Os valores podem ser ajustados conforme a necessidade:

| Variável      | Descrição                                  | Padrão               |
| ------------- | ------------------------------------------ | -------------------- |
| `APP_NAME`    | Nome amigável da aplicação                 | Calculadora Baseline |
| `APP_VERSION` | Versão semântica corrente                  | 1.0.0                |
| `APP_ENV`     | Ambiente (development/staging/production)  | development          |
| `DEBUG`       | Ativa logs de depuração                    | true                 |
| `LOG_LEVEL`   | Nível de log (DEBUG, INFO, WARNING, ERROR) | INFO                 |
| `LOCALE`      | Configuração de localidade                 | pt_BR                |
| `TIMEZONE`    | Fuso horário utilizado                     | America/Sao_Paulo    |

## Baseline

A primeira baseline do projeto está marcada com a tag **`v1.0.0`** no Git. Para listar as baselines disponíveis:

```bash
git tag -l
```

Para conferir o conteúdo exato congelado na baseline:

```bash
git checkout v1.0.0
```

Os Itens de Configuração que compõem essa baseline estão descritos em [`CONFIG_MAP.md`](./CONFIG_MAP.md).

## Autor

Repositório mantido por **Victor Cunha** como parte das atividades da disciplina.
