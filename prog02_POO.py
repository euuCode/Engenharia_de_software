"""
================================================================
 Calculadora Avançada em Python (POO)
 Autor: Márcio Ferreira (versão aprimorada)

 Descrição:
 -----------
 Calculadora que realiza operações básicas e algumas avançadas:
 - Soma, Subtração, Multiplicação, Divisão
 - Potência, Raiz Quadrada, Porcentagem

 Recursos:
  - Validação de entrada (só aceita números)
  - Tratamento para divisão por zero
  - Menu interativo no console
================================================================
"""

from enum import Enum
import math


class Operacao(Enum):
    SOMA = "+"
    SUBTRACAO = "-"
    MULTIPLICACAO = "×"
    DIVISAO = "÷"
    POTENCIA = "^"
    RAIZ = "√"
    PORCENTAGEM = "%"

    def executar(self, a: float, b: float = 0) -> float:
        if self == Operacao.SOMA:
            return a + b
        elif self == Operacao.SUBTRACAO:
            return a - b
        elif self == Operacao.MULTIPLICACAO:
            return a * b
        elif self == Operacao.DIVISAO:
            if b == 0:
                print("⚠️ Não dá pra dividir por zero.")
                return float("nan")
            return a / b
        elif self == Operacao.POTENCIA:
            return math.pow(a, b)
        elif self == Operacao.RAIZ:
            if a < 0:
                print("⚠️ Não dá pra tirar raiz de número negativo.")
                return float("nan")
            return math.sqrt(a)
        elif self == Operacao.PORCENTAGEM:
            return (a * b) / 100
        else:
            return float("nan")

    def __str__(self):
        nomes = {
            Operacao.SOMA: "Soma (+)",
            Operacao.SUBTRACAO: "Subtração (-)",
            Operacao.MULTIPLICACAO: "Multiplicação (×)",
            Operacao.DIVISAO: "Divisão (÷)",
            Operacao.POTENCIA: "Potência (^)",
            Operacao.RAIZ: "Raiz Quadrada (√)",
            Operacao.PORCENTAGEM: "Porcentagem (%)",
        }
        return nomes[self]


class Calculadora:
    def __init__(self):
        self.operacoes = {
            "1": Operacao.SOMA,
            "2": Operacao.SUBTRACAO,
            "3": Operacao.MULTIPLICACAO,
            "4": Operacao.DIVISAO,
            "5": Operacao.POTENCIA,
            "6": Operacao.RAIZ,
            "7": Operacao.PORCENTAGEM,
        }

    def exibir_menu(self):
        print("\n=== Calculadora Avançada ===")
        for k, v in self.operacoes.items():
            print(f"{k}️⃣  {v}")
        print("0️⃣  Sair")

    def ler_numero(self, mensagem: str) -> float:
        while True:
            try:
                return float(input(mensagem))
            except ValueError:
                print("⚠️ Entrada inválida! Digite só número.")

    def iniciar(self):
        while True:
            self.exibir_menu()
            escolha = input("Escolha uma opção: ")

            if escolha == "0":
                print("👋 Saindo... valeu!")
                break

            operacao = self.operacoes.get(escolha)
            if operacao is None:
                print("⚠️ Opção inválida! Tenta de novo.")
                continue

            num1 = self.ler_numero("Digite o primeiro número: ")
            num2 = 0

            if operacao != Operacao.RAIZ:
                num2 = self.ler_numero("Digite o segundo número: ")

            resultado = operacao.executar(num1, num2)
            if not math.isnan(resultado):
                print(f"✅ Resultado: {resultado:.2f}")


if __name__ == "__main__":
    Calculadora().iniciar()
