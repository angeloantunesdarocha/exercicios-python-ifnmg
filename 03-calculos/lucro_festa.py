quantidade_visitantes = int(input("Digite a quantidade de visitantes: "))
valor_ingresso = float(input("Digite o valor de cada ingresso: "))
gasto_alimentacao = float(input("Digite o gasto com alimentação por visitante: "))

receita_total = quantidade_visitantes * valor_ingresso
gasto_total = quantidade_visitantes * gasto_alimentacao
lucro_liquido = receita_total - gasto_total

print(f"Total de receita: R$ {receita_total:.2f}")
print(f"Total de gasto com alimentação: R$ {gasto_total:.2f}")
print(f"Lucro líquido: R$ {lucro_liquido:.2f}")
