# 16)[DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um
#     fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele
#     já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule
#     quantos dias de vida um fumante perderá e exiba o total em dias.

quant_dia = int(input("Quantos cigarros você fuma por dia? : "))
quant_ano = int(input("Quantos anos já fumou: "))

red = quant_ano * 365 * quant_dia * 10
#dia = 24 x 60 minutos

print(f"Redução do tempo de vida: {round(red / 1440,2)} dias")
