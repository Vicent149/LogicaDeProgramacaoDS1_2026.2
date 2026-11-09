compras = []
c1 = input("Insira a sua primeira compra: ")
c2 = input("Insira a sua segunda compra: ")
c3 = input("Insira a sua terceira compra: ")
compras.append(f"{c1}")
compras.append(f"{c2}")
compras.append(f"{c3}")
compras.sort()

print(f"Lista de compras {compras}")


