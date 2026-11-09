"""
EXERCÍCIO 02: Tupla de Coordenadas e Imutabilidade
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma tupla com as cidades ("Tianguá", "São Benedito").
Tente alterar a posição 1 e use try-except para capturar o TypeError,
exibindo uma mensagem explicativa sobre imutabilidade.
"""

# TODO: Desenvolva o algoritmo abaixo:

cidades = ("metropolis", "gotham", "coast city", "star city")
print("Tupla inicial: ", cidades)

c1 = str(input("Insira uma nova cidade: "))

try:
    cidades[1] = c1
except TypeError:
    print("Erro detectado, não é possivel alterar uma tupla")