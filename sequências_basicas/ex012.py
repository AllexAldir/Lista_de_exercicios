# 12) Crie um programa que leia o preço de um produto, calcule e mostre o seu
#     PREÇO PROMOCIONAL, com 5 % de desconto.

produto = float(input("Digite o preço do produto: "))
print(f"Valor com o desconto de 5% é: {produto - (produto*0.05) }")
