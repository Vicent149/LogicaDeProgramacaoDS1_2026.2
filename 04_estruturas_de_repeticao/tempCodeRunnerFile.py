senha = int("2002")
while True:
    senha = int(input("Insira sua senha: "))
    if senha == 2002:
        print("A senha esta correta. Bem Vindo")
        break
    else:
        print("Senha incorreta. Tente Novamente")