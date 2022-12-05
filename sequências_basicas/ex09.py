# 9) Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$)
# e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.
dolar = 3.45
dinheiro = float(input("Digite o valor que você tem em mãos para converter: "))
print(f"Você teria: {round(dinheiro / dolar,2)}")
