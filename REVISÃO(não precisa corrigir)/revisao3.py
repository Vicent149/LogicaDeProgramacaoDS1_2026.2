# Controle de Qualidade na Fábrica Em uma linha de produção, as peças passam por uma 
# balança. O operador informará o peso de N peças (pergunte ao usuário quantas peças serão 
# pesadas antes de iniciar). Sem utilizar listas, crie um programa que determine e exiba no final 
# qual foi o peso da peça mais pesada e qual foi o peso da peça mais leve que passou pela 
# esteira naquele lote. 

pecas = int(input("Insira a quantidade de peças a pesar: "))

for i in range(1,pecas+1):
    peso = float(input(f"Insira o peso da peça {i}: "))
    print(f"Item numero {i} de peso {peso}")
    if i == 1:
        pesada = peso
        leve = peso
    else:
        if peso > pesada:
            pesada = peso
        if peso < leve:
            leve = peso
print (f"""Peso mais leve: {leve}.
Peso mais pesado: {pesada}""")