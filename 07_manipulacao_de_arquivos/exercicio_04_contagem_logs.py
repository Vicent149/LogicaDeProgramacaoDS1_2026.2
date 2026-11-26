"""
EXERCÍCIO 04: Contagem de Falhas em Logs
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia um arquivo de texto e conte a frequência de palavras-chave de erro
exibindo o relatório consolidado.
"""

# TODO: Desenvolva o algoritmo abaixo:
nomearquivo = "acessos_laboratorio.txt"
palavrachave = "entrou"


with open("acessos_laboratorio.txt", "r", encoding= "utf-8") as arquivo:
    conteudo = arquivo.read()
    qtd = conteudo.count(palavrachave)
    print(conteudo)

print(f"""A palavra "entrou" aparece no arquivo {qtd} vezes""")