"""
EXERCÍCIO 03: Gerador de Alertas da Cagece
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Desenvolva um procedimento `emitir_alerta_fatura(nome_cliente, valor, data_vencimento)`
que imprima a mensagem:
"Prezado(a) [nome], sua fatura da Cagece no valor de R$ [valor] vence no dia [data]."
"""

# TODO: Desenvolva o procedimento abaixo:
def mensagem (nome,valor,venc):
    print(f"Prezado {nome}, a sua fatura esta no valor de {valor} R$, vencera no dia {venc}")
    return mensagem
pessoa = input("Insira o nome")
valorf = input("Insira o valor")
venci = input("Insira a data de vencimeto")
mensagem(pessoa,valorf,venci)