# 17) Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse
#     80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba
#     o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.

limite = 80
velo = float(input("Digite a velocidade de um carro: "))

if velo > limite:
    print(f"Você ultrapassou o limite de velocidade. Multa de R$5 por kilômetro. Valor total é: {(velo - limite) * 5}")
