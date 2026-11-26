"""
EXERCÍCIO 02: Leitura com Tratamento de Exceção
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Tente ler o arquivo `dados_iniciais_casas_paulino.csv`.
Trate a exceção FileNotFoundError com try-except exibindo alerta amigável.
"""

# TODO: Desenvolva o algoritmo abaixo:
try:
    with open("dados_iniciais_casas_paulino.csv", "r") as arquivo:
        conteudo = arquivo.read()
    print("Lendo")
    print(conteudo)
except FileNotFoundError:
        print("Não há nada a ser lido no arquivo")