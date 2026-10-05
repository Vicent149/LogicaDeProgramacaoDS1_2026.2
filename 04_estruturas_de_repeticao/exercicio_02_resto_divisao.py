"""
EXERCÍCIO 02: Resto da Divisão por 5
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia dois valores inteiros X e Y.
Utilize o laço for para imprimir todos os inteiros entre X e Y (em ordem crescente)
cujo resto da divisão por 5 seja igual a 2 ou igual a 3.
"""

# TODO: Desenvolva o algoritmo abaixo:
n1 = int(input("Insira o valor de X: "))
n2 = int(input("Insira o valor de Y: "))

print(f"Contando de {n1} a {n2}")
for i in range (n1, n2 + 1):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
