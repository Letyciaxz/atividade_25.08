valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
horas_trabalhadas = int(input("Digite o total de horas trabalhadas no mês: "))

salario = valor_hora * horas_trabalhadas
print(f"O salário bruto do funcionário é: R$ {salario:.2f}")
