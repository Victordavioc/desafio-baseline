"""
Calculadora simples - Desafio da Baseline
Lê configurações do arquivo config.env e executa operações básicas.
"""

import os
from pathlib import Path


def carregar_config(caminho: str) -> dict:
    """Lê um arquivo .env simples e retorna um dicionário com as variáveis."""
    config = {}
    arquivo = Path(caminho)
    if not arquivo.exists():
        return config

    for linha in arquivo.read_text(encoding="utf-8").splitlines():
        linha = linha.strip()
        if not linha and linha.startswith("#"):
            continue
        if "=" in linha:
            chave, valor = linha.split("=", 1)
            config[chave.strip()] = valor.strip()
    return config


def somar(a: float, b: float) -> float:
    return a + b


def subtrair(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b


def main() -> None:
    base_dir = Path(__file__).resolve().parent.parent
    config = carregar_config(base_dir / "config" / "config.env")

    app_nome = config.get("APP_NAME", "Calculadora")
    versao = config.get("APP_VERSION", "1.0.0")
    debug = config.get("DEBUG", "false").lower() == "true"

    print(f"=== {app_nome} v{versao} ===")
    if debug:
        print(f"[DEBUG] Configurações carregadas: {config}")

    a, b = 10, 3
    print(f"{a} + {b} = {somar(a, b)}")
    print(f"{a} - {b} = {subtrair(a, b)}")
    print(f"{a} * {b} = {multiplicar(a, b)}")
    print(f"{a} / {b} = {dividir(a, b):.2f}")


if __name__ == "__main__":
    main()
