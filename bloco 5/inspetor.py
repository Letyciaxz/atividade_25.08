produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade em estoque: "))
peso_unitario = float(input("Digite o peso unitário: "))

print(f"Produto: {produto} - Tipo: {type(produto)}")
print(f"Quantidade: {quantidade} - Tipo: {type(quantidade)}")
print(f"Peso unitário: {peso_unitario} - Tipo: {type(peso_unitario)}")