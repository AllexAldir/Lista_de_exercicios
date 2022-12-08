# 19) Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua
#     média e mostre na tela. No final, analise a média e mostre se o aluno teve ou
#     não um bom aproveitamento(se ficou acima da média 7.0).
media = 7

nome = input("Digite seu nome aqui: ").capitalize()
nota1 = float(input("Digite a primeira nota aqui: "))
nota2 = float(input("Digite a segunda nota aqui: "))
media_al = (nota1 + nota2) / 2

if media_al > media:
    print("Você passou!")
else:
    print("Você foi reprovado!")