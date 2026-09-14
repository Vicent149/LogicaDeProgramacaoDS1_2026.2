"""
EXERCÍCIO 01: Gestão de Tráfego Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
A loja Casas Paulino está veiculando anúncios no Meta Ads em Tianguá.
Escreva um programa que leia:
1. O valor total investido na campanha (em R$).
2. O número total de cliques obtidos.

Calcule e mostre na tela o Custo Por Clique (CPC) médio da campanha formatado em reais.
"""

# TODO: Desenvolva o algoritmo abaixo:

valor_campanha = float(input("Insira o valor: "))
valor_cliques = float(input("Insira o numero de cliques: "))
cpc = float(valor_campanha / valor_cliques)

print (f"A quantidade de CPC é: {cpc:.2f}")


