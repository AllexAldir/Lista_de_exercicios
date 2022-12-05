# 10) Faça um algoritmo que leia a largura e altura de uma parede, calcule e
# mostre a área a ser pintada e a quantidade de tinta necessária para o serviço,
# sabendo que cada litro de tinta pinta uma área de 2metros quadrados.

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura: "))
area = largura * altura

print(f"A are do espaço é: {area} metros quadrados e quantidade de tinta necessária é: {area/2} litros")