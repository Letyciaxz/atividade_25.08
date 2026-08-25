valor_total_conta = float(input("Digite o valor total da conta: "))
total_pessoas_mesa = int(input("Digite o total de pessoas na mesa: "))

valor_por_pessoa = valor_total_conta / total_pessoas_mesa

print(f"O valor que cada pessoa deve pagar é: R$ {valor_por_pessoa:.2f}")