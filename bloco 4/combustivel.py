distancia_percorrida = float(input("Digite a distância percorrida em km: "))
quantidade_litros = float(input("Digite a quantidade de litros gastos: "))

consumo_medio = distancia_percorrida / quantidade_litros

print(f"O consumo médio do veículo é: {consumo_medio:.2f} km/l")