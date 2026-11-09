# Calculadora de Frete de E-commerce Uma loja virtual precisa de um sistema para 
# calcular o valor do frete. Crie uma função que receba a distância em quilômetros e o tipo de 
# cliente ("Padrão" ou "VIP"). A regra é: R
# 15,00. 
# 0, 50 𝑝𝑜𝑟 𝑘𝑚 𝑟𝑜𝑑𝑎𝑑𝑜. 𝑆𝑒 𝑎 𝑑𝑖𝑠𝑡â𝑛𝑐𝑖𝑎 𝑓𝑜𝑟 𝑚𝑎𝑖𝑜𝑟 𝑞𝑢𝑒 100𝑘𝑚, ℎá 𝑢𝑚𝑎 𝑡𝑎𝑥𝑎 𝑓𝑖𝑥𝑎 𝑎𝑑𝑖𝑐𝑖𝑜𝑛𝑎𝑙 𝑑𝑒 𝑅
# Clientes VIP recebem 20% de desconto no valor final do frete. Peça para o usuário inserir os 
# dados e exiba o resultado utilizando a função criada. 

from importlib.metadata import distribution


def r(dist,client):
    if client == 1:
        frete = dist * 0.5
    elif client == 2:
        frete = (dist * 0.5) - ((dist * 0.5) * 0.2)
    return frete

dist = float(input("Insira a distancia em KM que o entregador percorrera: "))
client = int(input("Que tipo de cliente você é? 1-Padrão, 2-VIP: "))

fretefinal = r(dist,client)
print(f"O frete sera de {fretefinal}R$")