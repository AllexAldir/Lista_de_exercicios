# 22) Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua
#     situação em relação ao alistamento militar.
#     - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o
#     alistamento.
ano = 2022

r = int(input("Digite o ano que você nasceu: "))
ano_ = ano - r

if ano_ >= 18:
    print("Você está na idade de se alistar no exércio!")
else:
    print("Ainda não está!")

