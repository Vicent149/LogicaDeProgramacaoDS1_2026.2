numero = float(input("insira um numero "))
while True:
    soma = float(input("digite um numero (aperte 0 para encerrar)"))
    soma = soma + numero
    if soma == 0:
        break
print(f"a soma de todos os numeros é {soma}")