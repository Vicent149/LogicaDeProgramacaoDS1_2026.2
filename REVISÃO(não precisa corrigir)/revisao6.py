# Sistema de Tarifas de Táxi Crie duas funções distintas: tarifa_diurna(distancia) e 
# tarifa_noturna(distancia). A tarifa diurna cobra R 
# 4, 00 𝑑𝑒 𝑏𝑎𝑛𝑑𝑒𝑖𝑟𝑎 𝑑𝑎 𝑚𝑎𝑖𝑠 𝑅
# km. A noturna cobra R 
# 6, 00 𝑑𝑒 𝑏𝑎𝑛𝑑𝑒𝑖𝑟𝑎 𝑑𝑎 𝑚𝑎𝑖𝑠 𝑅
# 2,50 por 
# 3,20 por km. O programa principal deve usar 
# um laço para atender vários passageiros ao longo do turno de um motorista. Para cada 
# passageiro, pergunte se a corrida foi de dia (D) ou de noite (N) e a distância. Chame a função 
# adequada e some o valor para o caixa do motorista. O turno acaba quando a distância 
# informada for negativa.

from typing import final


def caixa(distancia):
    valor = 4 + distancia * 2.50
    return valor
    
def caixa2(distancia):
    valor =  6 + distancia * 3.20
    return valor

final = 0

while True:
    dn = input("Insira: D (diurno) ou N (noturno)?")
    km = float(input("Insira a quantidade de KM percorridos(Negativo encerra a função): "))
    if km < 0:
        print("Turno encerrado")
        break
    if dn.lower == "d":
        corrida = caixa(km)
        print(caixa)
    if dn.lower() == "n":
        corrida = caixa2(km)
        print(caixa2)

        final += corrida
        print(corrida)
        print(final)




