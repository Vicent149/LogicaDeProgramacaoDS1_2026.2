"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:

n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
n3 = float(input("Insira a terceira nota: "))
mc = float((n1 * n2 * n3) / 3)
p1 = 2
p2 = 3
p3 = 5
mp = float(((n1 * p1) + (n2 * p2) + (n3 * p3)) / (p1 + p2 + p3))
print(f"Sua media ponderada é {mp}")


