"""
EXERCÍCIO 04: Função Lambda de Desconto Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Escreva uma função anônima (lambda) que receba o valor de um produto
e retorne o valor com 15% de desconto à vista aplicado.
"""

# TODO: Desenvolva a expressão lambda e teste-a abaixo:

produto = lambda v: v - v * 0.15
valor = float(input("Insira o seu o preço do produto: "))

print("voce recebeu um desconto, o valor sera de ", produto(valor))