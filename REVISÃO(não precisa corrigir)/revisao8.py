#  Caixa de Supermercado Faça um programa para registrar os itens da compra de um 
# cliente. O programa deve ler o preço e a quantidade de cada item continuamente. Se o preço 
# digitado for negativo, a compra é encerrada. Se o total da compra ultrapassar R$ 200,00, o 
# sistema deve aplicar um desconto de 10% sobre o total. Exiba o valor bruto, o valor do 
# desconto e o valor final a pagar.


total  = 0

while True:
    
    produto = input("Insira o produto: ")
    preco_p = float(input("Insira o valor do produto (insira uma quantidade negativa para sair)"))
    if preco_p < 0:
            print("Compra encerrada")
            break
    quant = int(input("Insira a quantidade do produto"))
    total = preco_p * quant

if total >= 200:
    preco_d = 0.1 * total
    totalf = total - preco_d
else:
    preco_d = 0
    totalf = total - preco_d

print(f"""Valor: {total:.2f}
Valor do desconto: {preco_d:.2f}
Valor final {totalf:.2f}""")
