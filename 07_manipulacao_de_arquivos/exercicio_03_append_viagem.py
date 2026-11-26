"""
EXERCÍCIO 03: Adição ao Final de Arquivo (Append)
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Abra o arquivo `despesas_viagem.txt` no modo 'a' e anexe uma nova linha
de despesa sem apagar o histórico anterior.
"""

# TODO: Desenvolva o algoritmo abaixo:
with open("despesas_viagem.txt", "a") as arquivo:
    while True:
        despesas = input("Insira as novas despesas(insira (sair) para sair): ")
        if despesas == "sair":
            break
        else:
            arquivo.write(despesas + "\n")