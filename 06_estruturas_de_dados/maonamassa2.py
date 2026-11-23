numeros = []
for i in range(1,5):
    n1 = float(input("Insira um valor: "))
    numeros.append(n1)


matriz = [
    [numeros[0], numeros[1]],
    [numeros[2], numeros[3]]
]

soma = 0

for linha in matriz:
    for elemento in linha:
        soma += elemento

print(f"A soma total é igual a {soma}")