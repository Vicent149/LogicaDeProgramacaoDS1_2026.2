"""
EXERCÍCIO 04: Conjuntos (Set) de Disciplinas
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie 2 sets de estudantes (alunos_web e alunos_banco).
Calcule e imprima a Interseção (&) e a Diferença (-).
"""

# TODO: Desenvolva o algoritmo abaixo:

alunos_web = []
alunos_banco = []

n1 = int(input("Insira a quantidade de estudantes que estudam na Web: "))
n2 = int(input("Insira a quantidade de estudantes que estudam no Banco: "))

for i in range(0,n1):
    estudanteweb = input("Insira os estudantes que estudam na web: ")
    alunos_web.append(estudanteweb)

for i2 in range(0,n2):
    estudantebanco = input("Insira os estudantes que estudam no banco: ")
    alunos_banco.append(estudantebanco)


intersessao = set(alunos_web) & set(alunos_banco)
diferenca = set(alunos_web) - set(alunos_banco)
diferenca2 = set(alunos_banco) - set(alunos_web)

print("Alunos que estudam em ambas: ", intersessao)
print("Alunos que estudam apenas uma: ", diferenca, diferenca2)