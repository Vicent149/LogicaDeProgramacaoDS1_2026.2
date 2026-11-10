"""
EXERCÍCIO 03: Dicionário da Equipe EcoRadar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Estruture um dicionário com 3 membros (matrícula -> cargo).
Leia uma matrícula via terminal e exiba a função correspondente cadastrada.
"""

# TODO: Desenvolva o algoritmo abaixo:

aluno1 = input("Insira um itegrante que cuida da programação")
aluno2 = input("Insira um itegrante do design")
aluno3 = input("Insira um itegrante da marketing")


equipe = {
    f"{aluno1}": "Programador",
    f"{aluno2}": "Design",
    f"{aluno3}": "Marketing"
}

while True:
    n1 = int(input("Voce deseja olhar a função dos integrantes da equipe? 1-SIM 2-NÃO"))
    if n1 == 2:
        break
    if n1 == 1:
        n2 = int(input(f"""Voce deseja: 
Verificar posto do aluno: {aluno1}? digite 1
Verificar o posto do aluno: {aluno2}? digite 2
Verificar o posto do aluno: {aluno3}? digite 3
Verificar todos? digite 4
"""))
        if n2 == 1:
            print(f"Aluno: {aluno1}. Cargo: ", equipe[f"{aluno1}"])
        if n2 == 2:
            print(f"Aluno: {aluno2}. Cargo: ", equipe[f"{aluno2}"])
        if n2 == 3:
            print(f"Aluno: {aluno3}. Cargo: ", equipe[f"{aluno3}"])
        if n2 == 4:
            print(f"Aluno: {aluno1}. Cargo: ", equipe[f"{aluno1}"])
            print(f"Aluno: {aluno2}. Cargo: ", equipe[f"{aluno2}"])
            print(f"Aluno: {aluno3}. Cargo: ", equipe[f"{aluno3}"])
        if n2<1 or n2>4:
            print("Matricula não encontrada")