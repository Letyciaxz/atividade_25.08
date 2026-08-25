cafe_manha = float(input("Digite o valor gasto com o café da manhã: "))
almoco = float(input("Digite o valor gasto com o almoço: "))
jantar = float(input("Digite o valor gasto com o jantar: "))

gasto_total = cafe_manha + almoco + jantar

print(f"O gasto total do dia é: R$ {gasto_total:.2f}")