# 8) Desenvolva um programa que leia uma distância em metros e mostre os valores
#     relativos em outras medidas.
#     Ex:
#     Digite uma distância em metros: 185.72
#     A distância de 85.7m corresponde a:
#     0.18572Km
#     1.8572Hm
#     18.572Dam
#     1857.2dm
#     18572.0cm
#     185720.0mm
distancia = float(input("Digite uma distância em metros: "))
print(f"""
Valor em Kilometros: {distancia / 1000}km
Valor em Hectômetro: {distancia / 100}hm
Valor em Decâmetro: {distancia / 10}Dam
Valor em Decímetro: {round(distancia / 0.1,2)}dm
Valor em Centímetros: {round(distancia / 0.01,2)}
Valor em Milímetros: {round(distancia / 0.001,2)}
""")
