"""
EXERCÍCIO 03: Fórmula de Bhaskara
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 3 valores de ponto flutuante (A, B e C) de uma equação do 2º grau.
- Se A for 0 ou delta for negativo, imprima "Impossivel calcular".
- Caso contrário, calcule e mostre as duas raízes (R1 e R2) formatadas com 5 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:

from numbers import Real


a = int(input("Insira valor de A: "))
b = int(input("Insira valor de B: "))
c = int(input("Insira o valor de C: "))
delta = int(b ** 2 - 4 * a * c)
raiz = delta ** 0.5
x1 = (-b + (raiz)) / 2 * a
x2 = (-b - (raiz)) / 2 * a

if a and delta < 0:
    print("Essa operação não pode ser realizada")
else:
    print(f"As raizes da operação são: {x1} e {x2}")
