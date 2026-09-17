"""
EXERCÍCIO 02: Aumento de Salário Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de um colaborador da escola e aplique o percentual de reajuste:
- 0.00 a 400.00: 15%
- 400.01 a 800.00: 12%
- 800.01 a 1200.00: 10%
- 1200.01 a 2000.00: 7%
- Acima de 2000.00: 4%

Imprima: novo salário, valor do reajuste ganho e percentual aplicado.
"""

# TODO: Desenvolva o algoritmo abaixo:

salario = float(input("Insira seu salario: "))
imposto1 = 0.15
imposto2 = 0.12
imposto3 = 0.10
imposto4 = 0.07
imposto5 = 0.04

if 0 < salario < 400:
    print(f"Seu salario é {salario + imposto1 * salario}R$. com um reajuste de {imposto1 * salario:.2f} com o ganho percentual de {imposto1 * 100}%")
elif 400 < salario < 800:
    print (f"Seu salario é {salario + imposto2 * salario}, com um reajuste de {imposto2 * salario:.2f} e com percentual {imposto2 * 100}%")
elif 800 < salario < 1200:
    print (f"Seu salario é {salario + imposto3 * salario}, com o reajuste de {imposto3 *  salario:.2f} e com percentual {imposto3 * 100}%")
elif 1200 < salario < 2000:
    print(f"Seu salario é {salario + imposto4 * salario}, com reajuste de {imposto4 * salario:.2f} e com percentual {imposto4 * 100}%")
elif 2000 < salario:
    print(f"Seu salario é {salario + imposto5 * salario}, com o reajuste de {imposto5 * salario:.2f} e com percentual {imposto5 * 100}%")