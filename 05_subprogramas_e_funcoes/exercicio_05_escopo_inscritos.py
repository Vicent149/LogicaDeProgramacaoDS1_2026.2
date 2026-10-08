"""
EXERCÍCIO 05: Gestão de Escopo Global e Local
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Declare a variável global total_inscritos = 0.
Crie a função `inscrever_aluno(quantidade)` utilizando a diretiva `global`
para atualizar a variável. Demonstre o valor de total_inscritos antes e depois da chamada.
"""

# TODO: Desenvolva o algoritmo abaixo:
totalinscritos = int(0)
def inaluno(inscritos):
    print(f"O numero inicial de alunos inscritos são: {totalinscritos}")
    print(f"O numero final de alunos inscritos são {inscritos}")

alunos = int(input("Insira o numero de alunos que irão se inscrever: "))
inscritos = inaluno(alunos)