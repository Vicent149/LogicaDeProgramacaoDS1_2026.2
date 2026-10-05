"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:

from itertools import count


q = 0
s = 0
for i in range(6):
    n = int(input("Insira numeros: "))
    if n > 0:
        s += n
        q += 1
print(f"Positivos: {q}")
if q > 0:
    m = s / q
    print(f"Media: {m}")
else:
    print("Nulo")