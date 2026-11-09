marca = input("Insira a marca do veiculo que voce quer comprar: ")
modelo = input("Insira o modelo do veiculo que voce quer comprar: ")
ano = int(input("Insira o ano do veiculo que voce quer comprar"))

veiculo = {"Marca": marca, "modelo": modelo, "ano": ano}

for chave, valor in veiculo.items():
    print(chave, valor)
    