from tkinter import N


nome_arquivo = str("meus_softwares.txt")

with open(nome_arquivo, 'a', encoding="utf-8") as arquivo:
    for i in range(3):
        software = str(input("Insira o nome de 3 software: "))
        arquivo.write(software + "\n")

print("Arquivo SALVO")