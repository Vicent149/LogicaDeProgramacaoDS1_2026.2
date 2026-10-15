"""
DESAFIO 04: REFATORAÇÃO INVESTIGATIVA
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
O código monolítico repete cálculos de desconto e impostos várias vezes.

SUA MISSÃO:
1. Crie uma função calcular_preco_final(preco_base, taxa_desc, taxa_imp) com return.
2. Crie um procedimento exibir_relatorio_item(numero_item, preco_final) com print.
3. Teste suas funções refatoradas.
"""

# TODO: Desenvolva as funções modulares abaixo:

def precofinal (base,desc,imp):
    precofinal = float(base - ((base * 0.1) * desc)) + imp
    return precofinal
base = float(input("Insira o preço: "))
desc = float(input("Insira o desconto: "))
imp = float(input("Insira a taxa de imposto: "))

print("O valor final do produto é ", precofinal(base,desc,imp))