#  Caixa Eletrônico (ATM) Avançado Desenvolva um simulador de caixa eletrônico. O 
# programa deve exibir um menu contínuo com as opções: 1 - Depositar, 2 - Sacar, 3 - Consultar 
# Saldo, 4 - Sair. 
# ● O saldo inicial é zero. 
# ● Crie uma função para lidar com o saque, que receba o saldo atual e o valor desejado. 
# A função deve verificar se há saldo suficiente. Se não houver, deve exibir uma 
# mensagem de erro. 
# ● Desafio extra no saque: Se o saque for aprovado, o programa deve utilizar uma 
# lógica de repetição e decisões (ou r


saldo_i = 0
while True:
    opcao = int(input("""Escolha entre as opções
    Digite 1 para DEPOSITAR
    Digite 2 para SACAR
    Digite 3 para CONSULTAR
    Digite 4 para SAIR"""))
    if opcao == 4:
        print("Operação encerrada")
        break
    if opcao == 1:
        deposito = float(input("Insira o valor a se depositar: "))
        saldo_i = deposito + saldo_i
    if opcao == 2:
        saque = float(input("Insira o valor a ser sacado: "))
        saldo_i = saldo_i - saque
        if saque > saldo_i:
            print("INVALIDO")
        if opcao == 3:
            print(f"Seu saldo é de {saldo_i}R$")


