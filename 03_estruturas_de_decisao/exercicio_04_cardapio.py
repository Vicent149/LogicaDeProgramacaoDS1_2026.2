"""
EXERCÍCIO 04: Cardápio da Lanchonete
Disciplina: Lógica de Programação com Python

TABELA:
1 - Cachorro Quente: R$ 4.00
2 - X-Salada: R$ 4.50
3 - X-Bacon: R$ 5.00
4 - Torrada Simples: R$ 2.00
5 - Refrigerante: R$ 1.50

ENUNCIADO:
Leia o código do item e a quantidade consumida.
Calcule e mostre o total a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:

hotdog = 4.00
xs = 4.50
xb = 5.00
ts = 2.00
cc = 1.50
c1 = 1
c2 = 2
c3 = 3
c4 = 4
c5 = 5
opcao = int(input("Escolha: 1-HotDog, 2-XSalada, 3-XBacon, 4-TorradaSimples, 5-Refigerante: "))
qtd = int(input("Insira a quantidade desejada: "))

match opcao:
    case 1:
        print(f"Hot Dogs de {hotdog:.2f}R$. Codigo:{c1}. O valor final a pagar sera de {hotdog * qtd:.2f}R$")
    case 2:
        print(f"X Salada de {xs:.2f}R$. Codigo:{c2}. O valor final a pagar sera de {xs * qtd:.2f}R$")
    case 3:
        print(f"X Bacon de {xb:.2f}R$. Codigo:{c3}. O valor final a pagar sera de {xb * qtd:.2f}R$")
    case 4:
        print (f"Torrada simples de {ts:.2f}R$. Codigo:{c4}. O valor final a pagar sera de {ts * qtd:.2f}R$" )
    case 5:
        print(f"Refrigerante simples de {cc:.2f}R$. Codigo:{c4}. O valor final a pagar sera de {cc * qtd:.2f}R$")

