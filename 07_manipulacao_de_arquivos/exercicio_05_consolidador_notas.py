"""
EXERCÍCIO 05: Consolidador de Notas em Arquivo
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia a nota final de 5 alunos, armazene em uma lista e, ao final,
salve cada nota em uma nova linha do arquivo `notas_finais_2026.txt`.
"""

# TODO: Desenvolva o algoritmo abaixo:
with open("notas_finais_2026.txt", "a") as arquivo:
    for i in range(5):
        nota = (input(f"Insira a nota do aluno {i}: "))
        arquivo.write(nota + "\n")