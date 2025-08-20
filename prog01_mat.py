"""
Calculadora Simples em Python 🧮
Autor: Márcio Ferreira

Descrição:
-----------
Este programa é uma calculadora simples que realiza as quatro operações básicas:
- Adição
- Subtração
- Multiplicação
- Divisão

"""

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return "Erro: divisão por zero não é permitida." if b == 0 else a / b

def menu():
    print("\n=== Calculadora Simples ===")
    print("1️⃣  Somar")
    print("2️⃣  Subtrair")
    print("3️⃣  Multiplicar")
    print("4️⃣  Dividir")
    print("0️⃣  Sair")

def ler_numero(mensagem):
    """Solicita um número ao usuário até que seja digitado um valor válido."""
    entrada = input(mensagem)
    while not entrada.replace(".", "", 1).isdigit() and not (entrada.startswith("-") and entrada[1:].replace(".", "", 1).isdigit()):
        print("⚠️ Entrada inválida! Use apenas números.")
        entrada = input(mensagem)
    return float(entrada)

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "0":
        print(" Saindo da calculadora...")
        break

    if escolha not in {"1", "2", "3", "4"}:
        print("⚠️ Opção inválida! Tente novamente.")
        continue

    num1 = ler_numero("Digite o primeiro número: ")
    num2 = ler_numero("Digite o segundo número: ")

    operacoes = {
        "1": somar,
        "2": subtrair,
        "3": multiplicar,
        "4": dividir
    }

    resultado = operacoes[escolha](num1, num2)
    print(f"✅ Resultado: {resultado}")

