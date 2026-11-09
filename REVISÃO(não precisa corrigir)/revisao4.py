# Um condomínio está elegendo o novo síndico. Existem três candidatos 
# (1 - Ana, 2 - João, 3 - Maria). Crie um programa que receba os votos dos moradores 
# indefinidamente, até que o número 0 seja digitado para encerrar a urna. O programa deve 
# rejeitar votos inválidos (números diferentes de 0, 1, 2 e 3), pedindo que o usuário digite 
# novamente. Ao fim, exiba o total de votos de cada candidato e quem foi o vencedor. 

v_ana = 0
v_joao = 0
v_maria = 0

while True:
    cdt = int(input("""vote na chapa de seu candidato
    1 - ana
    2 - joao
    3 - maria"""))
    if cdt in (1,2,3):
        print("Voto valido")
        if cdt == 1:
            v_ana += 1
        elif cdt == 2:
            v_joao += 1
        elif cdt == 3:
            v_maria += 1
    elif cdt == 0:
        print("Votação encerrada")   
        print(f"""Ana:{v_ana}
João:{v_joao}
Maria:{v_maria}""")
        break
    else:
        print("Voto invalido. Digite novamente")