valor_pago = float(input("Digite o valor pago pelo cliente: "))
custo_produto = float(input("Digite o custo do produto: "))

troco = valor_pago - custo_produto

print(f"O troco é: R$ {troco:.2f}")