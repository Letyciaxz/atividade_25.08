COTACAO_DOLAR = 5.20
dolares = float(input("Quantos dólares você deseja trocar? "))

valor_reais = dolares * COTACAO_DOLAR

print(f"Você receberá R$ {valor_reais:.2f}")