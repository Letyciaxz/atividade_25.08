distancia_km = float(input("Digite a distância da viagem em quilômetros: "))
velocidade_media = float(input("Digite a velocidade média do carro em quilômetros por hora: "))

tempo_estimado = distancia_km / velocidade_media

print(f"O tempo estimado de viagem é: {tempo_estimado:.2f} horas")