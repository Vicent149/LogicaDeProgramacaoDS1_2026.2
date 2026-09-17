"""
EXERCÍCIO 01: Imposto de Renda de Lisarb
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de uma pessoa em Rombus (R$).
- Até R$ 2000.00: Isento
- De R$ 2000.01 até R$ 3000.00: 8% sobre o excedente de R$ 2000.00
- De R$ 3000.01 até R$ 4500.00: 18% sobre o excedente de R$ 3000.00 + 8% da faixa anterior
- Acima de R$ 4500.00: 28% sobre o que ultrapassar R$ 4500.00 + impostos anteriores

Imprima "Isento" ou o valor total do imposto formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:

salario = float(input("Insira o seu salario: "))
imposto1 = salario * 0.08
imposto2 = salario * 0.18 + imposto1
imposto3 = salario * 0.28 + imposto2

if salario < 2000:
    print("Vocé esta insento de imposto")
elif 3000 < salario > 2000:
    print(f"Voce tera de pagar {imposto1:.2f}R$ de imposto")
elif 4500 < salario > 3000:
    print(f"Voce tera de pagar {imposto2:.2f}R$ de imposto")
elif salario > 4500:
    print(f"voce tera de pagar {imposto3:.2f}R$ de imposto")