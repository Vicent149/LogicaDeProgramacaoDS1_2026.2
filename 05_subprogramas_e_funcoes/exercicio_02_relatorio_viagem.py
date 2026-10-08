"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:

def caucular_transporte(distancia,consumo,combustivel):
    custo1 = distancia * consumo / combustivel
    return custo1
def caucular_alimentação(pessoas,dias,diaria):
    custo2 = pessoas * dias * diaria
    return custo2

dist = float(input("Insira a sua distancia percorrida"))
cons = float(input("Insira o consumo de combustivel"))
comb = float(input("Insira a quantidade de combustivel"))
pes = int(input("Insira o numero de pessoas"))
dia = int(input("Insira o numero de dias"))
diar = float(input("Insira o valor da diaria"))

custo1 = caucular_alimentação(pes,dia,diar)
custo2 = caucular_transporte(dist,cons,comb)

print(f"O valor da viagem sera de {custo1 + custo2}")


