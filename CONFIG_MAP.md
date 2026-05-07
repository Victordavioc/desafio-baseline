# CONFIG_MAP — Mapa de Itens de Configuração (ICs)

Este documento lista todos os **Itens de Configuração (ICs)** que compõem o projeto **Desafio da Baseline** e estabelece a política de versionamento adotada. Ele faz parte da documentação de Gerência de Configuração de Software (GCS) e deve ser atualizado sempre que um novo IC for incluído, removido ou tiver sua versão alterada.

---

## 1. Política de Nomenclatura de Versões

O projeto adota o padrão **Versionamento Semântico** (SemVer 2.0.0 — https://semver.org/lang/pt-BR/).

### Formato

```
MAJOR.MINOR.PATCH
```

### Regras de incremento

| Componente | Quando incrementar                                                                                                                                          |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **MAJOR**  | Quando houver mudanças **incompatíveis** com a versão anterior (quebra de compatibilidade na API pública, remoção de funcionalidades, mudança no formato do `config.env`). |
| **MINOR**  | Quando forem adicionadas **novas funcionalidades** mantendo retrocompatibilidade (ex.: nova operação na calculadora, nova variável opcional de configuração).             |
| **PATCH**  | Quando forem feitas **correções de bugs** retrocompatíveis ou ajustes internos que não alterem o comportamento público.                                                  |

### Tags Git

- Toda baseline é marcada com uma tag no formato `vMAJOR.MINOR.PATCH` (ex.: `v1.0.0`, `v1.1.0`, `v2.0.0`).
- Pré-lançamentos podem usar sufixos: `v1.1.0-alpha`, `v1.1.0-beta.1`, `v1.1.0-rc.1`.
- Tags são **imutáveis**: uma vez publicadas, não devem ser sobrescritas.

### Versão atual da baseline

- **v1.0.0** — Baseline inicial do projeto.

---

## 2. Itens de Configuração (ICs)

Os ICs estão classificados em quatro categorias: código-fonte, documentação, configuração e ambiente/dependências.

### 2.1 Código-fonte

| ID      | Item             | Caminho        | Versão | Descrição                                       | Responsável  |
| ------- | ---------------- | -------------- | ------ | ----------------------------------------------- | ------------ |
| IC-001  | Aplicação principal | `src/main.py` | 1.0.0  | Script Python com a calculadora simples e leitura do `config.env`. | Victor Cunha |

### 2.2 Documentação

| ID      | Item            | Caminho           | Versão | Descrição                                                | Responsável  |
| ------- | --------------- | ----------------- | ------ | -------------------------------------------------------- | ------------ |
| IC-002  | README          | `README.md`       | 1.0.0  | Visão geral, instruções de uso e estrutura do projeto.   | Victor Cunha |
| IC-003  | Mapa de ICs     | `CONFIG_MAP.md`   | 1.0.0  | Este documento — política de versão e lista de ICs.      | Victor Cunha |
| IC-004  | Arquitetura     | `docs/ARCHITECTURE.md` | 1.0.0 | Descrição da arquitetura interna e fluxo de execução. | Victor Cunha |

### 2.3 Configuração

| ID      | Item              | Caminho             | Versão | Descrição                                                            | Responsável  |
| ------- | ----------------- | ------------------- | ------ | -------------------------------------------------------------------- | ------------ |
| IC-005  | Variáveis de ambiente | `config/config.env` | 1.0.0  | Variáveis utilizadas pela aplicação (nome, versão, ambiente, debug). | Victor Cunha |
| IC-006  | Git ignore        | `.gitignore`        | 1.0.0  | Define arquivos ignorados pelo controle de versão.                   | Victor Cunha |

### 2.4 Ambiente, bibliotecas e frameworks

| ID      | Item              | Versão  | Descrição                                                  | Origem                  |
| ------- | ----------------- | ------- | ---------------------------------------------------------- | ----------------------- |
| IC-007  | Python            | 3.9+    | Linguagem e interpretador utilizados pelo projeto.         | https://www.python.org/ |
| IC-008  | Biblioteca padrão `os` | 3.9+ | Manipulação de variáveis de ambiente.                      | Python stdlib           |
| IC-009  | Biblioteca padrão `pathlib` | 3.9+ | Manipulação de caminhos de arquivos.                  | Python stdlib           |
| IC-010  | Git               | 2.30+   | Sistema de controle de versão usado para criar a baseline. | https://git-scm.com/    |

> Atualmente o projeto não possui dependências externas (não há `requirements.txt`). Caso bibliotecas de terceiros sejam adicionadas no futuro, elas deverão ser registradas como novos ICs nesta seção e fixadas em um arquivo `requirements.txt` com versões pinadas.

---

## 3. Histórico de Baselines

| Versão  | Data       | Tag Git  | Descrição                                                              |
| ------- | ---------- | -------- | ---------------------------------------------------------------------- |
| 1.0.0   | 2026-05-07 | `v1.0.0` | Baseline inicial: estrutura de diretórios, código simples, README, config.env e CONFIG_MAP. |

---

## 4. Procedimento para gerar uma nova baseline

1. Garantir que a `main` está estável e todos os ICs foram revisados.
2. Atualizar este documento (`CONFIG_MAP.md`) registrando as mudanças de versão dos ICs afetados.
3. Atualizar o campo `APP_VERSION` em `config/config.env`.
4. Realizar o commit das alterações.
5. Criar a tag anotada correspondente:
   ```bash
   git tag -a vX.Y.Z -m "Baseline vX.Y.Z"
   git push origin vX.Y.Z
   ```
6. Adicionar uma nova linha à seção **Histórico de Baselines**.
