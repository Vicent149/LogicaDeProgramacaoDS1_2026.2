# Monitoramento de Temperatura em Estufa Um agricultor possui uma estufa e um sensor 
# de temperatura que faz leituras constantes. Escreva um programa que leia continuamente a 
# temperatura registrada (em graus Celsius) até que o usuário digite um valor de parada (por 
# exemplo, -99). Ao final, o programa deve exibir: 
# ● A temperatura média do período. 
# ● Quantas vezes a temperatura ultrapassou a marca de perigo (acima de 35°C). 

temperatura = 0
qtd35 = 0
qtd = 0
while True:
    temperatura1 = float(input("Insira a temperatura(valor de parada -99): "))
    if temperatura1 == -99:
        break
    elif temperatura >= 35:
        qtd35 += 1
    elif temperatura1 != -99:
        temperatura += temperatura1
        qtd += 1
    media = temperatura / qtd

print(f"a temperatura passou do ponto {qtd35} vezes. Com media de {media}")