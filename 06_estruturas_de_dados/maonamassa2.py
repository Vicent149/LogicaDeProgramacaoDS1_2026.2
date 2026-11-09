numeros = []
n1 = float(input("Insira um valor: "))
n2 = float(input("Insira um valor: "))
n3 = float(input("Insira um valor: "))
n4 = float(input("Insira um valor: "))
numeros.append(n1)
numeros.append(n2)
numeros.append(n3)
numeros.append(n4)

matriz = [
    [numeros[0], numeros[1]],
    [numeros[2], numeros[3]]
]

soma = 0

for linha in matriz:
    for elemento in linha:
        soma += elemento

print(f"A soma total é igual a {soma}")