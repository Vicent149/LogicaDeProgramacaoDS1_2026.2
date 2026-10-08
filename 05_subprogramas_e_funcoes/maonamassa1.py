def ca_media(n1,n2,n3):
    media = float((n1 + n2 + n3) / 3)
    return media

nota1 = float(input("Insira a sua primeira nota"))
nota2 = float(input("Insira a sua segunda nota"))
nota3 = float(input("Insira a sua terceira nota"))

mediaf = ca_media(nota1,nota2,nota3)

print(f"Sua media é {mediaf}")