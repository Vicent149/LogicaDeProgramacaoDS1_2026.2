"""
EXERCÍCIO 05: Acesso à Bilheteria do Parque
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba a idade do visitante (valor base do ingresso: R$ 100,00):
- Menor que 12 anos: "Infantil" (50% de desconto -> R$ 50,00)
- Maior ou igual a 60 anos: "Melhor Idade" (Gratuidade -> R$ 0,00)
- Demais idades: "Integral" (R$ 100,00)

Imprima o tipo de bilhete e o valor final a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:

idade = int(input("Insira a sua idade: "))
valorbase = 100
m12 = valorbase - (valorbase * 0.5)
m60 = 0

if idade < 12:
    print(f"Voce tera de pagar {m12:.2f}R$ para entrar")
elif idade >= 60:
    print(f"Parabens! voce tera 100% de desconto e tera de pagar {m60:.2f}R$ para entrar")
else:
    print(f"Voce tera de pagar {valorbase:.2f}R$ para entrar")