saldo_inicial = float(input("Digite o saldo inicial da conta: "))
valor_deposito = float(input("Digite o valor do depósito: "))

saldo_final = saldo_inicial + valor_deposito

print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso. Saldo atual: R$ {saldo_final:.2f}")