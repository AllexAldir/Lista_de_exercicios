# 14) A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva
# um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar,
# sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.

q_kil = float(input("Quantos kilometros percorridos? : "))
dias = int(input("Dias: "))
print(f"Preço total a pagar: {(90 * dias) + (0.2 * q_kil)}")