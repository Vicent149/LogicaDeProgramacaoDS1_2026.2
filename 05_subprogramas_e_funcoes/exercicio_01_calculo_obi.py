"""
EXERCÍCIO 01: Pontuação OBI (Astro Lume Devs)
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma função nomeada `calcular_pontuacao_total(fase1, fase2, fase3)` com a diretiva `def`
que receba as 3 notas como parâmetros e retorne a pontuação total da equipe.
"""

# TODO: Desenvolva a função e os testes abaixo:
def caucular_pontacao_total(fase1,fase2,fase3): 
    pontos = fase1 + fase2 + fase3
    return pontos
fase_1 = float(input("Insira a pontuação da primeira fase"))
fase_2 = float(input("Insira a da segunda fase"))
fase_3 = float(input("Insira a da terceira fase"))

pontf = caucular_pontacao_total(fase_1,fase_2,fase_3)
print(f"A pontuação total foi {pontf}")