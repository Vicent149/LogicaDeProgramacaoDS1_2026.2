"""
EXERCÍCIO 05: Matriz Bidimensional Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma matriz com 3 alunos [nome, nota1, nota2].
Percorra a matriz, calcule a média de cada um e exiba:
"Aluno: [Nome] | Média: [Média] | Situação: [Aprovado / Prova Final]"
(Critério: Média >= 6.0 aprovado).
"""

# TODO: Desenvolva o algoritmo abaixo:

# Matriz representando o diário de classe: [Nome, Nota 1, Nota 2]

nome_aluno = []
media_final = []
situacao_final = []

for i in range(3):
    nome = input(f"Insira o nome do {i} aluno")
    nome_aluno.append(nome)
    n1 = float(input(f"Insira a primeira nota do {i} aluno"))
    n2 = float(input(f"Insira a segunda nota do {i} aluno"))
    media = (n1 + n2) / 2
    if media >=6:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    media_final.append(media)
    situacao_final.append(situacao)

diario = [
    [nome_aluno[0], media_final[0], situacao_final[0] ],
    [nome_aluno[1], media_final[1], situacao_final[1] ],
    [nome_aluno[2], media_final[2], situacao_final[2]]
]

print(diario)



