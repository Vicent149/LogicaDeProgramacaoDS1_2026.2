# . Simulador de Rendimentos Crie uma função chamada calcular_juros que receba um 
# valor inicial, uma taxa de juros mensal e um número de meses. O programa deve usar um laço 
# de repetição dentro ou fora da função para calcular o crescimento do dinheiro mês a mês, 
# aplicando juros compostos. O programa deve imprimir o saldo ao final de cada mês. Se em 
# algum mês o saldo dobrar em relação ao valor inicial, o laço deve ser interrompido e uma 
# mensagem de "Meta Atingida antecipadamente!" deve ser exibida. 

def caucular_juro(valor,taxa,meses):
    for mes in range(1, meses + 1):
        saldo = valor + (valor * (taxa * 0.1 ))
        print(f"Mes {mes}, Saldo {saldo:.2f}")

vi = float(input("Insira o valor inicial"))
tjm = float(input("Insira a taxa de juros mensais"))
ms = int(input("Insira o numero de meses"))

caucular_juro(vi,tjm,ms)
print(caucular_juro)
