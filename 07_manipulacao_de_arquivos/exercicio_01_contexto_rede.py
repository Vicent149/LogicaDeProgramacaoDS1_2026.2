"""
EXERCÍCIO 01: Gerenciador de Contexto e Log de Rede
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Use `with open("acessos_laboratorio.txt", "w")` para criar e salvar
os horários de entrada e saída de 3 turmas no laboratório.
"""

# TODO: Desenvolva o algoritmo abaixo:

with open("acessos_laboratorio.txt", "w") as arquivo:
    for i in range(3):
        horario_e = input("Insira o horario de entrada no laboratorio: ")
        horario_s = input("Insira o horario de saida do laboratorio")
        turma = f"Turma {i} entrou as {horario_e} e saiu as {horario_s}"
        arquivo.write(turma + "\n")
        
